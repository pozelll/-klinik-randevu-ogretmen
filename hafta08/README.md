# YAZ325 — 8. hafta: Sürüm Adayından Doğrulanmış Teslime

Sekiz basamaklı öğretmen örneği. H5–H6 çalışmasının devamıdır; resmî ders izlencesi yerine yeni bir müfredat kararı değildir.

Dal: `release/h8-surum-adayi` · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19) · [Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17)

## Grubun iş bölümü

İki, üç ve dört kişilik gruplar paket tarifi, paket üretimi, bütünlük ve alıcı kontrollerini [grup büyüklüğüne göre](../docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşır. Her üye anlamlı bir çıktı ve gerçek katkı kaydı üretir; yazmadığı kapsamı inceler. Ortak yazılan bölüm için gerekirse grup dışından inceleyen belirlenir. Kendi sorumlularınızı ve sonuçlarınızı [grup kaydına](sablonlar/grup-kaydi.md) yazın; öğretmen örneğinin kişi ve süre varsayımlarını doğrudan kendi planınız saymayın.

| Basamak | Ekranda açılacak belge | Hazırlık sonucu |
|---|---|---|
| 1 | [Aday sürümü sabitledik](docs/01-surum-adayi.md) | Sabit kaynak, açık aday kimliği. |
| 2 | [Değişiklik notunu yazdık](docs/02-surum-notlari.md) | Ne değişti, nasıl açılır, ne bekliyor? |
| 3 | [Paket içeriğini tanımladık](docs/03-paket-tarifi.md) | 9 dosyalı çevrimdışı çalışma paketi. |
| 4 | [İki üretimi karşılaştırdık](docs/04-tekrarlanabilirlik.md) | İki üretim aynı paket içeriğini verdi. |
| 5 | [Bozuk paketi yakaladık](docs/05-butunluk-kontrolu.md) | Kontrollü bozulmalar reddedildi. |
| 6 | [Teslim dosyasını sınadık](docs/06-paketten-test.md) | Kaynak ve paket: 14’er senaryo geçti. |
| 7 | [Geri dönüşü planladık](docs/07-geri-donus.md) | Geri dönüş planı hazır; uygulanmadı. |
| 8 | [Teslim ve açık işleri kaydettik](docs/08-teslim-ve-degerlendirme.md) | İncelenebilir sürüm adayı hazır. |

## Materyal

- [Tek sayfalık, tıklanabilir süreç PDF'i](dagitim/YAZ325_Hafta_08_Surec_Infografik_Aktif_Linkli.pdf)
- [18 sayfalık H7–H8 ders anlatım rehberi](dagitim/YAZ325_Hafta_07_08_Ders_Anlatim_Rehberi.pdf)
- [Çalışan uygulama — 0.3.0-rc.1 ZIP](dagitim/Klinik_Randevu_0.3.0-rc.1.zip)
- [Gerçek CI kaydı](kanitlar/ci-kaydi.json) · [İlk koşuda yakalanan ve düzeltilen bulgu](kanitlar/ilk-ci-bulgusu.json)
- [Kabul ve teslim kapıları](docs/09-kabul-ve-teslim.md) · [Teknik başvuru kaynakları](docs/10-kaynaklar.md)
- [Grubun kendi çalışma formu](sablonlar/grup-kaydi.md)

Her basamakta önce soruyu sorun, ilgili dosyayı açın, gerçek sonucu gösterin; sonra grup kendi uygulamasını yapsın. Otomatik kontroller bağımsız insan incelemesi veya kullanıcı kabulü değildir. Öğrenci kendi sürümünü ve gerçek katkısını kaydeder.

Bağımsız inceleme, önceki PR bağımlılıklarının çözümü, birleştirme ve NFR-01–NFR-03 ölçümleri açık. Test süresi gerçekleşmiş insan emeği değildir.
