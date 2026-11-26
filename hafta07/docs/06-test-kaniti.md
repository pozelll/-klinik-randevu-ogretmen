# 7. hafta / 6. adım - Kabul ve regresyon testleri

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Yeni davranışı ve önceki akışların korunduğunu sınamak; her sonucu test edilen sürüme ve çalıştırma ortamına bağlamak.

Kabul testleri yeni değişikliği, regresyon testleri önceki davranışları kontrol eder. Farklı düzeylerdeki testler aynı gereksinimi sınayabildiğinden test sayısı doğrudan gereksinim sayısı olarak yorumlanmaz.

## Grup çalışması

1. Testleri kendi çalışma sürümünüzde çalıştırın.
2. Komutu, tarihi, tam commit'i ve araç sürümlerini kaydedin.
3. Başarılı ve başarısız sonuçları gerçek çıktıdan aktarın. Başarısızlık varsa düzeltme commit'ini ve yeniden kontrol sonucunu ekleyin.
4. Yerel test yürütümünü ve GitHub Actions koşusunu ayrı kaydedin.

## Yeniden çalıştırma

Proje kökünde:

```bash
node --test --test-reporter=tap tests/*.test.cjs
python -m pip install playwright
python -m playwright install chromium
python tests/browser_smoke.py
```

Linux CI, tarayıcı sistem bağımlılıkları için `python -m playwright install --with-deps chromium` kullanır. Varsayılan test komutu eski kanıt dosyalarını değiştirmez. Kendi tarayıcı kaydınızı üretmek için:

```bash
python tests/browser_smoke.py --evidence-dir kendi-kanit-klasorunuz
```

## Teslim edilecek çıktı

Test edilen commit, komut, ortam, tarih, gerçek sonuç dosyası ve varsa düzeltme/yeniden kontrol bağlantıları.

## Tarihli örnek sonuçlar

22 Kasım 2026 tarihli örnek: **30/30 Node testi ve 14/14 Chromium senaryosu başarılıdır.** Node testleri 8 H5, 7 karar tablosu ve 15 regresyon testinden oluşur. Tarayıcıda 9 önceki senaryoya 5 H7 senaryosu eklenmiştir. NFR-01–NFR-03 ölçümleri bu sayılara dahil değildir.

- Kaynak: `bd5fa3fb2c35d1c11864eed982fdbc20d539d58a`.
- Chromium: `157.0.8103.0`.
- [GitHub Actions koşusu: 45020807054](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45020807054).
- [Tarayıcı sonuçları ve kaynak dosya özetleri](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/hafta07/kanitlar/tarayici-sonuclari.json).
- [Node TAP kaydı](../kanitlar/node-test-sonuclari.tap) yerel çalışma ortamındaki gerçek yürütümdür; CI özeti ve tarayıcı JSON'u GitHub Actions yürütümündendir.

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)
