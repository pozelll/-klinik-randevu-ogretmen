# 5. hafta / 3. basamak - Veri erişimini ayırdık

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

Depo kimin iptal edebileceğini belirlemez; veriyi tutar. Kalıcı saklama kullanılamıyorsa oturum belleğiyle devam eder. demo-data.js ise sabit kişiler, tarihler, saatler, başlangıç verisi ve veri biçimi sözlüğüdür; dördüncü bir mimari katman değildir.

## Ekranda ne açacağım, ne yapacağım?

STORAGE_KEY değerinin ygs-klinik-randevu-demo-v1 kaldığını gösterin. Veri biçiminde schema, nextId ve appointments alanlarını inceleyin. repository.js içinde document, render veya confirm çağrısı olmadığını kontrol edin. Yanlış biçim ile BR-01 iş kuralı çakışmasının farklı denetimler olduğunu anlatın.

- [src/repository.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/repository.js)
- [src/demo-data.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/demo-data.js)
- [03-veri-erisimi.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/03-veri-erisimi.md)

## Kontrol sorusu

findById/list sonuçları bağımsız mı? Reddedilen işlemde nextId artıyor mu? Saklama hatası ekrana doğrudan depo tarafından mı yazılıyor?

**Öğrenciye soru:** Neden hem iptal için hem oluşturma için ayrı veri kopyaları yönetmiyoruz?

**Beklenen açıklama:** Ayrı kaynaklar bir işlemin diğerinin değişikliğini eski veriyle ezmesine yol açabilir. Bütün işlemler tek ortak depoyu kullanır.

## Öğrencinin yapacağı iş

Depo ile arayüz arasındaki doğrudan çağrıları kaldır. Gerçek saklama durumunu sonuç olarak üst bileşene ilet.

## Öğretmen örneğinin gerçek durumu

Tek ortak veri; arayüze doğrudan çağrı yok. Anahtar, schema:1 ve nextId düzeni korundu.

Görev: [#13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13) · İnceleme paketi: [PR #15](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.
