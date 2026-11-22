# 7. hafta / 6. basamak — Yeni ve eski akışı sınadık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Yeni özelliğin testinin geçmesi eski davranışın korunduğunu tek başına göstermez. Bu nedenle iptal, oluşturma, rol, saklama ve dar ekran akışlarını da yeniden çalıştırdık. Test kaydı hangi sürümde, hangi ortamda ve neyi kontrol ettiğimizi açıklamalıdır.

## Ekranda göster ve uygula

CI kaydını ve tarayıcı sonuçlarını açın. H7-B02’nin seçim öncesi/sonrası veriyi karşılaştırdığını gösterin. 30 Node testinin H5’ten gelen 8, karar tablosundan 7 ve regresyondan 15 testten oluştuğunu hatırlatın. Chromium sürümünü ve kaynak dosyaların SHA-256 özetlerini bulun.

- [06-test-kaniti.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/hafta07/docs/06-test-kaniti.md)
- [Tarayıcı sonuçları](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/hafta07/kanitlar/tarayici-sonuclari.json)
- [Başarılı CI koşusu](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45020807054)

## Öğrenciye soru

**30 + 14 sonucu 44 farklı gereksinimin sağlandığı anlamına gelir mi?**

Beklenen açıklama: Hayır. Bunlar farklı katmanlardaki kontrollerdir; aynı davranışı birden çok düzeyde sınayabilirler.

## Grubun yapacağı iş

Testlerini kendi sürümünde çalıştır. Başarısızlığı saklama; düzeltme commit’i ve yeniden kontrol sonucunu ekle.

Kontrol: Her “geçti” ifadesinin yürütüm kaydı ve kaynak sürümü bulunuyor mu?

## Hazırlığın gerçek durumu

30/30 Node · 14/14 Chromium geçti. Sonuçlar kaynak commit’iyle bağlı.

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)

## Yeniden çalıştırma

```bash
node --test --test-reporter=tap tests/*.test.cjs
python -m pip install playwright
python -m playwright install chromium
python tests/browser_smoke.py
```

Linux CI, tarayıcı sistem bağımlılıkları için `python -m playwright install --with-deps chromium` kullanır. Varsayılan test komutu eski kanıt dosyalarını değiştirmez. Kendi kaydınız için `--evidence-dir kendi-kanit-klasorunuz` verin.

Gerçek koşu: [45020807054](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45020807054), kaynak `bd5fa3fb2c35d1c11864eed982fdbc20d539d58a`, Chromium 157.0.8103.0. 30/30 Node ve 14/14 tarayıcı kontrolü başarılı. Node TAP dosyası çalışma ortamındaki gerçek yürütümdür; CI özeti ve tarayıcı JSON'u GitHub Actions yürütümündendir. NFR-01–NFR-03 ölçümleri bu sayılara dahil değildir.
