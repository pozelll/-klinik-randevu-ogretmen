"""H8: tanımlı kaynaktan tekrarlanabilir, çevrimdışı ders paketi.

SHA-256 içerik doğrulamasıdır; dijital imza veya yayın onayı değildir.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CONFIG = 'hafta08/config/surum-adayi.json'
APP_FILES = ('index.html', 'src/demo-data.js', 'src/repository.js',
             'src/rules.js', 'src/ui.js', 'LICENSE')
STAMP = (1980, 1, 1, 0, 0, 0)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8')


def definition(root=ROOT):
    value = json.loads((root / CONFIG).read_text(encoding='utf-8'))
    if set(value['sourceFiles']) != set(APP_FILES):
        raise ValueError('Aday tanımında kaynak dosya listesi beklenen listeyle aynı değil.')
    if len(value['sourceCommit']) != 40:
        raise ValueError('Tam kaynak commit kimliği gerekli.')
    return value


def expected_payload(root=ROOT):
    spec = definition(root)
    payload = {}
    for name in APP_FILES:
        data = (root / name).read_bytes()
        if digest(data) != spec['sourceFiles'][name]:
            raise ValueError('Kaynak dosya aday tanımıyla uyuşmuyor: ' + name)
        payload[name] = data
    readme = (root / 'hafta08/config/PAKET_README.md').read_bytes()
    if digest(readme) != spec['packageReadmeSha256']:
        raise ValueError('Paket yönergesi aday tanımıyla uyuşmuyor.')
    payload['README.md'] = readme
    payload['SURUM.json'] = json_bytes(spec)
    payload['SHA256SUMS.txt'] = ''.join(
        f'{digest(payload[name])}  {name}\n' for name in sorted(payload)
    ).encode('utf-8')
    return payload


def write_archive(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, STAMP)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, data)


def build(path, root=ROOT):
    # Kaynak hatasını çıktı yazılmadan önce yakala.
    payload = expected_payload(root)
    write_archive(path, payload)
    return verify(path, root)


def verify(path, root=ROOT):
    expected = expected_payload(root)
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != set(expected):
            raise ValueError('Paket dosya listesi eksik, fazla veya tekrarlı.')
        for name, data in expected.items():
            info = archive.getinfo(name)
            if info.file_size != len(data):
                raise ValueError('Dosya boyutu uyuşmuyor: ' + name)
            if archive.read(name) != data:
                raise ValueError('Dosya içeriği veya özeti uyuşmuyor: ' + name)
    return {'status': 'PASS', 'version': definition(root)['version'],
            'sourceCommit': definition(root)['sourceCommit'],
            'sha256': digest(path.read_bytes()), 'bytes': path.stat().st_size,
            'fileCount': len(expected), 'files': sorted(expected)}


def extract(path, target, root=ROOT):
    result = verify(path, root)
    if target.exists() and any(target.iterdir()):
        raise ValueError('Ayıklama hedefi boş olmalı; mevcut dosyaların üzerine yazılmaz.')
    target.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path) as archive:
        # verify yalnız sabit izinli adları kabul etti; extractall kullanılmaz.
        for name in sorted(expected_payload(root)):
            destination = target / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(archive.read(name))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    b = sub.add_parser('build'); b.add_argument('--output', type=Path, required=True)
    v = sub.add_parser('verify'); v.add_argument('package', type=Path)
    e = sub.add_parser('extract'); e.add_argument('package', type=Path); e.add_argument('--target', type=Path, required=True)
    args = parser.parse_args()
    if args.action == 'build': result = build(args.output)
    elif args.action == 'verify': result = verify(args.package)
    else: result = extract(args.package, args.target)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
