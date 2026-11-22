# YAZ325 — 7. ve 8. hafta öğretmen çalışma paketi

| Hafta | Konu | GitHub incelemesi |
|---|---|---|
| [7. hafta](hafta07/README.md) | Ertelenen görev, kontrollü değişiklik, kabul ve regresyon | [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18) |
| [8. hafta](hafta08/README.md) | Tekrarlanabilir aday paket, bütünlük, paket testi ve teslim | [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19) |

- [7. hafta süreç PDF'i](hafta07/dagitim/YAZ325_Hafta_07_Surec_Infografik_Aktif_Linkli.pdf)
- [8. hafta süreç PDF'i](hafta08/dagitim/YAZ325_Hafta_08_Surec_Infografik_Aktif_Linkli.pdf)
- [18 sayfalık H7–H8 ders anlatım rehberi](hafta08/dagitim/YAZ325_Hafta_07_08_Ders_Anlatim_Rehberi.pdf)
- [Çalışan uygulamanın ZIP'i — 0.3.0-rc.1](hafta08/dagitim/Klinik_Randevu_0.3.0-rc.1.zip)

Güncel birleşik ders dalı `release/h8-surum-adayi`. ZIP'i tamamen ayıklayın; index.html ile src/ birlikte tutulmalıdır. Uygulamayı açmak için Python veya Node.js gerekmez. Paket üretimi ve test araçları için [H8 yönergesini](hafta08/docs/06-paketten-test.md) izleyin.

30 Node testi, 14 kaynak tarayıcı senaryosu, 8 paket kontrolü ve aynı 14 senaryonun ayıklanmış dağıtım paketindeki yürütümü geçti. [Gerçek CI kaydı](hafta08/kanitlar/ci-kaydi.json). Bağımsız inceleme, kullanıcı kabulü, NFR ölçümleri ve birleştirme bekliyor; nihai Release yayımlanmadı. main henüz bu haftaları içermez.

Aşağıdaki haftalık açıklamalar tarihsel başlangıç kayıtlarıdır; güncel durum için yukarıdaki bağlantıları kullanın.

---

# YAZ325 — 7. hafta: kontrollü değişiklik yönetimi

- [7. hafta: sekiz basamak ve gerçek kanıtlar](hafta07/README.md) · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)
- [Tek sayfalık süreç PDF'i](hafta07/dagitim/YAZ325_Hafta_07_Surec_Infografik_Aktif_Linkli.pdf)

H3'te ertelenen #10 saat seçimi yardımı uygulandı. Güncel öğretmen dalı `feat/h7-saat-secimi-yardimi`; main henüz bu çalışmaları içermez. 30/30 Node testi ve 14/14 Chromium senaryosu geçti. Bağımsız inceleme, birleştirme ve NFR ölçümleri bekliyor.

Aşağıdaki haftalar tarihsel çalışma kayıtlarıdır; H7'nin güncel uygulaması saat yardımını da içerir.

---

# YAZ325 - 5. ve 6. hafta öğretmen çalışma paketi

- [5. hafta: mimariyi koda aktarma](hafta05/README.md) · [PR #15](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15)
- [6. hafta: karar tablosu, test kanıtı ve CI](hafta06/README.md) · [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16)
- [Yeniden çalıştırma](hafta06/docs/10-yeniden-calistirma.md) · [İzlenebilirlik](hafta06/docs/09-izlenebilirlik.md)

Uygulama: H5 kodu. H6: aynı uygulama üzerine test, CI ve öğretim belgeleri.
30 Node testi ve 9 Chromium senaryosu doğrulandı. Bağımsız inceleme ve birleştirme bekliyor.
Güncel ders dalı: `test/h6-karar-tablosu`; main henüz bu haftaları içermez.

---

# 5. hafta - Modüler Klinik Randevu öğretmen örneği

Bu dal, H4-MK-01 mimari kararını uygulayan öğretmen çalışma sürümüdür.
Başlangıç: `docs/h4-mimari-plan`, commit `5bb20cd2dbe10be9b246bbfee627a5d3fc771f8e`.
Önceki PR #7, #11 ve #12 açık olduğu için çalışma ayrı dalda sürdürülür.

## Açma ve deneme

Depo paketini tamamen ayıklayın. `index.html` ile `src/` klasörünü aynı kökte tutun.
`index.html` dosyasını tarayıcıda açın. Yalnız HTML dosyasını kopyalamak yeterli değildir.
Uygulama için Node.js veya sunucu gerekmez; otomatik testleri çalıştırmak için Node.js gerekir.
Yerel dosyalarda saklama davranışı tarayıcıya bağlıdır; kaydetme durumunu alt bölümden okuyun.

```bash
node --test tests/h5-smoke.test.cjs
```

Arayüz: `src/ui.js`; iş kuralları: `src/rules.js`; veri erişimi: `src/repository.js`.
`src/demo-data.js` ortak sentetik veri ve biçim sözlüğüdür, dördüncü bir mimari katman değildir.
H5 testleri 8/8 geçti; ayrıntılı ders belgeleri `hafta05/` altında izlenir.

Gerçek hasta verisi, gerçek giriş ve çoklu cihaz eşzamanlaması bu örneğin kapsamı dışındadır.
Otomatik kontrol bağımsız kişi incelemesi değildir. Önceki haftaların aşağıdaki yönergeleri tarihsel başlangıç bağlamıdır; bu dalı açarken yukarıdaki çok dosyalı düzen geçerlidir.

---

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

