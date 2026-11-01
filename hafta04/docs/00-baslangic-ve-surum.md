# 4. hafta — Başlangıç sürümü ve çalışma kaydı

## 1. Başlangıç kaydı

| Alan | Kayıt |
|---|---|
| Hazırlık tarihi | 1 Kasım 2026 |
| Çalışma | Klinik Randevu — öğretmen örneği |
| Depo | https://github.com/pozelll/-klinik-randevu-ogretmen |
| H3 başlangıç dalı | feat/h3-iptal-acikligi |
| Sabit başlangıç commit'i | da3ce51798344a6fafaee89cce42aa9aba90de17 |
| H4 çalışma dalı | docs/h4-mimari-plan |
| Ana uygulama | Proje kökündeki index.html |
| Bu haftanın belgeleri | hafta04/docs |
| Bu haftanın çizimleri | hafta04/diagrams |
| Başlangıç yedeği | https://drive.google.com/file/d/1fio_PzFoOk3OxslarpurXVtBv55_EBR0/view |

Bu kayıt öğretmen kopyasının kaydıdır. Öğrenci grupları kendi depo, dal ve commit
bilgilerini kullanır; kendi başlangıç ve katkı kayıtlarını yazar.

## 2. Hazırlıkta kontrol edilenler

- İlk iki haftanın dokuz belgesi, çizimleri ve üçüncü hafta dosyaları başlangıç sürümünde mevcut.
- Üçüncü haftanın 01–13 belgelerinin tamamı mevcut; 13 numaralı dosya boş bireysel yanıt formu.
- index.html içinde görünür iptal açıklaması ve genişletilmiş onay metni mevcut.
- Dördüncü hafta çalışmaları hafta04 klasöründe yürütülür; önceki haftaların dosyaları korunur.
- Üçüncü basamakta 01 belgesi öğretmen örneği olarak dolduruldu. Seçim: kısa geri bildirim döngüleriyle küçük artımlar halinde çevik çalışma. Boş öğrenci kopyası hafta04/sablonlar altında korunur.
- Dördüncü basamakta randevu iptalinin arayüz, iş kuralları ve veri erişimi sorumlulukları ayrıldı. 02 belgesinin ilgili bölümleri, düzenlenebilir 01-bilesen.drawio ve aynı çizim verisinden üretilmiş PNG hazır. Boş 02 öğrenci şablonu hafta04/sablonlar altında korunur.
- Beşinci basamakta mevcut düzen ile katmanlı/modüler düzen karşılaştırıldı. H4-MK-01 ile tek tarayıcıda katmanlı yapı ve sınırlı Repository uyarlaması seçildi; yarar, maliyet ve beşinci hafta uygulama sınırları 02 belgesine yazıldı.
- Çizim seçilen tasarımı gösterecek şekilde güncellendi. index.html henüz modüllere ayrılmadı.
- Altıncı basamakta H4-P0 ilk planı hazırlandı: dört kişilik örnek ekip, dokuz görev; kritik yol A–B–E–F–G–H–I, net süre 16 blok (8 saat), toplam emek 17 kişi-saat. Süreler öğretim varsayımıdır; gerçek takvim ve kişi ataması değildir.
- İlk plan hafta04/planlar/01-ilk-is-plani.md içinde ayrıca korundu. Yedinci basamakta H4-DK-01 kartıyla karar tablosu ve satır bazında kanıt hazırlığı eklendi; C 3 → 5, F 3 → 4 blok oldu.
- H4-P1 güncel hesabı 03 belgesine yazıldı: net süre 18 blok (9 saat), emek 19 kişi-saat; yeni kritik yol A–C–E–F–G–H–I. İlk H4-P0 bölümü ve ayrı kopyası değişmedi. Bağımlılıklar ve örnek kişi atamaları korundu; kişi çakışması yok.
- Yeni kart öğretim senaryosudur; gerçek paydaş talebi, uygulama değişikliği veya yapılmış test değildir. Sekizinci basamakta gerçek bağımsız inceleme ve teslim koşulları ele alınacak.
- İlk yedi basamakta uygulamanın T01–T06 kontrolleri yeniden çalıştırılmadı. Kaynak kod, belge ve çizim tutarlılığı ile iki planın ileri/geri hesapları, farkları ve kişi çakışmaları kontrol edildi; bu işlem bağımsız ekip incelemesi veya davranış testi değildir. Boş 01, 02 ve 03 öğrenci şablonları korundu.

## 3. Önceki PR'larla bağlantı

1 Kasım 2026 kontrolünde önceki iki PR açık ve birleştirilmemiştir:

| PR | Kaynak dal | Hedef dal | Durum |
|---|---|---|---|
| https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7 | docs/izlenebilirlik | main | Açık; birleştirilmedi |
| https://github.com/pozelll/-klinik-randevu-ogretmen/pull/11 | feat/h3-iptal-acikligi | docs/izlenebilirlik | Açık; birleştirilmedi |

H4 dalı, H3 çalışmasını korumak amacıyla yukarıdaki sabit H3 commit'inden başlar.
Bu bir hazırlık dalıdır; H3'ün onaylandığı veya main'e alındığı anlamına gelmez.
H4 PR'ı bu basamakta açılmaz.

Teslim aşamasında önce önceki PR'ların güncel durumunu kontrol edin. #7 ve #11
tamamlanınca H4 dalının güncel main ile ilişkisini, olası çakışmaları ve dosya
farklarını yeniden kontrol edin. H4 incelemesinde yalnız ilgili hafta değişiklikleri
açıkça görülebilmelidir. Önceki PR'lar bekliyorsa bağımlılığı yazın ve teslimi
tamamlanmış göstermeyin.

## 4. Bilgisayardaki çalışma kaydı

Bu alanlar kullanıcının bilgisayarından doğrulanmadı.

| Alan | Kayıt |
|---|---|
| Yerel üçüncü hafta yedeğinin konumu | [Doldurulacak] |
| Yerel dördüncü hafta çalışma klasörü | [Doldurulacak] |
| Tarayıcı ve uygulama dosyasının tam yolu | [Doldurulacak] |
| GitHub'a yüklenmemiş yerel değişiklik var mı? | [Kontrol edilecek] |

Dosya yedeği tarayıcıdaki randevu verilerinin yedeği değildir. Eski dosyaları ve
verileri sıfırlamadan saklayın.

## 5. Sekizinci basamakta doldurulacak inceleme ve teslim kaydı

| Alan | Kayıt |
|---|---|
| H4 PR bağlantısı ve hedef dal | [Henüz açılmadı] |
| İncelenen commit | [Doldurulacak] |
| Yazardan farklı inceleyen kişi | [Doldurulacak] |
| Bulgular ve düzeltmeler | [Doldurulacak] |
| Birleştirme koşulları ve sonucu | [Doldurulacak] |
| Ana sürüm kontrolü ve teslim bağlantısı | [Doldurulacak] |

İnceleyen yoksa “İnceleme bekliyor” yazın. Hazırlık commit'i, bağımsız inceleme veya
tamamlanmış teslim değildir.
