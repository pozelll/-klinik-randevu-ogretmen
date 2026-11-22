# 8. hafta / 7. basamak — Geri dönüşü planladık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Geri dönüş planı, hata olduğunda neyi durduracağımızı ve hangi bilinen sürümü kullanacağımızı tarif eder. Bu örnekte H6, yardım değişikliğinden önceki temel sürümdür. Yeni bir klasörde o sürümü açmak kaynak kodu değiştirir; tarayıcıdaki veriyi önceki ana otomatik döndürmez.

## Ekranda göster ve uygula

Planın tetikleyici, sorumlu, kaynak commit, doğrulama ve iletişim alanlarını açın. Öğrenci denemesinin kopyada yapılacağını belirtin. Burada canlı sisteme dönüş, veri geri yükleme veya gerçek dağıtım yapılmadığını gösterin. Farklı dosya adresinin localStorage davranışını etkileyebileceğini hatırlatın.

- [07-geri-donus.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/07-geri-donus.md)
- [H6 kaynak commit’i](https://github.com/pozelll/-klinik-randevu-ogretmen/commit/f100249a9ece6cb18ff905fe6a3bee8a6cb6f9f8)

## Öğrenciye soru

**Önceki JavaScript’i açmak eski randevu kayıtlarını geri getirir mi?**

Beklenen açıklama: Hayır. Kod ve tarayıcı verisi ayrı varlıklardır. Bu örnekte otomatik veri yedeği veya geri yükleme işlevi yoktur.

## Grubun yapacağı iş

Kendi değişikliğin için bir geri dönüş tetikleyicisi ve kontrol listesi yaz. Yapmadığın tatbikatı tamamlandı gösterme.

Kontrol: Plan kaynak dönüşü ile veri dönüşünü ayırıyor mu? Geri dönülecek sürüm ve kontrol belli mi?

## Hazırlığın gerçek durumu

Geri dönüş planı hazır; uygulanmadı. Kodun dönüşü, kullanıcı verisinin dönüşü değil.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## Geri dönüş planı — uygulanmadı

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
