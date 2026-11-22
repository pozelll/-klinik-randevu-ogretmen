"""Sentetik öğretmen uygulamasının Chromium kontrolleri; harici hesaba bağlanmaz.
Kurulum: python -m pip install playwright; python -m playwright install chromium
Çalıştırma: python tests/browser_smoke.py
Varsayılan çalıştırma, kanıt dosyalarının üzerine yazmaz. Kayıt için --evidence-dir verin.
"""
from pathlib import Path
import argparse, hashlib, json, shutil
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
KEY = 'ygs-klinik-randevu-demo-v1'
parser = argparse.ArgumentParser()
parser.add_argument('--evidence-dir', type=Path)
args = parser.parse_args()
results = []

def snapshot(page):
    return page.evaluate('(key) => JSON.parse(localStorage.getItem(key))', KEY)

def click_cancel(page, accept=True):
    page.once('dialog', lambda d: d.accept() if accept else d.dismiss())
    page.locator('[data-appointment-id="R001"] [data-action="cancel"]').click()

def run(name, fn, init=None, viewport=None):
    ctx = browser.new_context(viewport=viewport or {'width':1280, 'height':900})
    if init: ctx.add_init_script(init)
    page = ctx.new_page(); errors=[]
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto((ROOT/'index.html').as_uri())
    expect(page.locator('#slots button')).to_have_count(10)
    detail = fn(page)
    assert not errors, errors
    results.append({'id':name,'status':'PASS','actual':detail,'pageErrors':errors})
    ctx.close()

def t01(p):
    expect(p.locator('#cancel-help-title')).to_have_text('Randevu iptali hakkında')
    expect(p.locator('section[aria-labelledby="cancel-help-title"]')).to_contain_text('Tamamlandı')
    return 'H3 iptal açıklaması ve Tamamlandı sınırı ekranda.'
def t02(p):
    before = snapshot(p); click_cancel(p,False)
    assert snapshot(p)==before
    expect(p.locator('[data-time="09:00"]')).to_be_disabled()
    expect(p.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('Bekliyor')
    return 'ALT-01: onaydan vazgeçmede kayıt ve saat aynı.'
def t03(p):
    before=snapshot(p); messages=[]
    p.once('dialog',lambda d:(messages.append(d.message),d.accept()))
    p.locator('[data-appointment-id="R001"] [data-action="cancel"]').click()
    assert 'Tamam:' in messages[0] and 'İptal:' in messages[0]
    after=snapshot(p)
    assert len(before['appointments'])==len(after['appointments'])==7
    expect(p.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('İptal edildi')
    expect(p.locator('[data-time="09:00"]')).to_be_enabled()
    expect(p.locator('#notice-text')).to_contain_text('İlgili saat yeniden uygun.')
    return 'AC-03: kayıt listede kaldı, 09:00 açıldı, genel kayıt sayısı 7.'
def t04(p):
    expect(p.locator('[data-appointment-id="R003"] [data-action="cancel"]')).to_have_count(0)
    expect(p.locator('[data-time="11:00"]')).to_be_disabled()
    return 'Tamamlandı kaydında iptal düğmesi yok, saat kapalı.'
def t05(p):
    expect(p.locator('.appointment')).to_have_count(2)
    expect(p.locator('[data-appointment-id="R002"]')).to_have_count(0)
    p.locator('#patient-select').select_option('kaan')
    expect(p.locator('[data-appointment-id="R001"]')).to_have_count(0)
    expect(p.locator('[data-appointment-id="R002"]')).to_have_count(1)
    return 'Ece ve Kaan görünümleri kendi kayıtlarıyla sınırlı.'
def t06(p):
    p.locator('#role-reception').click(); expect(p.locator('#metric-total')).to_have_text('4')
    p.locator('#role-patient').click(); p.locator('[data-time="09:30"]').click(); p.locator('#book-appointment').click()
    p.locator('#role-reception').click(); expect(p.locator('#metric-total')).to_have_text('5')
    p.locator('#role-patient').click(); click_cancel(p,False)
    p.locator('#role-reception').click(); expect(p.locator('#metric-total')).to_have_text('5')
    p.locator('#role-patient').click(); click_cancel(p)
    p.locator('#role-reception').click(); expect(p.locator('#metric-total')).to_have_text('5')
    expect(p.locator('#metric-pending')).to_have_text('2')
    expect(p.locator('#metric-cancelled')).to_have_text('2')
    return 'Seçili doktor/gün toplamı 4 → 5 → 5 → 5; genel kayıt 7 → 8.'
def b07(p):
    click_cancel(p); p.reload()
    expect(p.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('İptal edildi')
    p.locator('[data-time="09:00"]').click(); p.locator('#book-appointment').click()
    p.locator('#role-doctor').click(); p.locator('[data-appointment-id="R008"] [data-action="complete"]').click()
    expect(p.locator('[data-appointment-id="R008"] .status-pill')).to_have_text('Tamamlandı')
    expect(p.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('İptal edildi')
    return 'Yenileme, yeniden oluşturma ve tamamlama birbiriyle tutarlı.'
def b08(p):
    expect(p.locator('#storage-label')).to_contain_text('Yalnız bu oturumun belleği')
    click_cancel(p)
    expect(p.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('İptal edildi')
    p.reload(); expect(p.locator('[data-appointment-id="R001"] .status-pill')).to_have_text('Bekliyor')
    return 'Saklama engelliyken uygulama çalıştı; yenilemede oturum değişikliği kayboldu.'
def b09(p):
    assert p.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    p.locator('[data-time="09:30"]').click(); p.locator('#book-appointment').click()
    expect(p.locator('[data-appointment-id="R008"]')).to_have_count(1)
    return '390 px görünümde yatay taşma yok; randevu oluşturulabiliyor.'

with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True, executable_path=shutil.which('chromium'), args=['--no-sandbox'])
    version=browser.version
    for name,fn in [('H3-T01',t01),('H3-T02',t02),('H3-T03',t03),('H3-T04',t04),('H3-T05',t05),('H3-T06',t06),('H6-B07',b07)]:run(name,fn)
    run('H6-B08',b08,"Object.defineProperty(window,'localStorage',{get(){throw new Error('Test: saklama engelli');}});")
    run('H6-B09',b09,viewport={'width':390,'height':844})
    browser.close()
sources={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['index.html','src/demo-data.js','src/repository.js','src/rules.js','src/ui.js']}
report={'executedAt':datetime.now(timezone.utc).isoformat(),'browser':'Chromium '+version,
        'method':'Headless Playwright; file://; sentetik ve yalıtılmış yeni tarayıcı oturumları',
        'scope':'NFR kullanılabilirlik / yanıt süresi / klavye ölçümü değildir; bağımsız insan incelemesi değildir.',
        'sources':sources,'results':results}
if args.evidence_dir:
    args.evidence_dir.mkdir(parents=True,exist_ok=True)
    (args.evidence_dir/'tarayici-sonuclari.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
