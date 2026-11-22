# 3. hafta — Ekip ve ürün hedefi

Çalışma: Klinik Randevu — Pınar Kızıloğlu öğretmen uygulaması  
Hazırlık tarihi: 28.10.2026  
Sürüm: 0.1 — üçüncü haftanın başlangıç planı  
Dosyanın projedeki yeri: hafta-03/docs/01-ekip-hedef.md  
Durum: Hedef ve kapsam hazırlandı. Üçüncü haftanın kod değişiklikleri, yeni testleri ve bağımsız incelemesi henüz yapılmadı.

Mevcut depo: https://github.com/pozelll/-klinik-randevu-ogretmen  
Önceki belge çalışması: PR #7; 2 commit, 10 değişen dosya; son görülen durum Open / No reviews.  
Son doğrulanan belge commit'i: 7d27505.  
Kullanılan yerel index.html yolu: Henüz bu belgeye yazılmadı; randevu denemelerinde kullanılan mevcut dosyanın yolu daha sonra kaydedilecek.  
Üçüncü haftanın dalı: feat/h3-iptal-acikligi — planlanan ad; henüz oluşturulmadı.

## Bu dosyayı neden yazıyoruz?

Kod değiştirmeden önce hangi kullanıcı sorununu ele alacağımızı ve bu çalışmanın sınırını açıklıyoruz. Aynı Klinik Randevu projesine devam ediyoruz. Bu dosya, önceki docs/01-vizyon-kapsam.md dosyasının yerine geçmez; üçüncü haftanın ayrı çalışma kaydıdır.

## Ürün hedefi

**Hasta, uygun saati seçip kendi randevusunu anlaşılır bir akışla yönetebilsin.**

Bu hedef kullanıcıya sağlanacak faydayı anlatır. Bir düğme eklemek veya bir dosyayı yüklemek, tek başına ürün hedefi değildir.

## Bu haftanın odak noktası

**Hasta, randevuyu iptal etmeyi onaylamak ile iptal işleminden vazgeçerek randevusunu korumak arasındaki farkı işlemden önce anlayabilsin.**

Bu, üçüncü haftanın planlanan iyileştirmesidir; başarılmış sonuç değildir. Sprint hedefi ve seçilecek işler, daha sonra hafta-03/docs/05-sprint-plani.md içinde birlikte netleştirilecek.

### Bu ihtiyacı nereden çıkardık?

- Önceki G-03-T1 ve G-03-T2 denemelerinde vazgeçme görevi planlanmışken onay penceresindeki Tamam seçildi ve iptal gerçekleşti.
- G-03-T3'te penceredeki İptal seçildi; R011 Bekliyor, 09:00 Dolu kaldı.
- Bu kayıtlar, iki seçeneğin anlamının öğretimde açıklanması gerektiğini gösterdi. Bütün kullanıcıların hata yaptığı veya yazılımın vazgeçme işlemini yanlış uyguladığı sonucu çıkarılmadı.
- İlgili belgeler: ../../docs/08-prototip-gozlemleri.md, ../../docs/03-gereksinimler.md içindeki FR-03 ve ../../docs/06-riskler.md içindeki RSK-01.

Bu bölüm önceki gözlemlere dayanır. Üçüncü hafta için yeni başlangıç denemesi yapılmış gibi kaydedilmez.

## Planlanan iki küçük ürün değişikliği

| Değişiklik | Kullanıcıya faydası | Şimdiki durum |
|---|---|---|
| Ana ekrana görünür iptal açıklaması eklemek | Hangi kaydın iptal edilebildiğini ve iptalin sonucunu işlemden önce açıklamak. | Planlandı; kod uygulanmadı. |
| İptal onay penceresinin açıklama metnini netleştirmek | Tamam'ın iptali onayladığını, İptal'in işlemden vazgeçip randevuyu koruduğunu açıkça söylemek. | Planlandı; kod uygulanmadı. |

Tarayıcının yerel onay penceresindeki düğme adları bu çalışma kapsamında değiştirilmez. Açıklama metni iyileştirilir. Yeni bir özel onay penceresi geliştirilmiyor.

## Kapsam

- Mevcut çevrimdışı Klinik Randevu eğitim prototipi.
- Hasta rolünün kendi Bekliyor kaydını iptal etmesi ve vazgeçmesi; FR-03, AC-03, ALT-01 ve BR-01 ile tutarlılık.
- İş listesi, kabul koşulları, çalışma planı ve değişiklik kararının hazırlanması.
- Planlanan metin/HTML değişikliklerinin uygulanması; sonra gerçek sonuçların test kaydına yazılması.
- Gerçek katkı, GitHub değişiklik kaydı ve yazardan/ortak yazardan farklı kişinin incelemesinin takip edilmesi.

## Kapsam dışı

- Resepsiyona veya Doktora iptal yetkisi eklemek.
- Kimlik doğrulama, sunucu, SMS, ortak veritabanı veya çoklu cihaz eşzamanlaması geliştirmek.
- Önceki gözlemleri yeni test sonucu olarak sunmak.

