# 6. hafta / 5. basamak - Tarayıcı testleri

## Amaç

Kullanıcının düğme, liste, onay penceresi ve günlük toplamlarla izlediği akışı uygulama üzerinde sınayın. Vazgeçme ile onaylı iptali ayrı senaryolar olarak kaydedin.

## Çalışma

1. [Yeniden çalıştırma rehberine](10-yeniden-calistirma.md) göre uygulamayı ve tarayıcı test ortamını hazırlayın.
2. Kendi çalışma sürümünüzde vazgeçme ve onaylı iptal akışlarını çalıştırın. Tarayıcı, tarih, başlangıç verisi ve gerçek sonucu yazın.
3. [Tarayıcı test dosyasındaki](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/browser_smoke.py) H3-T02 ve H3-T03 senaryolarını karşılaştırın.
4. Oluşturma, iptal ve tamamlama sonrasında seçili doktor/gün toplamlarıyla bütün veri kümesindeki kayıt sayısını ayrı kaydedin.

## Teslim edilecek çıktı

Her senaryo için başlangıç durumu, kullanıcı işlemi, beklenen ve gerçekleşen sonuç, test edilen commit ve kanıt bağlantısı. Önceki haftadaki ekran görüntülerini yeni çalıştırma sonucu olarak kullanmayın.

## Örnek kanıt

22 Kasım 2026 tarihli [tarayıcı sonuçlarında](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/kanitlar/tarayici-sonuclari.json) 9/9 Chromium senaryosu başarılıdır. T06'nın yeni sentetik başlangıcında seçili doktor/gün toplamı 4 → 5 → 5 → 5, bütün veri kümesindeki kayıt sayısı 7 → 8'dir. Bu değerler aynı başlangıç verisi için değerlendirilir.

Bu senaryolar kapsamlı kullanılabilirlik veya klavye erişilebilirliği ölçümü değildir; bu ölçümler ayrı planlanır.

[Görev #14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · [PR #16 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16)
