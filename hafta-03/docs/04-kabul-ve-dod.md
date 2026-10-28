# 3. hafta — Kabul koşulları ve Bitti Tanımı

Çalışma: Klinik Randevu — öğretmen uygulaması  
Tarih: 28.10.2026  
Sürüm: 0.2 — değişiklik kartı sonrası kabul koşulları  
Konum: hafta-03/docs/04-kabul-ve-dod.md  
Durum: İlk açıklamalar f857deb ile kaydedildi; R011 onaylı iptal ve R012 vazgeçme gözlemleri mevcut. Tamamlandı sınırını açıkça söyleyen ek cümle çalışma kopyasında hazırlandı; kullanıcının yeni sürüm kontrolü, kalan testler ve bağımsız inceleme bekliyor.

## İki kavramı nasıl ayırıyoruz?

**Kabul koşulu:** Belirli bir işin beklenen sonucunu tarif eder. Örneğin H3-02 için onay penceresinin Tamam ve İptal seçeneklerini açıklaması.

**Bitti Tanımı (Definition of Done / DoD):** Bu ders uygulamasında her iki iş için ortak kalite ve teslim koşullarıdır. Metnin uygulanması, gerçek kontrol, başka kişinin incelemesi ve erişilebilir kanıt birlikte değerlendirilir.

Bu dosya, önceki docs/04-kabul-kriterleri.md belgesinin yerine geçmez. Önceki FR-03, AC-03, ALT-01 ve BR-01 davranışlarına bağlı kalarak üçüncü haftanın iki metin değişikliğini ayrıntılandırır. 05-sprint-plani.md güncel seçiminde H3-01 ve H3-02 korunuyor; 06-degisiklik-karti.md ile Tamamlandı sınırının açıkça yazılması eklendi.

## 1. İşe özel kabul koşulları

| Kimlik | İş | Verilen durum | İşlem | Beklenen sonuç |
|---|---|---|---|---|
| H3-AC01 | H3-01 | Hasta rolünde ana ekran açık. | İptal işlemini başlatmadan ana açıklamayı oku. | Açıklama onay penceresi açılmadan görünür; hastanın kendi Bekliyor randevusunu iptal edebildiğini söyler. Tamamlandı durumundaki randevuların iptal edilemeyeceğini ayrıca açıkça söyler. Resepsiyon veya Doktora yeni iptal yetkisi vaat etmez. |
| H3-AC02 | H3-01 | Ana ekranda yeni açıklama bulunuyor. | Metni mevcut iptal ve saat kuralıyla karşılaştır. | İptal edilen kaydın listede kaldığı açıklanır. Aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt yoksa saatin yeniden uygun olduğu belirtilir. Metin BR-01 ile çelişmez. |
| H3-AC03 | H3-02 | Hasta kendi Bekliyor randevusunu görüyor. | İlgili kartta İptal et seçeneğiyle pencereyi açıp metni oku. | İlgili randevu ayırt edilebilir; Tamam seçiminin iptali onayladığı, İptal seçiminin işlemden vazgeçip randevuyu koruduğu açıkça yazılıdır. Kayıt ve saat üzerindeki iptal sonucu ana açıklamayla tutarlıdır. |
| H3-AC04 | H3-02 | Ayrı ayrı planlanmış iki denemede hastanın kendi Bekliyor kaydı var; aynı zaman diliminde başka iptal edilmemiş kayıt yok. | Önce vazgeçme denemesinde penceredeki İptal'i; ayrı iptal denemesinde Tamam'ı seç. | Vazgeçmede kayıt Bekliyor ve saat Dolu kalır. Onaylanan iptalde kayıt İptal edildi olarak listede kalır, saat Uygun olur. Her denemede yeni kayıt oluşmaz ve toplam kayıt sayısı değişmez. |
| H3-AC05 | H3-01 | Hasta / Ece / Deniz / 12.11.2030; R003 / 11:00 Tamamlandı. | Yeni ana açıklamayı, R003 işlem alanını ve 11:00 saatini incele. | Metinde Tamamlandı durumundaki randevuların iptal edilemeyeceği açıkça görünür. R003 üzerinde İptal et düğmesi yoktur; 11:00 Kapalı kalır. |

Bu satırlar beklenen sonuçlardır; Geçti sonucu değildir. Açıklama ve pencere kontrolleriyle davranış denemeleri, daha sonra 08 test belgesinde ayrı sonuçlarla kaydedilecek. H3-AC04 iki ayrı deneme içerir; biri başarılı diye diğeri başarılı sayılmaz.

