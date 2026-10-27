# Klinik Randevu — başlangıç paketi

**Yazılım Geliştirme Süreçleri · Birleşik 1–2. hafta · Sürüm 0.1**

Bu paket, gereksinim analizi ve ekip çalışma sürecini uygulamak için hazırlanmış küçük bir eğitim prototipidir. Öğrenciler önce çalışan davranışı inceler; ardından paydaş sorularını, kapsamı, gereksinimleri, kabul koşullarını ve görev kartlarını kendileri yazar. Başlangıç haftalarında C# veya Java kurulumu gerekmez.

## 1. Açma

1. ZIP dosyasının tamamını bir klasöre çıkarın. ZIP'in içinden doğrudan çalıştırmayın.
2. Bu klasördeki **index.html** dosyasına çift tıklayın.
3. Dosya güncel bir tarayıcıda açılır. JavaScript açık olmalıdır.
4. Başlangıçta **Hasta**, **Ece Yılmaz**, **Doktor Deniz Arı** ve **12 Kasım 2030** seçilidir.
5. İnternet, sunucu, paket yükleme, bulut hesabı veya ödeme gerekmez. GitHub hesabı yalnız dersin belge, issue ve pull request etkinlikleri için kullanılır.

**Ders testi:** Aynı klasördeki **ders-testi.html** dosyasını çift tıklayarak 6 soruluk çevrimdışı testi açın. Her soruda önce yanıt verin, ardından gerekçeyi okuyun. İlk deneme sonucu ve kopyalanabilir sonuç kaydı en sonda görünür. Sonucu `docs/07-toplanti-notu.md` dosyanıza aktarın; yanıtlar otomatik kaydedilmez veya gönderilmez, sayfayı yenileyince silinir.

### Ekranda nerede ne var?

| Alan | Görev |
|---|---|
| Simülasyon rolü | Hasta, Resepsiyon veya Doktor görünümünü seçer. Gerçek giriş yapmaz. |
| Örnek hasta | Hasta rolünde canlandırılan, resepsiyon rolünde adına kayıt açılacak kişiyi seçer. |
| Doktor / Görevli doktor | İncelenen doktoru; doktor rolünde canlandırılan doktor kimliğini seçer. |
| Tarih | 12 veya 13 Kasım 2030 örnek gününü seçer. |
| B1 — Uygun saatler | Saatleri inceleme, uygun saati seçme ve randevuyu onaylama. |
| B2 — Randevularım / Günlük randevu listesi | Role göre kayıtları ve izin verilen işlemleri gösterir. |
| B3 — Günlük toplamlar | Resepsiyon ve doktora, seçili doktor/tarih için sayıları gösterir. |
| Örnek veriyi sıfırla | Onayınızdan sonra başlangıç verilerini geri getirir. |

## 2. Altı işlev

| Kimlik | İşlev | Demodaki davranış |
|---|---|---|
| FR-01 | Uygun saatleri listeleme | Seçili doktor ve tarihin saatleri Uygun, Dolu veya Kapalı olarak görünür. |
| FR-02 | Randevu oluşturma | Hasta ve Resepsiyon uygun saat seçip Randevuyu onayla düğmesini kullanır. |
| FR-03 | Kendi randevusunu iptal etme | Hasta yalnız kendi Bekliyor kaydını onay vererek iptal eder; saat yeniden uygun olur. |
| FR-04 | Yetkili günlük liste | Resepsiyon ve Doktor, seçili doktor ve tarihin bütün örnek kayıtlarını görür. |
| FR-05 | Randevuyu tamamlama | Yalnız Doktor, görevli olarak seçili doktorun Bekliyor kaydını Tamamlandı yapar. |
| FR-06 | Yetkili günlük toplamlar | Resepsiyon ve Doktor bekleyen, tamamlanan, iptal edilen ve toplam kayıt sayısını görür. |

Hasta görünümünde B2 yalnız seçili hasta, doktor ve tarihteki kayıtları gösterir. Resepsiyon bu prototipte iptal veya tamamlama yapmaz. Doktor rolünde randevu oluşturulmaz. Bu davranışları gereksinim belgenize aktarmadan önce inceleyin; bir prototipin mevcut davranışı, paydaşın onaylanmış ihtiyacıyla aynı şey değildir.

