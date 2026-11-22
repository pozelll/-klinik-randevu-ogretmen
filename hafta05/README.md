# YAZ325 - 5. hafta: Mimariyi Koda Aktarma

Sekiz basamaklı, aktif GitHub bağlantılı öğretmen örneği. Hazırlık: 22 Kasım 2026.
Önceki dersleri değiştiren resmî müfredat kararı değildir; H4 mimari kararının uygulama ve test devamıdır.

Çalışma dalı: `feat/h5-moduler-uygulama` · [PR #15](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15) · [Görev #13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13)

## Grubun iş bölümü

İki, üç ve dört kişilik gruplar veri erişimi, iş kuralları, arayüz ve davranış kontrollerini [grup büyüklüğüne göre](../docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşır. Her üye anlamlı bir çıktı ve gerçek katkı kaydı üretir; yazmadığı kapsamı inceler. Ortak yazılan bölüm için gerekirse grup dışından inceleyen belirlenir. Kendi sorumlularınızı ve sonuçlarınızı [grup kaydına](sablonlar/grup-kaydi.md) yazın; öğretmen örneğinin kişi ve süre varsayımlarını doğrudan kendi planınız saymayın.

| Basamak | Ekranda açılacak belge | Hazırlık sonucu |
|---|---|---|
| 1 | [Başlangıcı sabitledik](docs/01-baslangic.md) | H5 çalışma dalı ve görev #13 hazır. |
| 2 | [Sözleşmeyi netleştirdik](docs/02-sozlesme.md) | findById · list · update sınırı kuruldu. |
| 3 | [Veri erişimini ayırdık](docs/03-veri-erisimi.md) | Tek ortak veri; arayüze doğrudan çağrı yok. |
| 4 | [İş kurallarını ayırdık](docs/04-is-kurallari.md) | Ret → yazma yok; uygun istek → güncelleme. |
| 5 | [Arayüzü bağladık](docs/05-arayuz.md) | Üç sorumluluk çalışan akışta birleşti. |
| 6 | [İlk kontrolleri çalıştırdık](docs/06-kontrol.md) | H5-S01–H5-S08: 8/8 geçti. |
| 7 | [Commit ve PR hazırladık](docs/07-commit-pr.md) | Taslak PR #15 açık; hedef H4 dalı. |
| 8 | [Teslim ve devamı belirledik](docs/08-teslim.md) | Uygulama ve öğretim paketi hazır. |

## Ders akışı

Her basamakta önce soruyu sorun, sonra ilgili dosyayı açın, en son gerçek sonuç kaydını gösterin.
Öğrenciler kendi depolarında kendi çıktısını üretir. Öğretmen testini kendi çalıştırması gibi kaydetmez.
Kavramlar, dosyalar, test sonuçları ve inceleme durumu ayrı tutulur.

## Ders materyali

[Tek sayfalık süreç infografiği](dagitim/YAZ325_Hafta_05_Surec_Infografik_Aktif_Linkli.pdf)

## Açık işler

- Bağımsız kişi incelemesi ve varsa bulguların kapanışı.
- Önceki PR bağımlılıklarının çözümü ve koşullar sağlanınca birleştirme.
- NFR-01 kullanılabilirlik, NFR-02 yanıt süresi ve NFR-03 klavye ölçümleri.
- Öğrenci gruplarının gerçek katkı, süre ve kendi sürümlerindeki test kayıtları.

Otomatik test süreleri, 4. haftanın 9 saat / 19 kişi-saat planının gerçekleşmiş emek ölçümü değildir.
