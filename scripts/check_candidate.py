"""Gerçek üretim ve kontrollü bozulma denemeleri; dağıtım dosyasını değiştirmez."""
from pathlib import Path
from tempfile import TemporaryDirectory
from datetime import datetime, timezone
from html.parser import HTMLParser
import argparse
import json
import shutil
import build_candidate as candidate


def must_reject(action):
    try:
        action()
    except ValueError as exc:
        return str(exc)
    raise AssertionError('Bozuk girdi reddedilmedi.')


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__(); self.names = []
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            attributes = dict(attrs)
            if 'src' in attributes: self.names.append(attributes['src'])


def run(profile='h8'):
    results = []
    config, readme = candidate.profile_paths(profile)
    def passed(id, actual): results.append({'id': id.replace('H8-', profile.upper()+'-'), 'status': 'PASS', 'actual': actual})
    with TemporaryDirectory(prefix=profile+'-candidate-') as temp:
        temp = Path(temp); a = temp/'a.zip'; b = temp/'b.zip'
        first = candidate.build(a, profile=profile); second = candidate.build(b, profile=profile)
        assert a.read_bytes() == b.read_bytes()
        passed('H8-P01', {'twoBuildsSameBytes': True, 'firstSha256': first['sha256'], 'secondSha256': second['sha256']})
        assert first['fileCount'] == 9
        passed('H8-P02', {'verifiedManifest': True, 'fileCount': 9, 'sourceCommit': first['sourceCommit']})
        payload = candidate.expected_payload(profile=profile)
        changed = dict(payload); changed['src/ui.js'] = b'X' + payload['src/ui.js'][1:]
        bad = temp/'changed.zip'; candidate.write_archive(bad, changed)
        passed('H8-P03', must_reject(lambda: candidate.verify(bad, profile=profile)))
        missing = dict(payload); del missing['src/rules.js']
        bad2 = temp/'missing.zip'; candidate.write_archive(bad2, missing)
        passed('H8-P04', must_reject(lambda: candidate.verify(bad2, profile=profile)))
        extra = dict(payload); extra['beklenmeyen.txt'] = b'extra'
        bad3 = temp/'extra.zip'; candidate.write_archive(bad3, extra)
        passed('H8-P05', must_reject(lambda: candidate.verify(bad3, profile=profile)))
        changed['SHA256SUMS.txt'] = ''.join(f'{candidate.digest(changed[name])}  {name}\n' for name in sorted(changed) if name != 'SHA256SUMS.txt').encode('utf-8')
        bad4 = temp/'self-consistent.zip'; candidate.write_archive(bad4, changed)
        passed('H8-P06', must_reject(lambda: candidate.verify(bad4, profile=profile)))
        source = temp/'source'
        for name in (*candidate.APP_FILES, config, readme):
            dest = source/name; dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(candidate.ROOT/name, dest)
        (source/'src/ui.js').write_bytes(b'changed-source')
        rejected_output = temp/'must-not-exist.zip'
        message = must_reject(lambda: candidate.build(rejected_output, source, profile))
        assert not rejected_output.exists()
        passed('H8-P07', message)
        target = temp/'extracted'; candidate.extract(a, target, profile=profile)
        parser = Scripts(); parser.feed((target/'index.html').read_text(encoding='utf-8'))
        assert parser.names == ['src/demo-data.js', 'src/repository.js', 'src/rules.js', 'src/ui.js']
        assert all((target/name).is_file() for name in parser.names)
        assert len([x for x in target.rglob('*') if x.is_file()]) == 9
        passed('H8-P08', {'extractionComplete': True, 'scriptReferences': parser.names})
        assert candidate.verify(a, profile=profile)['sha256'] == first['sha256']
    return {'executedAt': datetime.now(timezone.utc).isoformat(),
            'method': 'Python stdlib; iki gerçek üretim ve geçici kopyalarda kontrollü bozulma',
            'package': first, 'results': results,
            'scope': 'İçerik/üretim kontrolü; dijital imza, kullanıcı kabulü veya bağımsız inceleme değildir.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--evidence', type=Path)
    parser.add_argument('--profile', choices=candidate.PROFILE_PATHS, default='h8')
    args = parser.parse_args()
    report = run(args.profile); text = json.dumps(report, ensure_ascii=False, indent=2)+'\n'
    if args.evidence:
        args.evidence.parent.mkdir(parents=True, exist_ok=True); args.evidence.write_text(text, encoding='utf-8')
    print(text)
