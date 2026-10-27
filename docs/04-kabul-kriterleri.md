# 04 — Kabul koşulları

Ekip: Öğretmen denemesi  
Tarih: 27.10.2026  
Sürüm: Belge 1.0 — kabul koşulları ve kalite kontrol planları çalışma metni  
İncelenen prototip: Klinik Randevu v0.1  
Durum: Belgenin çalışma metni tamamlandı: AC-01–AC-07, ALT-01 ve AC-NFR-01–AC-NFR-03 planları hazır. AC-01–AC-06 ile ALT-01 önceki gözlemlere, AC-07 G-07 kullanıcı bildirimine dayanır. Üç kalite kontrolü henüz uygulanmadı; durumları Ölçülmedi olarak korunur. Bağımsız ekip incelemesi yapılmadı. Bu belge bütün gereksinimlerin eksiksiz sınandığı veya kalite hedeflerinin sağlandığı anlamına gelmez.

**Verilen (Given):** Başlangıç durumu ve gerekli veri.  
**Ne zaman (When):** Kullanıcının tek belirgin eylemi.  
**O zaman (Then):** Dışarıdan gözlenebilir beklenen sonuç.

Yeni bir denemede beklenen sonuç, çalıştırmadan önce yazılır. Gerçek sonuç uygulama denenince kaydedilir. Hazırlanmış bir senaryo henüz denenmediyse “Çalıştırılmadı” yazılır. Bu öğretmen çalışmasında önceki denemeler de kabul koşulu biçimine dönüştürülmektedir; böyle bir sonuç kullanıldığında kaynak gözlem kimliği açıkça belirtilir. Önceki gözlemden aktarım, yeni çalıştırma olarak sunulmaz. Henüz yazılmamış satırlar “Hazırlanacak” durumundadır.

**AC**, kabul koşulu kimliğidir. Bir gereksinimin belirli bir durumda karşılandığını hangi gözlenebilir sonuçla anlayacağımızı belirtir. Bir gereksinimin farklı durumları için birden fazla kabul koşulu gerekebilir.

## İlk örnek — AC-01: hasta değişince saat doluluğunun korunması

Bu örnek, FR-01'in saat uygunluğunu doktor ve tarihe göre göstermesini ele alır. Hasta değişince doktorun mevcut randevusunun korunması, BR-01 ile de ilişkilidir.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Hasta rolü, Ece Yılmaz, Deniz Arı ve 12 Kasım 2030 seçilidir. Deniz Arı'nın 09:00 saatinde Ece'ye ait R011 kaydı Bekliyor durumundadır. |
| Ne zaman | Örnek hasta seçimi Kaan Demir olarak değiştirilir. |
| O zaman | Doktor Deniz Arı ve tarih 12 Kasım 2030 olarak kalırken B1 alanındaki 09:00 saati Dolu görünmeye devam etmelidir. Hasta değişimi bu saati Uygun yapmamalıdır. |
| Gerçek sonuç | G-04 denemesinde Kaan seçilince 09:00 Dolu kaldı. Gözlemde doktor Deniz Arı ve tarih 12 Kasım 2030 olarak korundu. |
| Durum | Geçti — önceki G-04 gözlemine göre. Bu adımda yeniden çalıştırılmadı. |

**Neden bu sonuç bekleniyor?** Saat uygunluğunun anahtarı doktor + tarih + saattir. Kaan kendi randevu listesini görürken doktorun Ece için ayrılmış 09:00 saati dolu kalır. Hastanın kendi listesinin değişmesi, doktorun saatinin boşaldığını göstermez.

**Örneğe özgü veri:** R011, Ece, Kaan ve 09:00 bu öğretmen denemesindeki verilerdir. Öğrenci kendi deneyinde kullandığı gerçek kayıt kimliğini ve seçimi yazmalıdır. Genel koşul, başka bir hastaya ait bekleyen randevunun saatinin hasta değişince dolu kalmasıdır.

## İkinci örnek — AC-02: uygun saate randevu oluşturma

Bu örnek, FR-02'nin Hasta rolündeki başarılı randevu oluşturma akışını ele alır. Saatin Uygun durumundan Dolu durumuna geçmesi FR-01 ile; aynı doktor, tarih ve saatte iptal edilmemiş başka kayıt bulunmaması BR-01 ile ilişkilidir.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Hasta rolü, Ece Yılmaz, Deniz Arı ve 12 Kasım 2030 seçilidir. Bu doktor ve tarihte 09:30 için iptal edilmemiş randevu yoktur. Kullanıcı, uygun olan 09:30 saatini seçmiştir. |
| Ne zaman | Kullanıcı Randevuyu onayla düğmesine basar. |
| O zaman | B2 Randevularım alanında Ece Yılmaz / Deniz Arı / 12.11.2030 / 09:30 bilgilerini taşıyan yeni kayıt Bekliyor durumunda görünmeli; B1 alanındaki 09:30 saati Dolu olmalıdır. |
| Gerçek sonuç | G-01'de R008 kaydı bu hasta, doktor, tarih ve saat bilgileriyle Bekliyor olarak göründü; 09:30 Dolu oldu. Üst bildirim alanında R008 oluşturuldu mesajı görüldü. |
| Durum | Geçti — önceki G-01 gözlemine göre. Bu adımda yeniden çalıştırılmadı. |

**Neden iki alanı kontrol ediyoruz?** B2'deki kayıt, randevunun hangi hasta, doktor, tarih ve saat için oluşturulduğunu ve durumunu gösterir. B1'deki Dolu bilgisi, doktorun o saatinin artık ayrıldığını gösterir. Yalnız oluşturuldu mesajını görmek, bu iki sonucun doğru olduğunu tek başına göstermez.

**Seçmek ile oluşturmak farklıdır:** Uygun saate tıklamak saati seçer; bu aşamada saat etiketi Seçili olabilir. Yeni randevu Randevuyu onayla işlemiyle oluşturulur. Bu nedenle saat seçimini Verilen bölümündeki hazırlığa, onay düğmesine basmayı Ne zaman bölümüne koyduk.

### Öğrenci uygulamasında izlenecek adımlar

1. Hasta rolünü, Ece Yılmaz'ı, Deniz Arı'yı ve 12 Kasım 2030 tarihini seçin.
2. B1'de 09:30'un Uygun olduğunu kontrol edin. Uygun değilse denemeyi aynı başlangıç koşulu varmış gibi sürdürmeyin; uygun başka bir saat kullanacaksanız senaryodaki saati de değiştirin.
3. Uygun saati seçin ve Seçiminiz alanındaki hasta, doktor, tarih ve saati kontrol edin. Bu, senaryonun hazırlığıdır.
4. Randevuyu onayla düğmesine bir kez basın.
5. B2'de yeni kaydın bilgilerini ve Bekliyor durumunu; B1'de aynı saatin Dolu olduğunu kontrol edin.
6. Gerçekte oluşan kayıt kimliğini ve sonucu kendi gözlem dosyanıza yazın. Görüntü alıyorsanız seçimler, B1'de ilgili saat ve B2'de yeni kayıt okunabilsin. Kabul koşulunun Gerçek sonuç alanına gözlem kimliğini ekleyin; yalnız beklenen sonucu kopyalamayın.

Bu adımlar öğrencinin kendi uygulaması içindir. Öğretmen denemesinin G-01 sonucu burada kaynağıyla yeniden kullanıldı; yeni kayıt oluşturulmadı.

**Kayıt kimliği ve zaman sırası:** R008 bizim önceki denememizde oluşan kimliktir; beklenen sonuç her öğrencide R008 çıkması değildir. Öğrenci kendi yeni kayıt kimliğini yazmalıdır. R008, G-01'de Bekliyor durumundaydı; daha sonraki G-02 denemesinde iptal edildi. Bugünkü listede İptal edildi görünmesi, G-01'deki başarılı oluşturma sonucunu değiştirmez. AC numaraları bu belgedeki koşulları tanımlar; gözlemlerin kronolojik sırası G kimlikleriyle izlenir. Her senaryo kendi Verilen koşullarıyla değerlendirilir.

**Kapsama notu:** Bu sonuç Hasta rolünün tanımlanan başarılı akışına aittir. Resepsiyon rolünde oluşturma henüz elle denenmedi. Dolu saate ikinci kayıt oluşturma girişimi de G-01'in kapsamı değildir; ilgili reddedilen işlem koşulu ayrıca ele alınacak. Bu gözlem, başka cihazda görünme veya yanıt süresi ölçümü sağlamaz.

## Üçüncü örnek — AC-03: kendi bekleyen randevusunu onaylayarak iptal etme

Bu örnek, FR-03'ün Hasta rolünde kendi Bekliyor kaydını onay vererek iptal etme akışını ele alır. Saatin yeniden Uygun olması FR-01 ve BR-01 ile ilişkilidir.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Hasta rolü, Ece Yılmaz, Deniz Arı ve 12 Kasım 2030 seçilidir. Ece'nin R008 / 09:30 kaydı Bekliyor, B1'de 09:30 Dolu durumundadır. Aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt yoktur. R008 kartındaki İptal et düğmesiyle açılan onay penceresi ekrandadır. |
| Ne zaman | Kullanıcı onay penceresindeki Tamam düğmesine basar. |
| O zaman | R008 kaydı B2'de İptal edildi durumuyla listede kalmalı; B1'de 09:30 yeniden Uygun görünmelidir. |
| Gerçek sonuç | G-02'de R008 için onay penceresi görüldü ve iptal işlemi onaylandı. İşlem sonrasında R008 İptal edildi durumuyla listede kaldı; 09:30 Uygun oldu. Üstte R008 iptal edildi bildirimi görüldü. |
| Durum | Geçti — önceki G-02 gözlemine göre. Bu adımda yeniden çalıştırılmadı. |

**Neden kayıt listede kalıyor?** Bu prototipte iptal işlemi kaydın durumunu değiştirir. Böylece önce oluşturulmuş ve sonra iptal edilmiş randevu görülebilir. Aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt bulunmadığı için saat yeniden Uygun olur. Buradaki listede kalma davranışı, gerçek bir kurumun veri saklama politikası olarak yorumlanmaz.

**Düğmelerin anlamı:** Aşağıdaki adlar öğretmen denemesinde gördüğümüz Türkçe arayüze aittir. Karttaki işlem ile onay penceresindeki seçenekleri ayrı okuyun.

| Nerede? | Düğme | Yaptığı işlem |
|---|---|---|
| Randevu kartı | İptal et | Bu randevu için iptal onayı penceresini açar. |
| Onay penceresi | Tamam | Randevunun iptalini onaylar. AC-03'te bu seçenek kullanılır. |
| Onay penceresi | İptal | İptal etme isteğinden vazgeçirir; randevuyu korur. Bu dal ALT-01 alternatif senaryosunda açıklanmıştır. |