## 2. Ortak Bitti Tanımı — sınıf uygulaması

| Ortak koşul | Gerekli kanıt | H3-01 | H3-02 |
|---|---|---|---|
| 1. İlgili değişiklik uygulanmış ve kapsamla uyumlu. | Değişen dosya, gerçek commit/PR bağlantısı ve ilgili kod farkı. | Bekliyor | Bekliyor |
| 2. İşe özel kabul koşulları ve ilgili mevcut davranışlar gerçekten kontrol edilmiş. | Rol, başlangıç kaydı, adımlar, beklenen/gözlenen sonuç ve tarih içeren test kaydı; uygun ekran kanıtı. | Bekliyor | Bekliyor |
| 3. Katkıyı yazmayan veya birlikte yazmayan başka bir kişi incelemiş. | Gerçek inceleyen kişi, tarih ve inceleme sonucu. | Bekliyor | Bekliyor |
| 4. Teslimi engelleyen bulgular giderilmiş ve yeniden kontrol edilmiş. | Bulgu varsa düzeltme ve tekrar kontrol kaydı; yoksa gerçek incelemenin bulgu bulunmadığı sonucu. | Bekliyor | Bekliyor |
| 5. Güncel ürün, belgeler ve kanıtlara erişilebiliyor. | Son sürümün dosya/commit bağlantıları ve erişim kontrolü; iş, kabul koşulu, test ve PR bağlantıları tutarlı. | Bekliyor | Bekliyor |

Bu beş satır ders için belirlenen ortak koşullardır. Tek kişinin kendi kontrolü, başka kişinin incelemesi yerine geçmez. Öğretmen hazırlığında bağımsız inceleme yapılana kadar ilgili satır Bekliyor kalır. Gerçekleştirilmemiş işlem için isim, tarih veya bağlantı yazılmaz.

## 3. Kontrolün sınırları

- Hasta, Resepsiyon ve Doktorun mevcut yetkileri korunur. Bu çalışma rol yetkisi eklemez.
- Tarayıcının yerel onay penceresinin düğme adları değiştirilmez; açıklama metni düzenlenir. Kontrol tablosu önceki Türkçe tarayıcı ekranımızdaki Tamam/İptal adlarını kullanır.
- Bu çevrimdışı eğitim prototipindeki rol seçimi gerçek kimlik doğrulaması veya sunucu güvenliği kanıtı değildir.
- İşlevin doğru çalışması, metnin tüm kullanıcılarca kolay anlaşıldığını kanıtlamaz. Önceki kalite ölçümleri yapılmadıkça Ölçülmedi olarak kalır; öğretmenle yönlendirilmiş denemeler bağımsız kullanıcı ölçümü yerine sayılmaz.
- Mevcut öğretmen verileri bu belgeyi hazırlamak için sıfırlanmaz. Geçmişte R011'in korunduğunu gösteren G-03-T3, yeni metin uygulanmış sürümün testi sayılmaz.

## 4. Testi nasıl kaydedeceğiz?

Her denemede önce kullanılan sürüm, rol, doktor, tarih ve kayıt kimliği yazılacak. Beklenen sonuç bu belgeden alınacak; gözlenen sonuç yalnız deneme yapıldıktan sonra doldurulacak. Sonuç Geçti, Kaldı veya Yapılmadı olarak belirtilecek. İptal denemesinde kayıt durumu değişeceği için kullanılacak başlangıç kaydı ayrıca planlanacak; eski öğretmen kaydı gelişigüzel iptal edilmeyecek.

## 5. Şimdiki karar

**H3-01 ve H3-02 henüz tamamlanmadı.** İlk uygulama ve bazı gözlemler mevcut; yeni ek cümlenin kullanıcı ekranında doğrulanması, kalan kontroller, bağımsız inceleme ve teslim bekleniyor. Plan belgesinin kaydedilmesi, ürün değişikliğinin tamamlanması değildir.

## Kaydetme ve sonraki adım

Bu dosyayı hafta-03/docs klasörüne, ilk üç belgenin yanına 04-kabul-ve-dod.md adıyla kaydedin. Özellikle H3-AC04 satırını ve ortak beş koşulu okuyun.

Sonraki adım: Güncellenmiş index.html ile H3-AC05 kontrolünü yapmak ve gerçek sonucu test kaydına aktarmak. Sonrasında yeni kod ve belge değişiklikleri çalışma dalına kaydedilecek.