**BR-01:** Aynı doktor, tarih ve saat için iptal edilmemiş ikinci randevu oluşturulamaz. Bekliyor ve Tamamlandı kayıtları saati kapatır. İptal edilmiş kayıt saati serbest bırakır; kayıt geçmişte kalır.

## 3. Sabit örnek veri

Tüm adlar ve kayıtlar sentetiktir. Ece Yılmaz ve Kaan Demir örnek hastalar; Deniz Arı ve Selin Kaya örnek doktorlardır. Takvim yalnız **12–13 Kasım 2030** günlerini kullanır. Bilgisayarın bugünkü tarihine göre değişmez; geçmiş saat engeli uygulanmaz.

Sıfırlama sonrasında Deniz Arı / 12 Kasım 2030:

| Kayıt | Hasta | Saat | Durum |
|---|---|---|---|
| R001 | Ece Yılmaz | 09:00 | Bekliyor |
| R002 | Kaan Demir | 10:00 | Bekliyor |
| R003 | Ece Yılmaz | 11:00 | Tamamlandı |
| R004 | Kaan Demir | 13:00 | İptal edildi |

**09:30 başlangıçta uygundur.** Diğer doktor ve tarihte de örnek kayıtlar vardır.

## 4. Kayıtların saklanması

Veri sunucuya gönderilmez. Tarayıcı izin verirse randevu değişiklikleri `localStorage` içinde bu tarayıcıda saklanır. Yerel dosyaların saklama davranışı tarayıcıya ve dosyanın konumuna bağlı olabilir. Dosyayı taşımak, farklı tarayıcı kullanmak veya tarayıcı verilerini temizlemek önceki kaydı erişilemez kılabilir.

Kalıcı saklama kullanılamıyorsa uygulama aynı oturumda bellekte çalışır; sayfa yenilendiğinde başlangıç verileri geri gelir. Ekranın altındaki **Kaydetme** açıklamasını okuyun. Rol, hasta, doktor ve tarih seçimleri yeniden açılışta başlangıç değerlerine döner; saklanan kısım randevu kayıtlarıdır.

Aynı anda tek sekmeyle çalışın. Sekmeler, tarayıcılar ve cihazlar arasında eşzamanlama veya eşzamanlı çakışma önleme garantisi yoktur. Öğrencilerin kopyaları ortak bir veritabanı kullanmaz.

## 5. Belgeler ve görev kartları

`docs/` klasöründeki alanları ekibiniz doldurur. Köşeli parantezli yerler boş çalışma alanlarıdır. `issues/` klasöründeki altı kartı GitHub Issue içine kopyalayabilirsiniz; dosyaların varlığı GitHub'da otomatik issue oluşturmaz. GitHub işlemleri için ders rehberindeki adımları izleyin.

1. Vizyon ve kapsam
2. Paydaşlar ve sorular
3. Gereksinimler ve iş kuralı
4. Kabul koşulları
5. İzlenebilirlik
6. Riskler
7. Toplantı ve karar notu
8. Prototip gözlemleri
9. Dönüşümlü ekip rolleri

## 6. Sınırlar

Rol seçimi gerçek kimlik doğrulama değildir. Kontroller yalnız istemci tarafında eğitim amaçlıdır; geliştirici araçlarıyla değiştirilebilir. Gerçek hasta verisi veya kurum sistemi için kullanılmaz. Sunucu, güvenli kimlik altyapısı, ortak veritabanı, C#/Java MVC uygulaması, otomatik test/CI servisi, e-posta veya SMS bu pakette bulunmaz.

Daha ayrıntılı özellik ve sınırlar: **BILINEN_KISITLAR.md**. Bu prototip 1–2. haftanın inceleme aracıdır; ilerideki MVC projesinin tamamlanmış hali değildir.

## Lisans

Özgün başlangıç dosyaları MIT lisansıyla sunulmuştur. Lisans metni **LICENSE** dosyasındadır.
