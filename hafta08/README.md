# YAZ325 - 8. hafta: Sürüm Adayından Doğrulanmış Teslime

Öğrenci çalışma rehberi · Güncelleme: 26 Kasım 2026.

Bu hafta uygulamanızın belirli bir sürümünden teslim paketi hazırlayacak, paketin içeriğini doğrulayacak ve ayıklanan paket üzerinde test çalıştıracaksınız. Her grup kendi kaynak sürümünü, ürettiği dosyaları ve gerçek sonuçlarını kaydeder.

Örnek çalışma dalı: `release/h8-surum-adayi` · [Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19). PR #19, 22 Kasım 2026 tarihinde `main` dalına birleştirilmiştir.

## Çalışma adımları

| Adım | Çalışma yönergesi | Grubun üreteceği çıktı |
|---|---|---|
| 1 | [Aday sürüm kimliği](docs/01-surum-adayi.md) | Aday adı, tam kaynak commit'i ve dosya listesi. |
| 2 | [Sürüm notları](docs/02-surum-notlari.md) | Değişiklik, açılış yönergesi ve bilinen sınırlar. |
| 3 | [Paket tarifi](docs/03-paket-tarifi.md) | Teslim edilecek dosyaların listesi ve görevleri. |
| 4 | [Tekrarlanabilir üretim](docs/04-tekrarlanabilirlik.md) | İki üretimin dosyaları, özetleri ve karşılaştırması. |
| 5 | [Paket bütünlüğü](docs/05-butunluk-kontrolu.md) | Sağlam paket doğrulaması ve kopyada yapılan olumsuz deneme. |
| 6 | [Paketten test](docs/06-paketten-test.md) | Ayıklanmış teslim dosyaları üzerinde gerçek test sonucu. |
| 7 | [Geri dönüş planı](docs/07-geri-donus.md) | Tetikleyici, sorumlu, bilinen sürüm ve doğrulama adımları. |
| 8 | [Teslim ve değerlendirme](docs/08-teslim-ve-degerlendirme.md) | Paket, kanıt, alıcı değerlendirmesi ve açık iş kaydı. |

## Grubun iş bölümü

Paket tarifi, üretim, bütünlük ve alıcı kontrollerini [grup büyüklüğüne göre](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşın. Her üyenin katkısını ve ilgili dosyaları [grup kaydına](sablonlar/grup-kaydi.md) yazın. İnceleyen kişi, değerlendirdiği içeriğin yazımına katılmamış olmalıdır; ortak yazılan bölüm için gerekirse grup dışından inceleme planlayın.

## Kaynaklar

- [Tek sayfalık, tıklanabilir süreç PDF'i](dagitim/YAZ325_Hafta_08_Surec_Infografik_Aktif_Linkli.pdf)
- [H8 örnek uygulama paketi: 0.3.0-rc.1 ZIP](dagitim/Klinik_Randevu_0.3.0-rc.1.zip)
- [Tarihli CI kaydı](kanitlar/ci-kaydi.json) · [İlk koşuda yakalanan ve düzeltilen bulgu](kanitlar/ilk-ci-bulgusu.json)
- [Kabul ve teslim kaydı](docs/09-kabul-ve-teslim.md) · [Teknik başvuru kaynakları](docs/10-kaynaklar.md)
- [Boş grup çalışma formu](sablonlar/grup-kaydi.md)

## Örnek sonuçların kullanımı

22 Kasım 2026 tarihli H8 kayıtlarında 30 Node testi, 8 paket kontrolü, kaynak uygulamada 14 tarayıcı senaryosu ve ayıklanmış pakette aynı 14 senaryo başarılıdır. H8'in `0.3.0-rc.1` paketi, o haftanın tarihli örneğidir; deponun daha sonraki sürümleriyle karıştırılmamalıdır. Bu sayfalardaki örnek komutlar için `release/h8-surum-adayi` dalının araçlarını ve kaynaklarını birlikte kullanın.

Kendi çalıştırmanızın commit'ini, tarihini, ortamını ve gerçek sonucunu ayrıca kaydedin. Teknik testler, bağımsız kişi incelemesi, kullanıcı kabulü ve NFR ölçümleri ayrı değerlendirilir. Yapılmamış ölçüm veya geri dönüş denemesini tamamlanmış olarak yazmayın.
