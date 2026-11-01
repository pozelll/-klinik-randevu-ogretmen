# İlk dört hafta - Öğretmen ve öğrenci dağıtımı

1 Kasım 2026. Proje: Yazılım Geliştirme Süreçleri / Klinik Randevu.

| Dosya | Kullanıcı / içerik |
|---|---|
| [Ilk_4_Hafta_Ogretmen_Rehberi.pdf](Ilk_4_Hafta_Ogretmen_Rehberi.pdf) | Öğretmen: 30 sayfa; neyi/nerede/neden yaptık, dosya haritası, hesap açıklaması, sınıf gösterimi ve soru-cevap. |
| [Ilk_4_Hafta_Ogrenci_Takip_Rehberi.pdf](Ilk_4_Hafta_Ogrenci_Takip_Rehberi.pdf) | Öğrenci: 49 sayfa; önceki 33 sayfa korundu, iki başlangıç sayfası ve 14 sayfalık H4 uygulaması eklendi. |
| [Ilk_4_Hafta_Ogrenci_Calisma_Paketi.zip](Ilk_4_Hafta_Ogrenci_Calisma_Paketi.zip) | Öğrenci: 66 dosya; uygulama, ilk üç haftanın şablonları/kod parçaları, yeni H4 boş formları, çizim taslağı, plan girdileri/kartı ve öğrenci PDF'i. |
| [Ogretmen_Rehberi_Kaynak_Metin.md](Ogretmen_Rehberi_Kaynak_Metin.md) | Öğretmen PDF'inin düzenlenebilir metni. |
| [Ogrenci_H4_Eki_Kaynak_Metin.md](Ogrenci_H4_Eki_Kaynak_Metin.md) | Yeni başlangıç ve H4 sayfalarının düzenlenebilir metni. |
| [DOSYA_KONTROL.json](DOSYA_KONTROL.json) | Çıktıların boyut, SHA-256 ve PDF sayfa sayısı. |

## Devam eden öğrenci grubu

Önce kendi dolu H3 projesini yedekler. ZIP'ten yalnız 4-haftada-eklenecek/hafta04 klasörünü mevcut köke ekler. Dolu dosyaların üstüne boş başlangıç yazmaz. H4 çizimindeki üç kutu taslaktır; öğrenciler sorumlulukları ve okları tamamlayıp PNG üretir. Öğretmenin dolu H4 cevapları öğrenci çalışma dosyalarına eklenmedi.

## Öğretmen çalışma kopyası

Bu depoda docs/h4-mimari-plan dalındaki kök index.html, docs, diagrams, hafta-03 ve hafta04 birlikte öğretmen örneğini oluşturur. [Tam öğretmen çalışma ZIP'i](https://drive.google.com/file/d/1NQCBc6oMpXIZTIMRXOEr_2cBx15foto4/view) aynı proje için kullanılır. Bu dosyalar öğrenci boş şablonlarından ayrıdır.

## Kaynak ve durum

İçeriğin proje dayanağı 8b668fbed7e348fc25a7e5ffa6c69d3ae9f14f3b. İlk üç dersin öğrenci uygulaması ve şablonları Ilk_3_Ders_Ogrenci_Dagitim_Paketi_20261029.zip dosyasından bayt düzeyinde korunmuştur. Önceki 33 sayfalık [öğrenci PDF'i](https://drive.google.com/file/d/1ilMtGD5i6u0X8Fm__s8-fBRYPtdYA1oE/view) yeni PDF içinde aynı gövdeyle yer alır; birleşik sayfa numarası eklenmiştir.

H4 tasarım ve plan hazırlığı tamamlandı; bağımsız inceleme ve main'e birleştirme bekliyor. Yeni rehberler hazırlanırken uygulama testleri yeniden çalıştırılmadı. Tarihli eski aşama kayıtları, yeni başarı veya bağımsız onay gibi sunulmadı.

## Kontrol

PDF'lerin bütün sayfaları görsel olarak incelendi; sayfa taşması/kenar dışı metin kontrolü geçti. Öğrenci ZIP'i açılıp bütünlüğü ve dosya listesi kontrol edildi; beş H4 çalışma formunda doldurulacak alanlar ve boş inceleme kutuları korunuyor. Bu kontroller bağımsız insan incelemesi değildir.
