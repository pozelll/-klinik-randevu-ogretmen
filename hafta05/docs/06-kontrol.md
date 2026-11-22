# 5. hafta / 6. basamak - İlk kontrolleri çalıştırdık

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

Testin geçmesi tanımlanan beklentinin belirli veriyle sağlandığını gösterir. Bütün sistemin hatasızlığı veya bağımsız kişi onayı anlamına gelmez. İlk sekiz test sorumlulukları ayırırken kritik davranışların korunmasına odaklanır.

## Ekranda ne açacağım, ne yapacağım?

Proje kökünde node --test tests/h5-smoke.test.cjs komutunu çalıştırın. Kanıt dosyasını açıp sekiz test adını sonuçlarla eşleştirin. H5-S04’te iptal, yeniden oluşturma ve tamamlama zincirini; H5-S06’da yazma hatasına rağmen oturum belleğinin değişmesini gösterin.

- [tests/h5-smoke.test.cjs](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/tests/h5-smoke.test.cjs)
- [06-kontrol.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/06-kontrol.md)
- [Node test sonucu](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/kanitlar/node-test-sonuclari.tap)

## Kontrol sorusu

Komut doğru kökte mi çalıştırıldı? Gerçek sonuç ve sürüm kaydı var mı? 8/8 sonucu yalnız bu testlere mi atfediliyor?

**Öğrenciye soru:** 8/8 geçtiğinde bağımsız inceleme kutusunu işaretleyebilir miyiz?

**Beklenen açıklama:** Hayır. Otomatik test ile başka kişinin kod ve kanıt incelemesi farklı işlerdir.

## Öğrencinin yapacağı iş

Testi kendi çalışma kopyanda çalıştır. Tarih, commit, araç sürümü ve gerçek sonucu kaydet; çalıştırmadığın testi geçti yazma.

## Öğretmen örneğinin gerçek durumu

H5-S01–H5-S08: 8/8 geçti. Tarayıcı regresyonu H6’da ayrıca izlenir.

Görev: [#13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13) · İnceleme paketi: [PR #15](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.