### Öğrenci uygulamasında izlenecek adımlar

1. Hasta rolü, hasta, doktor ve tarihi seçin. Kendi seçili hastanıza ait bir Bekliyor kaydı ve buna karşılık gelen Dolu saati belirleyin. Öğretmen örneği Ece / Deniz Arı / 12.11.2030 / R008 / 09:30'dur; kendi kaydınızın bilgilerini yazın.
2. İlgili randevu kartındaki İptal et düğmesine basın. Açılan pencerede doğru kayıt kimliğinin, tarihin ve saatin yazdığını kontrol edin. Bu, kabul koşulundaki başlangıcı hazırlar.
3. Penceredeki Tamam düğmesine basarak iptali onaylayın.
4. B2'de aynı kaydın listede kaldığını ve durumunun İptal edildi olduğunu kontrol edin.
5. B1'de aynı saatin Uygun olduğunu kontrol edin. Bu senaryoda aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt bulunmamalıdır.
6. Gerçek işlemi, kayıt kimliğini ve iki alandaki sonucu 08-prototip-gozlemleri.md dosyasına yazın. 04 numaralı dosyanın Gerçek sonuç alanına bu gözlemin kimliğini ekleyin. Görüntü alıyorsanız onay penceresini ve işlem sonrasındaki B1/B2 alanlarını ayrı karelerle kaydedebilirsiniz.

Bu adımlar öğrencinin kendi uygulaması içindir. Burada G-02'nin geçmiş sonucu kullanıldı. Öğretmen çalışmasındaki R008 artık iptal edilmiş olduğundan aynı kayıt için yeniden iptal işlemi yapılmadı. Yeni bir öğrenci denemesinde başlangıç kaydı gerçekten Bekliyor olmalıdır; başka kayıt veya saat kullanılırsa senaryo buna göre güncellenir.

**Kapsama notu:** AC-03, iptalin onaylandığı bu örneği doğrular. Onay penceresinden vazgeçme dalı, hasta listesinin yalnız kendi kayıtlarını göstermesi ve diğer rollerin yetki sınırları bu satırın tek başına doğruladığı sonuçlar değildir. Vazgeçme için önceki G-03-T3 gözlemi ALT-01 alternatif senaryosuna bağlandı. NFR-01'deki yardımsız ve süreli kullanılabilirlik ölçümü henüz yapılmadı.

## Dördüncü örnek — AC-04: günlük randevu listesini görme

FR-04, Doktor ve Resepsiyon rollerinin seçili doktorun seçili tarihteki bütün örnek hasta kayıtlarını görmesini ister. Bekliyor, Tamamlandı ve İptal edildi durumları listede ayırt edilebilmelidir. Bu kapsam, bütün doktorların bütün tarihlerdeki kayıtları anlamına gelmez.

AC-04 altında iki senaryo kullanıyoruz. AC-04A doktor görünümünü, AC-04B resepsiyonda hasta seçiminin listeyi tek hastaya daraltmamasını ele alır. Her birinin başlangıcı ve gözlem kaynağı ayrıdır.

### AC-04A — Doktor görünümü

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Hasta rolü, Kaan Demir, Deniz Arı ve 12 Kasım 2030 seçilidir. Seçili doktor ve tarihte Ece ve Kaan'ın kayıtları vardır. R011 ve R002 Bekliyor, R003 Tamamlandı; R001, R009, R010, R008 ve R004 İptal edildi durumundadır. |
| Ne zaman | Simülasyon rolü Doktor yapılır. |
| O zaman | B2 Günlük randevu listesinde seçili doktor ve tarihin Ece ve Kaan kayıtları birlikte görünmeli; Bekliyor, Tamamlandı ve İptal edildi durumları okunabilmelidir. |
| Gerçek sonuç | G-05'te Ece ve Kaan birlikte listelendi. R011 ve R002 Bekliyor, R003 Tamamlandı; R001, R009, R010, R008 ve R004 İptal edildi olarak görüldü. |
| Durum | Geçti — önceki G-05 gözlemine göre. Bu adımda yeniden çalıştırılmadı. |

G-05'te Örnek hasta alanının pasif olduğu da görüldü. Bu görünümde listeyi daraltmak için hasta seçilmez; görevli doktor ve tarih seçimi liste kapsamını belirler.

### AC-04B — Resepsiyonda hasta seçimi günlük listeyi daraltmaz

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Doktor rolü, Deniz Arı ve 12 Kasım 2030 seçilidir. Örnek hasta seçimi Kaan Demir olarak korunmuştur. Aynı doktor ve tarihte Ece'nin R011 / 09:00 kaydı Bekliyor, Kaan'ın R002 / 10:00 kaydı Tamamlandı durumundadır. |
| Ne zaman | Simülasyon rolü Resepsiyon yapılır. |
| O zaman | Örnek hasta alanında Kaan seçiliyken B2 günlük listesinde Ece'nin R011 / 09:00 / Bekliyor kaydı da görünmelidir. Günlük liste Kaan'ın kayıtlarıyla sınırlandırılmamalıdır. |
| Gerçek sonuç | G-06'da Resepsiyon rolünde Örnek hasta Kaan seçiliyken günlük listede Ece'nin kayıtları ve R011 / 09:00 / Bekliyor görüldü. |
| Durum | Geçti — önceki G-06 gözlemine göre. Bu adımda yeniden çalıştırılmadı. |

Bu örnek, seçili hastadan başka bir hastanın kaydının da listelendiğini doğrular. Resepsiyondaki Örnek hasta alanı, yeni randevunun hangi hasta adına oluşturulacağını belirler. Günlük listenin kapsamı seçili doktor ve tarihtir. Resepsiyonda yeni kayıt oluşturma yeteneği pakette tanımlıdır; bu rolde oluşturma henüz elle denenmedi.

### Üç rolü karşılaştırma

| Rol | B2'deki listenin kapsamı | Bu çalışmadaki dayanak |
|---|---|---|
| Hasta | Seçili hastanın, seçili doktor ve tarihteki kendi kayıtları. | G-04: Kaan'ın kayıtları göründü; Ece'ninkiler bu listede görünmedi. FR-03 ile ilgilidir. |
| Doktor | Seçili doktor ve tarihin bütün örnek hasta kayıtları. | AC-04A / G-05: Ece ve Kaan birlikte; üç kayıt durumu da görüldü. |
| Resepsiyon | Seçili doktor ve tarihin bütün örnek hasta kayıtları; hasta seçimi listeyi daraltmaz. | AC-04B / G-06: Kaan seçiliyken Ece'nin R011 kaydı da görüldü. Bu gözlem bütün kayıtların tek tek denetlendiği iddiası değildir. |

**Gözlemlerin zaman sırası:** G-05'te R002 Bekliyor durumundaydı. Daha sonra G-05-B'de doktor R002'yi tamamladı. G-06, bu işlemden sonraki resepsiyon görünümüdür. R002'nin iki gözlem arasındaki durum farkını rol değiştirmeye bağlamayın. AC-04'ün iki alt senaryosu kendi başlangıç durumuyla değerlendirilir; kayıt sayıları ve kimlikleri öğretmen denemesine özgüdür.

### Öğrenci uygulamasında izlenecek adımlar

1. Deniz Arı ve 12 Kasım 2030 için en az iki farklı örnek hastaya ait kayıtlar bulunduğunu kontrol edin. Kendi kayıt kimliklerinizi ve başlangıç durumlarını not edin. Üç durumun da listelenmesini inceleyecekseniz Bekliyor, Tamamlandı ve İptal edildi örnekleri bulunmalıdır.
2. Hasta rolünde Kaan'ı seçip kendi kayıt listesini okuyun. Bu karşılaştırma, günlük listeye geçince kapsamın nasıl değiştiğini anlamaya yardımcı olur.
3. Doktor rolüne geçin. B2'de seçili doktor ve tarih başlığını, farklı hastaların kayıtlarını ve durum etiketlerini kontrol edin. Bu liste kontrolünde Tamamlandı düğmesine basmadan mevcut durumları kaydedin.
4. Kaan hasta seçimi korunarak Resepsiyon rolüne geçin. Örnek hasta alanında Kaan seçili olduğunu ve B2'de Ece'ye ait bir kaydın da göründüğünü kontrol edin.
5. İki rol için gerçek sonuçları ayrı gözlem satırlarına yazın. Hasta, doktor, tarih, kayıt kimliği ve durum bilgilerini kendi denemenizden alın. AC-04A ve AC-04B'nin Gerçek sonuç alanlarını ilgili gözlem kimlikleriyle eşleştirin.
6. Görüntü kaydedecekseniz rol seçimi, doktor/tarih başlığı ve B2'de farklı hastaların kayıtları okunabilsin. Resepsiyon görüntüsünde Kaan seçimiyle birlikte Ece'nin kaydı da görünmelidir.

Bu adımlar öğrencinin kendi uygulaması içindir. Öğretmen çalışmasında G-05 ve G-06 yeniden kullanılmaktadır; bu adımda rol değiştirme veya yeni görüntü alma işlemi yapılmadı. Öğrenci başlangıcında kayıt durumları öğretmen örneğinden farklıysa senaryoya kendi durumlarını yazar. Listeyi gözlemek için randevu durumlarını öğretmen örneğindeki eski değerlere geri çevirmesi gerekmez.

**Kapsama notu:** AC-04A tanımlanan doktor listesini, AC-04B ise resepsiyonda Kaan seçiminin Ece kaydını gizlememesini doğrular. Resepsiyon listesindeki bütün kayıtların tek tek karşılaştırılması, başka doktor/tarih seçimleri, boş liste ve farklı veri miktarları bu iki gözlemle bütünüyle doğrulanmış sayılmaz. Günlük sayıların doğruluğu AC-06'da, doktorun tamamlama işlemi AC-05'te ayrıca ele alınacak. Buradaki rol seçimi eğitim simülasyonudur; gerçek giriş ve erişim güvenliği testi değildir.

## Beşinci örnek — AC-05: doktorun bekleyen randevuyu tamamlaması

