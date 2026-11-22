"""H9 sürüm paneli: beş yapısal kontrol ve isteğe bağlı anlam kapısı."""
from pathlib import Path
import argparse
import json

KEYS = {'surum', 'kanal', 'duyuru', 'hasta_notu', 'personel_notu', 'iptal_notu'}
CORRECT_CANCEL = 'İptal edilen randevu geçmişte korunur; saat yeniden uygun olur.'


def check(raw, meaning=False):
    data = None
    try:
        data = json.loads(raw)
    except (ValueError, TypeError):
        pass
    checks = [
        ('P01', 'JSON nesnesi okunabilir', isinstance(data, dict)),
        ('P02', 'Altı beklenen alan var', isinstance(data, dict) and set(data) == KEYS),
        ('P03', 'Alanlar boş olmayan kısa metin', isinstance(data, dict) and set(data) == KEYS and all(isinstance(v, str) and 0 < len(v.strip()) <= 300 for v in data.values())),
        ('P04', 'Ders sürümü ve kanal uyumlu', isinstance(data, dict) and isinstance(data.get('surum'), str) and ((data.get('surum') == '0.9.0-dev' and data.get('kanal') == 'gelistirme') or (data.get('surum') in {'0.9.0', '0.9.1'} and data.get('kanal') == 'egitim'))),
        ('P05', 'Çakışma işareti yok', bool(raw) and not any(m in raw for m in ('<<<<<<<', '=======', '>>>>>>>'))),
    ]
    if meaning:
        checks.append(('A01', 'İptal açıklaması korunmuş kayıt davranışıyla uyumlu', isinstance(data, dict) and data.get('iptal_notu') == CORRECT_CANCEL))
    return {'scope': 'Sürüm paneli kontrolü; klinik uygulama testleri veya insan incelemesi değildir.',
            'checks': [{'id': id, 'name': name, 'passed': bool(ok)} for id, name, ok in checks],
            'passed': sum(bool(c[2]) for c in checks), 'total': len(checks),
            'status': 'PASS' if all(c[2] for c in checks) else 'FAIL'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path, nargs='?', default=Path(__file__).resolve().parents[1]/'panel/surum.json')
    parser.add_argument('--anlam', action='store_true')
    args = parser.parse_args()
    report = check(args.file.read_text(encoding='utf-8'), args.anlam)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['status'] == 'PASS' else 1)
