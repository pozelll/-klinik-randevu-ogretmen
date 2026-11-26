# 5. hafta / 3. adım - Veri erişimi

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Okuma, veri biçimi denetimi, oturum verisi ve kalıcı saklama işlemlerini tek veri erişimi bileşeninde toplamak.

Oluşturma, iptal ve tamamlama işlemleri aynı veri kaynağını kullanır. Ayrı veri kopyalarının ayrı ayrı saklanması, bir işlemin sonucunun eski veriyle üzerine yazılmasına yol açabilir. Kalıcı saklama kullanılamadığında uygulama oturum belleğiyle devam eder ve saklama sonucunu üst bileşene iletir.

## Veri düzeni

Örnek uygulamada saklama anahtarı `ygs-klinik-randevu-demo-v1` olarak korunur. Veri yapısı `schema`, `nextId` ve `appointments` alanlarını içerir; şema değeri `1`'dir.

`src/demo-data.js`, başlangıç verisini, sabit kişi/tarih/saat bilgilerini ve veri biçimini tanımlar. `src/repository.js` veriyi okur ve saklar. Yetki ve randevu çakışması gibi iş kararları ise iş kuralları bileşeninin sorumluluğundadır.

## Grup çalışması

1. Kendi uygulamanızda randevu işlemlerinin kullandığı veri kaynağını ortaklaştırın.
2. Veri erişimi bileşeninden ekrana yazma, çizim ve kullanıcı onayı alma çağrılarını çıkarın.
3. Okuma sonuçlarını bağımsız kopyalar olarak sunun; saklama durumunu işlem sonucuna ekleyin.
4. Veri biçimi hatasını, iş kuralı çakışmasını ve kalıcı yazma hatasını ayrı sonuçlarla kaydedin.

Teslime veri erişimi dosyasını ve saklama sonucunu kullanan üst bileşenin bağlantısını ekleyin.

## Örnek uygulama kaydı

22 Kasım 2026 tarihli H5 çalışmasında ortak veri kaynağı, saklama anahtarı, `schema:1` ve `nextId` düzeni korunmuştur. Veri erişimi bileşeni arayüze doğrudan çağrı yapmaz.

## Kaynaklar

- [src/repository.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/repository.js)
- [src/demo-data.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/demo-data.js)
- [H5 dalındaki veri erişimi yönergesi](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/03-veri-erisimi.md)
- [Görev #13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13)
- [PR #15 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15)
