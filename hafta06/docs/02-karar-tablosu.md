# 6. hafta / 2. basamak - Yedi karar satırını kurduk

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

Karar tablosu koşullar ile beklenen eylem arasındaki ilişkiyi görünür kılar. Burada yedi temsil edici satır var; bütün olası birleşimleri kapsadığı iddia edilmiyor. Satırlar aynı değişmiş veriyi paylaşırsa yanlış bir başlangıcı sınayabiliriz.

## Ekranda ne açacağım, ne yapacağım?

Tablodaki K01 bulunmayan kayıt; K02 resepsiyon; K03 doktor; K04 başka hasta; K05 Tamamlandı; K06 İptal edildi; K07 kendi Bekliyor kaydı satırlarını okuyun. Her testin seedData ile yeni bir veri kümesi kurduğunu gösterin.

- [02-karar-tablosu.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/docs/02-karar-tablosu.md)
- [tests/h6-decision.test.cjs](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/h6-decision.test.cjs)

## Kontrol sorusu

Her satırın başlangıç durumu doğru mu? K07 öncesi başka testin iptali taşınmış mı? Test numarası, kanıt ve beklenen sonuç aynı mı?

**Öğrenciye soru:** K05 ile K06 aynı hata kodunu döndürürken neden ayrı satırdır?

**Beklenen açıklama:** Tamamlandı ve İptal edildi iki farklı başlangıç durumudur. Aynı ret kodu, ikisinin de ayrı sınanması gereğini ortadan kaldırmaz.

## Öğrencinin yapacağı iş

Her satır için koşul ve beklenen veri değişimini yaz. Yedi satırın tamamına tek ekran görüntüsü ekleme.

## Öğretmen örneğinin gerçek durumu

DK-K01–DK-K07 ayrı ayrı tanımlandı. Her satır yeni veriyle başlar; önceki sonucu taşımaz.

Görev: [#14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · İnceleme paketi: [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.

## Yedi satırın kesin eşleştirmesi

| Satır | Kayıt | Rol | Sahiplik | Durum | Beklenen | İstek sırasında update / kalıcı yazma |
|---|---|---|---|---|---|---|
| DK-K01 | Yok (R999) | Hasta | Uygulanmaz | Uygulanmaz | NOT_FOUND | 0 / 0 |
| DK-K02 | R001 | Resepsiyon | Ece'nin | Bekliyor | ROLE | 0 / 0 |
| DK-K03 | R001 | Doktor | Ece'nin | Bekliyor | ROLE | 0 / 0 |
| DK-K04 | R001 | Hasta: Kaan | Başkasının | Bekliyor | OWNER | 0 / 0 |
| DK-K05 | R001 | Hasta: Ece | Kendi | Tamamlandı | STATUS | 0 / 0 |
| DK-K06 | R001 | Hasta: Ece | Kendi | İptal edildi | STATUS | 0 / 0 |
| DK-K07 | R001 | Hasta: Ece | Kendi | Bekliyor | OK; İptal edildi | 1 / 1 |

Her satır yeni seedData, yeni depo ve yeni servis ile çalışır. Başlangıçtaki hazırlık yazımları istek sırasındaki yazma sayısına dahil edilmez. K07'de depolama kullanılabilir olduğu için 1 kalıcı yazma vardır; saklama hatası ayrı testtir.