Bu örnek FR-05'i ele alır. Doktor, seçili doktor ve tarihin günlük listesindeki Bekliyor kaydını tamamlar. Kaydın durumu, ilgili saat ve günlük toplamlar birlikte kontrol edilir. Saatin Kapalı olması FR-01 ve BR-01; sayılardaki değişim FR-06 ile ilişkilidir.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Doktor rolü, görevli doktor Deniz Arı ve 12 Kasım 2030 seçilidir. Kaan Demir'in R002 / 10:00 kaydı Bekliyor, ilgili saat Dolu durumundadır. Kaydın Tamamlandı işlem düğmesi vardır. B3 günlük toplamları 2 bekleyen, 1 tamamlanan, 5 iptal edilen ve 8 toplam kayıttır. |
| Ne zaman | Doktor, R002 kartındaki Tamamlandı düğmesine basar. |
| O zaman | R002 listede Tamamlandı etiketiyle görünmeli; bu kayıtta tamamlama düğmesi artık bulunmamalıdır. B1'de 10:00 Kapalı olmalıdır. B3'te 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıt görünmelidir. |
| Gerçek sonuç | G-05-B'de R002 Tamamlandı etiketiyle görüldü ve tamamlama düğmesi kayboldu. 10:00 Kapalı oldu. Günlük toplamlar 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıt olarak görüldü. R011 / Ece / 09:00 Bekliyor olarak kaldı. |
| Durum | Geçti — önceki G-05-B gözlemine göre. Başlangıç kayıt ve toplamları G-05'te bulunur. Bu adımda yeniden çalıştırılmadı. |

### Önce ve sonra

| Kontrol edilen | İşlem öncesi | İşlem sonrası |
|---|---|---|
| B2 — R002'nin durum etiketi | Bekliyor | Tamamlandı |
| B2 — R002'nin tamamlama düğmesi | Var | Yok |
| B1 — 10:00 | Dolu | Kapalı |
| B3 — Bekleyen | 2 | 1 |
| B3 — Tamamlanan | 1 | 2 |
| B3 — İptal edilen | 5 | 5 |
| B3 — Toplam kayıt | 8 | 8 |

**Toplam neden değişmiyor?** Var olan bir kayıt Bekliyor durumundan Tamamlandı durumuna geçer. Yeni kayıt eklenmez ve kayıt silinmez. Bu nedenle bekleyen bir azalır, tamamlanan bir artar; iptal edilen ve toplam kayıt sayıları aynı kalır. Öğretmen örneğinde işlem öncesi 2 + 1 + 5 = 8, işlem sonrası 1 + 2 + 5 = 8'dir. Bu sayılar seçili doktor ve tarihin randevu kayıtlarıdır; hasta sayısı değildir.

**Saat neden Uygun olmuyor?** Bu prototipte Tamamlandı kaydı, BR-01 bakımından iptal edilmemiş bir kayıttır. O saat yeniden randevuya açılmaz ve Kapalı gösterilir. AC-03'teki iptal örneğinde ise ilgili saat yeniden Uygun olmuştu. İptal etme ile tamamlama farklı durum değişiklikleridir.

**Etiket ve düğme:** İşlem öncesindeki Bekliyor etiketi mevcut durumu, karttaki Tamamlandı düğmesi yapılabilecek işlemi gösterir. İşlem sonrasında Tamamlandı durum etiketi kalır; aynı kayda tamamlama düğmesi sunulmaz. Burada kullanılan düğme doktorun randevu kartındadır; iptal onayı penceresindeki Tamam düğmesiyle karıştırılmamalıdır.

### Öğrenci uygulamasında izlenecek adımlar

1. Doktor rolünü, Deniz Arı'yı ve 12 Kasım 2030 tarihini seçin. Günlük listede bu doktor ve tarihe ait bir Bekliyor kaydı bulun. Öğretmen örneği R002 / Kaan / 10:00'dır; kendi kaydınızın kimliğini, hastasını ve saatini yazın.
2. İşlem öncesinde kaydın Bekliyor etiketini, tamamlama düğmesini ve ilgili Dolu saati kontrol edin. B3'teki dört sayıyı not edin.
3. Seçtiğiniz kaydın Tamamlandı düğmesine bir kez basın.
4. B2'de aynı kaydın Tamamlandı etiketini ve tamamlama düğmesinin artık bulunmadığını kontrol edin.
5. B1'de aynı saatin Kapalı olduğunu kontrol edin.
6. B3'te bekleyenin bir azaldığını, tamamlananın bir arttığını, iptal edilen ve toplam kayıt sayılarının değişmediğini kontrol edin. Kendi başlangıç sayılarınıza göre karşılaştırın; öğretmen örneğindeki 8'i zorunlu sonuç saymayın.
7. Önceki ve sonraki değerleri 08-prototip-gozlemleri.md dosyasında kendi gözlem satırınıza yazın. AC-05'in Gerçek sonuç alanına bu gözlem kimliğini ekleyin. Görüntü kaydedecekseniz B1, B2 ve B3 bilgilerini okunabilir karelerde gösterin.

Bu adımlar öğrencinin kendi uygulaması içindir. Öğretmen çalışmasındaki R002 daha önce tamamlandı; bu adımda aynı işlem yeniden yapılmadı. Yeni bir öğrenci denemesi için başlangıç kaydı Bekliyor olmalıdır. Öğrenci farklı bir kayıt kullanırsa senaryodaki kimlik, hasta, saat ve başlangıç toplamlarını kendi denemesine uyarlar.

**Kapsama notu:** Bu gözlem, tanımlanan Doktor rolündeki başarılı tamamlama akışını ve bu işlemdeki toplam değişimini doğrular. Tamamlanmış kayda arayüzde yeniden düğme sunulmaması gözlendi; ayrıca ikinci bir tamamlama isteği gönderilmedi. Hasta veya resepsiyonla tamamlama girişimi, farklı doktor/tarih örnekleri ve bütün toplam güncelleme yolları bu satırla sınanmış sayılmaz. Genel günlük toplam kontrolü AC-06'da ele alınacak. Kalite hedefleri için yeni ölçüm yapılmadı.

## Altıncı örnek — AC-06: günlük toplamların kayıtlarla tutarlı olması

Bu örnek FR-06'yı ele alır. Sayılacak kayıtların kapsamı, B2 günlük listesinde olduğu gibi seçili doktor ve tarihtir. Bu senaryoda doktor görünümünden resepsiyona geçilir; arada randevu oluşturulmaz veya kayıt durumu değiştirilmez. Bu nedenle günlük sayılar aynı kalmalıdır. Örnek hasta alanındaki Kaan seçimi, resepsiyondaki sayıları yalnız Kaan'ın kayıtlarıyla sınırlandırmamalıdır.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Doktor rolü, Deniz Arı ve 12 Kasım 2030 seçilidir; Örnek hasta seçimi Kaan olarak korunmuştur. G-05-B sonrasındaki günlük kayıtlarda R011 Bekliyor, R002 ve R003 Tamamlandı; R001, R004, R008, R009 ve R010 İptal edildi durumundadır. Doktor görünümündeki B3 sayıları 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıttır. |
| Ne zaman | Kullanıcı, doktor ve tarihi değiştirmeden Resepsiyon rolüne geçer. |
| O zaman | B3'te 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıt görünmelidir. Sayılar seçili doktor ve tarihin kayıtlarıyla uyuşmalı; toplam 1 + 2 + 5 = 8 olmalıdır. Rol geçişi kayıtları değiştirmediğinden sayılar korunmalıdır. |
| Gerçek sonuç | G-06'da Resepsiyon rolünde ve Kaan seçiliyken B3'te 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıt görüldü. Bunlar G-05-B sonrasındaki doktor görünümüyle aynıydı. |
| Durum | Geçti — tanımlanan rol geçişi ve toplamlar için önceki G-06 gözlemine göre. Başlangıç toplamları G-05-B'dedir. Bu adımda yeniden çalıştırılmadı. |

### Kayıtlardan beklenen sayıyı çıkarma

Aşağıdaki döküm, G-05'te kaydedilen kayıt kimlikleri ve G-05-B'de R002'nin Tamamlandı durumuna geçmesi esas alınarak hazırlanmıştır. Bu tablo yeni bir uygulama denemesi veya G-06'da bütün liste satırlarının yeniden tek tek incelendiği iddiası değildir. G-06'nın doğrudan kanıtı, resepsiyon görünümündeki B3 değerleridir.

| Durum | Önceki gözlemlere göre kayıt kimlikleri | Beklenen sayı | G-06'da görülen B3 değeri |
|---|---|---:|---:|
| Bekliyor | R011 | 1 | 1 |
| Tamamlandı | R002, R003 | 2 | 2 |
| İptal edildi | R001, R004, R008, R009, R010 | 5 | 5 |
| Toplam kayıt | Yukarıdaki sekiz farklı kayıt kimliği | 8 | 8 |

**İki kontrol yapıyoruz:** Önce her durumdaki kayıt sayısını ilgili B3 değeriyle karşılaştırırız. Sonra üç durumun toplamının Toplam kayıt değerine eşit olduğunu kontrol ederiz. Yalnız 1 + 2 + 5 = 8 hesabını yapmak, kayıtların doğru doktor ve tarihten sayıldığını tek başına göstermez; liste kapsamı ve durumlar da kontrol edilmelidir.

**İptaller neden toplamda?** İptal edilen kayıtlar bu prototipte listede kalır. Toplam kayıt, Bekliyor + Tamamlandı + İptal edildi kayıtlarının toplamıdır. Dolayısıyla 8 kayıt, 8 farklı hasta veya 8 dolu saat demek değildir. Aynı hastanın birden fazla kaydı olabilir; iptal edilmiş bir kayıt da toplam kayıtta sayılır.

**AC-05 ile bağlantısı:** AC-05'te bir randevunun tamamlanması sayıları 2 / 1 / 5 / 8'den 1 / 2 / 5 / 8'e değiştirmişti. AC-06'da bu işlemden sonraki veri korunurken rol değiştiriyoruz; 1 / 2 / 5 / 8'in korunmasını kontrol ediyoruz. Bu iki senaryo farklı eylemlerin sonucunu değerlendirir.

### Öğrenci uygulamasında izlenecek adımlar

