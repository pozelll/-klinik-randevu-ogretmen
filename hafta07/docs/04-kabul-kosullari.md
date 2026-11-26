# 7. hafta / 4. adım - Kabul koşulları

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Değişikliğin kabul edilmesi için gereken davranışları çalıştırmadan önce tanımlamak; beklenen ve gerçekleşen sonuçları ayrı kaydetmek.

Kabul koşulu gözlenebilir bir sonuç içermelidir. Örnek saat yardımında açıklamanın değişmesiyle birlikte verinin hangi anda değiştiği de sınanır. Ekrandaki metin ve kayıt sayısı ayrı gözlemlenir.

## Grup çalışması

1. Kendi değişikliğiniz için olumlu, olumsuz ve durum değişimi içeren en az üç kabul senaryosu yazın.
2. Her senaryoya kimlik verin; başlangıç verisini, eylemi ve beklenen sonucu tanımlayın.
3. Senaryoları kendi sürümünüzde çalıştırıp gerçek sonucu ve kanıt bağlantısını ekleyin.
4. Her kabul koşulunu ilgili gereksinime ve test kimliğine bağlayın.

## Teslim edilecek çıktı

Senaryo kimliği, başlangıç durumu, eylem, beklenen sonuç, gerçek sonuç ve kanıt bağlantısı içeren kabul tablosu.

## Tarihli örnek kabul tablosu

Tablodaki PASS sonuçları 22 Kasım 2026 tarihli örnek yürütüme aittir; grubunuzun kendi çalıştırma sonucu olarak kullanılamaz.

| Kimlik | Başlangıç ve eylem | Beklenen sonuç | Gerçek |
|---|---|---|---|
| H7-B01 | Yeni oturum aç | Yardım görünür, onay kapalı, 7 kayıt | PASS |
| H7-B02 | 09:30 seç; ardından onayla | Seçimde 7; onayda 8 kayıt ve nextId=9; yardım başlangıca döner | PASS |
| H7-B03 | 13:30 seç; hasta, doktor, tarihi sırayla değiştir | Her değişimde seçim ve eski saat metni silinir; veri aynı | PASS |
| H7-B04 | Seçimden sonra doktor rolü; sonra resepsiyon ve Kaan | Doktorda 10 saat kapalı; resepsiyon Kaan adına kayıt açar | PASS |
| H7-B05 | 390 × 844 px görünümde saat seç | Yardım görünür, yatay taşma yok, 7 kayıt | PASS |

Yürütüm ayrıntıları [tarayıcı sonuçlarında](../kanitlar/tarayici-sonuclari.json) bulunur. 390 px görünüm kontrolü; klavye, ekran okuyucu veya gerçek kullanıcı değerlendirmesinin yerine geçmez.

Tamamlanma ölçütlerini (Definition of Done) ayrı izleyin: kabul ve regresyon sonuçları, sürüm ve belge bağlantıları, gerçek inceleme ve birleştirme durumu. Bir ölçütün tamamlanması diğerlerinin de tamamlandığı anlamına gelmez.

[browser_smoke.py](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/tests/browser_smoke.py)

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)