Öğretmenin mevcut randevu verileri bu hazırlık için sıfırlanmaz. İleride yeni deneme gerekiyorsa uygun başlangıç durumu ayrıca planlanır; önceki kayıtların üstüne başarı sonucu yazılmaz.

## Sınıf düzeni — 19 öğrenci

| Grup | Öğrenci sayısı | Bu oturum için önerilen sorumluluk dağılımı |
|---|---:|---|
| Grup 1 | 5 | 1 Product Owner, 1 Scrum Master, 3 Developers |
| Grup 2 | 5 | 1 Product Owner, 1 Scrum Master, 3 Developers |
| Grup 3 | 5 | 1 Product Owner, 1 Scrum Master, 3 Developers |
| Grup 4 | 4 | 1 Product Owner, 1 Scrum Master, 2 Developers |
| Toplam | 19 | Her grup kendi proje kopyasında aynı etkinliği yapar. |

Bu dağılım ders için geçici bir sorumluluk planıdır; öğrencilerin gerçek adları henüz atanmadı. Uygulamadaki Hasta, Resepsiyon ve Doktor rolleriyle karıştırılmaz. Herkes üretim, kontrol ve açıklama çalışmalarına katılır; sorumluluklar sonraki etkinliklerde döndürülür. Ayrıntılı ilk grup planı önceki ../../docs/09-ekip-rolleri.md içinde korunur.

| Sorumluluk | Bu derste neyi takip eder? |
|---|---|
| Product Owner | Kullanıcıya faydayı, ürün hedefini ve işlerin sırasını. |
| Scrum Master | Scrum'ın anlaşılmasını, verimli çalışmayı ve engellerin giderilmesini desteklemeyi. |
| Developers | Seçilen işi nasıl yapacaklarının planını, uygulamayı ve kaliteyi. |

Geliştirici sorumluluğu yalnız kod yazmak değildir; belge, test ve doğrulama da ürün çalışmasına dahildir. Beş kişilik grupta üç geliştirici açıklama, onay metni ve test/kanıt takibini paylaşabilir; dört kişilik grupta iki geliştirici bu işleri birlikte planlar. Testi tek bir kişiye bırakmak veya aynı kişinin kendi katkısını bağımsız incelemiş saymak bu planın amacı değildir.

**Öğretmen denemesi:** Şu anda adımları öğretmen hazırlığı olarak birlikte çalışıyoruz. Tek kişinin farklı bakış açılarını canlandırması gerçek bir Scrum Takımı oluşturulduğu veya bağımsız inceleme yapıldığı anlamına gelmez. 135 dakikalık etkinlik sıkıştırılmış sınıf simülasyonudur.

## Önceki çalışmadan açık kalanlar

- PR #7'nin açıklaması son 10 dosyalık kapsamla eşleştirilecek. Son ekranda açıklama ve dört görev kutusu önceki durumda.
- PR #7 için gerçek, yazar/ortak yazar olmayan kişi incelemesi ve son teslim kontrolü bekliyor; PR açık kalıyor.
- İlk iki haftanın ders-testi.html içindeki altı soruluk testinin gerçek ilk deneme sonucu docs/07-toplanti-notu.md içine henüz eklenmedi.
- Kalite gereksinimlerinin ölçümleri hâlâ Ölçülmedi; önceki küçük işlev denemeleri ölçüm yerine sayılmıyor.

Bu açık işler izlenirken üçüncü haftanın hedef ve plan hazırlığına başlanır. Önceki işler tamamlandı veya birleştirildi olarak işaretlenmez.

## Şimdi kaydedeceğimiz çıktı

1. Randevu denemelerini yaptığınız index.html dosyasının bulunduğu mevcut proje klasöründe hafta-03 klasörü oluşturun.
2. Onun içinde docs klasörü oluşturun.
3. Bu dosyayı hafta-03/docs/01-ekip-hedef.md olarak kaydedin. Uzantısı .md olmalı; .md.txt olmamalı.
4. Dosyayı açıp Ürün hedefi, Bu haftanın odak noktası ve 19 öğrencilik grup tablosunu okuyun.

Beklenen sonuç: Üçüncü haftanın hedefi ve kapsamı kayıtlıdır. Bu adımda index.html üzerinde değişiklik yapılmaz; yeni test sonucu oluşmaz. Sonraki adım, başlangıç gözlemini ve geliştirme ihtiyacını ayrı kaydetmektir.

Kaynak: Ken Schwaber ve Jeff Sutherland, Scrum Guide (Kasım 2020), Scrum Team ve Product Goal bölümleri; https://scrumguides.org/scrum-guide.html — kontrol 28.10.2026. Grup büyüklükleri, iş paylaşımı ve kısa ders uygulaması bu sınıf için hazırlanmış öğretim planıdır.
