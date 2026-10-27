# 02 — Paydaşlar, ihtiyaçlar ve sorular

Ekip: Öğretmen denemesi  
Tarih: 27.10.2026  
Sürüm: Belge 0.3 — doldurulmuş öğretmen çalışma örneği  
Durum: Üç bölüm hazır. Görüşme notu, ders için önerilen kurgu yanıtlar içerir; gerçek paydaş doğrulaması yapılmadı.

Bu belge Klinik Randevu v0.1 eğitim prototipi için hazırlanmıştır. Aşağıdaki ihtiyaçlar ders senaryosu ve prototip gözlemlerinden türetilen başlangıç önerileridir; gerçek paydaş görüşmesinde doğrulanmış yanıtlar değildir. Son bölümde öğretmenin sınıfta kullanabileceği örnek senaryo yanıtları ve bunların kapsam üzerindeki etkileri yer alır.

## Paydaşlar ve ihtiyaçları

Paydaş, sistemden etkilenen, sistemin kullanımına katılan veya ihtiyaç ve iş kuralları hakkında karar sürecine katkı veren kişi ya da gruptur. Paydaşın uygulamada ayrı bir kullanıcı rolü veya ekranı bulunması zorunlu değildir.

| Paydaş | Sistemden beklediği sonuç | Soracağımız soru | Henüz doğrulanmayan varsayım |
|---|---|---|---|
| Hasta | Seçtiği doktor ve tarihte uygun saate randevu alabilmek, kendi randevusunun durumunu izlemek ve planı değişirse bekleyen randevusunu anlaşılır bir onayla iptal edebilmek. | İptal onayındaki düğmelerin “Randevuyu iptal et” ve “Vazgeç” olarak adlandırılması size daha anlaşılır gelir mi? | Hastanın bekleyen randevusunu kendi başına iptal edebilmesi gerektiğini ve önerilen ifadelerin anlaşılmayı kolaylaştıracağını varsayıyoruz. Gerçek kullanıcı geri bildirimi henüz alınmadı. |
| Resepsiyon (sekreter) | Seçili hasta adına randevu oluşturabilmek; seçili doktorun günlük kayıtlarını ve toplamlarını takip ederek randevu akışını yönetebilmek. | Hastanın talebi üzerine bekleyen randevuyu iptal edebilmeli misiniz; bu işlem hangi koşullarda yapılmalı? | Hasta adına kayıt açma ve günlük akışı izleme ihtiyacı olduğunu varsayıyoruz. Resepsiyonun gerçek kurumdaki iptal yetkisi ve koşulları henüz doğrulanmadı. |
| Doktor | Kendi günlük randevularında bekleyen ve tamamlanan muayeneleri ayırt edebilmek; biten muayenenin durumunu güncel tutabilmek. | Muayene tamamlandığında randevuyu kim, hangi anda “Tamamlandı” olarak işaretlemeli? | Tamamlama bilgisini muayene sonrasında ilgili doktorun gireceğini varsayıyoruz. Mevcut prototip bu işlemi doktor rolüne sunuyor; gerçek klinikteki iş bölümü henüz doğrulanmadı. |
| Klinik yönetimi — ek paydaş | Randevu akışının ve işlem sorumluluklarının açık olması; hasta, resepsiyon ve doktorun çalışma ihtiyaçlarına uygun bir kapsam belirlenmesi. | Hasta, doktor ve resepsiyonun farklı cihazlardan aynı kayıtları görmesi gerekiyor mu; değişiklikler diğer kullanıcılara ne kadar sürede yansımalı? | Yetki ve ortak çalışma gereksinimleri için karar verecek veya ilgili karar sahibini belirleyecek kişinin klinik yönetimi içinde olduğunu varsayıyoruz. Karar sahibi ve ortak veri ihtiyacı henüz doğrulanmadı. |

**Ek paydaşın gerekçesi:** Klinik yönetimi, rol yetkileri ve farklı cihazlardan ortak çalışma gibi birden fazla kullanıcıyı etkileyen ihtiyaçları değerlendirebilecek örnek paydaştır. Gerçek bir projede doğru karar sahibi görüşmeyle belirlenir. Bu ekleme, mevcut prototipe yeni bir yönetici rolü veya ekranı eklemez.