1. Doktor rolünde bir doktor ve tarih seçin. Karşılaştırma boyunca doktoru, tarihi ve kayıtları aynı tutun. Öğretmen örneğinde Deniz Arı / 12 Kasım 2030 kullanıldı.
2. B2 günlük listesindeki her kaydın kimliğini ve durumunu okuyun. Her kayıt kimliğini bir kez sayarak Bekliyor, Tamamlandı ve İptal edildi gruplarına ayırın.
3. Kendi sayımınızı B3'ün üç durum değeriyle karşılaştırın. Üç sayının toplamının hem saydığınız kayıt sayısına hem de B3 Toplam kayıt değerine eşit olduğunu kontrol edin.
4. Resepsiyon rolüne geçin. Aynı doktor ve tarihin seçili kaldığını kontrol edin; arada kayıt oluşturmayın, iptal etmeyin veya tamamlamayın.
5. Günlük toplamların önceki sayımla aynı olduğunu kontrol edin. Örnek hasta Kaan seçiliyse bu seçimin günlük toplamları yalnız Kaan'a daraltmadığını da inceleyin.
6. Doktor, tarih, kayıt kimlikleri, elle saydığınız değerler ve iki rolde gördüğünüz B3 değerlerini kendi 08-prototip-gozlemleri.md dosyanıza yazın. Fark varsa beklenen ve görülen değeri ayrı kaydedin.
7. AC-06'nın Gerçek sonuç alanına kendi gözlem kimliğinizi ekleyin. Görüntü alacaksanız rol/doktor/tarih ve B3 değerleri okunabilsin; sayımın dayanağı B2 kayıtları da kayıt altında olsun.

Bu adımlar öğrencinin kendi uygulaması içindir. Öğrencinin kayıt sayıları 1 / 2 / 5 / 8 olmak zorunda değildir; beklenen değer kendi başlangıç kayıtlarından hesaplanır. Öğretmen çalışmasında önceki G-05, G-05-B ve G-06 kayıtları kullanıldı; yeni sayfa denemesi veya yeni görüntü alınmadı.

**Kapsama notu:** Bu sonuç, tanımlanan veriyle doktor görünümünden resepsiyona geçişteki toplamları kapsar. Başka doktor/tarih seçimleri, boş liste, yeni randevu veya iptal sonrasındaki bütün güncelleme yolları bu tek koşulla doğrulanmış sayılmaz. Hasta rolünde sayıların gizlenmesi gereksinimde ve paket kodunda yer alır; bunun için ayrı elle yapılmış gözlem henüz kaydedilmedi. Kalite hedefleri için yeni ölçüm yapılmadı.

## Yedinci örnek — AC-07: dolu saatin yeni randevu için seçilememesi

**BR-01:** Aynı doktor, tarih ve saat için iptal edilmemiş ikinci randevu oluşturulamaz. Bu senaryo, kuralın normal arayüzde saat seçimi sırasında uygulanan engelini kontrol eder; FR-01 ve FR-02 ile ilişkilidir. Resepsiyon rolü seçilir, çünkü bu rol uygun saatlerde randevu oluşturabilir ve günlük listedeki bütün örnek hastaları görebilir.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Resepsiyon rolü, örnek hasta Kaan Demir, doktor Deniz Arı ve 12 Kasım 2030 seçilidir. Ece'nin R011 / 09:00 kaydı Bekliyor durumundadır; 09:00 Dolu görünür. Başka bir saat seçili değildir ve Randevuyu onayla düğmesi pasiftir. |
| Ne zaman | Kullanıcı, 09:00 Dolu saatine tıklayarak bu saati seçmeye çalışır. |
| O zaman | 09:00 Dolu olarak kalmalı ve Seçili olmamalıdır. Randevuyu onayla düğmesi pasif kalmalı; bu girişimle yeni randevu kaydı oluşmamalı ve mevcut R011 değişmemelidir. |
| Gerçek sonuç | Kullanıcı 27.10.2026'da beklenen sonuçların tamamını alıntılayarak “evet bu oldu” diye doğruladı: 09:00 seçilemedi ve Dolu kaldı; onay düğmesi pasif kaldı; yeni kayıt oluşmadı ve R011 değişmedi. Sonuç G-07'ye kaydedildi. |
| Durum | Geçti — G-07'deki kullanıcı bildirimine göre, tanımlanan arayüz kontrolü kapsamında. Bu deneme için ekran görüntüsü paylaşılmadı. |

**Neden hastayı Kaan seçiyoruz?** Dolu saatteki R011, Ece'ye aittir. Yeni randevu başka hasta için düşünülse de doktor + tarih + saat aynı kalır. Hasta değişikliği o saati boşaltmaz. Aynı 09:00 için eski İptal edildi kayıtlarının bulunması da R011'in Bekliyor olmasını geçersiz kılmaz. Kural, o saatteki iptal edilmemiş kayıtları esas alır.

**Bu denemede uyarı penceresi beklemiyoruz:** Mevcut kod, Dolu saat düğmesini pasif yapar. Böyle bir düğmeye tıklamak saati seçmemelidir. Saat seçilemediğinden Randevuyu onayla da pasif kalmalıdır. Uyarı penceresi açılmaması tek başına hata değildir. Kullanıcı, G-07'de saat seçiminin engellendiğini ve onay düğmesinin pasif kaldığını bildirdi; uyarı penceresi hakkında ayrıca sonuç vermedi.

### Öğrenci uygulamasında izlenecek kısa kontrol

1. Resepsiyon rolü düğmesine tıklayın. Kaan Demir, Deniz Arı ve 12 Kasım 2030 seçimlerini yapın. Bu hazırlıktan sonra başka bir uygun saate tıklamayın.
2. B2'de Ece'nin R011 / 09:00 kaydının Bekliyor olduğunu, B1'de 09:00'ın Dolu olduğunu kontrol edin. Başka saat seçili olmamalı ve Randevuyu onayla pasif olmalıdır. Başlangıç koşulları farklıysa bu senaryoyu yapılmış saymayın; mevcut durumu kaydedin.
3. B1'de 09:00 Dolu saatine bir kez tıklamayı deneyin.
4. 09:00'ın Dolu kalıp kalmadığını, Seçili olup olmadığını ve Randevuyu onayla düğmesinin hâlâ pasif olup olmadığını okuyun. Bu kontrol için onay düğmesine basmanız gerekmez.
5. B2'de R011'in değişmediğini ve yeni kayıt oluşmadığını kontrol edin. Öncesinde günlük toplam 8 ise, başka işlem yapılmadığında toplamın yine 8 olması beklenir. Öğrenci kendi başlangıç toplamını kullanır.
6. Gerçek sonucu kendi 08-prototip-gozlemleri.md dosyanıza yeni bir gözlem olarak yazın; AC-07'ye bu gözlem kimliğini bağlayın. Öğretmen çalışmasının sonucu G-07'de kullanıcı bildirimi olarak kayıtlıdır. Öğrenci kendi denemesinin sonucunu ve gözlem kimliğini kullanmalıdır.

Öğrenci farklı kayıt veya saat kullanıyorsa, aynı doktor/tarih/saatte başka bir hastaya ait Bekliyor kayıt bulunmalı; senaryodaki hasta, kayıt kimliği ve saat kendi verisine göre güncellenmelidir. Dolu saatin seçilememesi bu senaryonun beklenen engelidir; denemenin başarısız olduğu anlamına gelmez. Seçili olursa veya onay düğmesi etkinleşirse bu fark gerçek sonuca yazılmalıdır.

### Kanıtları birbirinden ayırma

| Dayanak | Ne biliyoruz? | Neyi doğrulamıyor? |
|---|---|---|
| G-04 ve G-06 | Ece'nin randevusu varken, Kaan seçili görünümde 09:00 Dolu kaldı. | Dolu saate tıklama girişiminin bütün sonucu bu gözlemlerde kayıtlı değil. |
| Mevcut index.html kodu | Dolu saatin pasif yapılması ve randevu oluşturma sırasında aynı doktor/tarih/saatte iptal edilmemiş kayıt aranması tanımlı. | Kodun okunması, çalıştırılmış bir çakışma testi değildir. |
| G-07 — kullanıcı bildirimi | Kullanıcı, saat seçiminin engellendiğini, onayın pasif kaldığını, yeni kayıt oluşmadığını ve R011'in değişmediğini doğruladı. | Bu deneme için ekran görüntüsü paylaşılmadı; doğrudan ikinci oluşturma isteğinin reddi veya eşzamanlı işlemler sınanmadı. |

**Kapsama notu:** Bu senaryo, normal arayüzde dolu saatin seçilmesini engelleyen davranışı sınar. Randevu oluşturma fonksiyonuna doğrudan ikinci kayıt isteği iletilerek ret kontrolü ayrıca çalıştırılmadı. Tamamlandı durumundaki Kapalı saat, eşzamanlı istekler, çoklu sekme ve çoklu cihaz davranışları bu senaryonun kapsamı dışındadır. Başlangıç prototipi sekmeler veya cihazlar arasında çakışmasız çalışma garantisi vermez.

## Kabul koşulları tablosu

AC-01–AC-07'nin kısa kayıtları aşağıdaki tabloda da yer alır. AC-04'ün ayrıntılı iki alt senaryosu yukarıdadır. ALT-01 alternatif senaryosu tablodan sonra yer alır. Her sonuç kendi gözlem kaynağı ve kapsamıyla değerlendirilmelidir; kalite kontrolleri ayrıca hazırlanacaktır.

