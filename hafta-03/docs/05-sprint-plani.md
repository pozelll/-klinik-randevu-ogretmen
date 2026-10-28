# 3. hafta — İlk Sprint planı

Çalışma: Klinik Randevu — öğretmen uygulaması  
Tarih: 28.10.2026  
Sürüm: 0.1 — ilk plan; yeni bilgi sonrası güncelleme henüz yapılmadı  
Konum: hafta-03/docs/05-sprint-plani.md  
Sprint etiketi: H3-S1  
Durum: Plan hazır; işler uygulanmadı, test edilmedi ve tamamlanmadı.

## 1. Hedef

**Ürün hedefi:** Hasta, uygun saati seçip kendi randevusunu anlaşılır bir akışla yönetebilsin.

**Bu çalışma için Sprint hedefi:** Hastanın iptal koşullarını ve iptali onaylamak ile işlemden vazgeçmek arasındaki farkı işlem öncesinde görebileceği tutarlı açıklamaları sunmak; mevcut iptal/vazgeçme davranışlarını korumak.

**Değerlendirmede soracağımız soru:** Ana ekrandaki açıklama ile onay penceresi, iptal koşulunu ve iki seçeneğin sonucunu tutarlı biçimde söylüyor mu; iptal ve vazgeçme denemeleri beklenen sonuçları veriyor mu?

Bu soru açıklamaların varlığını, tutarlılığını ve işlevin korunmasını değerlendirmeye yöneliktir. Kullanıcıların metni daha hızlı veya daha kolay anladığını söylemek için ayrıca kullanıcı ölçümü gerekir.

## 2. Kapasite varsayımı

Bu sınıf etkinliği için kapasite **8 göreli puan** olarak verilmiştir. Ölçülmüş ekip hızı, sekiz saatlik süre veya öğrenci notu değildir. Beş kişilik gruplara otomatik olarak daha yüksek, dört kişilik gruba daha düşük puan atanmıyor; ortak alıştırmada aynı varsayımla plan yapılıyor.

135 dakikalık ders etkinliği sıkıştırılmış bir öğretim simülasyonudur. Bu plan gerçek bir ekibin geçmiş hız verilerinden çıkarılmadı. Puanlarla ders dakikaları arasında dönüşüm yapılmaz.

## 3. İlk seçim

| İş | İlk / güncel puan | İlk plandaki yeri | Hedefle ilişkisi |
|---|---:|---|---|
| H3-01 — Görünür iptal açıklaması | 2 / 2 | Seçildi; başlanmadı. | İptal koşulunu ve sonucunu işlemden önce gösterir; hedefin temel parçası. |
| H3-02 — Onay penceresinde sonucu açıklama | 3 / 3 | Seçildi; başlanmadı. | İptal ile vazgeçme farkını karar anında açıklar; hedefin temel parçası. |
| H3-03 — Saat seçimine kısa yardım | 3 / 3 | Seçildi; başlanmadı. | Randevu akışına yardımcı olur; iptal açıklığı hedefi için zorunlu değildir. |
| Toplam | 8 / 8 | Verilen kapasiteyle eşit. | 2 + 3 + 3 = 8. |

İlk iki iş kullanıcı gözlemimizle doğrudan bağlantılıdır. H3-03, başlangıç tahminlerine göre kalan kapasiteye sığdığı için yardımcı iş olarak alındı; ileride kapasite değişirse yeniden değerlendirilebilir. H3-04, H3-05 ve H3-06 iş listesinde aday olarak kalır; bu haftanın planına alınmadı.

**Bağımlılık:** H3-01 ile H3-02 aynı iptal kuralını açıklayacak. İki metnin ifadeleri uygulamadan önce birlikte kararlaştırılacak. Biri diğerinden farklı yetki veya sonuç vaat etmeyecek.

## 4. Uygulama sırası ve kanıt planı

| Sıra | İş / hazırlık | Küçük görev | Beklenen çıktı / kanıt |
|---|---|---|---|
| 1 | Ortak hazırlık | Doğru proje dosyasını ve ayrı üçüncü hafta dalını belirle; mevcut randevu verilerini koru. | Gerçek dosya konumu ve oluşturulduğunda dal bağlantısı. |
| 2 | H3-01 / H3-02 | İptal koşulu, sonuç ve seçenek açıklamalarını birlikte netleştir. | Onaylanan çalışma metni; 04 belgesindeki kabul koşullarıyla eşleşme. |
| 3 | H3-01 | Ana ekrana görünür açıklamayı uygula. | İlgili dosya farkı, commit ve gerçek ekran görüntüsü. |
| 4 | H3-02 | Mevcut iptal onay metnini güncelle. | Pencere metni, dosya farkı ve ayrı iptal/vazgeçme kontrol kayıtları. |
| 5 | H3-03 | Yardımın yerini/metnini ve kabul koşulunu yaz; ardından uygula. | Saat seçme davranışını değiştirmeyen yardım ve ilgili kontrol sonucu. |
| 6 | Ortak kalite ve teslim | Gerçek kontrolleri yap, katkıyı yazmayan kişiye incelet, bulguları gider ve son erişimi doğrula. | Test belgesi, inceleme kaydı, varsa yeniden kontrol ve teslim bağlantıları. |