**Paydaş ile öğrenci görevi arasındaki ayrım:** Hasta, resepsiyon, doktor ve klinik yönetimi ürünün paydaşlarıdır. Sınıftaki 5 + 5 + 5 + 4 kişilik gruplarda belgeyi yazma, denemeyi uygulama veya sonucu kontrol etme gibi işler öğrenci sorumluluklarıdır; bunlar daha sonra `09-ekip-rolleri.md` dosyasında düzenlenecek.

**Gözlemle ilişki:** Hastaya sorulan iptal açıklığı sorusu G-03 tekrarlarına; resepsiyonun iptal yetkisi sorusu G-06'ya; doktorun tamamlama sorusu G-05-B'ye; ortak kayıt sorusu aynı dosya ve tarayıcıdaki yenileme denemesine dayanır. Bu gözlemler `08-prototip-gozlemleri.md` dosyasındadır. Gözlem, mevcut prototipin davranışını gösterir; paydaş ihtiyacının onayı ayrıca alınır.

## Rol ve işlem tablosu

Prototipte gördüğünüzü yazın. Bu gözlem, gerçek kurumun onaylanmış yetki tasarımı değildir.

Bu tablo, mevcut prototipin rol davranışlarını gösterir. **G-…**, `08-prototip-gozlemleri.md` içindeki deneme kaydına işaret eder. **Paket**, `README.md` açıklaması ve `index.html` kodu incelenerek belirlenen davranıştır; tek başına öğretmen oturumunda uygulanmış bir deneme anlamına gelmez. Evet/Hayır ifadeleri yalnız bu prototipte işlemin ilgili role sunulup sunulmadığını belirtir.

| İşlem | Hasta | Resepsiyon | Doktor | Paydaşa sorulacak nokta |
|---|---|---|---|---|
| Uygun saatleri görüntüleme | Evet; seçili doktor ve tarihin saat durumları. G-01 / G-04. | Evet; seçili doktor ve tarihin saat durumları. G-06 / Paket. | Evet; saatleri görüntüler, kayıt oluşturmak için seçemez. G-05-B / Paket. | Saatler hangi doktor ve tarihler için gösterilmeli; çalışma saatlerini kim belirlemeli? |
| Randevu oluşturma | Evet; seçili örnek hasta adına uygun saate Bekliyor kaydı. G-01. | Evet; seçili örnek hasta adına. Paket; öğretmen oturumunda bu işlem henüz uygulanmadı. | Hayır; Randevuyu onayla düğmesi pasif. G-05 / Paket. | Hasta adına yeni kayıt oluşturma yetkisi hangi rollerde olmalı? |
| Kendi randevusunu iptal etme | Evet; yalnız kendi Bekliyor kaydı için onayla. Vazgeçerse kayıt korunur. G-02 / G-03-T3. | Hayır; iptal işlemi sunulmuyor. G-06. | Hayır; iptal işlemi sunulmuyor. Paket. | Hasta dışında resepsiyon da iptal yapabilmeli mi; hangi koşullarda? |
| Günlük listeyi görüntüleme | Yalnız kendi kayıtları; seçili doktor ve tarih için Randevularım listesi. G-04. | Evet; seçili doktorun o günkü bütün örnek hasta kayıtları. G-06. | Evet; görevli olarak seçili doktorun o günkü bütün örnek hasta kayıtları. G-05. | Her rol hangi hastaların ve doktorların kayıtlarını görebilmeli? |
| Tamamlandı işlemi | Hayır. Paket. | Hayır; tamamlama işlemi sunulmuyor. G-06. | Evet; görevli olarak seçili doktorun günlük listesindeki Bekliyor kaydı için. G-05-B. | Muayene tamamlandığında bu bilgiyi kim, hangi anda girmeli? |
| Günlük toplamlar | Hayır; sayılar gösterilmez, bölümün resepsiyon ve doktora açık olduğu açıklanır. Paket; hasta görünümündeki bu alan için ayrıca deneme kaydı tutulmadı. | Evet; seçili doktor ve tarih için. G-06. | Evet; seçili doktor ve tarih için. G-05 / G-05-B. | Hangi roller hangi toplamları görmeli; doktor ve gün bazındaki özet yeterli mi? |

