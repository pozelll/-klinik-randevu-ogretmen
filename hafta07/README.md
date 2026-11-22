# YAZ325 — 7. hafta: Kontrollü Değişiklik Yönetimi

Sekiz basamaklı öğretmen örneği. H5–H6 çalışmasının devamıdır; resmî ders izlencesi yerine yeni bir müfredat kararı değildir.

Dal: `feat/h7-saat-secimi-yardimi` · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18) · [Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10)

## Grubun iş bölümü

İki, üç ve dört kişilik gruplar değişiklik analizi, uygulama, yeni kabul kontrolleri ve regresyonu [grup büyüklüğüne göre](../docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşır. Her üye anlamlı bir çıktı ve gerçek katkı kaydı üretir; yazmadığı kapsamı inceler. Ortak yazılan bölüm için gerekirse grup dışından inceleyen belirlenir. Kendi sorumlularınızı ve sonuçlarınızı [grup kaydına](sablonlar/grup-kaydi.md) yazın; öğretmen örneğinin kişi ve süre varsayımlarını doğrudan kendi planınız saymayın.

| Basamak | Ekranda açılacak belge | Hazırlık sonucu |
|---|---|---|
| 1 | [Ertelenen işi seçtik](docs/01-baslangic.md) | H3-03, 7. haftanın işine dönüştü. |
| 2 | [Değişikliği sınırladık](docs/02-degisiklik-karti.md) | H7-DK-01: yardım metni ve durumu. |
| 3 | [Etkiyi ve riski gördük](docs/03-etki-ve-plan.md) | Ürün değişikliği iki dosyada. |
| 4 | [Kabulü gözlenebilir yaptık](docs/04-kabul-kosullari.md) | H7-B01–B05: beş kabul kontrolü. |
| 5 | [Yardımı uyguladık](docs/05-uygulama.md) | Seçim ve onay adımı ayrılıyor. |
| 6 | [Yeni ve eski akışı sınadık](docs/06-test-kaniti.md) | 30/30 Node · 14/14 Chromium geçti. |
| 7 | [İncelemeye sunduk](docs/07-pr-ve-inceleme.md) | H7 → H6: taslak PR #18 açık. |
| 8 | [Sonraki haftaya bağladık](docs/08-devretme.md) | İzlenebilir değişiklik paketi hazır. |

## Materyal

- [Tek sayfalık, tıklanabilir süreç PDF'i](dagitim/YAZ325_Hafta_07_Surec_Infografik_Aktif_Linkli.pdf)
- [Grubun kendi çalışma formu](sablonlar/grup-kaydi.md)

Her basamakta önce soruyu sorun, ilgili dosyayı açın, gerçek sonucu gösterin; sonra grup kendi uygulamasını yapsın. Otomatik kontroller bağımsız insan incelemesi veya kullanıcı kabulü değildir. Öğrenci kendi sürümünü ve gerçek katkısını kaydeder.

Bağımsız inceleme, önceki PR bağımlılıklarının çözümü, birleştirme ve NFR-01–NFR-03 ölçümleri açık. Test süresi gerçekleşmiş insan emeği değildir.
