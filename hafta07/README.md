# YAZ325 - 7. hafta: Kontrollü Değişiklik Yönetimi

Öğrenci çalışma rehberi · Güncelleme: 26 Kasım 2026.

Bu hafta önceki iş listesinden bir değişiklik seçerek kapsamını, etkilerini, kabul koşullarını ve testlerini hazırlayacaksınız. Örnek çalışma, 5. ve 6. haftadaki modüler uygulamaya saat seçimi yardımı ekler.

Örnek dal: `feat/h7-saat-secimi-yardimi` · [Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)

Örnek test sonuçları 22 Kasım 2026 tarihli çalıştırmalara aittir. PR #18 aynı gün `main` dalına birleştirilmiştir. Her grup kendi sürümünü, katkılarını ve gerçek sonuçlarını ayrıca kaydeder.

## Çalışma adımları

| Adım | Çalışma yönergesi | Grubun üreteceği çıktı |
|---|---|---|
| 1 | [Ertelenen işin seçimi](docs/01-baslangic.md) | Önceki karar, yeni seçim gerekçesi ve başlangıç commit'i. |
| 2 | [Değişiklik kartı](docs/02-degisiklik-karti.md) | Sorun, kapsam, kapsam dışı işler ve kabul bağlantısı. |
| 3 | [Etki ve risk planı](docs/03-etki-ve-plan.md) | Değişen dosyalar, etkiler, riskler ve kontroller. |
| 4 | [Kabul koşulları](docs/04-kabul-kosullari.md) | Gözlenebilir sonuçları tanımlayan senaryolar. |
| 5 | [Değişikliğin uygulanması](docs/05-uygulama.md) | Çalışan değişiklik, durum geçişi ve commit kaydı. |
| 6 | [Kabul ve regresyon testleri](docs/06-test-kaniti.md) | Kendi sürümünüzün test sonuçları ve yürütüm bilgileri. |
| 7 | [PR ve inceleme](docs/07-pr-ve-inceleme.md) | Değişiklik açıklaması, inceleme kapsamı ve gerçek sonuç. |
| 8 | [İzlenebilirlik ve devir](docs/08-devretme.md) | Gereksinim, görev, kod ve kanıt bağlantıları; açık işler. |

## Grubun iş bölümü

Değişiklik analizi, uygulama, kabul kontrolleri ve regresyonu [grup büyüklüğüne göre](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşın. Her üyenin sorumluluğunu ve gerçek katkısını [grup kaydına](sablonlar/grup-kaydi.md) yazın. İncelemeyi ilgili içeriğin yazımına katılmamış bir üye yapar; ortak yazılan bölüm için gerekirse grup dışından inceleme planlanır.

## Çalışma materyali

- [Tek sayfalık süreç infografiği](dagitim/YAZ325_Hafta_07_Surec_Infografik_Aktif_Linkli.pdf)
- [Gereksinim, değişiklik ve test eşleştirmesi](docs/09-izlenebilirlik.md)
- [Grubun kendi çalışma formu](sablonlar/grup-kaydi.md)

## Örnek sonuçların kapsamı

22 Kasım 2026 tarihli H7 kayıtlarında 30 Node testi ve 14 Chromium senaryosu başarılıdır. Tarayıcı kontrollerinin 9'u önceki davranışları, 5'i yeni saat yardımını kapsar. Bu sayılar farklı gereksinimlerin sayısı veya NFR ölçüm sonucu değildir.

Otomatik test, başka kişinin incelemesi ve kullanıcı kabulü ayrı kaydedilir. Test çalışma süresi grup emeğinin ölçümü değildir; grubunuzun gerçekleşen süresini ayrıca yazın. İnfografikteki sürüm ve durum bilgileri hazırlandığı tarihin kaydıdır; güncel birleştirme durumu PR sayfasında bulunur.