**Tabloyu okurken:** Saatleri görmek, o saate randevu oluşturabilmekten ayrı bir işlemdir. Hastanın kendi kayıtlarını görmesi de bütün hastaların günlük listesini görmekten farklıdır. Tamamlandı durumundaki bir randevunun saati Kapalı kalır; iptal edilen kayıt ise saati serbest bırakır.

**Kanıtın kapsamı:** Resepsiyonun kayıt oluşturması ve hasta görünümünde günlük toplamların gösterilmemesi kod/paket incelemesiyle belirlendi; bu iki davranış için öğretmen oturumunda ayrıca uygulama sonucu kaydedilmedi. Paket olarak işaretlenen diğer hücreler de kod/paket bilgisidir. Tablodaki rol seçimi eğitim amaçlıdır; gerçek kimlik doğrulama veya sunucu yetkilendirmesi kanıtı oluşturmaz.

**Rol değişimindeki hasta seçimi:** Hasta rolünde seçili kişi Randevularım listesini belirler. Resepsiyonda hasta seçimi, adına yeni kayıt açılacak kişiyi belirler; günlük listeyi tek hastaya daraltmaz. Doktor rolünde Örnek hasta seçimi pasiftir. G-04, G-05 ve G-06 bu farkları gösterir.

## Görüşme notu

**Kayıt türü:** Öğretmenin sınıfta kullanabileceği görüşme simülasyonu örnekleri.  
**Hazırlama tarihi:** 27.10.2026. Bu tarih, yapılmış bir paydaş görüşmesinin tarihi değildir.  
**Gerçek görüşme durumu:** Gerçek paydaşla görüşülmedi; alınmış yanıt veya onay bulunmuyor. Aşağıdaki yanıtlar ders için hazırlanmış önerilerdir. Sınıfta uygulanmış görüşme veya kabul edilmiş karar olarak kaydedilmemiştir.

### Örnek 1 — İptal işleminin anlaşılması

- **Soru:** İptal onayındaki düğmelerin “Randevuyu iptal et” ve “Vazgeç” olarak adlandırılması size daha anlaşılır gelir mi?
- **Öğretmenin senaryo yanıtı — kurgu:** “Evet. Hangi seçeneğin iptali gerçekleştirdiğini ve hangisinin işlemden vazgeçirdiğini açıkça anlamak istiyorum. İptali onaylayınca kaydın listede kalacağını ve saatin yeniden açılacağını da önceden görebilmeliyim.”
- **Bu yanıtın kapsam üzerindeki etkisi:** İptal akışının açıklığı bir kullanılabilirlik ihtiyacı olarak kaydedilir. Başlangıç prototipinde mevcut davranış belgelenir. Üçüncü hafta planındaki iki küçük değişiklik, ana ekrandaki iptal koşulu/sonucu açıklaması ile onay penceresinin metnidir. Bu değişiklikler henüz uygulanmadı. Tarayıcının mevcut onay penceresinde Tamam/İptal düğmeleri kullanılır; iki metin değişikliği düğme adlarını değiştirmez. Özel düğme adları olan ayrı bir pencere, ayrıca değerlendirilecek geliştirme adayıdır.
- **Bağlantı:** G-03 tekrarları; FR-03; ileride 03 numaralı belgede açıklık için ölçülebilir kullanılabilirlik hedefi ve 04 numaralı belgede kabul koşulu hazırlanacak.

### Örnek 2 — Resepsiyonun iptal yetkisi

