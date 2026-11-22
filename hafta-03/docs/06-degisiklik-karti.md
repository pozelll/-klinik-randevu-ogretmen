# 3. hafta — Değişiklik kartı ve plan kararı

Tarih: 28.10.2026  
Sürüm: 0.1  
Konum: hafta-03/docs/06-degisiklik-karti.md

## 1. Derste verilen yeni bilgi

**Eğitim senaryosu:** “Tamamlandı durumundaki randevunun iptal edilemediğini ana açıklamada da açıkça okuyabilmeliyim.”

Bu, ders için hazırlanmış değişiklik kartıdır; gerçek bir paydaş görüşmesi veya kullanıcı şikâyeti değildir. Önceki yanlış Tamam seçimi bu talebin kaynağı olarak gösterilmez.

Uygulama zaten yalnız hastanın kendi Bekliyor kaydının iptaline izin veriyor. Yeni iş, ana açıklamada Tamamlandı kaydının iptal edilemeyeceğini ayrıca belirtmek ve R003 üzerinden bu sınırı kontrol etmektir. Rol veya işlem yetkisi değişmeyecek.

## 2. Tahmin değişikliği — öğretim varsayımı

H3-01 ilk tahmini 2 olarak korunur; güncel tahmini 3 olur. Diğer tahminler ve 8 puanlık kapasite aynı kalır. Bu bir ders varsayımıdır; gerçek ekip ölçümü veya kalan çalışma süresi hesabı değildir. H3-01'in önceki açıklama kısmı uygulanmış olsa da inceleme ve yeni kapsam beklediğinden iş Tamamlandı değildir.

| Hesap | Sonuç |
|---|---:|
| İlk plan: H3-01 (2) + H3-02 (3) + H3-03 (3) | 8 |
| Aynı kapsamın yeni tahmini: 3 + 3 + 3 | 9 |
| Kapasite | 8 |
| Kapasite aşımı | 1 |
| Güncel seçim: H3-01 (3) + H3-02 (3) | 6 |
| Bu seçim sonrası ayrılmamış kapasite | 2 |

## 3. Öğretmen uygulaması için karar

- H3-01 ve H3-02 güncel planda kalır; iptal açıklığı hedefine doğrudan hizmet eder.
- H3-03 saat seçimi yardımı bu çalışmadan çıkarılıp ürün iş listesinde bekletilir. Silinmez veya tamamlandı sayılmaz.
- Kalan 2 puana, 3 puanlık H3-03 sığmadığı için iş zorla eklenmez. Her kapasite biriminin mutlaka doldurulması gerekmez.
- Test, bağımsız inceleme ve diğer ortak Bitti Tanımı koşulları korunur.
- İlk plan ve ilk tahminler silinmez; değişiklik gerekçesi bu kartla izlenir.

Bu, öğretmen hazırlığı için örnek karardır. Gerçek bir Product Owner/Developers toplantısı yapılmış gibi katılımcı veya toplantı sonucu yazılmadı. Sınıfta gruplar kararı tartışıp kendi gerekçelerini kaydeder.

## 4. Uygulanacak küçük ek değişiklik

Ana açıklamaya eklenecek cümle: **Tamamlandı durumundaki randevular iptal edilemez.**

04-kabul-ve-dod.md içinde H3-01'e ilişkin kabul koşulu bu açık ifadeyi içerecek şekilde güncellenecek. R003 Tamamlandı kaydında İptal et düğmesinin bulunmadığı ve 11:00'ın Kapalı kaldığı ayrıca kaydedilecek. Önceki görüntüde bu görünüm vardı; yeni ek metin uygulanmış sürüm için kontrol henüz yapılmadı.

Kod ve kabul koşulu değişikliği bu kart hazırlanırken henüz uygulanmadı. Sonraki adımda birlikte yapılacak.

## 5. İlerleme ve GitHub

Son doğrulanan kod commit'i: f857deb — İptal koşulunu ve onay seçeneklerini açıkla. Dal: feat/h3-iptal-acikligi. Ekranda index.html bu commit mesajıyla görünüyor; dosya farkının tüm satırları bu görüntüde açık değil.

Yeni ek cümle bu commit içinde yapılmış sayılmaz. H3 görevleri/pano güncellemesi henüz yapılmadı. Görev kartları oluşturulduğunda H3-01 kapsamı ve güncel puanı 3, H3-02 puanı 3, H3-03'ün ertelendiği açıkça gösterilecek. H3-01/H3-02 bağımsız inceleme beklediği için Done işaretlenmeyecek.

## 6. Kaydedilecek belgeler

06-degisiklik-karti.md yeni dosyadır. 03-product-backlog.md ve 05-sprint-plani.md güncellendi; eski ilk tahmin ve ilk plan korunuyor. Üç dosya aynı hafta-03/docs klasörüne kaydedilir. GitHub'a yükleme henüz gerçekleşmedi.
