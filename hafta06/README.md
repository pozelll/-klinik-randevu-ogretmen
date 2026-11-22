# YAZ325 - 6. hafta: Karar Tablosundan Test Kanıtına

Sekiz basamaklı, aktif GitHub bağlantılı öğretmen örneği. Hazırlık: 22 Kasım 2026.
Önceki dersleri değiştiren resmî müfredat kararı değildir; H4 mimari kararının uygulama ve test devamıdır.

Çalışma dalı: `test/h6-karar-tablosu` · [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16) · [Görev #14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14)

## Grubun iş bölümü

İki, üç ve dört kişilik gruplar karar tablosu, test yazımı, test yürütümü ve kanıt incelemesini [grup büyüklüğüne göre](../docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşır. Her üye anlamlı bir çıktı ve gerçek katkı kaydı üretir; yazmadığı kapsamı inceler. Ortak yazılan bölüm için gerekirse grup dışından inceleyen belirlenir. Kendi sorumlularınızı ve sonuçlarınızı [grup kaydına](sablonlar/grup-kaydi.md) yazın; öğretmen örneğinin kişi ve süre varsayımlarını doğrudan kendi planınız saymayın.

| Basamak | Ekranda açılacak belge | Hazırlık sonucu |
|---|---|---|
| 1 | [Test kapsamını belirledik](docs/01-test-plani.md) | Kural, veri erişimi ve ekran kontrolleri ayrıldı. |
| 2 | [Yedi karar satırını kurduk](docs/02-karar-tablosu.md) | DK-K01–DK-K07 ayrı ayrı tanımlandı. |
| 3 | [Kuralları kanıtladık](docs/03-kural-testleri.md) | 7/7 karar satırı geçti. |
| 4 | [Bütünleşmeyi denedik](docs/04-butunlesme.md) | 8 H5 + 7 karar + 15 regresyon = 30/30. |
| 5 | [Ekran akışını kontrol ettik](docs/05-tarayici.md) | 9/9 Chromium senaryosu geçti. |
| 6 | [Otomatik kontrolü kurduk](docs/06-ci.md) | GitHub Actions: başarılı. |
| 7 | [İnceleme paketini açtık](docs/07-inceleme.md) | Taslak PR #16 açık; hedef H5 dalı. |
| 8 | [Kanıt ve teslimi bağladık](docs/08-teslim.md) | 30 Node + 9 tarayıcı kontrolü kayıtlı. |

## Ders akışı

Her basamakta önce soruyu sorun, sonra ilgili dosyayı açın, en son gerçek sonuç kaydını gösterin.
Öğrenciler kendi depolarında kendi çıktısını üretir. Öğretmen testini kendi çalıştırması gibi kaydetmez.
Kavramlar, dosyalar, test sonuçları ve inceleme durumu ayrı tutulur.

## Ders materyali

[Tek sayfalık süreç infografiği](dagitim/YAZ325_Hafta_06_Surec_Infografik_Aktif_Linkli.pdf)

## Açık işler

- Bağımsız kişi incelemesi ve varsa bulguların kapanışı.
- Önceki PR bağımlılıklarının çözümü ve koşullar sağlanınca birleştirme.
- NFR-01 kullanılabilirlik, NFR-02 yanıt süresi ve NFR-03 klavye ölçümleri.
- Öğrenci gruplarının gerçek katkı, süre ve kendi sürümlerindeki test kayıtları.

Otomatik test süreleri, 4. haftanın 9 saat / 19 kişi-saat planının gerçekleşmiş emek ölçümü değildir.

## Derste ve sonrasında

- [5. ve 6. hafta ayrıntılı anlatım rehberi](dagitim/YAZ325_Hafta_05_06_Ders_Anlatim_Rehberi.pdf)
- [Gereksinim–test–kanıt eşleştirmesi](docs/09-izlenebilirlik.md)
- [İndirme, açma ve test komutları](docs/10-yeniden-calistirma.md)
- [Boş grup kayıt formu](sablonlar/grup-kaydi.md)