- **Soru:** Resepsiyon hastanın talebi üzerine bekleyen randevuyu iptal edebilmeli mi; bu işlem hangi koşullarda yapılmalı?
- **Öğretmenin senaryo yanıtı — kurgu:** “Bu ilk sürümde resepsiyon hasta adına randevu oluştursun ve günlük akışı izlesin. İptali hasta kendi bekleyen kaydı üzerinde yapsın. Resepsiyona iptal yetkisi verilmesini sonraki ihtiyaç değerlendirmesinde ayrıca ele alalım.”
- **Bu yanıtın kapsam üzerindeki etkisi:** Başlangıç sürümünün mevcut rol sınırı korunur. Resepsiyona yeni iptal veya tamamlama işlemi eklenmez. Resepsiyon iptali, koşulları ve önceliği henüz kararlaştırılmamış geliştirme adayı olarak kalır. Hasta için kendi Bekliyor kaydını onayla iptal etme koşulu FR-03'te açıkça yazılacak.
- **Bağlantı:** G-06; FR-02 / FR-03 / FR-04 / FR-06; 01 numaralı belgenin başlangıç kapsamı.

### Örnek 3 — Muayenenin tamamlanması

- **Soru:** Muayene tamamlandığında randevuyu kim, hangi anda “Tamamlandı” olarak işaretlemeli?
- **Öğretmenin senaryo yanıtı — kurgu:** “Muayene bittiğinde ilgili doktor kendi günlük listesindeki bekleyen randevuyu Tamamlandı olarak işaretlesin. Hasta ve resepsiyon bu işlemi yapmasın.”
- **Bu yanıtın kapsam üzerindeki etkisi:** FR-05'in aktörü ve koşulu netleştirilir: görevli olarak seçilen doktor, kendi günlük listesindeki Bekliyor kaydı tamamlayabilir. Başlangıç prototipindeki davranış korunur; tamamlanan saatin yeniden açılmaması ve günlük sayıların tutarlı güncellenmesi kabul koşullarına aktarılacak. Bu kurgu yanıt, mevcut kodun gerçek kurum tarafından onaylandığı anlamına gelmez.
- **Bağlantı:** G-05-B; FR-05 / FR-06; BR-01.

### Örnek 4 — Farklı cihazlarda ortak kayıt

- **Soru:** Hasta, doktor ve resepsiyonun farklı cihazlardan aynı kayıtları görmesi gerekiyor mu; değişiklikler diğer kullanıcılara ne kadar sürede yansımalı?
- **Öğretmenin senaryo yanıtı — kurgu:** “İleride ortak kayıtlarla çalışmayı isteriz. Başlangıç denemesinde yerel örnek veriler yeterli olsun. Cihazlar arasında paylaşımın ayrıntılarını ve gerekli güncellenme süresini sonraki aşamada belirleyelim.”
- **Bu yanıtın kapsam üzerindeki etkisi:** Merkezi veritabanı, cihazlar arası eşzamanlama ve eşzamanlı kayıt çakışmalarını yönetme başlangıç sürümünün dışında kalır. İleri sürüm için gereksinim adayı kaydedilir; belirli bir teslim haftası veya sayısal güncellenme süresi taahhüt edilmez. Mevcut yenileme gözlemi yalnız incelenen dosya ve tarayıcı için geçerlidir.
- **Bağlantı:** 08 numaralı belgenin Kayıt davranışı bölümü; 01 numaralı belgedeki kapsam dışı maddeleri ve ortak kayıt sorusu.

**Kayıtların sonraki kullanımı:** Bu örnekler sınıfta kullanıldığında gerçek uygulama tarihi, canlandırılan roller ve öğrencilerin çıkardığı kararlar `07-toplanti-notu.md` dosyasına ders simülasyonu etiketiyle yazılacak. Gerçek bir paydaşla görüşülürse, o kişinin gerçek yanıtı ayrı kayıt olarak eklenecek. 01 numaralı belgedeki gerçek paydaş doğrulaması bekleyen sorular, bu kurgu yanıtlar nedeniyle kapanmış sayılmaz. İlk iki tablodaki diğer sorular ile ortak kayıtların güncellenme süresi açık kalır.

**Bu adımın çıktısı:** Soru, yanıtın kaynağı ve kapsam etkisi ayrı gösterilmiş dört örnek görüşme notu. Yeni uygulama testi, GitHub işlemi veya kod değişikliği yapılmış gibi kayıt oluşturulmadı.

Dayanak dosyalar: `01-vizyon-kapsam.md`, `08-prototip-gozlemleri.md`, `README.md` ve `index.html`.
