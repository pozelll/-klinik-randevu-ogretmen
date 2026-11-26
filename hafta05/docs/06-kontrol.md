# 5. hafta / 6. adım - İlk davranış testleri

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Sorumlulukları ayrı bileşenlere taşırken temel davranışların korunduğunu test etmek ve sonuçları uygulama sürümüne bağlamak.

## Testi çalıştırma

Node.js bulunan bir ortamda, terminali projenin kök dizininde açın ve şu komutu çalıştırın:

```bash
node --test tests/h5-smoke.test.cjs
```

H5-S01–H5-S08 kapsamındaki sekiz test, temel iş kurallarını ve veri davranışlarını sınar. H5-S04 iptal, yeniden oluşturma ve tamamlama zincirini; H5-S06 kalıcı yazma hatasında oturum verisinin davranışını ele alır.

## Grup çalışması

1. Testi kendi çalışma kopyanızda çalıştırın.
2. Komutu, tarihi, Node.js sürümünü ve uygulamanın commit'ini kaydedin.
3. Başarılı ve başarısız test sayılarını gerçek çıktıdan aktarın. Başarısız sonuç varsa ilgili davranışı ve düzeltmeyi belgeleyin.
4. Sonuç dosyasının bağlantısını [grup kaydına](../sablonlar/grup-kaydi.md) ekleyin.

Bir testin geçmesi, o testteki beklentinin kullanılan veri ve sürüm için sağlandığını gösterir. Kodun başka bir kişi tarafından incelenmesi ayrı bir faaliyettir; yalnızca gerçekleşen incelemeyi kaydedin.

## Tarihli örnek sonuç

**22 Kasım 2026 tarihli H5 kaydı: 8 başarılı, 0 başarısız test.** Bu, aşağıdaki kanıt dosyasında kayıtlı örnek çalıştırmanın sonucudur. Grubunuzun sonucunu kendi çalıştırmanızdan üretin. Tarayıcı regresyonları 6. haftada ayrı kaydedilir.

## Kaynaklar

- [tests/h5-smoke.test.cjs](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/tests/h5-smoke.test.cjs)
- [22 Kasım 2026 Node test sonucu](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/kanitlar/node-test-sonuclari.tap)
- [H5 dalındaki test yönergesi](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/06-kontrol.md)
- [Görev #13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13)
- [PR #15 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15)