| Kimlik | Gereksinim | Verilen | Ne zaman | O zaman | Gerçek sonuç | Durum |
|---|---|---|---|---|---|---|
| AC-01 | FR-01; BR-01 ile ilişkili | Hasta rolü, Ece, Deniz Arı, 12.11.2030. Ece'nin R011 / 09:00 kaydı Bekliyor. | Örnek hasta Kaan Demir yapılır. | Doktor ve tarih korunurken B1'de 09:00 Dolu kalır; hasta değişimi saati Uygun yapmaz. | G-04: Kaan seçildi; Deniz Arı / 12.11.2030 korundu; 09:00 Dolu kaldı. | Geçti — önceki gözlem; yeni çalıştırma yok. |
| AC-02 | FR-02; FR-01 ve BR-01 ile ilişkili | Hasta rolü, Ece, Deniz Arı, 12.11.2030. İptal edilmemiş kayıt bulunmayan uygun 09:30 saati seçilmiş. | Randevuyu onayla düğmesine basılır. | B2'de bu bilgilerle yeni kayıt Bekliyor görünür; B1'de 09:30 Dolu olur. | G-01: R008 / Ece / Deniz Arı / 12.11.2030 / 09:30 Bekliyor; saat Dolu; R008 oluşturuldu bildirimi görüldü. | Geçti — önceki gözlem; yeni çalıştırma yok. |
| AC-03 | FR-03; FR-01 ve BR-01 ile ilişkili | Hasta rolü, Ece, Deniz Arı, 12.11.2030. R008 / 09:30 Bekliyor, saat Dolu; aynı doktor/tarih/saatte başka iptal edilmemiş kayıt yok. R008 için iptal onayı penceresi açık. | Onay penceresindeki Tamam düğmesine basılır. | R008 listede İptal edildi durumuyla kalır; 09:30 Uygun olur. | G-02: R008 İptal edildi durumuyla listede kaldı; 09:30 Uygun oldu; R008 iptal edildi bildirimi görüldü. | Geçti — önceki gözlem; yeni çalıştırma yok. |
| AC-04 | FR-04 | AC-04A: Hasta/Kaan, Deniz Arı, 12.11.2030; G-05 öncesi kayıtlar. AC-04B: Doktor, aynı doktor/tarih ve Kaan seçimi; G-05-B sonrası kayıtlar. Ayrıntılı başlangıçlar yukarıdadır. | A: Doktor rolü seçilir. B: Resepsiyon rolü seçilir. Bunlar iki ayrı senaryodur. | A: Ece ve Kaan kayıtları üç durum etiketiyle günlük listede görünür. B: Kaan seçiliyken Ece'nin R011 / 09:00 / Bekliyor kaydı da görünür. | AC-04A / G-05: iki hasta ve üç durum görüldü. AC-04B / G-06: Kaan seçiliyken Ece'nin R011 kaydı görüldü. | İki alt senaryo da geçti — kendi önceki gözlemine göre; yeni çalıştırma yok. |
| AC-05 | FR-05; FR-01, FR-06 ve BR-01 ile ilişkili | Doktor / Deniz Arı / 12.11.2030. R002 / Kaan / 10:00 Bekliyor; saat Dolu. Günlük sayılar: 2 bekleyen, 1 tamamlanan, 5 iptal, 8 toplam. | R002 kartındaki Tamamlandı düğmesine basılır. | R002 Tamamlandı; tamamlama düğmesi yok; 10:00 Kapalı. Sayılar: 1 bekleyen, 2 tamamlanan, 5 iptal, 8 toplam. | G-05-B: durum etiketi, düğmenin kaybolması, Kapalı saat ve 1 / 2 / 5 / 8 toplamları görüldü. Başlangıç: G-05. | Geçti — önceki gözlem; yeni çalıştırma yok. |
| AC-06 | FR-06; liste kapsamı FR-04 ile ilişkili | Doktor / Deniz Arı / 12.11.2030, Kaan seçimi korunmuş. G-05-B sonrası kayıtlar: 1 bekleyen, 2 tamamlanan, 5 iptal edilen, 8 toplam. | Doktor ve tarih değiştirilmeden Resepsiyon rolüne geçilir. | B3 değerleri 1 / 2 / 5 / 8 olarak kalır; kayıtların durum sayımıyla ve 1 + 2 + 5 = 8 hesabıyla uyuşur. | G-06'da 1 / 2 / 5 / 8 görüldü; G-05-B sonrası doktor değerleri korundu. Kayıt dökümü önceki G-05 ve G-05-B'den çıkarıldı. | Geçti — önceki gözlemlere göre, tanımlanan kapsamda; yeni çalıştırma yok. |
| AC-07 | BR-01; FR-01 ve FR-02 ile ilişkili | Resepsiyon / Kaan / Deniz Arı / 12.11.2030. Ece'nin R011 / 09:00 kaydı Bekliyor; saat Dolu. Başka saat seçili değil, onay düğmesi pasif. | 09:00 Dolu saatine tıklanarak seçilmeye çalışılır. | Saat Dolu kalır, Seçili olmaz; onay düğmesi pasif kalır; yeni kayıt oluşmaz ve R011 değişmez. | G-07: Kullanıcı bütün beklenen sonuçların gerçekleştiğini yazılı doğruladı. Yeni ekran görüntüsü paylaşılmadı. | Geçti — kullanıcı bildirimine göre, tanımlanan kapsamda. |

**Saat durumlarının kapsamı:** AC-01 hasta değişince doluluğun korunmasını, AC-02 randevu oluşturulunca saatin Dolu olmasını, AC-03 iptal onaylanınca yeniden Uygun olmasını ve AC-05 tamamlama sonrasında Kapalı olmasını ele alır. Bu örnekler FR-01'in bütün doktor, tarih, rol ve saat durumlarının sınandığı anlamına gelmez; her koşulun sınırı kendi kapsama notunda belirtilmiştir.

## Alternatif senaryo — ALT-01: iptal işleminden vazgeçme

Bu, AC-03'teki iptal onayının alternatif akışıdır. Kullanıcı onay penceresinde kararını değiştirir ve randevusunu korur. İlgili gereksinim FR-03'tür; saatin dolu kalması FR-01 ve BR-01 ile ilişkilidir. Alternatif akış, uygulamada hata oluştuğu anlamına gelmez.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Hasta rolü, Ece Yılmaz, Deniz Arı ve 12 Kasım 2030 seçilidir. R011 / 09:00 kaydı Bekliyor, 09:00 Dolu durumundadır. R011 kartındaki İptal et düğmesiyle açılan iptal onayı penceresi ekrandadır. |
| Ne zaman | Kullanıcı onay penceresinde Tamam yerine İptal düğmesine basar. |
| O zaman | Onay penceresi kapanmalı; R011 Bekliyor durumunda ve 09:00 Dolu olarak kalmalıdır. Randevu iptal edilmemelidir. |
| Gerçek sonuç | G-03-T3'te kullanıcı, pencerede Tamam yerine İptal'e bastığını belirtti. Önceki görüntülerde açık onay penceresi ve pencere kapandıktan sonra R011'in Bekliyor, 09:00'ın Dolu kaldığı görüldü. |
| Durum | Geçti — önceki G-03-T3 gözlemine göre. Bu adımda yeniden çalıştırılmadı. |
| Bu sonuç oluşmasaydı kullanıcı ne yaşardı? | Kullanıcı iptal etmekten vazgeçtiği hâlde randevusu iptal olabilir ve saati yeniden uygun görünebilirdi. Bu, kullanıcının randevuyu koruma kararına aykırı olurdu. Bu cümle olası etkiyi açıklar; G-03-T3'te böyle bir hata gözlenmedi. |

### Aynı onay penceresindeki iki karar

| Seçenek | İlgili koşul | Kayıt sonucu | Saat sonucu |
|---|---|---|---|
| Tamam | AC-03 — iptali onaylama | İptal edildi; kayıt listede kalır. | Aynı doktor/tarih/saatte başka iptal edilmemiş kayıt yoksa Uygun. |
| İptal | ALT-01 — iptal isteğinden vazgeçme | Bekliyor olarak kalır. | Dolu olarak kalır. |

Karttaki İptal et düğmesi bu pencereyi açar. Pencerenin içindeki İptal düğmesi ise o isteği geri çeker. Bu ayrım, üçüncü haftadaki açıklama metni iyileştirmesine de dayanak olacaktır; mevcut prototipin düğme adları bu adımda değiştirilmedi.

### Öğrenci uygulamasında izlenecek adımlar

1. Hasta rolünde kendi seçili hastanıza ait bir Bekliyor kaydı bulun. Doktor, tarih, kayıt kimliği ve Dolu saati not edin.
2. Kaydın İptal et düğmesine basarak onay penceresini açın. Penceredeki kayıt kimliği, tarih ve saati kontrol edin.
3. Onay penceresindeki İptal düğmesine basın.
4. Pencerenin kapandığını, aynı kaydın Bekliyor kaldığını ve aynı saatin Dolu olduğunu kontrol edin.
5. Sonucu kendi gözlem dosyanıza yazın ve ALT-01'in Gerçek sonuç alanına gözlem kimliğini ekleyin. Gerçekte farklı bir düğmeye basıldıysa yapılan eylemi ve sonucu olduğu gibi kaydedin.

Öğretmen çalışmasında bu deneme G-03-T3'te zaten yapılmıştı; tekrar yapılması istenmedi. Önceki G-03, G-03-T1 ve G-03-T2 kayıtları değiştirilmedi. G-03'te seçilen düğme doğrulanamamıştı; T1 ve T2'de kullanıcı Tamam'a bastığını açıklamıştı. Bunlar başarılı vazgeçme denemeleri olarak yeniden sınıflandırılmaz.

**Kapsama notu:** Bu sonuç, belirtilen kayıtla iptal isteğinden vazgeçme davranışını doğrular. Düğme adlarının bütün kullanıcılarca kolay anlaşıldığı veya NFR-01'deki yardımsız ve süreli kullanılabilirlik hedefinin sağlandığı anlamına gelmez. Kalite ölçümü henüz yapılmadı.

## Kalite hedeflerinin kabul kontrolleri

Bu kontroller, `03-gereksinimler.md` dosyasındaki mevcut NFR hedeflerini değerlendirmek içindir. Hedefler sınıf çalışması için önerilmiştir; dış bir standardın zorunlu eşikleri olarak sunulmaz. AC-01–AC-07 ve ALT-01'in başarılı sonuçları, kalite hedeflerinin ölçüldüğü anlamına gelmez.

| Kabul kontrolü | Gereksinim | Hazırlık durumu | Ölçüm durumu |
|---|---|---|---|
| AC-NFR-01 | NFR-01 — kullanılabilirlik | Plan ve boş kayıt tabloları hazır. | Ölçülmedi. |
| AC-NFR-02 | NFR-02 — yanıt süresi | Plan ve on denemelik boş kayıt tablosu hazır. | Ölçülmedi. |
| AC-NFR-03 | NFR-03 — klavyeyle kullanım | Dört görev için kontrol adımları ve boş kayıt tablosu hazır. | Ölçülmedi. |

### AC-NFR-01 — İptal ve vazgeçme görevlerinin yardımsız tamamlanması

**Amaç:** Kullanıcıların randevuyu iptal etme ve iptal isteğinden vazgeçme görevlerini doğru, yardımsız ve belirlenen sürede tamamlayıp tamamlayamadığını değerlendirmek. Burada yalnız işlevin sonuç vermesi değil, katılımcının görevi nasıl tamamladığı da ölçülür.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Aynı prototip sürümü ve aynı görev metinleriyle çalışacak dört farklı katılımcı vardır. Önceki prototip deneyimleri kaydedilir. Her katılımcının her görevi için ayrı bir Bekliyor kaydı hazırlanır. Hasta rolü, Ece Yılmaz, Deniz Arı ve 12 Kasım 2030 seçilidir. Gözlemci düğme seçimi konusunda ipucu vermez. |
| Ne zaman | Her katılımcı sırayla G1 randevuyu iptal etme ve G2 iptal isteğinden vazgeçme görevlerini uygular; her görevin süresi, gerçek sonucu ve yardım bilgisi ayrı kaydedilir. |
| O zaman | Dört katılımcının en az üçü, iki görevin ikisini de doğru ve görev çözümüne yönelik yardım almadan tamamlamalıdır. Her görev ayrı ayrı en fazla 60 saniye sürmelidir. |
| Gerçek sonuç | Henüz dört katılımcıyla ölçüm yapılmadı; süre, yardım ve sonuç kayıtları yok. |
| Durum | Ölçülmedi — plan hazır. Önceki öğretmen denemeleri bu ölçümün yerine geçmez. |

