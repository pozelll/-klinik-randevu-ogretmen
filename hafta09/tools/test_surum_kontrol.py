"""Sürüm alanındaki bozuk JSON türleri rapor üretimini çökertmemeli."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys
import unittest

from surum_kontrol import check


TOOLS = Path(__file__).resolve().parent
FINAL_PANEL = TOOLS.parent / 'panel' / 'surum.json'


class PanelValidationTests(unittest.TestCase):
    def test_final_panel_passes_all_six_checks(self):
        report = check(FINAL_PANEL.read_text(encoding='utf-8'), meaning=True)
        self.assertEqual((report['status'], report['passed'], report['total']),
                         ('PASS', 6, 6))

    def test_container_version_is_rejected_without_exception(self):
        for invalid in ([], {'major': 0, 'minor': 9}):
            with self.subTest(version=invalid):
                data = json.loads(FINAL_PANEL.read_text(encoding='utf-8'))
                data['surum'] = invalid
                report = check(json.dumps(data), meaning=True)
                self.assertEqual(report['status'], 'FAIL')
                checks = {row['id']: row['passed'] for row in report['checks']}
                self.assertFalse(checks['P03'])
                self.assertFalse(checks['P04'])
                self.assertTrue(checks['A01'])
                self.assertEqual(report['total'], 6)

    def test_broken_json_produces_a_failed_report(self):
        report = check('{"surum":', meaning=True)
        self.assertEqual(report['status'], 'FAIL')
        checks = {row['id']: row['passed'] for row in report['checks']}
        self.assertFalse(checks['P01'])
        self.assertFalse(checks['P04'])
        self.assertFalse(checks['A01'])

    def test_cli_rejects_bad_version_with_json_and_exit_one(self):
        data = json.loads(FINAL_PANEL.read_text(encoding='utf-8'))
        data['surum'] = []
        with TemporaryDirectory(prefix='h9-invalid-panel-') as temp:
            path = Path(temp) / 'surum.json'
            path.write_text(json.dumps(data), encoding='utf-8')
            result = subprocess.run(
                [sys.executable, str(TOOLS / 'surum_kontrol.py'), str(path), '--anlam'],
                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stderr, '')
        report = json.loads(result.stdout)
        self.assertEqual(report['status'], 'FAIL')
        self.assertEqual(report['total'], 6)


if __name__ == '__main__':
    unittest.main()
