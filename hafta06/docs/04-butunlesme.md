# 6. hafta / 4. basamak - Bütünleşme ve regresyon

## Amaç

Ortak veri kullanan bileşenleri birlikte sınayın. Oluşturma, iptal ve tamamlama işlemlerinin birbirinin değişikliklerini koruduğunu; hata durumlarının önceki davranışları bozmadığını kontrol edin.

## Çalışma

1. Proje kökünde H5 ve H6 testlerini birlikte çalıştırın:

   ```bash
   node --test tests/h5-smoke.test.cjs tests/h6-decision.test.cjs tests/h6-regression.test.cjs
   ```

2. [Regresyon testlerinde](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/h6-regression.test.cjs) H6-R06 saklama hatasını, H6-R04 başlangıç BR-01 çakışmasını ve H6-R14 kontrollü dayanıklılık senaryosunu inceleyin.
3. Kendi grubunuzda aynı veriyi kullanan iki işlemi art arda çalıştırın. İlk işlemin sonucunun ikinci işlemden sonra korunduğunu gösterin.
4. Hata senaryolarını ayrı kaydedin: bozuk veri biçimi, iş kuralı çakışması ve saklama hatası farklı durumlardır. Kullanılan test ikamesini ve gerçek tarayıcı kontrolünü ayrı belirtin.

## Teslim edilecek çıktı

İşlem sırası, başlangıç verisi, her adımdan sonraki veri, test edilen commit ve gerçek test sonucu.

## Örnek kanıt

22 Kasım 2026 tarihli [Node test kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/kanitlar/node-test-sonuclari.tap) 30 başarılı test içerir: 8 H5 + 7 karar + 15 regresyon. H5'in 8 testi bu toplamın içindedir. H6-R14, ürün akışının normalde oluşturmadığı çakışmayı kontrollü olarak depoya ekleyen bir dayanıklılık testidir.

[Görev #14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · [PR #16 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16)