### Katılımcıya okunacak görevler

Görev metnindeki kayıt kimliği ve saat, hazırlanan kayda göre doldurulur. Görevin amacı söylenir; hangi düğmeye basılacağı söylenmez. Aşağıdaki beklenen sonuç sütunu gözlemci içindir; ölçüm sırasında katılımcıya çözüm yönergesi olarak verilmez.

| Görev | Katılımcıya okunacak metin | Gözlemcinin kontrol edeceği sonuç |
|---|---|---|
| G1 — İptal | “[Kayıt kimliği] / [saat] için bekleyen randevunuzu iptal edin.” | Aynı kayıt İptal edildi durumuyla listede kalır; aynı doktor/tarih/saatte başka iptal edilmemiş kayıt yoksa saat Uygun olur. |
| G2 — Vazgeçme | “[Kayıt kimliği] / [saat] randevunuz için iptal sürecini başlatın, sonra randevunuzu koruyarak işlemden vazgeçin.” | Onay penceresi kapanır; aynı kayıt Bekliyor, saat Dolu kalır. |

**G1/G2 bu bölümdeki görev kodlarıdır.** `08-prototip-gozlemleri.md` içindeki G-01/G-02 gözlem kimlikleriyle karıştırılmamalıdır.

### Ölçümün hazırlanması ve uygulanması

1. **Dört farklı katılımcı belirleyin.** P1–P4 kodlarını kullanın; her kişinin uygulamayı veya bu akışı daha önce görüp görmediğini kaydedin. Bir kişinin dört tekrarını dört katılımcı saymayın. 5 + 5 + 5 + 4 kişilik sınıf düzeninde, katılımcılar gerektiğinde diğer gruplardan seçilebilir. Böylece dört kişilik grup da kendi gözlemci ve kayıt tutan öğrencilerini görevlendirip dört ayrı katılımcıyla çalışabilir.
2. **Ortamı kaydedin.** Ölçüm tarihi, prototip sürümü, kullanılan cihaz/tarayıcı ve süreyi ölçen araç yazılır. Aynı görev metinleri kullanılır; bu planın görev sırası G1, ardından G2'dir. Katılımcı bilgilerine bu sıra da kaydedilir.
3. **Başlangıçları hazırlayın.** Her katılımcı ve her görev için ayrı bir Bekliyor kayıt ve Dolu saat hazır olmalıdır. İptal görevinde aynı doktor/tarih/saatte başka iptal edilmemiş kayıt bulunmamalıdır. Görevler eşdeğer başlangıçlarla sunulur; farklı kayıt kimlikleri görev metninde belirtilir. Ölçüm için ayrılmış test ortamı kullanılır; önceki öğretmen gözlemleri ve çalışma verileri bu plan nedeniyle sıfırlanmaz. Bu adımda yeni test ortamı açılmadı veya kayıt hazırlanmadı.
4. **G1'i okuyup süreyi başlatın.** Metin okunduktan sonra başlangıç işaretiyle süre başlar. Rol ve örnek kayıt hazırlığı süreye dahil değildir. Katılımcı bitirdiğini söylediğinde süre durur; o andaki kayıt ve saat durumu kontrol edilir. Gözlemci hangi düğmeye basılacağını söylemez.
5. **Gerçek sonucu ve yardımı kaydedin.** Doğru/yanlış sonuç, süre, yardım isteği ve verilen yardım ayrı belirtilir. Düğme adı söylemek, adımı tarif etmek veya işlemi katılımcı yerine yapmak çözüm yardımıdır; böyle tamamlanan görev yardımsız sayılmaz. Yardım istenmiş ama verilmeden görev tamamlanmışsa bu iki bilgi ayrı yazılır. Sürenin 60 saniyeyi aşması, diğer sonuçlar doğru olsa da o görevin başarı koşulunu sağlamaz. Görev bitirilmediyse süre uydurulmaz; tamamlanmadığı kaydedilir.
6. **G2'yi ayrı kayıtla uygulayın.** Yeni görevin Bekliyor başlangıcını hazırlayın. G2 için aynı başlatma, durdurma ve sonuç kaydetme yöntemini kullanın. İki görevin süreleri birbirine eklenerek tek bir 60 saniyelik sınırla karşılaştırılmaz.
7. **Kişi bazında değerlendirin.** Bir katılımcı ancak iki görevin ikisinde de doğru sonuç, yardım verilmemesi ve ayrı ayrı en fazla 60 saniye koşullarını sağlarsa başarılıdır. Bir görevdeki başarı diğer görevdeki eksikliği karşılamaz. Aynı kişilerin her iki görevi de başarması gerekir.
8. **Dört kişinin sonucunu birleştirin.** En az üç başarılı katılımcı varsa hedef karşılanır. Eksik katılımcı veya eksik görev kaydı varsa dört kişilik ölçüm tamamlanmış sayılmaz. Gerçek tablolar 08 numaralı belgeye yeni kalite gözlemleri olarak eklenecek; eski G kayıtları korunacaktır.

### Doldurulacak ölçüm alanları

- Ölçüm tarihi: [ölçüm sırasında yazılacak]
- Prototip sürümü: [ölçüm sırasında yazılacak]
- Cihaz / tarayıcı: [ölçüm sırasında yazılacak]
- Süre ölçme aracı: [ölçüm sırasında yazılacak]
- Gözlemci / kayıt tutan: [ölçüm sırasında yazılacak]

| Katılımcı | Önceki prototip / görev deneyimi | Planlanan görev sırası |
|---|---|---|
| P1 | [yazılacak] | G1 → G2 |
| P2 | [yazılacak] | G1 → G2 |
| P3 | [yazılacak] | G1 → G2 |
| P4 | [yazılacak] | G1 → G2 |

| Katılımcı / görev | Kayıt kimliği ve saat | Süre (sn) | Gözlenen kayıt ve saat durumu | Yardım istendi mi? | Çözüm yardımı verildi mi? |
|---|---|---|---|---|---|
| P1 / G1 | — | — | — | — | — |
| P1 / G2 | — | — | — | — | — |
| P2 / G1 | — | — | — | — | — |
| P2 / G2 | — | — | — | — | — |
| P3 / G1 | — | — | — | — | — |
| P3 / G2 | — | — | — | — | — |
| P4 / G1 | — | — | — | — | — |
| P4 / G2 | — | — | — | — | — |

Boş alanlar ölçüm yapılmadığını gösterir; sıfır saniye, yardım yok veya başarılı sonucu anlamına gelmez. Her görev için doğru sonuç / yardım verilmedi / süre ≤ 60 saniye koşulları bu gerçek kayıtlardan değerlendirilir.

| Katılımcı | G1 bütün koşulları sağladı mı? | G2 bütün koşulları sağladı mı? | Kişi başarılı mı? |
|---|---|---|---|
| P1 | Ölçülmedi | Ölçülmedi | Belirlenmedi |
| P2 | Ölçülmedi | Ölçülmedi | Belirlenmedi |
| P3 | Ölçülmedi | Ölçülmedi | Belirlenmedi |
| P4 | Ölçülmedi | Ölçülmedi | Belirlenmedi |

**Başarılı katılımcı sayısı:** Henüz hesaplanmadı. **Hedef:** En az 3/4. **Genel sonuç:** Ölçülmedi.

**Kapsama notu:** Bu küçük sınıf ölçümü, belirtilen iki görevi bu sürüm ve dört katılımcıyla değerlendirir. Bütün kullanıcılar için genellenmiş kullanılabilirlik sonucu değildir. Önceki öğretmen denemelerinde adımlar birlikte açıklanmıştı ve dört ayrı kişinin süre/yardım kayıtları tutulmamıştı; bu nedenle o gözlemler NFR-01 ölçümü olarak kullanılamaz. Bu bölümde yalnız plan ve boş formlar hazırlandı; katılımcı testi yapılmadı.

### AC-NFR-02 — Doktor seçimi sonrası doğru içeriğin yanıt süresi

**Amaç:** Yeni doktor seçimi onaylandıktan sonra B1 saatlerin, B2 günlük listenin ve B3 günlük toplamların doğru içerikle ne kadar sürede güncellendiğini ölçmek. Hedef, `03-gereksinimler.md` içindeki NFR-02 ile aynıdır: belirtilen koşullardaki on seçimin tamamında doğru sonuç en fazla 1 saniyede görünmelidir.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Aynı bilgisayar ve tarayıcı sürümü, aynı prototip sürümü, tek uygulama sekmesi ve en fazla 20 örnek randevu kaydı kullanılır. Rol Resepsiyon, tarih 12 Kasım 2030'dur. Açık onay penceresi veya geliştirici araçlarında yapay yavaşlatma yoktur. Deniz Arı ve Selin Kaya için beklenen saat, kayıt ve toplamlar ölçümden önce belirlenmiştir. Ekran kaydı başlangıç eylemini ve üç alanı birlikte değerlendirmeye elverişlidir. |
| Ne zaman | Başlangıçta Deniz Arı seçiliyken Deniz Arı ile Selin Kaya arasında sırayla toplam on doktor seçimi değişikliği yapılır. Her seçimin onaylanma anından üç alanın da doğru güncellendiği ana kadar geçen süre ölçülür. |
| O zaman | On değişikliğin her birinde B1, B2 ve B3 doğru içerikle en fazla 1 saniyede güncellenmelidir. On denemenin tamamı koşulu sağlamalıdır. |
| Gerçek sonuç | Henüz zaman bilgisi içeren ekran kaydı alınmadı veya on denemenin süresi ölçülmedi. |
| Durum | Ölçülmedi — plan ve boş tablo hazır. Önceki statik ekran görüntülerinden süre hesaplanmadı. |

### Ölçümün başlangıcı ve bitişi

| Nokta | Tanım |
|---|---|
| Başlangıç | Kullanıcının yeni doktor seçimini tıklama veya Enter ile onayladığı an. Doktor seçeneklerini düşünme ve listeyi açma süresi dahil değildir. |
| Bitiş | Yeni doktor ve seçili tarih için B1 saatler, B2 günlük liste ve B3 günlük toplamların tamamının doğru göründüğü ilk an. Yalnız doktor adının değişmesi yeterli değildir. |
| Süre | Bitiş zamanı − başlangıç zamanı. Kayıttaki zaman damgaları kullanılır. |
| Karar | İçerik doğru, ölçüm yeterince açık ve süre en fazla 1 saniyeyse o deneme koşulu sağlar. Yanlış içerik veya 1 saniyeyi aşan süre hedefi sağlamaz. Sınırın ayırt edilemediği ölçüm Belirsiz olarak kaydedilir. |

