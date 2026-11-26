# 8. hafta / 7. adım - Geri dönüş planı

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Bir sorun ortaya çıktığında dağıtımı hangi koşulda durduracağınızı, hangi bilinen sürüme döneceğinizi ve sonucu nasıl doğrulayacağınızı planlayın. Kaynak kodunun önceki sürümünü açmak, tarayıcıdaki veriyi önceki durumuna otomatik olarak döndürmez.

## Grup çalışması

1. Kendi değişikliğiniz için bir geri dönüş tetikleyicisi belirleyin.
2. Karar sorumlusunu, bilinen temel sürümün tam commit'ini ve kontrol adımlarını yazın.
3. Kaynak dosyalarının geri alınmasıyla veri yedeği veya veri geri yükleme ihtiyacını ayrı tanımlayın.
4. Bir deneme yapacaksanız kopya üzerinde çalışın; mevcut çalışma veya kullanıcı verisinin üzerine yazmayın.
5. Planın durumunu ve gerçekten yapılan denemeyi ayrı kaydedin.

## Teslim edilecek çıktı

Tetikleyici, ilk eylem, sorumlu, temel sürüm, uygulama yolu, doğrulama ve kapanış alanları bulunan geri dönüş planı. Deneme yapılmadıysa kaydı “plan hazır; uygulanmadı” olarak bırakın.

## 22 Kasım 2026 tarihli örnek plan - uygulanmadı

H6, saat yardımı değişikliğinden önceki temel sürüm olarak seçilmiştir.

| Alan | Plan |
|---|---|
| Tetikleyici | Saat yardımı yanlış durumu gösteriyor veya paket açılışı başarısız |
| İlk eylem | Adayı dağıtmayı durdur; sorun, tarayıcı ve tam sürümü kaydet |
| Kararı verecek kişi | Öğretim üyesi / grubun belirleyeceği sorumlu; gerçek atama derste yapılır |
| Bilinen temel | H6 `f100249a9ece6cb18ff905fe6a3bee8a6cb6f9f8` |
| Uygulama yolu | Bu commit'in kaynaklarını ayrı yeni klasöre al; mevcut çalışma ve tarayıcı verisinin üzerine yazma |
| Kontrol | H6'nın 30 Node + 9 tarayıcı senaryosunu o sürümün araçlarıyla yeniden çalıştır |
| Veri sınırı | Kaynak değişimi localStorage yedeği veya veri göçü değildir |
| Kapanış | Yeni test sonucu, kullanılan sürüm ve yeniden dağıtım kararı kaydedilir |

Bu hazırlıkta gerçek üretim yayını, geri dönüş tatbikatı veya kullanıcı verisi geri yüklemesi yapılmadı. Ayrı klasördeki dosya URL'si saklama davranışını değiştirebilir; önceki kayıtların göründüğünü varsaymayın. Oturum verisi gerekirse mevcut örneğin kapsamı dışında ayrı yedekleme gereksinimi tanımlanmalıdır.

[H6 kaynak commit'i](https://github.com/pozelll/-klinik-randevu-ogretmen/commit/f100249a9ece6cb18ff905fe6a3bee8a6cb6f9f8)

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
