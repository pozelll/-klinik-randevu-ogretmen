# 6. hafta / 3. basamak - Kuralları kanıtladık

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

Yalnız ret mesajını kontrol etmek yeterli değildir. Reddedilen isteğin kaydı gizlice değiştirmediğini de göstermeliyiz. Bu yüzden sonucu, önce/sonra veri eşitliğini, update çağrısını ve kalıcı yazma sayısını birlikte denetliyoruz.

## Ekranda ne açacağım, ne yapacağım?

node --test tests/h6-decision.test.cjs komutunu gösterin. Kanıt JSON’unda DK-K02 için updateCalls:0 ve storageWritesDuringRequest:0 alanlarını bulun. DK-K07’de status değişir; toplam kayıt sayısı, nextId ve diğer kayıtlar korunur.

- [tests/h6-decision.test.cjs](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/h6-decision.test.cjs)
- [Karar satırı kanıtları](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/kanitlar/karar-tablosu-sonuclari.json)
- [03-kural-testleri.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/docs/03-kural-testleri.md)

## Kontrol sorusu

Kanıt gerçek test yürütümünden mi üretildi? Ret satırlarında bütün veri aynı mı? Başarılı iptalde yalnız amaçlanan kayıt mı değişti?

**Öğrenciye soru:** Test mesajı doğru olsa da veri yanlışlıkla değişmiş olabilir mi?

**Beklenen açıklama:** Evet. Bu nedenle sadece mesajı değil, veri durumunu ve yan etkileri de karşılaştırırız.

## Öğrencinin yapacağı iş

Bir ret senaryosunu seç; önce/sonra veriyi ve yazma sayısını ayrı göster. Sonucu kendi çalıştırdığın sürümle eşleştir.

## Öğretmen örneğinin gerçek durumu

7/7 karar satırı geçti. Başarılı iptal toplamı ve nextId değerini korur.

Görev: [#14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · İnceleme paketi: [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.
