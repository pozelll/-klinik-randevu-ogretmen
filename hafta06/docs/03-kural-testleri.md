# 6. hafta / 3. basamak - İş kuralı testleri

## Amaç

İşlemin sonuç kodunu ve veri üzerindeki etkisini birlikte sınayın. Bir ret senaryosunda önceki veri, güncelleme çağrıları ve kalıcı yazma sayısı ayrı ayrı kontrol edilir.

## Çalışma

1. Proje kökünde karar testlerini çalıştırın:

   ```bash
   node --test tests/h6-decision.test.cjs
   ```

2. [Test dosyasındaki](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/h6-decision.test.cjs) DK-K01-DK-K07 kimliklerini [karar tablosuyla](02-karar-tablosu.md) eşleştirin.
3. Bir ret senaryosu seçin. Önce/sonra veriyi, `updateCalls` ve `storageWritesDuringRequest` değerlerini kendi çalıştırmanızdan kaydedin.
4. Başarılı işlemde değişen kaydı ve korunması gereken alanları karşılaştırın. Kayıt sayısı ve `nextId` değerini de kaydınıza ekleyin.

## Teslim edilecek çıktı

Test kimliği, kaynak commit, tarih, komut, gerçek sonuç, önce/sonra veri ve yazma sayısı. Kanıt üretme komutları için [yeniden çalıştırma rehberini](10-yeniden-calistirma.md) kullanın.

## Örnek kanıt

22 Kasım 2026 tarihli [karar satırı kayıtlarında](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/kanitlar/karar-tablosu-sonuclari.json) 7/7 test başarılıdır. DK-K02'de `updateCalls:0` ve `storageWritesDuringRequest:0` kaydedilmiştir. DK-K07'de durum değişmiş; toplam kayıt sayısı, `nextId` ve diğer kayıtlar korunmuştur. Bu örnek kayıt kendi test yürütümünüzün yerine geçmez.

[Görev #14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · [PR #16 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16)
