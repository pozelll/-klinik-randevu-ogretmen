"""Local UI performance evidence; not human acceptance or server load testing.

Run: python tests/performance_checks.py --evidence-dir own-evidence
Optional --record-video keeps a Playwright recording for a separate visual review.
The original NFR-02 specifies screen-recording frame analysis. This instrumented
event-to-render proxy does not silently replace or certify that acceptance method.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math
import os
import platform
import shutil
import sys
import time
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
KEY = 'ygs-klinik-randevu-demo-v1'
DATE = '2030-11-12'
TIMES = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '13:00', '13:30', '14:00', '14:30']
LABELS = {'pending': 'Bekliyor', 'completed': 'Tamamlandı', 'cancelled': 'İptal edildi'}
DOCTORS = {'deniz': 'Doktor Deniz Arı', 'selin': 'Doktor Selin Kaya'}
PATIENTS = {'ece': 'Ece Yılmaz', 'kaan': 'Kaan Demir'}


def seed(count):
    # Independent fixture: same seven baseline records as the published demo.
    specs = [('ece', 'deniz', DATE, '09:00', 'pending'),
             ('kaan', 'deniz', DATE, '10:00', 'pending'),
             ('ece', 'deniz', DATE, '11:00', 'completed'),
             ('kaan', 'deniz', DATE, '13:00', 'cancelled'),
             ('ece', 'selin', DATE, '09:30', 'pending'),
             ('kaan', 'selin', DATE, '11:00', 'completed'),
             ('kaan', 'deniz', '2030-11-13', '10:30', 'pending')]
    rows = [dict(zip(('patientId', 'doctorId', 'date', 'time', 'status'), values),
                 id=f'R{i:03}') for i, values in enumerate(specs, 1)]
    for i in range(8, count + 1):
        # Historical cancellations do not introduce active slot conflicts.
        rows.append({'id': f'R{i:03}', 'patientId': 'ece' if i % 2 else 'kaan',
                     'doctorId': 'deniz' if i % 2 else 'selin', 'date': DATE,
                     'time': TIMES[(i - 8) % len(TIMES)], 'status': 'cancelled'})
    return {'schema': 1, 'nextId': count + 1, 'appointments': rows}


def expected_view(data, doctor):
    rows = sorted((x for x in data['appointments'] if x['doctorId'] == doctor and x['date'] == DATE),
                  key=lambda a: (a['time'], a['id']))
    totals = {s: sum(a['status'] == s for a in rows) for s in LABELS}
    totals['total'] = len(rows)
    slots = []
    for t in TIMES:
        occupied = next((a for a in rows if a['time'] == t and a['status'] != 'cancelled'), None)
        slots.append({'time': t, 'disabled': occupied is not None,
                      'label': 'Uygun' if occupied is None else 'Kapalı' if occupied['status'] == 'completed' else 'Dolu'})
    return {'doctor': doctor, 'doctorLabel': DOCTORS[doctor], 'totals': totals, 'slots': slots,
            'rows': [{'id': a['id'], 'time': a['time'], 'patient': PATIENTS[a['patientId']],
                      'status': LABELS[a['status']]} for a in rows]}


INSTRUMENT = r"""({expectations}) => {
  window.__perf = {records: [], expected: expectations, mutationExpected: null};
  const visibleState = () => {
    const q = s => document.querySelector(s);
    return {
      doctor: q('#doctor-select').value,
      rows: Array.from(document.querySelectorAll('#appointments .appointment')).map(e => ({
        id: e.dataset.appointmentId, time: e.querySelector('.time-block').textContent,
        patient: e.querySelector('.appointment-name').textContent,
        status: e.querySelector('.status-pill').textContent
      })),
      slots: Array.from(document.querySelectorAll('#slots button')).map(e => ({
        time: e.dataset.time, disabled: e.disabled, label: e.querySelector('small').textContent
      })),
      totals: Object.fromEntries(['pending','completed','cancelled','total'].map(s =>
        [s, Number(q('#metric-'+s).textContent)]))
    };
  };
  const dailyCorrect = expected => {
    const actual = visibleState();
    return actual.doctor === expected.doctor &&
      JSON.stringify(actual.rows) === JSON.stringify(expected.rows) &&
      JSON.stringify(actual.slots) === JSON.stringify(expected.slots) &&
      Object.keys(expected.totals).every(k => actual.totals[k] === expected.totals[k]) &&
      document.querySelector('#slots-subtitle').textContent.includes(expected.doctorLabel) &&
      document.querySelector('#appointments-subtitle').textContent.includes(expected.doctorLabel) &&
      !document.querySelector('#summary-metrics').hidden;
  };
  const mutationCorrect = expected => {
    const saved = JSON.parse(localStorage.getItem('ygs-klinik-randevu-demo-v1'));
    const row = saved.appointments.find(a => a.id === expected.id);
    const element = document.querySelector('[data-appointment-id="'+expected.id+'"]');
    const slot = document.querySelector('[data-time="09:30"]');
    return saved.appointments.length === expected.count && row &&
      row.status === expected.status && element &&
      element.querySelector('.status-pill').textContent === expected.label &&
      slot.disabled === (expected.status !== 'cancelled');
  };
  window.__perf.begin = (kind, expected, trusted) => {
    const start = performance.now();
    const verify = () => kind === 'doctor' ? dailyCorrect(expected) : mutationCorrect(expected);
    const finish = () => {
      const correct = verify();
      const end = performance.now();
      window.__perf.records.push({kind, target: expected.doctor || expected.id, trustedEvent: trusted,
        startMs: start, endMs: end, durationMs: end-start, correct,
        rowCount: document.querySelectorAll('#appointments .appointment').length});
    };
    // The first rAF observes post-handler DOM. A second rAF allows a paint opportunity.
    // This is a conservative instrumented proxy, not proof of physical pixel presentation.
    requestAnimationFrame(() => requestAnimationFrame(finish));
  };
  document.addEventListener('change', e => {
    if(e.target.id === 'doctor-select') window.__perf.begin('doctor',
      window.__perf.expected[e.target.value], e.isTrusted);
  }, true);
  document.addEventListener('click', e => {
    if(e.target.closest('#book-appointment') && window.__perf.mutationExpected)
      window.__perf.begin('create', window.__perf.mutationExpected, e.isTrusted);
  }, true);
  const originalConfirm = window.confirm.bind(window);
  window.confirm = message => {
    const accepted = originalConfirm(message);
    if(accepted && window.__perf.mutationExpected)
      window.__perf.begin('cancel_after_confirmation', window.__perf.mutationExpected, null);
    return accepted;
  };
}"""


def stats(samples):
    values = sorted(x['durationMs'] for x in samples)
    span = samples[-1]['endMs'] - samples[0]['startMs'] if samples else 0
    return {'trials': len(samples), 'percentileMethod': 'Nearest rank; descriptive small-sample result, not a population guarantee.',
            'p50Ms': values[math.ceil(.5 * len(values)) - 1] if values else None,
            'p95Ms': values[math.ceil(.95 * len(values)) - 1] if values else None,
            'maxMs': max(values) if values else None,
            'errors': sum(not x['correct'] for x in samples),
            'errorRate': sum(not x['correct'] for x in samples) / len(samples) if samples else None,
            'serialObservedUpdatesPerSecond': len(samples) * 1000 / span if span else None,
            'serialIntervalMs': span,
            'throughputScope': 'Single tab sequential instrumented run; interval includes Playwright gaps. Not concurrent users or server throughput.'}


def wait_sample(page, index):
    page.wait_for_function('(i) => window.__perf.records.length > i', arg=index, timeout=15000)
    return page.evaluate('(i) => window.__perf.records[i]', index)


def run_level(browser, count, args):
    data = seed(count)
    options = {'viewport': {'width': 1280, 'height': 900}, 'reduced_motion': 'reduce'}
    if args.record_video:
        options['record_video_dir'] = str(args.evidence_dir / 'videos' / str(count))
        options['record_video_size'] = {'width': 1280, 'height': 900}
    context = browser.new_context(**options)
    # Only first document load is seeded. Reload must read the application's persisted result.
    context.add_init_script(f"if (!sessionStorage.getItem('perf-seeded')) {{localStorage.setItem({json.dumps(KEY)}, {json.dumps(json.dumps(data))}); sessionStorage.setItem('perf-seeded','yes');}}")
    page = context.new_page()
    page.set_default_timeout(15000)
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto((args.app_dir / 'index.html').as_uri())
    expect(page.locator('#slots button')).to_have_count(10)
    assert page.evaluate('(key) => JSON.parse(localStorage.getItem(key)).appointments.length', KEY) == count
    page.locator('#role-reception').click()
    page.evaluate(INSTRUMENT, {'expectations': {d: expected_view(data, d) for d in DOCTORS}})
    samples = []
    # No warm-up trials discarded: all ten changes, including the first, are retained.
    for trial in range(10):
        target = 'selin' if trial % 2 == 0 else 'deniz'
        page.locator('#doctor-select').focus()
        page.keyboard.press('ArrowDown' if target == 'selin' else 'ArrowUp')
        sample = wait_sample(page, trial)
        sample['trial'] = trial + 1
        sample['recordCount'] = count
        assert sample['target'] == target and sample['trustedEvent'], sample
        samples.append(sample)
    summary = stats(samples)
    result = {'recordCount': count, 'fixtureSHA256': hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest(),
              'operation': 'Reception, 12 November 2030, doctor selection using native keyboard ArrowDown/ArrowUp',
              'samples': samples, 'summary': summary,
              'declaredThresholdMs': 1000 if count <= 20 else None,
              'instrumentedThresholdResult': ('PASS' if all(s['correct'] and s['durationMs'] <= 1000 for s in samples) else 'FAIL') if count <= 20 else 'EXPLORATORY_NO_ACCEPTANCE_THRESHOLD'}
    transactions = []
    # At the schema limit no extra record is valid. Measure its rejection, not invented capacity.
    page.locator('#role-patient').click()
    if count < 1000:
        for cycle in range(3):
            next_id = count + cycle + 1
            expected = {'id': f'R{next_id:03}', 'count': next_id, 'status': 'pending', 'label': LABELS['pending']}
            page.evaluate('(v) => window.__perf.mutationExpected = v', expected)
            page.locator('[data-time="09:30"]').click()
            before = page.evaluate('window.__perf.records.length')
            page.locator('#book-appointment').click()
            created = wait_sample(page, before)
            assert created['correct'], created
            transactions.append(created)
            expected.update(status='cancelled', label=LABELS['cancelled'])
            page.evaluate('(v) => window.__perf.mutationExpected = v', expected)
            page.once('dialog', lambda d: d.accept())
            before = page.evaluate('window.__perf.records.length')
            page.locator(f'[data-appointment-id="R{next_id:03}"] [data-action="cancel"]').click()
            cancelled = wait_sample(page, before)
            assert cancelled['correct'], cancelled
            transactions.append(cancelled)
        result['transactions'] = {'samples': transactions,
                                  'create': stats([s for s in transactions if s['kind'] == 'create']),
                                  'cancelAfterNativeConfirmation': stats([s for s in transactions if s['kind'] == 'cancel_after_confirmation']),
                                  'acceptanceThreshold': None,
                                  'scope': 'Exploratory; cancellation timer begins after native confirm returns accepted. Human decision time excluded.'}
    else:
        before_data = page.evaluate('(key) => localStorage.getItem(key)', KEY)
        page.locator('[data-time="09:30"]').click()
        page.locator('#book-appointment').click()
        assert page.evaluate('(key) => localStorage.getItem(key)', KEY) == before_data
        expect(page.locator('#notice-text')).to_contain_text('en fazla 1.000')
        result['capacityBoundary'] = {'status': 'PASS', 'recordCount': 1000, 'attemptedExtraRecord': 'rejected', 'dataUnchanged': True}
    saved = page.evaluate('(key) => JSON.parse(localStorage.getItem(key))', KEY)
    before_reload = time.perf_counter()
    page.reload()
    expect(page.locator('#slots button')).to_have_count(10)
    restored = page.evaluate('(key) => JSON.parse(localStorage.getItem(key))', KEY)
    assert restored == saved
    if count < 1000:
        expect(page.locator(f'[data-appointment-id="R{count+3:03}"] .status-pill')).to_have_text('İptal edildi')
    result['reloadRecovery'] = {'status': 'PASS', 'recordCount': len(restored['appointments']),
                                'persistedStateEqual': True, 'wallClockMsIncludingAutomation': (time.perf_counter() - before_reload) * 1000,
                                'scope': 'Same-origin reload, not crash durability or cross-device recovery; no latency acceptance threshold.'}
    result['pageErrors'] = errors
    assert not errors, errors
    context.close()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--app-dir', type=Path, default=ROOT)
    parser.add_argument('--evidence-dir', type=Path)
    parser.add_argument('--record-video', action='store_true')
    args = parser.parse_args()
    args.app_dir = args.app_dir.resolve()
    if args.record_video and not args.evidence_dir:
        parser.error('--record-video requires --evidence-dir')
    if args.evidence_dir:
        args.evidence_dir.mkdir(parents=True, exist_ok=True)
    paths = ['index.html', 'src/demo-data.js', 'src/repository.js', 'src/rules.js', 'src/ui.js']
    report = {'executedAt': datetime.now(timezone.utc).isoformat(), 'platform': platform.platform(),
              'logicalCpuCount': os.cpu_count(), 'machine': platform.machine(),
              'context': {'viewport': {'width': 1280, 'height': 900}, 'headless': True,
                          'reducedMotion': 'reduce', 'origin': 'file://', 'tabsPerContext': 1},
              'python': sys.version.split()[0], 'sources': {p: hashlib.sha256((args.app_dir/p).read_bytes()).hexdigest() for p in paths},
              'method': 'Native keyboard doctor changes; browser performance.now from capture-phase change to a second requestAnimationFrame. Correct slots, exact daily rows and totals checked together.',
              'limitations': ['Headless local single-tab browser; no server or multi-user load tested.',
                              'Two rAF callbacks are a paint-opportunity proxy, not a physical display measurement.',
                              'Instrumentation and content-oracle work add overhead.',
                              'Original NFR-02 screen-recording frame analysis is not claimed complete.',
                              'NFR-01 human usability and independent human acceptance are not simulated.',
                              '100/1000-record results are exploratory; no performance threshold was invented.'],
              'formalNFR02ScreenRecordingAcceptance': 'NOT_ASSESSED', 'results': []}
    failure = None
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True, executable_path=shutil.which('chromium'), args=['--no-sandbox'])
            report['browser'] = 'Chromium ' + browser.version
            for count in (7, 20, 100, 1000):
                report['results'].append(run_level(browser, count, args))
            browser.close()
    except Exception as exc:
        failure = {'type': type(exc).__name__, 'message': str(exc)}
    report['failure'] = failure
    report['technicalResult'] = 'PASS' if not failure and len(report['results']) == 4 and all(
        x['summary']['errors'] == 0 and x['instrumentedThresholdResult'] != 'FAIL' for x in report['results']) else 'FAIL'
    content = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    if args.evidence_dir:
        (args.evidence_dir/'performans-sonuclari.json').write_text(content, encoding='utf-8')
    print(content)
    return 0 if report['technicalResult'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
