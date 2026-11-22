# 7. hafta / 4. basamak — Kabulü gözlenebilir yaptık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Kabul koşulu önce beklediğimiz davranışı tarif eder; test onu gerçekten çalıştırır. Başlangıçta onay kapalıdır. Saat seçince yardım değişir ama kayıt sayısı değişmez. Onaylayınca tek yeni kayıt oluşur. Başarı sadece ekrandaki yazıya bakılarak değerlendirilmez.

## Ekranda göster ve uygula

Beş satırlık kabul tablosunu açın. B02’de başlangıç verisi 7 kayıt, seçim sonrası yine 7 ve onay sonrası 8 kayıttır. B03’te hasta, doktor ve tarih değişiminin seçimi temizlediğini gösterin. B04’te doktor rolünün randevu oluşturamadığını, B05’te 390 px kontrolünün sınırını açıklayın.

- [04-kabul-kosullari.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/hafta07/docs/04-kabul-kosullari.md)
- [browser_smoke.py](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/tests/browser_smoke.py)

## Öğrenciye soru

**390 px ekranda taşma olmaması erişilebilirliği kanıtlar mı?**

Beklenen açıklama: Hayır. Yalnız bu görünüm kontrolünün sonucudur. Klavye, ekran okuyucu ve gerçek kullanıcı değerlendirmesi ayrıca gerekir.

## Grubun yapacağı iş

Kendi değişikliğin için olumlu, olumsuz ve durum değişimi içeren üç kabul senaryosu yaz.

Kontrol: Beklenen sonuç, test kimliği ve gerçek sonuç arasında bire bir bağlantı var mı?

## Hazırlığın gerçek durumu

H7-B01–B05: beş kabul kontrolü. Kapsamlı erişilebilirlik ölçümü değil.

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)

## Kabul tablosu

| Kimlik | Başlangıç ve eylem | Beklenen sonuç | Gerçek |
|---|---|---|---|
| H7-B01 | Yeni oturum aç | Yardım görünür, onay kapalı, 7 kayıt | PASS |
| H7-B02 | 09:30 seç; ardından onayla | Seçimde 7; onayda 8 kayıt ve nextId=9; yardım başlangıca döner | PASS |
| H7-B03 | 13:30 seç; hasta, doktor, tarihi sırayla değiştir | Her değişimde seçim ve eski saat metni silinir; veri aynı | PASS |
| H7-B04 | Seçimden sonra doktor rolü; sonra resepsiyon ve Kaan | Doktorda 10 saat kapalı; resepsiyon Kaan adına kayıt açar | PASS |
| H7-B05 | 390 × 844 px görünümde saat seç | Yardım görünür, yatay taşma yok, 7 kayıt | PASS |

Bu satırların yürütüm ayrıntıları `../kanitlar/tarayici-sonuclari.json` içindedir. Definition of Done: kabul ve regresyon geçti, sürüm/kanıt/belge bağlı; bağımsız inceleme ve birleştirme tamamlanmadığı için bütün DoD kapandı denmez.
