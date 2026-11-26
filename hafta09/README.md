# YAZ325 - 9. hafta: Gitflow, Sürüm ve Hotfix

Öğrenci çalışma rehberi · Güncelleme: 26 Kasım 2026.

Bu hafta iki dalın ortak başlangıcını doğrulayacak, çakışmayı çözecek, bir sürümü etiketleyecek ve düzeltmeyi iki hedef dala taşıyacaksınız. Her grup kendi katkılarını, komut sonuçlarını, kalite kararını ve teslim kaydını oluşturur.

Örnek çalışma dalı: `docs/h9-gitflow-teslim` · [Görev #20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) · [PR #21 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21).

## Çalışma adımları

| Adım | Çalışma yönergesi | Grubun üreteceği çıktı |
|---|---|---|
| 1 | [Başlangıç ve dal planı](docs/01-baslangic.md) | Başlangıç commit'i, ürün kapsamı ve dal planı. |
| 2 | [İki feature, ortak taban](docs/02-feature.md) | İki katkı commit'i ve ortak ata doğrulaması. |
| 3 | [Çakışmayı anlamıyla çöz](docs/03-cakisma.md) | İki ihtiyacı koruyan çözüm, gerekçe ve kontrol kaydı. |
| 4 | [Release ve etiket](docs/04-release.md) | Sürüm kapsamı, etiket türü ve hedef commit. |
| 5 | [Hotfix'i iki dala taşı](docs/05-hotfix.md) | Düzeltme, iki hedef için atalık ve son içerik kontrolü. |
| 6 | [Kanıtı yeniden üret](docs/06-kanit.md) | Koşu kaydı, sonuç dosyaları ve bundle doğrulaması. |
| 7 | [Kaliteyle sürüm kararı](docs/07-karar.md) | Kanıta bağlı yayın kararı ve açık iş listesi. |
| 8 | [Kapsamı kapat, devret](docs/08-devir.md) | Kapsam tablosu, katkılar ve alıcı teslim kaydı. |

## Grubun iş bölümü

Dal katkılarını, çakışma çözümünü, sürüm ve hotfix kontrollerini [grup büyüklüğüne göre](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşın. Her üyenin anlamlı çıktısını ve gerçek katkı kaydını [grup formuna](sablonlar/grup-kaydi.md) yazın. İnceleyen kişi, değerlendirdiği içeriğin yazımına katılmamış olmalıdır; ortak yazılan bölüm için gerekirse grup dışından inceleme planlayın.

## Kaynaklar

- [Tek sayfalık süreç PDF'i — 22 Kasım 2026 eğitim özeti](dagitim/YAZ325_Hafta_09_Surec_Infografik_Aktif_Linkli.pdf)
- [Gitflow çalışma ZIP'i](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/dagitim/YAZ325_Hafta09_Gitflow_Calisma_Paketi.zip): araçlar, panel, senaryolar, çalışma belgeleri, kanıtlar ve H8 başlangıç uygulaması.
- [Kurulum ve teknik kaynaklar](docs/47-yeniden-calistirma-ve-kaynaklar.md)
- [Kanıt zinciri](docs/43-git-kanit-ve-izlenebilirlik.md) · [Konu kapsamı](docs/46-konu-kapsam-tablosu.md)
- [Güncel klinik teknik kapanış kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md) · [İnsan kabulü için çalışma formu](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/50-insan-kabul-oturumu.md)

## Örnek sonuçların kullanımı

22 Kasım 2026 tarihli Gitflow örneğinde yerel ve [CI yürütümü](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202073) 12/12 süreç kontrolünü; son panel 6/6 kontrolü geçti. Aynı hazırlığın [klinik CI kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202040), 30 Node testi, 14 kaynak tarayıcı senaryosu, 8 paket kontrolü ve pakette aynı 14 tarayıcı senaryosunu içerir.

Laboratuvarın `0.9.x` paneli ve H8 başlangıç paketi `0.3.0-rc.1` ayrı kapsamlardır. Daha sonraki klinik `0.3.0-rc.2` adayı, klavye ve performans ölçümleri 49 numaralı kayıttadır. Önceki hazırlık belgelerindeki açık PR ve yapılmamış ölçüm ifadeleri kendi tarihleriyle okunmalıdır.

Otomatik örneğin Git yazarı “YAZ325 Otomatik Ders Deneyi”dir. Bu kayıtlar grubun insan katkısı veya bağımsız incelemesi olarak kullanılamaz. Kendi koşunuzun tarihini, ortamını, tam commit'ini ve gerçek sonucunu ayrıca kaydedin. Klinik nihai yayın kararı, eksik insan kabulü kayıtları nedeniyle **BEKLET** durumundadır; tamamlanmamış kabulü başarılı işaretlemeyin.
