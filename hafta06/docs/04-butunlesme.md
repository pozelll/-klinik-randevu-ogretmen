# 6. hafta / 4. basamak - Bütünleşmeyi denedik

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

Bir bileşenin tek başına doğru olması, birlikte çalıştıklarında eski verinin yazılmadığını göstermez. Oluşturma, iptal ve tamamlama aynı depoyu kullanmalıdır. Yazma hatasında oturum verisi ile son kalıcı kopyanın ayrımı ayrıca sınanır.

## Ekranda ne açacağım, ne yapacağım?

node --test tests/*.test.cjs komutuyla tüm Node testlerini çalıştırın. H6-R06’da başarısız yazmadan sonra son kalıcı kopyanın korunduğunu; H6-R04’te başlangıç BR-01 çakışmasının saptandığını gösterin. H6-R14, ürün akışının normalde oluşturmadığı çakışmayı kontrollü olarak depoya ekleyen dayanıklılık deneyidir.

- [tests/h6-regression.test.cjs](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/h6-regression.test.cjs)
- [04-butunlesme.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/docs/04-butunlesme.md)
- [Node test sonucu](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/kanitlar/node-test-sonuclari.tap)

## Kontrol sorusu

30 testin içinde H5’in 8 testi yeniden sayılıyor mu? 30’a ayrıca 8 eklenmemelidir. Bozuk biçim, iş kuralı çakışması ve saklama hatası ayrılıyor mu?

**Öğrenciye soru:** Bir testte kullanılan sahte saklama nesnesi gerçek localStorage mıdır?

**Beklenen açıklama:** Hayır. Kontrollü test ikamesidir. Hata durumlarını tekrarlanabilir kılar; gerçek tarayıcı akışı ayrıca sınanır.

## Öğrencinin yapacağı iş

Ortak veri kullanan iki işlemi art arda sınayıp ilk işlemin sonucunun kaybolmadığını göster.

## Öğretmen örneğinin gerçek durumu

8 H5 + 7 karar + 15 regresyon = 30/30. İptal → oluşturma → tamamlama aynı depoda.

Görev: [#14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · İnceleme paketi: [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.