### Önceden hazırlanacak doğruluk referansı

Beklenen değerler, kullanılan örnek veri ve kayıt dökümünden çıkarılır. Ölçüm sırasında hızlı görünen herhangi bir ekran doğru sayılmaz. İki doktorun kayıtları ve saat durumları ayrı kontrol edilir; B3 sayıları da kayıtların durumlarına göre hesaplanır.

| Doktor / tarih | B1 — beklenen saat durumları | B2 — beklenen kayıt kimlikleri ve durumlar | B3 — bekleyen / tamamlanan / iptal / toplam |
|---|---|---|---|
| Deniz Arı / 12.11.2030 | [ölçüm öncesi hazırlanacak] | [ölçüm öncesi hazırlanacak] | [ölçüm öncesi hesaplanacak] |
| Selin Kaya / 12.11.2030 | [ölçüm öncesi hazırlanacak] | [ölçüm öncesi hazırlanacak] | [ölçüm öncesi hesaplanacak] |

Bu tablo henüz doldurulmadı. Önceki öğretmen gözlemlerindeki Deniz Arı sayıları, yeni ölçümdeki verinin kontrol edilmesi yerine otomatik olarak kullanılmaz.

### Öğrenci uygulamasında izlenecek adımlar

1. **Ortamı kaydedin.** Bilgisayar, işletim sistemi, tarayıcı ve prototip sürümü; pencere boyutu/yakınlaştırma; ekran kayıt aracı ve kayıt zaman bilgileri yazılır. Aynı ortam bütün on denemede korunur. Başlangıçtaki örnek kayıt sayısı en fazla 20 olmalıdır; bu sınır yalnız bir günlük görünümü değil, kullanılan test verisini kapsar. İptal kayıtları da kayıt sayısına dahildir.
2. **Beklenen içeriği hazırlayın.** Deniz Arı ve Selin Kaya'nın 12 Kasım 2030 kayıt dökümlerini, saat durumlarını ve günlük toplamlarını yukarıdaki referans tablosuna yazın. Ölçüm serisi sırasında yeni randevu oluşturmayın, iptal veya tamamlama yapmayın.
3. **Görünürlüğü hazırlayın.** Rol ve doktor seçimi ile B1, B2 ve B3'ün güncellenmesini aynı kayıtta değerlendirebileceğiniz sabit pencere düzenini kurun. Alanlar okunabilir olmalıdır. Bir alanı sonradan sayfayı kaydırarak görmek, o alanın güncellenme anını göstermez; eksik görünürlükle kesin süre sonucu vermeyin.
4. **Başlangıcı kurun.** Resepsiyon rolünü, 12 Kasım 2030'u ve Deniz Arı'yı seçin; ilk ekranın tamamlanmasını bekleyin. Bu başlangıç seçimi on denemeden biri değildir. Açık onay penceresini kapatın; yapay yavaşlatma kullanmayın.
5. **On değişikliği kaydedin.** İlk değişiklik Deniz Arı → Selin Kaya, ikinci Selin Kaya → Deniz Arı olur. Aynı sıra beş gidiş-dönüşte toplam on değişiklik verir. Her seçimin sonucu görünür hâle geldikten sonra sonraki seçime geçin. Seçimi onaylayan eylemin kayıtta belirlenebilir olmasına dikkat edin.
6. **Kaydı inceleyin.** Her deneme için başlangıç ve bitiş zamanını belirleyin; B1/B2/B3'ü doğru doktorun referansıyla karşılaştırın. Bitiş için üç alanın en son doğru hâle geldiği an kullanılır. Bir alandaki yanlışlık o denemenin doğru sonuç koşulunu bozar.
7. **Süreyi ve belirsizliği yazın.** Zaman farkını saniye olarak kaydedin. Sabit kare hızı doğrulanmışsa kare farkı / kare hızı hesabı kullanılabilir; değişken kare hızında gerçek zaman damgaları gerekir. Başlangıç ve bitiş aynı kare aralığında ayırt edilebiliyorsa 0 saniye yerine bir kare aralığından kısa yazın. Başlangıç belirlenemiyorsa veya 1 saniye sınırı kayıt çözünürlüğü nedeniyle ayırt edilemiyorsa Belirsiz yazın; Geçti vermeyin. Sorunlu kaydı ve nedenini koruyarak uygun kayıtla tekrar edin.
8. **Seriyi değerlendirin.** On denemenin her birinde doğru içerik ve süre ≤ 1 saniye aranır. Ortalama süre kabul ölçütü değildir. Her süreyi ve en büyük süreyi raporlayın; üst sınırla ifade edilen ölçümler varsa bunları olduğu gibi belirtin. Geçerli ölçümde sınırı aşan veya yanlış sonuç veren deneme varsa hedef sağlanmaz. Eksik/belirsiz ölçüm varsa 10/10 başarı doğrulanmış sayılmaz.
9. **Kanıtı bağlayın.** Ekran kaydının dosya adını, zaman/kare referanslarını, doğruluk tablosunu ve gerçek ölçümleri 08 numaralı belgeye yeni kalite kaydı olarak ekleyin. AC-NFR-02'nin Gerçek sonuç alanına bu gözlem kimliğini yazın. Önceki G kayıtları korunur.

### Doldurulacak ortam ve ölçüm tablosu

- Ölçüm tarihi: [yazılacak]
- Bilgisayar / işletim sistemi / tarayıcı sürümü: [yazılacak]
- Prototip sürümü / örnek kayıt sayısı: [yazılacak]
- Pencere boyutu / yakınlaştırma: [yazılacak]
- Kayıt aracı / video dosyası: [yazılacak]
- Kare hızı / sabit veya değişken oluşu / zaman damgası bilgisi: [yazılacak]
- Üç alanın görünürlüğü ve ölçüm belirsizliği: [yazılacak]

| Deneme | Planlanan geçiş | Başlangıç → bitiş zaman/kare referansı | Süre (sn) veya süre üst sınırı | B1/B2/B3 doğru mu? | Karar / açıklama |
|---|---|---|---|---|---|
| 1 | Deniz Arı → Selin Kaya | — | — | — | Ölçülmedi |
| 2 | Selin Kaya → Deniz Arı | — | — | — | Ölçülmedi |
| 3 | Deniz Arı → Selin Kaya | — | — | — | Ölçülmedi |
| 4 | Selin Kaya → Deniz Arı | — | — | — | Ölçülmedi |
| 5 | Deniz Arı → Selin Kaya | — | — | — | Ölçülmedi |
| 6 | Selin Kaya → Deniz Arı | — | — | — | Ölçülmedi |
| 7 | Deniz Arı → Selin Kaya | — | — | — | Ölçülmedi |
| 8 | Selin Kaya → Deniz Arı | — | — | — | Ölçülmedi |
| 9 | Deniz Arı → Selin Kaya | — | — | — | Ölçülmedi |
| 10 | Selin Kaya → Deniz Arı | — | — | — | Ölçülmedi |

İçerik kontrolünde üç alanın tamamı doğrulanır; yanlış veya belirsiz alan varsa açıklamada B1/B2/B3 belirtilir. Çizgiler henüz ölçüm olmadığını gösterir; 0 saniye veya doğru sonuç anlamına gelmez. Süre yalnız üst sınırla ifade edilebiliyorsa, bu sınırın 1 saniyeyi aşmaması ve içerik kontrolünün doğru olması gerekir; daha geniş bir üst sınır hedefin sağlandığını kanıtlamaz.

**Hedef:** Doğru içerikle 10/10 değişiklik, her biri en fazla 1 saniye. **En büyük süre veya bunun üst sınırı:** Henüz belirlenmedi. **Başarılı deneme sayısı:** Henüz hesaplanmadı. **Genel sonuç:** Ölçülmedi.

**Kapsama notu:** Bu kontrol, belirtilen ortam ve en fazla 20 örnek kayıtla yerel arayüz yanıtını değerlendirir. Ağ/sunucu performansı, çok sayıda eşzamanlı kullanıcı, başka cihazlar veya genel ölçeklenebilirlik sonucu değildir. Ekran kaydı gözlenebilir güncellemeyi ölçmek için kullanılır; ölçüm çözünürlüğünün desteklemediği kesinlikte süre verilmez. Bu adımda yalnız plan ve boş tablolar hazırlandı; kayıt alınmadı, süre ölçülmedi.

### AC-NFR-03 — Dört temel görevin klavyeyle tamamlanması

**Amaç:** Randevu oluşturma, iptal isteğinden vazgeçme, iptal etme ve doktorun randevuyu tamamlaması görevlerinin fare kullanmadan yapılabilmesini kontrol etmek. İşlemin doğru sonucu, kullanılan öğelerde görünür klavye odağı ve klavyeyle ilerleyebilme birlikte değerlendirilir. Hedef, NFR-03'teki dört görevin tamamıdır.

| Alan | Yazılacak bilgi |
|---|---|
| Verilen | Aynı prototip ve tarayıcı sürümü kullanılır. Her göreve uygun örnek kayıt ve saat durumu hazırlanır. Uygulama sayfası açıktır; görevlerde gerekli rol ve seçim alanlarına klavyeyle ulaşılır. Fare ve dokunmatik yüzey kullanılmaz. |
| Ne zaman | K1 randevu oluşturma, K2 iptalden vazgeçme, K3 iptal etme ve K4 doktorun tamamlama görevleri klavyeyle uygulanır; kullanılan kontroller ve onay penceresi incelenir. |
| O zaman | Dört görevin dördü de doğru sonuçla, fare kullanılmadan tamamlanmalıdır. Kullanılan etkin öğelerde odak görünür olmalı ve klavyeyle ilerlemeyi engelleyen bir takılma bulunmamalıdır. |
| Gerçek sonuç | Henüz bu dört görevlik klavye kontrolü yapılmadı. Önceki fareli denemeler ve kodda odak biçiminin bulunması, bu çalıştırmanın sonucu değildir. |
| Durum | Ölçülmedi — plan ve boş kayıt tablosu hazır. |

### Kullanılacak tuşlar ve odak

| Tuş / kavram | Bu kontrolde kullanımı |
|---|---|
| Tab | Klavyeyle ulaşılabilen sonraki öğeye ilerlemek. |
| Shift + Tab | Önceki öğeye dönmek. |
| Ok tuşları | Hasta, doktor ve tarih gibi seçim alanlarında seçenekler arasında ilerlemek. Alanın davranışına göre Enter ile seçim onaylanır. |
| Enter / Boşluk | Odaktaki düğmeyi etkinleştirmek; kontrolün desteklediği tuş kullanılır. |
| Odak | Klavyenin o anda hangi öğede olduğunu gösteren görünür işaret; örneğin düğme çevresindeki çerçeve. Fare imlecinin konumu değildir. |

