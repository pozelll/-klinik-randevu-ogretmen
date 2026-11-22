"""Ayrı, yeni klasörde gerçek Gitflow deneyi. Ana ders deposuna push/merge yapmaz."""
from pathlib import Path
from datetime import datetime, timezone
from tempfile import TemporaryDirectory
import argparse
import hashlib
import json
import os
import shutil
import subprocess
from surum_kontrol import check, CORRECT_CANCEL

H9 = Path(__file__).resolve().parents[1]
PANEL = 'panel/surum.json'


def execute(output):
    if output.exists() and any(output.iterdir()):
        raise ValueError('Çıktı klasörü boş olmalı; önceki deneme veya çalışma silinmez.')
    output.mkdir(parents=True, exist_ok=True)
    lab = output/'lab-deposu'; lab.mkdir()
    logs = []; checks = []; commits = {}
    env = dict(os.environ)
    for key in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES'):
        env.pop(key, None)
    env.update({'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull,
                'GIT_TERMINAL_PROMPT': '0', 'GIT_EDITOR': 'true', 'LC_ALL': 'C.UTF-8'})

    def git(*args, allowed=(0,), cwd=lab):
        result = subprocess.run(['git', *args], cwd=cwd, env=env, capture_output=True, text=True)
        logs.append({'command': ['git', *args], 'exitCode': result.returncode,
                     'stdout': result.stdout.replace(str(output), '${LAB_OUTPUT}'),
                     'stderr': result.stderr.replace(str(output), '${LAB_OUTPUT}')})
        if result.returncode not in allowed:
            raise RuntimeError(f'git {args} başarısız: {result.stderr}')
        return result

    def record(id, condition, actual):
        if not condition:
            raise AssertionError(f'{id}: {actual}')
        checks.append({'id': id, 'status': 'PASS', 'actual': actual})

    def fixture(name):
        return (H9/'senaryolar'/f'{name}.json').read_text(encoding='utf-8')

    def write(name):
        (lab/PANEL).write_text(fixture(name), encoding='utf-8')

    def commit(key, message):
        git('add', PANEL); git('commit', '-m', message)
        commits[key] = git('rev-parse', 'HEAD').stdout.strip()
        return commits[key]

    git('init', '-b', 'main', '--object-format=sha1')
    git('config', 'user.name', 'YAZ325 Otomatik Ders Deneyi')
    git('config', 'user.email', 'ders@example.invalid')
    git('config', 'commit.gpgsign', 'false'); git('config', 'tag.gpgsign', 'false')
    git('config', 'core.autocrlf', 'false')
    (lab/'panel').mkdir(); write('00-baslangic')
    for name in ('index.html', 'style.css'):
        shutil.copyfile(H9/'panel'/name, lab/'panel'/name)
    (lab/'README.md').write_text('Gitflow öğretmen deneyi. 0.9.x yalnız panel laboratuvarıdır. Gerçek GitHub PR veya insan incelemesi içermez.\n', encoding='utf-8')
    git('add', '.'); git('commit', '-m', 'lab: ortak panel baslangici')
    commits['baseline'] = git('rev-parse', 'HEAD').stdout.strip()
    record('H9-G01', check(fixture('00-baslangic'))['passed'] == 5, 'Başlangıç panelinde 5/5 yapısal kontrol geçti; anlam doğrulanmadı.')
    git('switch', '-c', 'develop')
    git('switch', '-c', 'feature/hasta-bilgi')
    write('01-hasta'); commit('patient', 'feat: hasta bilgisini ekle')
    git('switch', 'develop'); git('switch', '-c', 'feature/personel-bilgi')
    write('02-personel'); commit('staff', 'feat: personel bilgisini ekle')
    common = git('merge-base', 'feature/hasta-bilgi', 'feature/personel-bilgi').stdout.strip()
    record('H9-G02', common == commits['baseline'], {'commonFeatureBase': common})
    git('switch', 'develop'); git('merge', '--no-ff', 'feature/hasta-bilgi', '-m', 'merge: hasta katkisini developa al')
    git('switch', 'feature/personel-bilgi')
    conflict = git('merge', '--no-ff', 'develop', '-m', 'merge: guncel developu personele al', allowed=(1,))
    unmerged = git('diff', '--name-only', '--diff-filter=U').stdout.strip()
    raw = (lab/PANEL).read_text(encoding='utf-8')
    (output/'cakisma-oncesi-cozulmemis.txt').write_text(raw, encoding='utf-8')
    record('H9-G03', conflict.returncode == 1 and unmerged == PANEL, {'expectedConflict': True, 'unmergedPath': unmerged})
    rejected = check(raw)
    record('H9-G04', rejected['status'] == 'FAIL', {'unresolvedPanelRejected': True, 'checks': rejected})
    write('03-cozum'); commit('resolution', 'merge: iki katkili duyuruyla cakismayi coz')
    resolved = json.loads((lab/PANEL).read_text(encoding='utf-8'))
    parents = git('rev-list', '--parents', '-n', '1', 'HEAD').stdout.split()[1:]
    record('H9-G05', len(parents) == 2 and 'Hastalar' in resolved['duyuru'] and 'personel' in resolved['duyuru'] and resolved['hasta_notu'] == json.loads(fixture('01-hasta'))['hasta_notu'] and resolved['personel_notu'] == json.loads(fixture('02-personel'))['personel_notu'], {'parents': parents, 'combinedAnnouncement': resolved['duyuru']})
    git('switch', 'develop'); git('merge', '--no-ff', 'feature/personel-bilgi', '-m', 'merge: personel ve cozumunu developa al')
    git('switch', '-c', 'release/0.9.0')
    write('04-release'); commit('release', 'release: panel 0.9.0 egitim surumu')
    git('switch', 'main'); git('merge', '--no-ff', 'release/0.9.0', '-m', 'merge: release 0.9.0 egitim ana dalina')
    commits['releaseMain'] = git('rev-parse', 'HEAD').stdout.strip()
    git('tag', '-a', 'egitim-hafta09-v0.9.0', '-m', 'Yalniz yerel Gitflow egitim senaryosu; klinik yayini degildir')
    tag_target = git('rev-parse', 'egitim-hafta09-v0.9.0^{}').stdout.strip()
    record('H9-G06', tag_target == commits['releaseMain'] and git('cat-file', '-t', 'egitim-hafta09-v0.9.0').stdout.strip() == 'tag', {'annotatedReleaseTagTarget': tag_target})
    git('switch', 'develop'); git('merge', '--no-ff', 'release/0.9.0', '-m', 'merge: release bilgisini developa tasi')
    # Eski rehberdeki yanlış cümle kontrollü senaryo girdisidir; gerçek uygulama kusuru değildir.
    late_finding = check(fixture('04-release'), meaning=True)
    record('H9-G07', late_finding['passed'] == 5 and late_finding['total'] == 6 and late_finding['status'] == 'FAIL', {'structuralPassMeaningFail': True, 'checks': late_finding})
    git('switch', 'main'); git('switch', '-c', 'hotfix/0.9.1')
    write('05-hotfix'); hotfix = commit('hotfix', 'fix: iptal kaydinin korundugunu acikla')
    final_checks = check(fixture('05-hotfix'), meaning=True)
    record('H9-G08', final_checks['status'] == 'PASS', final_checks)
    git('switch', 'main'); git('merge', '--no-ff', 'hotfix/0.9.1', '-m', 'merge: hotfix egitim ana dalina')
    commits['hotfixMain'] = git('rev-parse', 'HEAD').stdout.strip()
    git('tag', '-a', 'egitim-hafta09-v0.9.1', '-m', 'Yalniz yerel Gitflow egitim hotfix etiketi')
    git('switch', 'develop'); git('merge', '--no-ff', 'hotfix/0.9.1', '-m', 'merge: hotfixi developa da tasi')
    commits['develop'] = git('rev-parse', 'HEAD').stdout.strip()
    ancestry = {branch: git('merge-base', '--is-ancestor', hotfix, branch).returncode for branch in ('main', 'develop')}
    equal = git('diff', '--exit-code', 'main', 'develop', '--', PANEL).returncode == 0
    record('H9-G09', ancestry == {'main': 0, 'develop': 0} and equal, {'hotfixAncestorExitCodes': ancestry, 'panelContentsEqual': equal})
    latest_tag = git('rev-parse', 'egitim-hafta09-v0.9.1^{}').stdout.strip()
    record('H9-G10', latest_tag == commits['hotfixMain'] and git('rev-parse', 'egitim-hafta09-v0.9.0^{}').stdout.strip() == commits['releaseMain'], {'releaseTagUnmoved': commits['releaseMain'], 'hotfixTagTarget': latest_tag})
    history = git('log', '--graph', '--decorate', '--oneline', '--all').stdout
    (output/'git-gecmisi.txt').write_text(history, encoding='utf-8')
    bundle = (output/'YAZ325_Hafta09_Gitflow_Deneyi.bundle').resolve()
    git('bundle', 'create', str(bundle), '--all'); git('bundle', 'verify', str(bundle))
    clone = (output/'yeniden-acilan').resolve()
    git('clone', '-b', 'develop', str(bundle), str(clone), cwd=output)
    restored = git('show', 'HEAD:'+PANEL, cwd=clone).stdout
    record('H9-G11', json.loads(restored)['iptal_notu'] == CORRECT_CANCEL and git('rev-parse', 'HEAD', cwd=clone).stdout.strip() == commits['develop'], 'Bundle yeni klasöre klonlandı; son panel ve commit kimliği korundu.')
    record('H9-G12', git('status', '--porcelain').stdout == '' and git('remote').stdout == '', 'Deney deposu temiz; harici remote ve push yok.')
    graph = []
    for line in git('log', '--all', '--reverse', '--topo-order', '--format=%H|%P|%s').stdout.splitlines():
        sha, parent_text, subject = line.split('|', 2); graph.append({'sha': sha, 'parents': parent_text.split(), 'subject': subject})
    report = {'executedAt': datetime.now(timezone.utc).isoformat(), 'gitVersion': git('--version').stdout.strip(),
              'method': 'Yeni yerel Git deposunda gerçek commit, merge, çakışma, annotated tag ve bundle; insan incelemesi simüle edilmez.',
              'clinicalBaseline': 'a95a59b96d822f1225e4815b8c6ac4f928691cd5',
              'scope': '0.9.x yalnız panel laboratuvarıdır; Klinik uygulama 0.3.0-rc.1 olarak korunur. Yerel merge, GitHub PR merge veya insan onayı değildir.',
              'results': checks, 'commits': commits, 'graph': graph,
              'bundle': {'filename': bundle.name, 'bytes': bundle.stat().st_size, 'sha256': hashlib.sha256(bundle.read_bytes()).hexdigest()},
              'clinicalReleaseDecision': 'BEKLET: bağımsız inceleme, NFR ve performans kanıtı tamamlanmadı.'}
    (output/'gitflow-sonuclari.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (output/'komut-kaydi.json').write_text(json.dumps(logs, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output:
        report = execute(args.output.resolve())
    else:
        with TemporaryDirectory(prefix='yaz325-h9-') as temp:
            report = execute(Path(temp))
    print(json.dumps(report, ensure_ascii=False, indent=2))