04-kabul-ve-dod.md şu an ilk iki işin kabul koşullarını içerir. H3-03 uygulanacaksa kendi koşulları önceden eklenir. Başlangıç önerisi: yardım uygun saatin seçilmesi ve ardından onay verilmesini açıklasın; Dolu/Kapalı saatlerin seçilemeyeceğini doğru anlatsın; mevcut saat seçme davranışı korunsun. Bu öneri henüz onaylanmış veya denenmiş sonuç değildir.

Kalite ve teslim işleri seçilen işlerin tamamlanmasının parçasıdır; zaman kazanmak için Bitti Tanımı kaldırılmaz. Sekiz puanlık toplam, incelemenin yapılmış olduğunu veya işlerin kesin yetişeceğini göstermez.

## 5. Sınıfta sorumluluk paylaşımı

19 öğrenci: Grup 1, 2 ve 3 beşer; Grup 4 dört kişi. Gerçek adlar henüz atanmadı.

| Sorumluluk | Beş kişilik grup | Dört kişilik grup |
|---|---|---|
| Ürün hedefi ve iş sırası | 1 Product Owner sorumluluğu. | 1 Product Owner sorumluluğu. |
| Çalışmayı kolaylaştırma ve engeller | 1 Scrum Master sorumluluğu. | 1 Scrum Master sorumluluğu. |
| Uygulama ve kalite | 3 Developers; küçük işleri birlikte paylaşır. | 2 Developers; küçük işleri birlikte paylaşır. |

Bu, öğretim amaçlı sorumluluk planıdır. Herkes üretim ve kontrol çalışmasına katkı verebilir; test yalnız tek bir kişinin işi değildir. Katkıyı yazmayan veya birlikte yazmayan kişi ilgili katkıyı inceler. Gerekirse başka gruptan inceleyen seçilir. Gerçek görev paylaşımı ve katkılar çalışıldıkça kaydedilir.

Şu anda öğretmen hazırlığı yapılıyor; gerçek bir ekip planlama toplantısı yapıldığı iddia edilmiyor.

## 6. Yeni bilgi sonrası güncel plan

**Henüz hazırlanmadı.** İlk plan yukarıda korunacak. Dersin değişiklik kartı aşamasında yeni bilgi verildiğinde şu alanlar doldurulacak:

| Alan | Şimdiki durum |
|---|---|
| Yeni bilgi ve kaynağı | Henüz bu aşamada ele alınmadı. |
| Değişen tahmin ve gerekçe | Yok; ilk ve güncel tahminler aynı. |
| Yeni toplam ve kapasite farkı | Henüz yeniden hesaplanmadı. |
| Güncel seçim / ertelenen iş | Henüz karar verilmedi. |
| Hedefin nasıl korunduğu | Değişiklik kararında açıklanacak. |
| Kalitenin nasıl korunduğu | Ortak Bitti Tanımı uygulanmaya devam edecek. |

Yeni bilgi için hazırlanmış 06-degisiklik-karti.md, rehberin ilgili aşamasında ele alınacak. O kart gerçek kullanıcı şikâyeti veya yapılmış toplantı olarak sunulmayacak.

## 7. GitHub ve mevcut çalışma

Planlanan dal adı: feat/h3-iptal-acikligi; henüz oluşturulmadı. Önceki belge PR #7 açık olduğundan, kod çalışmasına başlamadan dalın başlangıç noktası ve dosyalar birlikte kontrol edilecek. Üçüncü hafta değişiklikleri yanlışlıkla önceki belge PR'ına eklenmeyecek.

Yeni H3 görevleri, PR ve test sonuçları henüz yok. Bağlantılar işlemler gerçekleştikçe yazılacak.

## Kaydetme

Bu dosyayı ilk dört belgenin yanına hafta-03/docs/05-sprint-plani.md olarak kaydedin. İlk plan tablosundaki 2 + 3 + 3 = 8 hesabını ve H3-03'ün neden yardımcı iş olduğunu okuyun.

Beklenen çıktı: İlk plan kayıtlıdır. Sonraki uygulama adımında çalışma dosyası ve GitHub dalı hazırlanacak; değişiklik kartı kendi ders aşamasında açılacak.
