# 7. hafta / 5. adım - Değişikliğin uygulanması

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Değişiklik kartındaki davranışı uygulamak ve açıklama metnini uygulamanın gerçek durumuyla tutarlı tutmak.

Örnek uygulamada saat yardımı, `renderSlots` çalışırken güncellenir. Yardım metni rol ve seçili saat durumuna bağlıdır. Saat seçimi kayıt oluşturmaz; oluşturma, iptal ve tamamlama işlemleri `src/rules.js` üzerinden yürür.

`aria-describedby`, yardım ile ilgili alanı ilişkilendirir; `aria-live`, değişen açıklamanın bildirilmesine yönelik bir ipucudur. Bu özelliklerin bulunması tek başına klavye veya ekran okuyucu uygunluğu kanıtı değildir.

## Grup çalışması

1. Kendi değişiklik kartınızda belirtilen davranışı uygulayın.
2. Değişikliği en az bir durum geçişiyle sınayın. Örneğin saat seçiminden sonra tarih veya rol değiştiğinde açıklamanın güncel durumu yansıtmasını kontrol edin.
3. Kullanıcının seçimi, onayı ve veri değişiminin hangi adımlarda gerçekleştiğini ayrı kaydedin.
4. Dosya değişikliklerini commit ile kaydedin ve bağlantıyı [grup formuna](../sablonlar/grup-kaydi.md) ekleyin.

## Teslim edilecek çıktı

Değişen dosyalar, uygulama commit'i ve en az bir durum geçişinin başlangıç/sonuç kaydı.

## Tarihli örnek uygulama

22 Kasım 2026 tarihli [kod farkı](https://github.com/pozelll/-klinik-randevu-ogretmen/commit/bd5fa3fb2c35d1c11864eed982fdbc20d539d58a), yardımın `renderSlots` içinde güncellendiği uygulamayı gösterir. Başlangıç verisi 7 kayıttır.

Örneği incelemek için proje klasörünü tamamen ayıklayıp `index.html` dosyasını `src/` ile birlikte açın. 09:30 seçimi, onaydan önce tarih değişimi ve doktor rolüne geçişi ayrı senaryolar olarak deneyin. Yeniden denemelerde yalıtılmış bir tarayıcı oturumu kullanın veya gerekli gözlemleri kaydettikten sonra yalnız sentetik örnek veriyi sıfırlayın.

- [src/ui.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/src/ui.js)
- [index.html](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/index.html)

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)