Sabit bir Tab sayısı ezberlenmez; kayıtlar ve kullanılabilir düğmeler değiştikçe sıra değişebilir. Her adımda öğenin etiketi ve odak işareti okunur. Pasif bir düğmenin Tab sırasında atlanması tek başına hata değildir. Etkin bir öğeye ulaşamamak, odağı görememek veya klavyeyle bir alandan çıkamamak sorun olarak kaydedilir.

### Dört görevin başlangıcı ve beklenen sonucu

| Görev | Gerekli başlangıç | Klavyeyle yapılacak işlem | Doğrulanacak sonuç |
|---|---|---|---|
| K1 — Randevu oluşturma | Hasta rolü için seçilecek örnek hasta/doktor/tarihte uygun bir saat bulunur. | Rol ve seçim alanlarına ulaşılır, uygun saat seçilir, Randevuyu onayla etkinleştirilir. | Yeni kayıt doğru bilgilerle Bekliyor; seçilen saat Dolu olur. |
| K2 — İptalden vazgeçme | Seçili hastaya ait Bekliyor kayıt ve Dolu saat vardır. | Kaydın İptal et düğmesiyle pencere açılır; penceredeki İptal seçeneğine ulaşılıp etkinleştirilir. | Pencere kapanır; aynı kayıt Bekliyor, saat Dolu kalır. |
| K3 — Randevuyu iptal etme | Seçili hastaya ait Bekliyor kayıt vardır; aynı doktor/tarih/saatte başka iptal edilmemiş kayıt yoktur. | Kaydın İptal et düğmesiyle pencere açılır; Tamam seçeneğine ulaşılıp etkinleştirilir. | Kayıt İptal edildi durumuyla listede kalır; saat Uygun olur. |
| K4 — Doktorun tamamlaması | Görevli seçilecek doktor ve tarihte bir Bekliyor kayıt vardır. | Doktor rolüne ve ilgili seçimlere klavyeyle ulaşılır; kaydın Tamamlandı düğmesi etkinleştirilir. | Kayıt Tamamlandı, saat Kapalı olur; aynı kayıtta tamamlama düğmesi artık görünmez. |

Bu görevlerde kayıt kimlikleri ve saatler ölçüm sırasında kullanılan gerçek örneklere göre yazılır. K3'te iptal edilen bir kayıt, K4'te Bekliyor başlangıcı yerine kullanılamaz. Her görevin koşulu ayrı kontrol edilir; gerekirse önceden hazırlanmış başka bir Bekliyor kayıt kullanılır. Öğretmen gözlemlerini yeniden üretmek için eski veriler sıfırlanmaz. Bu adımda yeni kayıt veya ölçüm ortamı hazırlanmadı.

### Öğrenci uygulamasında izlenecek adımlar

1. **Ortamı ve başlangıç verisini yazın.** İşletim sistemi, tarayıcı ve prototip sürümü ile her görevdeki kayıt/saat bilgileri not edilir. Hazırlık tamamlandıktan sonra görev akışında fare kullanılmaz. Rol, hasta, doktor ve tarih seçimi de klavye kontrolüne dahildir.
2. **K1'i uygulayın.** Tab ve Shift + Tab ile Hasta rolüne ulaşın; Enter veya Boşluk ile etkinleştirin. Hasta, doktor ve tarih alanlarına klavyeyle ulaşıp seçimleri yapın. Uygun saati ve Randevuyu onayla düğmesini klavyeyle etkinleştirin. Yeni kayıt ve saat sonucunu kontrol edin.
3. **K2'yi uygulayın.** Hazırlanmış kendi Bekliyor kaydınızın İptal et düğmesine Tab ile ulaşın ve etkinleştirin. Onay penceresinde görünür odağı izleyerek İptal seçeneğine ulaşın; etiketini okuyup etkinleştirin. Pencere kapandıktan sonra kaydın ve saatin korunmasını, sayfada klavyeyle devam edebilmeyi kontrol edin. Varsayılan odaktaki seçeneğin hangisi olduğunu tahmin etmeyin.
4. **K3'ü uygulayın.** Geçerli Bekliyor kaydı için iptal penceresini klavyeyle açın. Bu kez Tamam seçeneğine ulaşıp etkinleştirin. Kayıt İptal edildi, saat Uygun olmalıdır. İşlemden sonra klavyeyle ilerlemeye devam edilebilmelidir.
5. **K4'ü uygulayın.** Doktor rolüne, görevli doktor ve tarih seçimlerine klavyeyle ulaşın. O günlük listedeki Bekliyor kaydın Tamamlandı düğmesini etkinleştirin. Kayıt Tamamlandı, saat Kapalı olmalı; aynı kayıtta işlem düğmesi kalmamalıdır.
6. **Her görevde odağı ve ilerlemeyi kaydedin.** Kullanılan etkin düğme veya seçim alanına odak geldiğinde işaretin görüldüğünü kontrol edin. İşlemden ve onay penceresinden sonra hangi öğeye ulaşılabildiğini not edin. Sorun varsa öğe adı, kullanılan tuş ve gerçekleşen davranış yazılır; yalnız çalışmadı denmez.
7. **Gerçek sonucu değerlendirin.** Her görev için doğru işlev sonucu, fare kullanılmaması, görünür odak ve takılma olmaması birlikte aranır. Fareyle müdahale edilerek bitirilen görev klavyeyle tamamlandı sayılmaz. Sorun yaşanırsa ilk sonuç korunur; düzeltilmiş veya tekrar edilmiş deneme ayrı kaydedilir.
8. **Kanıtı bağlayın.** Dört görevin gerçek sonuçları 08 numaralı dosyaya yeni kalite gözlemleri olarak eklenir. AC-NFR-03'e bu gözlem kimlikleri yazılır. Bir ekran görüntüsü tek başına bütün akışın fare kullanılmadan tamamlandığını göstermez; kullanılan tuşlar ve eylemler de gözlem metninde bulunmalıdır.

### Doldurulacak kontrol tablosu

- Ölçüm tarihi / uygulayan kişi: [yazılacak]
- İşletim sistemi / tarayıcı sürümü / prototip sürümü: [yazılacak]
- Başlangıç verisi ve ilgili doktor/tarih: [yazılacak]
- Kullanılan tuşlar / varsa görüntü veya video dosyası: [yazılacak]

| Görev | Kayıt kimliği / saat | Doğru sonuç oluştu mu? | Akışta fare kullanıldı mı? | Kullanılan öğelerde odak görünür mü? | Klavyeyle takılma var mı? | Karar / sorun / gözlem kimliği |
|---|---|---|---|---|---|---|
| K1 — Oluşturma | — | — | — | — | — | Ölçülmedi |
| K2 — Vazgeçme | — | — | — | — | — | Ölçülmedi |
| K3 — İptal | — | — | — | — | — | Ölçülmedi |
| K4 — Tamamlama | — | — | — | — | — | Ölçülmedi |

**Hedef:** Dört görevin tamamı, bütün klavye koşullarıyla başarılı. **Başarılı görev sayısı:** Henüz hesaplanmadı. **Genel sonuç:** Ölçülmedi.

Bu hedefe NFR-01'in dört katılımcı/60 saniye veya NFR-02'nin 1 saniye sınırı eklenmez. Burada dört farklı görev, görünür odak ve klavyeyle ilerleyebilme değerlendirilir. Süre ölçümü bu kabul koşulunun parçası değildir.

**Kapsama notu:** Bu çalışma erişilebilirliğin belirtilen dört görevdeki klavye boyutunu kapsar. Ekran okuyucu, renk/kontrast, büyütme ve bütün tarayıcı/cihaz koşulları değerlendirilmiş sayılmaz. Kodda klavye odağı için görsel biçim bulunması, gerçek tarayıcıda dört görevin geçtiğini kanıtlamaz. Bu adımda yalnız plan ve boş tablo hazırlandı; klavye denemesi yapılmadı.

## Belgenin durumu ve kaydetme

Bu dosyanın çalışma metni hazırdır. Yedi ana kabul koşulu, iptalden vazgeçme alternatifi ve üç kalite kontrol planı birlikte yer alır. İşlevsel örneklerin dayanakları ilgili G gözlemlerinde, kalite kontrollerinin henüz yapılmadığı ise ölçüm tablolarında açıkça belirtilmiştir. Bağımsız ekip incelemesi yapılmadı; kapsam sınırları her bölümde korunur.

1. Güncel dosyayı `04-kabul-kriterleri.md` adıyla indirin.
2. `index.html` dosyasının bulunduğu proje klasörünün `docs` klasörüne kaydedin. Eski boş veya eksik kopya yerine bu çalışma metni kullanılmalı; varsa kendi ek notlarınız korunmalıdır.
3. Dosyayı yeniden açın. AC-07'nin G-07 kullanıcı bildirimine bağlı Geçti durumunu, ALT-01'in G-03-T3 bağlantısını ve üç NFR'nin Ölçülmedi durumunu kontrol edin.
4. Gerçek kalite ölçümleri yapıldığında yeni gözlem kayıtlarını ve ilgili sonuç alanlarını güncelleyin; planın hazır olması nedeniyle boş sonuçları başarılıya çevirmeyin.

Bu kaydetme yönergesi, kullanıcının bilgisayarında dosyanın kaydedildiğinin doğrulanması değildir. Çalışma dosyası kayda hazır olarak sunulmuştur.

Dayanak dosyalar: `03-gereksinimler.md` ve `08-prototip-gozlemleri.md` içindeki G-04 (AC-01), G-01 (AC-02), G-02 (AC-03), G-05 (AC-04A, AC-05 başlangıcı ve AC-06 kayıt dökümü), G-06 (AC-04B ve AC-06 sonucu) ve G-05-B (AC-05 sonucu ve AC-06 başlangıç toplamları) kayıtları. Düğmelerin anlamını açıklayan vazgeçme gözlemi G-03-T3'tedir. G-05-B, doktor ve resepsiyon gözlemleri arasındaki R002 durum değişimini açıklar.

AC-07'nin başlangıç örneği için G-04/G-06, beklenen engelin tanımı için `index.html` içindeki saat ve oluşturma kontrolleri kullanıldı. Sonuç G-07'de kullanıcı bildirimi olarak kaydedildi. ALT-01, önceki G-03-T3 kullanıcı açıklaması ve görüntülerine dayanır; yeniden çalıştırılmadı.
