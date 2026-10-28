# 3. hafta — Ürün iş listesi (Product Backlog)

Çalışma: Klinik Randevu — öğretmen uygulaması  
Tarih: 28.10.2026  
Sürüm: 0.1 — ilk sıralama ve başlangıç tahminleri  
Konum: hafta-03/docs/03-product-backlog.md

## Bu dosya ne işe yarar?

Üründe yapılabilecek işleri bir araya getirir ve hangi işe neden önce bakacağımızı açıklar. Bir işin bu listede olması, bu hafta yapılacağı veya tamamlandığı anlamına gelmez. Bu haftaya alınacak işler daha sonra 05-sprint-plani.md içinde seçilecek.

Dayanak: 01-ekip-hedef.md içindeki kullanıcı faydası ve 02-gozlem.md içindeki önceki iptal/vazgeçme gözlemleri. İlk iki iş bu gözlemlere dayanır; diğerleri eğitim için hazırlanmış aday iyileştirmelerdir, gerçek kullanıcı talebi olarak doğrulanmamıştır.

## İlk iş listesi

| Sıra | İş kimliği | Yapılacak iş | Bağlantı | İlk puan | Güncel puan | Bağımlılık / açık karar | Durum |
|---|---|---|---|---:|---:|---|---|
| 1 | H3-01 | Ana ekranda iptal koşulunu ve sonucunu görünür açıklamak. | FR-03 | 2 | 2 | Açıklama mevcut rol ve randevu kurallarıyla uyumlu olmalı. | Aday; başlanmadı. |
| 2 | H3-02 | Onay penceresinde iptal ve vazgeçme seçeneklerinin sonucunu açıklamak. | FR-03 / BR-01 | 3 | 3 | H3-01 ile ortak ve tutarlı metin kararı gerekir. | Aday; başlanmadı. |
| 3 | H3-03 | Saat seçimine kısa yardım eklemek. | FR-01 / FR-02 | 3 | 3 | Yardımın yeri ve metni netleştirilecek. | Aday; başlanmadı. |
| 4 | H3-04 | Randevuyu başka saate taşımak. | Yeni gereksinim adayı | 8 | 8 | Taşıma yetkisi, çakışma ve eski kaydın durumu kararlaştırılmalı. | Gelecek için aday; bu haftanın kapsamı dışında. |
| 5 | H3-05 | SMS ile hatırlatma göndermek. | Yeni gereksinim adayı | 8 | 8 | Sunucu, hizmet sağlayıcı ve izin tasarımı gerekir. | Gelecek için aday; bu haftanın kapsamı dışında. |
| 6 | H3-06 | Doktorlar arası özet görünümü hazırlamak. | FR-06 genişletme adayı | 5 | 5 | Özeti kimin göreceği ve hangi verilerin sayılacağı kararlaştırılmalı. | Gelecek için aday; bu haftanın kapsamı dışında. |

## İlk iki işi neden öne aldık?

**H3-01:** Hasta, iptal işlemine başlamadan önce hangi randevuyu iptal edebileceğini ve sonucunu görsün. Önceki gözlemimizle doğrudan bağlantılı ve sınırlı bir değişikliktir.

**H3-02:** Hasta, karar verdiği anda Tamam ile iptali onayladığını; İptal ile işlemden vazgeçip randevuyu koruduğunu anlayabilsin. H3-01 ile birlikte aynı kullanıcı ihtiyacını karşılamayı hedefler. Tarayıcının düğme adları değiştirilmez; açıklama metni düzenlenir.

H3-03 yardımcı bir öneridir; iptal açıklığını iyileştirmek için zorunlu değildir. Son üç aday daha geniş kapsam veya yeni kararlar gerektirir. Bu sıra öğretmen uygulaması için önerilen başlangıç sırasıdır; ölçülmüş kullanıcı değeri sıralaması değildir.

## Puanları nasıl okuyacağız?

Buradaki puanlar sınıf etkinliğinde karşılaştırma yapmak için verilmiş başlangıç tahminleridir. Saat, gün, öğrenci notu veya tamamlanma yüzdesi değildir. İşin kapsamını, zorluğunu ve belirsizliğini birlikte düşünmek için kullanılır. Gerçek bir ekibin yaptığı tahmin toplantısının sonucu olarak sunulmaz.

Örneğin H3-01 için 2, H3-02 için 3 puan verilmesi ikinci işin göreli olarak daha fazla uğraş gerektirebileceğini varsayar; 3 saat süreceği anlamına gelmez. İlk ve güncel puanlar şimdilik aynıdır. Yeni bilgi geldiğinde ilk tahmini koruyup güncel tahmini ve değişiklik gerekçesini ayrıca yazacağız.

Bu adımda bütün puanları toplayıp haftalık teslim sözü vermiyoruz. Kapasiteyi ve seçimi 05-sprint-plani.md içinde ele alacağız.

## GitHub bağlantıları

H3-01–H3-06 bu belgedeki iş kimlikleridir; GitHub Issue numarası değildir. Henüz üçüncü hafta için gerçek görev oluşturulmadı.

| İş kimliği | Gerçek Issue URL |
|---|---|
| H3-01 | Henüz oluşturulmadı. |
| H3-02 | Henüz oluşturulmadı. |
| H3-03 | Henüz oluşturulmadı. |
| H3-04 | Henüz oluşturulmadı. |
| H3-05 | Henüz oluşturulmadı. |
| H3-06 | Henüz oluşturulmadı. |

Önceki Issue #3, FR-03 belgesinin doğrulanmasıyla ilgilidir. Bu haftanın kod değişikliği işi olarak otomatik kullanılmaz. Gerçek bağlantılar görevler oluşturulunca eklenecek.

## Sınıfta uygulanışı

Üç beş kişilik ve bir dört kişilik grup, kendi gözlemlerini kullanarak ilk iki tercihini gerekçelendirecek. Bir öğrenci listeyi yazarken diğerleri ihtiyaç bağlantısını, kapsamı ve tahminlerin gerekçesini tartışacak. Gerçek isimler ve katkılar çalışma yapıldıktan sonra kaydedilecek. Öğretmenin hazır sırasını kopyalamak yerine farklı sıra öneren grup, gerekçesini açıklayabilir.

## Kaydetme

Bu dosyayı 01-ekip-hedef.md ve 02-gozlem.md ile aynı hafta-03/docs klasörüne 03-product-backlog.md adıyla kaydedin.

Beklenen çıktı: İlk iş listesi, başlangıç tahminleri ve öncelik gerekçesi kayıtlıdır. Kod değişikliği ve test sonucu henüz yoktur.

Sonraki dosya: 04-kabul-ve-dod.md. Seçmeyi düşündüğümüz işler için beklenen sonucu ve bir işi tamamlandı sayma koşullarını açıklayacağız.
