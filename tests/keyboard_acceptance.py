"""Klavye kabul kontrolü: fare veya locator.focus/select_option kullanılmaz.

Normal kip: sayfa adımları klavye, native confirm kararı Playwright API'si;
bu kip native pencerenin klavye kabulünü KAPATMAZ.

Tam native tuş denemesi (Linux):
  xvfb-run -a python tests/keyboard_acceptance.py --native-dialog --evidence-dir kanit
Gerekenler: Playwright/Chromium, Xvfb, xdotool. scrot varsa native ekran görüntüsü
de alınır. Bu görüntünün odak görünürlüğü ayrıca görsel incelenmelidir.
NFR-01'in dört gerçek katılımcılı kullanılabilirlik deneyi bu test değildir.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import base64
import hashlib
import json
import os
import shutil
import subprocess
import time

from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
KEY = 'ygs-klinik-randevu-demo-v1'


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-dir', type=Path, default=ROOT)
    parser.add_argument('--evidence-dir', type=Path)
    parser.add_argument('--native-dialog', action='store_true')
    parser.add_argument('--embed-native-screenshots', action='store_true',
                        help='Native PNG kanıtlarını JSON içine base64 olarak da ekler.')
    return parser.parse_args()


class KeyboardSession:
    def __init__(self, page, args, test_id):
        self.page = page
        self.args = args
        self.test_id = test_id
        self.trace = []
        self.dialogs = []

    def focus_state(self):
        return self.page.evaluate('''() => {
          const e = document.activeElement;
          const r = e.getBoundingClientRect(), s = getComputedStyle(e);
          return {tag:e.tagName, id:e.id, time:e.dataset.time || null,
            action:e.dataset.action || null, record:e.dataset.id || null,
            label:e.getAttribute('aria-label') || e.textContent.trim().slice(0,100),
            disabled:Boolean(e.disabled), focusVisible:e.matches(':focus-visible'),
            outlineStyle:s.outlineStyle, outlineWidth:s.outlineWidth,
            outlineColor:s.outlineColor, outlineOffset:s.outlineOffset,
            visible:r.width>0 && r.height>0 && r.bottom>0 && r.right>0 &&
              r.top<innerHeight && r.left<innerWidth && s.visibility!=='hidden'};
        }''')

    def visible_focus(self, reason):
        state = self.focus_state()
        self.trace.append({'event':reason, 'focus':state})
        assert state['tag'] not in ('BODY', 'HTML'), f'{reason}: odak kayboldu: {state}'
        assert not state['disabled'], f'{reason}: pasif öğede odak: {state}'
        assert state['visible'] and state['focusVisible'], f'{reason}: görünür klavye odağı yok: {state}'
        assert state['outlineStyle'] not in ('none', 'hidden') and float(state['outlineWidth'].removesuffix('px')) >= 1, f'{reason}: odak çerçevesi yok: {state}'
        assert state['outlineColor'] not in ('transparent', 'rgba(0, 0, 0, 0)'), f'{reason}: saydam odak çerçevesi'
        return state

    def reach(self, selector, reverse=False):
        """Hedefe yalnız Tab/Shift+Tab ile ulaşır; DOM odağı programla taşımaz."""
        assert self.page.locator(selector).count() == 1, f'Tek hedef bekleniyordu: {selector}'
        for step in range(81):
            if self.page.locator(selector).evaluate('(e) => e===document.activeElement'):
                self.visible_focus('Hedefe ulaşıldı: '+selector)
                return
            if step == 80:
                raise AssertionError(f'80 klavye adımında erişilemeyen hedef: {selector}')
            self.page.keyboard.press('Shift+Tab' if reverse else 'Tab')
            state = self.focus_state()
            if state['tag'] not in ('BODY', 'HTML'):
                self.visible_focus('Shift+Tab' if reverse else 'Tab')

    def press(self, key, after=True):
        self.visible_focus('Tuş öncesi: '+key)
        self.page.keyboard.press(key)
        if after:
            self.visible_focus('Tuş sonrası: '+key)

    def select_second(self, selector, expected):
        self.reach(selector)
        self.press('Home')
        self.press('ArrowDown')
        expect(self.page.locator(selector)).to_have_value(expected)

    def select_first(self, selector, expected):
        self.reach(selector)
        self.press('Home')
        expect(self.page.locator(selector)).to_have_value(expected)

    def confirm(self, selector, accept):
        self.reach(selector)
        entry = {'decision':'accept' if accept else 'dismiss',
                 'trigger':'page.keyboard Enter', 'observed':False}

        def on_dialog(dialog):
            entry.update({'observed':True, 'type':dialog.type, 'message':dialog.message})
            assert dialog.type == 'confirm'
            if self.args.native_dialog:
                # The OS event goes to Chromium's native modal. No CDP/Playwright
                # dialog.accept()/dismiss() is used in this mode.
                windows = subprocess.run(
                    ['xdotool', 'search', '--onlyvisible', '--name', 'Klinik Randevu'],
                    capture_output=True, text=True, check=True, timeout=5).stdout.split()
                assert windows, 'Görünür Klinik Randevu Chromium penceresi bulunamadı.'
                window = windows[-1]
                subprocess.run(['xdotool', 'windowfocus', '--sync', window],
                               capture_output=True, check=True, timeout=5)
                # Native dialog painting follows the opening event asynchronously.
                time.sleep(0.35)
                if self.args.evidence_dir and shutil.which('scrot'):
                    name = f'{self.test_id}-dialog-{len(self.dialogs)+1}.png'
                    dest = self.args.evidence_dir/name
                    subprocess.run(['scrot', '-o', str(dest)],
                                   capture_output=True, check=True, timeout=5)
                    entry['nativeScreenshot'] = name
                    entry['nativeScreenshotSHA256'] = hashlib.sha256(dest.read_bytes()).hexdigest()
                    if self.args.embed_native_screenshots:
                        entry['nativeScreenshotBase64'] = base64.b64encode(dest.read_bytes()).decode()
                key = 'Return' if accept else 'Escape'
                subprocess.run(['xdotool', 'key', '--clearmodifiers', key],
                               capture_output=True, check=True, timeout=5)
                entry.update({'method':'X11 xdotool keyboard', 'windowId':window, 'key':key,
                              'playwrightDialogDecisionUsed':False})
            else:
                (dialog.accept if accept else dialog.dismiss)()
                entry.update({'method':'Playwright dialog API; native keyboard NOT verified',
                              'playwrightDialogDecisionUsed':True})
            self.dialogs.append(entry)

        self.page.once('dialog', on_dialog)
        self.press('Enter', after=False)
        assert entry['observed'], 'Beklenen native onay penceresi açılmadı.'
        self.visible_focus('Onay penceresi kapandıktan sonra')

    def snapshot(self):
        return self.page.evaluate('(key)=>JSON.parse(localStorage.getItem(key))', KEY)


def create(k):
    p = k.page
    k.reach('#role-patient'); k.press('Enter')
    k.reach('[data-time="09:30"]')
    before = k.snapshot()
    k.press('Space')
    expect(p.locator('[data-time="09:30"]')).to_have_attribute('aria-pressed', 'true')
    assert k.snapshot() == before, 'Saat seçimi veri değiştirmemeli.'
    assert p.locator('[data-time="09:30"]').evaluate('(e)=>e===document.activeElement'), 'Yeniden çizim seçilen saatten odağı kopardı.'
    k.reach('#book-appointment'); k.press('Enter')
    data = k.snapshot()
    assert len(data['appointments']) == 8 and data['appointments'][-1]['id'] == 'R008'
    expect(p.locator('[data-appointment-id="R008"] .status-pill')).to_have_text('Bekliyor')
    expect(p.locator('[data-time="09:30"]')).to_be_disabled()
    return 'Yalnız klavyeyle 09:30 seçildi ve R008 oluşturuldu; kayıt/saat doğrulandı.'


def dismiss_cancel(k):
    before = k.snapshot()
    k.confirm('[data-appointment-id="R001"] [data-action="cancel"]', False)
    assert k.snapshot() == before
    expect(k.page.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('Bekliyor')
    expect(k.page.locator('[data-time="09:00"]')).to_be_disabled()
    k.reach('#book-appointment', reverse=True) if k.page.locator('#book-appointment').is_enabled() else k.reach('#date-select', reverse=True)
    return 'İptal başlatıldı ve vazgeçildi; veri ve dolu saat korundu, Shift+Tab ile çıkılabildi.'


def cancel(k):
    before = k.snapshot()
    k.confirm('[data-appointment-id="R001"] [data-action="cancel"]', True)
    after = k.snapshot()
    assert len(after['appointments']) == len(before['appointments']) == 7
    expect(k.page.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('İptal edildi')
    expect(k.page.locator('[data-time="09:00"]')).to_be_enabled()
    k.reach('[data-time="09:00"]'); k.press('Space')
    expect(k.page.locator('[data-time="09:00"]')).to_have_attribute('aria-pressed', 'true')
    return 'İptal kaydı korundu; 09:00 açıldı ve klavyeyle yeniden seçilebildi.'


def complete(k):
    k.reach('#role-doctor'); k.press('Enter')
    expect(k.page.locator('#patient-select')).to_be_disabled()
    k.reach('[data-appointment-id="R001"] [data-action="complete"]'); k.press('Space')
    expect(k.page.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('Tamamlandı')
    expect(k.page.locator('[data-time="09:00"]')).to_be_disabled()
    expect(k.page.locator('#metric-completed')).to_have_text('2')
    k.reach('#doctor-select', reverse=True)
    return 'Doktor rolüne geçildi, R001 tamamlandı; kapalı saat/toplam ve ters klavye yolu doğrulandı.'


def selection_fields(k):
    k.reach('#role-reception'); k.press('Space')
    k.select_second('#patient-select', 'kaan')
    k.select_first('#patient-select', 'ece')
    k.select_second('#doctor-select', 'selin')
    expect(k.page.locator('#slots-subtitle')).to_contain_text('Selin Kaya')
    expect(k.page.locator('#metric-total')).to_have_text('2')
    k.select_first('#doctor-select', 'deniz')
    k.select_second('#date-select', '2030-11-13')
    expect(k.page.locator('#metric-total')).to_have_text('1')
    k.select_first('#date-select', '2030-11-12')
    expect(k.page.locator('#metric-total')).to_have_text('4')
    return 'Rol, hasta, doktor ve tarih yalnız Tab/ok/Home/Enter/Boşluk ile değiştirildi.'


def reset(k):
    create(k)
    before = k.snapshot()
    k.confirm('#reset-data', False)
    assert k.snapshot() == before
    k.confirm('#reset-data', True)
    assert len(k.snapshot()['appointments']) == 7
    expect(k.page.locator('#role-patient')).to_have_attribute('aria-pressed', 'true')
    return 'Sıfırlamadan vazgeçme değişikliği korudu; onay başlangıçtaki 7 sentetik kaydı yükledi.'


def main():
    args = parse_args()
    args.app_dir = args.app_dir.resolve()
    if args.evidence_dir:
        args.evidence_dir = args.evidence_dir.resolve()
        args.evidence_dir.mkdir(parents=True, exist_ok=True)
    if args.native_dialog:
        assert os.environ.get('DISPLAY'), '--native-dialog için X11 DISPLAY (ör. xvfb-run) gerekir.'
        assert shutil.which('xdotool'), '--native-dialog için xdotool kurulu olmalı.'
    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=not args.native_dialog,
                                    executable_path=shutil.which('chromium'),
                                    args=['--no-sandbox', '--window-size=1280,1000'])
        version = browser.version
        for test_id, fn in [('NFR03-K01', create), ('NFR03-K02', dismiss_cancel),
                            ('NFR03-K03', cancel), ('NFR03-K04', complete),
                            ('KB-K05', selection_fields), ('KB-K06', reset)]:
            ctx = browser.new_context(viewport={'width':1280, 'height':900})
            page = ctx.new_page(); page.set_default_timeout(15000)
            page_errors = []; page.on('pageerror', lambda error: page_errors.append(str(error)))
            k = KeyboardSession(page, args, test_id)
            status = 'FAIL'; actual = None; error = None
            try:
                page.goto((args.app_dir/'index.html').as_uri())
                expect(page.locator('#slots button')).to_have_count(10)
                actual = fn(k)
                assert not page_errors, page_errors
                status = 'PASS'
                if args.evidence_dir:
                    page.screenshot(path=str(args.evidence_dir/f'{test_id}-sonuc.png'), full_page=True)
            except Exception as exc:
                error = f'{type(exc).__name__}: {exc}'
            finally:
                results.append({'id':test_id, 'status':status, 'actual':actual, 'error':error,
                                'focusTrace':k.trace, 'dialogs':k.dialogs, 'pageErrors':page_errors})
                ctx.close()
        browser.close()
    passed = sum(r['status'] == 'PASS' for r in results)
    paths = ['index.html', 'src/demo-data.js', 'src/repository.js', 'src/rules.js', 'src/ui.js']
    report = {
        'executedAt':datetime.now(timezone.utc).isoformat(), 'browser':'Chromium '+version,
        'method':'Page actions use only keyboard Tab/Shift+Tab/Home/arrows/Enter/Space; no click, select_option or programmatic focus.',
        'nativeDialogMethod':'X11 xdotool Return/Escape' if args.native_dialog else 'Playwright API: native keyboard NOT verified',
        'nfr03':{
            'coreTaskChecksPassed':sum(r['status']=='PASS' for r in results[:4]), 'coreTaskChecksTotal':4,
            'pageFocusEvidence':'Computed :focus-visible, visible bounds and nontransparent outline at every used page control; dynamic focus loss fails.',
            'nativeDialogKeyboardTested':args.native_dialog,
            'nativeDialogFocusVisualReview':'Inspect native screenshots separately; browser-chrome focus styling is outside DOM inspection.',
            'verdict':'AUTOMATED_FAILURE' if passed<6 else 'NATIVE_KEYS_AND_PAGE_TASKS_PASS_VISUAL_REVIEW_PENDING' if args.native_dialog else 'PARTIAL_NATIVE_DIALOG_NOT_KEYBOARD_TESTED'},
        'nfr01':'NOT_MEASURED: requires four different real participants; this automation is not a usability participant.',
        'limitations':['One Chromium build/environment; not a general accessibility conformance claim.',
                       'No independent human review or user acceptance is asserted.'],
        'sources':{p:hashlib.sha256((args.app_dir/p).read_bytes()).hexdigest() for p in paths},
        'passed':passed, 'total':len(results), 'results':results}
    if args.evidence_dir:
        (args.evidence_dir/'klavye-sonuclari.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed == len(results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
