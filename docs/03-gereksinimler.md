# 03 — Gereksinim taslağı

Ekip: Öğretmen denemesi  
Tarih: 27.10.2026  
Sürüm: Belge 0.4 — doldurulmuş öğretmen çalışma örneği  
İnceleyen: İkinci ekip üyesinin incelemesi henüz yapılmadı.  
Durum: Dört bölümün çalışma metni hazır. Kalite hedefleri henüz ölçülmedi; gerçek paydaş doğrulaması ve ikinci ekip üyesinin incelemesi yapılmadı.

Her satırda sistemin yapacağı işi açık ve kontrol edilebilir biçimde yazın. Ekrandaki düğme adı tek başına gereksinim değildir. Önceliğinizi ve gerekçenizi ekleyin.

Bu taslak, Klinik Randevu v0.1 başlangıç prototipinin kapsamı, paydaş tablosu ve mevcut gözlemler temel alınarak hazırlanmıştır. 02 numaralı belgedeki görüşme örnekleri ders senaryosudur; gereksinimler gerçek klinik tarafından onaylanmış değildir. Prototipte hazır bulunan davranışları yazılı gereksinimlere dönüştürüyoruz.

## İşlevsel gereksinimler

**FR**, işlevsel gereksinim kimliğidir; sistemin yapacağı işi belirtir. **Aktör**, o işlevi kullanan roldür. **Koşul**, işlemin hangi durumda yapılabileceğini sınırlar. FR-01–FR-06 kimlikleri 01 ve 02 numaralı belgelerle aynı anlamda korunmuştur.

**Öncelik önerisi:** Yüksek, temel randevu akışını ve kayıt durumunu doğrudan etkileyen işlerdir. Orta, günlük takibi kolaylaştıran ancak bilgisi kayıt listesinden de elde edilebilen özet işlevidir. Bu sıralama öğretmen örneğidir; altı gereksinimin tamamı başlangıç kapsamındadır. Orta öncelik, kapsamdan çıkarıldığı anlamına gelmez.

| Kimlik | Başlık | Sistem ne yapmalı? | Aktör / koşul | Öncelik ve gerekçe |
|---|---|---|---|---|
| FR-01 | Uygun saatleri listeleme | Seçili doktor ve örnek tarihe ait sabit saatleri listelemeli. İptal edilmemiş kayıt bulunmayan saatleri Uygun, Bekliyor kaydı bulunan saatleri Dolu, Tamamlandı kaydı bulunan saatleri Kapalı olarak göstermeli. Hasta veya resepsiyon uygun bir saati seçtiğinde seçilen saat ayırt edilebilmeli. | Hasta, Resepsiyon ve Doktor saatleri görüntüler. Doktor bu alandan randevu oluşturmak için saat seçemez. Doktor/tarih değiştiğinde gösterilen saatler o seçime göre güncellenir. | Yüksek: Kullanıcının uygun saati belirlemesi ve dolu veya tamamlanmış saate yönelmemesi için temel bilgidir. |
| FR-02 | Randevu oluşturma | Hasta veya resepsiyon uygun saati seçip onayladığında seçili hasta, doktor, tarih ve saat bilgileriyle yeni bir randevu oluşturmalı. Yeni kayıt Bekliyor durumunda listede görünmeli ve seçilen saat Dolu olmalı. BR-01'e aykırı ikinci kayıt oluşturulmamalı. | Hasta kendi canlandırdığı örnek kişi adına; Resepsiyon seçili örnek hasta adına işlem yapar. Geçerli seçim ve uygun saat gerekir. Doktor rolü kayıt oluşturamaz. Bu metin küçük başlangıç prototipinin çalışma sınırları içindir. | Yüksek: Ürünün temel randevu alma işini gerçekleştirir; doğru kişi ve zamana kayıt açılması gerekir. |
| FR-03 | Kendi randevusunu iptal etme | Hasta görünümünde yalnız seçili hastanın seçili doktor ve tarihteki kayıtlarını göstermeli. Hastanın kendi Bekliyor kaydını iptal etmek istemesi üzerine onay istemeli. Onay verilirse kayıt İptal edildi durumuna geçmeli, listede kalmalı ve saat BR-01'e göre yeniden uygun olmalı. Vazgeçilirse randevu durumu ve saatin doluluğu değişmemeli. | Yalnız Hasta rolü; kayıt seçili hastaya ait ve Bekliyor olmalı. Tamamlandı veya İptal edildi durumundaki kayıt iptal edilemez. Resepsiyon ve Doktor bu işlemi yapamaz. | Yüksek: Hastanın plan değişikliğini yönetmesini ve vazgeçtiğinde randevusunun korunmasını sağlar. |
| FR-04 | Yetkili günlük liste | Resepsiyon ve Doktor rollerinde seçili doktorun seçili tarihteki bütün örnek hasta kayıtlarını göstermeli. Bekliyor, Tamamlandı ve İptal edildi durumları ayırt edilebilmeli. Resepsiyonda örnek hasta seçimi günlük listeyi tek hastaya daraltmamalı. | Resepsiyon ve Doktor; kapsam yalnız seçili doktor ve tarihtir. Hasta rolü bu bütün hasta listesini görmez; kendi kayıtları FR-03 kapsamında gösterilir. | Yüksek: Klinik çalışanlarının o günkü randevuları ve durumlarını birlikte takip etmesini sağlar. |
| FR-05 | Doktorun randevuyu tamamlaması | Görevli olarak seçilen doktor, günlük listesindeki Bekliyor kaydı tamamladığında kayıt Tamamlandı durumuna geçmeli. İlgili saat Kapalı kalmalı; bu kayda yeniden tamamlama işlemi sunulmamalı. Durum değişikliği günlük toplamlara yansımalı. | Yalnız Doktor rolü; kayıt görevli olarak seçili doktora ve seçili tarihe ait, Bekliyor durumunda olmalı. Hasta ve Resepsiyon tamamlama yapamaz. | Yüksek: Bekleyen ve biten muayenelerin ayrılmasını ve tamamlanan saatin yeniden kullanılmamasını sağlar. |
| FR-06 | Yetkili günlük toplamlar | Resepsiyon ve Doktor rollerine seçili doktor ve tarih için Bekleyen, Tamamlanan, İptal edilen ve Toplam kayıt sayılarını göstermeli. Toplam kayıt sayısı üç durumun toplamına eşit olmalı. Randevu oluşturma, durum değişimi veya doktor/tarih seçimi değiştiğinde sayılar mevcut kayıtlarla tutarlı güncellenmeli. Hasta rolünde bu sayılar gösterilmemeli. | Resepsiyon ve Doktor; yalnız seçili doktor ve tarihin kayıtları sayılır. İptal edilen kayıtlar toplam kayıt sayısına dahildir. | Orta: Günlük akışın hızlı okunmasını sağlar; ayrıntılar günlük listede de bulunur. Bu özet yine başlangıç sürümünün kapsamındadır. |

### Bir gereksinimi birlikte okuyalım

**FR-05 örneği:** “Sistem, görevli olarak seçilen doktorun günlük listesindeki Bekliyor kaydını tamamlamasına izin vermeli; işlem sonrasında kayıt Tamamlandı, ilgili saat Kapalı olmalı.”

- Aktör: Doktor.
- İşlem öncesi koşul: Kayıt seçili doktor ve tarihe ait, Bekliyor durumunda.
- İşlem: Muayenesi biten kaydı tamamlamak.
- Beklenen sonuç: Kayıt Tamamlandı olur, saat Kapalı kalır; FR-06 kapsamında bekleyen sayısı bir azalır, tamamlanan sayısı bir artar, toplam kayıt sayısı değişmez.
- Gözlem bağlantısı: G-05-B'de R002 için bu davranış görüldü. R002 kimliği ve o denemedeki toplam sekiz sayısı, bütün gruplar için zorunlu gereksinim değerleri değildir.

### Dayanak ve doğrulama durumu

- FR-01: G-01, G-04, G-05-B ve G-06; seçili doktor/tarih ve rol davranışları için başlangıç paketi.
- FR-02: Hasta rolünde G-01. Resepsiyonun oluşturma yeteneği pakette bulunur; öğretmen oturumunda bu rolde yeni kayıt oluşturma henüz uygulanmadı.
- FR-03: G-02, G-03-T3 ve G-04. Onay penceresinde Tamam iptali onaylar; İptal işlemden vazgeçer. Üçüncü haftanın metin iyileştirmeleri henüz uygulanmadı.
- FR-04: G-05 ve G-06.
- FR-05: G-05-B.
- FR-06: Doktor ve resepsiyon için G-05, G-05-B ve G-06. Hasta görünümünde sayıları gizleme davranışı kod/paket incelemesine dayanır; bu alan için ayrıca öğretmen deneme kaydı tutulmadı.

Bu liste, gereksinimleri mevcut gözlemlerle ilişkilendirir; bütün koşulların bütün veri durumlarında sınandığı anlamına gelmez. Ayrıntılı kabul koşulları daha sonra 04 numaralı belgede yazılacak. Rol kısıtları bu eğitim arayüzünün davranışlarıdır; gerçek kimlik doğrulama veya sunucu yetkilendirmesi bu başlangıç sürümünün kapsamında değildir.

## Kalite gereksinimleri — öğrenci taslağı

**NFR**, bu belgede kalite gereksinimi kimliğidir. İşlevsel gereksinim sistemin yapacağı işi, kalite gereksinimi o işin kullanımına ve çalışma niteliğine ilişkin ölçülebilir hedefi belirtir.

**Durum:** Aşağıdaki sayılar ders için önerilen başlangıç hedefleridir; ölçülmüş sonuç veya dış bir standardın zorunlu eşiği değildir. Hedef, ölçüm koşulu ve yöntem denemeden önce kaydedilir. Deneme sonunda sonuç ayrıca yazılır; hedefe ulaşılıp ulaşılmadığı gerçek sonuçla değerlendirilir. Bu adımda kalite ölçümü yapılmadı.

| Kimlik | Kalite konusu | Ölçülebilir hedef | Ölçüm koşulu | Nasıl kontrol edilecek? |
|---|---|---|---|---|
| NFR-01 | Kullanılabilirlik | Dört farklı katılımcının en az üçü, bekleyen randevuyu iptal etme ve iptal işleminden vazgeçerek randevuyu koruma görevlerinin ikisini de yardım almadan doğru tamamlamalı. Her görev en fazla 60 saniye sürmeli. | Aynı uygulama sürümü, aynı görev metinleri ve her görev için hazırlanmış ayrı Bekliyor kaydı. Hasta rolü, Ece Yılmaz, Deniz Arı, 12 Kasım 2030. Katılımcının önceki prototip deneyimi kaydedilir. Gözlemci hangi düğmeye basılacağını söylemez. | Her katılımcı için iki görevin süresi, doğru/yanlış sonuç ve yardım ihtiyacı kaydedilir. Bir katılımcı ancak iki görevi de doğru, yardımsız ve süre sınırında bitirirse başarılı sayılır. Başarılı katılımcı sayısı en az 3/4 olmalı. |
| NFR-02 | Yanıt süresi | Doktor seçimi değiştirildikten sonra B1 saatler, B2 günlük liste ve B3 günlük toplamlar yeni seçime uygun biçimde en fazla 1 saniyede güncellenmeli. Belirlenen koşullardaki 10 denemenin tamamı bu sınırı sağlamalı. | Aynı bilgisayar ve tarayıcı sürümü; tek sekme; en fazla 20 örnek randevu kaydı; Resepsiyon rolü; 12 Kasım 2030. Deniz Arı ve Selin Kaya arasında 10 seçim değişikliği. Açık onay penceresi veya geliştirici araçlarında yavaşlatma yok. | Seçimin onaylandığı an ile üç alanın yeni seçime ait doğru içeriği gösterdiği an arasındaki süre ekran kaydından ölçülür. On süre ve en büyük süre yazılır; her biri en fazla 1 saniye olmalı. Seçim yaparken geçen kullanıcı düşünme süresi ölçüme dahil edilmez. |
| NFR-03 | Erişilebilirlik — klavyeyle kullanım | Dört temel görevin tamamı fare kullanmadan tamamlanabilmeli: randevu oluşturma, iptalden vazgeçme, randevu iptali ve doktorun randevuyu tamamlaması. Kullanılan etkin öğelerde klavye odağı görünür olmalı ve klavyeyle ilerlemeyi engelleyen takılma olmamalı. | Aynı uygulama ve tarayıcı sürümü; örnek veriler; her göreve uygun rol ve kayıt durumu. Klavye ile Tab, Shift+Tab, ok tuşları ve gerektiğinde Enter/Boşluk kullanılır. İptal onay penceresi de kontrol kapsamındadır. | Her görev için tamamlandı/tamamlanamadı, odak görünürlüğü ve takılma var/yok kaydı tutulur. Hedef, dört görevin de fare kullanmadan ve belirtilen odak koşullarını sağlayarak tamamlanmasıdır. Bu kontrol erişilebilirliğin klavye boyutunu kapsar; genel erişilebilirlik uygunluğunu tek başına kanıtlamaz. |

### Ölçümün daha sonra uygulanması

Bu alt bölüm ölçüm planıdır; aşağıdaki kontroller henüz çalıştırılmadı. Yeni denemelerin sonuçları 08 numaralı belgeye ayrı kayıtlarla eklenecek; önceki gözlemler korunacak.

**NFR-01 için:** Dört ayrı kişi kullanılır; tek kişinin dört denemesi dört katılımcı olarak sayılmaz. Katılımcılar gerektiğinde diğer gruplardan seçilebilir; böylece dört kişilik grup da aynı hedefle çalışabilir. Katılımcıya sırayla “Bekleyen randevunuzu iptal edin” ve “İptal sürecini başlatın, sonra randevunuzu koruyarak işlemden vazgeçin” görevleri verilir. Her görevin başında ayrı bir Bekliyor kaydı hazırdır. Görev okunup başlama işareti verildiğinde süre başlar; katılımcı bitirdiğini söylediğinde durur ve kaydın gerçek durumu kontrol edilir. İptal görevinde kayıt İptal edildi ve saat Uygun; vazgeçme görevinde kayıt Bekliyor ve saat Dolu olmalıdır. Yanlış iptal veya yardım isteme ayrıca kaydedilir. Görev sırası ve önceki deneyim yazılır; küçük sınıf denemesinden bütün kullanıcılar için genelleme yapılmaz.

**NFR-02 için:** Ölçüm ekran kaydı üzerinden yapılır; kayıt yazılımı ve kare hızı not edilir. Başlangıç, seçimin tıklama veya Enter ile onaylandığı andır; bitiş, yeni doktorun saatleri, günlük listesi ve toplamlarının tamamının doğru göründüğü andır. Yanlış içerik hız hedefini sağlamış sayılmaz. Her denemeye sıra numarası ve süre verilir. Aynı kare içinde görünen değişim için sıfır saniye yazmak yerine “bir kare aralığından kısa” denir. Sınırın ayırt edilemediği bir kayıt başarılı sayılmaz; ölçüm belirsizliği kaydedilir ve uygun kayıtla tekrar edilir. Bu kontrol yerel arayüzün belirtilen veri miktarındaki yanıtıdır; cihazlar arası paylaşım veya yoğun kullanıcı yükü testi değildir.

**NFR-03 için:** Her görev uygun başlangıç durumundan yürütülür. Rol ve seçim alanlarına klavyeyle ulaşılır; ilgili işlem ve onay/vazgeçme adımı fare kullanmadan tamamlanır. Hangi öğede olduğumuzu gösteren odak çerçevesi kontrol edilir. Pasif bir düğmenin Tab sırasında atlanması, o düğmenin zaten kullanılamadığı durumda tek başına hata sayılmaz. Erişilemeyen etkin düğme, görünmeyen odak veya klavyeyle çıkılamayan alan açıkça kaydedilir. Görevin sonucu randevu ve saat durumlarıyla kontrol edilir. Renk, ekran okuyucu, büyütme gibi diğer erişilebilirlik boyutları bu dört görevlik kontrolün dışında ayrıca değerlendirilebilir.

### Hedef ile sonuç arasındaki ayrım

| Kimlik | Bu adımda yazılan hedef | Şu anki ölçüm durumu |
|---|---|---|
| NFR-01 | En az 3/4 katılımcı; iki görevin her biri en fazla 60 saniye, doğru ve yardımsız. | Ölçülmedi. Önceki iptal denemeleri dört kişilik bu ölçümün yerine geçmez. |
| NFR-02 | 10/10 doktor seçimi değişikliğinde doğru ekran güncellemesi en fazla 1 saniye. | Ölçülmedi. Önceki ekran görüntülerinden yanıt süresi hesaplanmadı. |
| NFR-03 | Dört görevin tamamı klavyeyle; kullanılan etkin öğelerde görünür odak ve ilerleyebilme. | Ölçülmedi. Önceki fareli denemeler klavye kontrolünü doğrulamaz. |

Bir hedef sağlanmazsa gerçek sonuç ve gözlenen sorun kaydedilir. Hedef veya kapsam yeniden değerlendirilecekse değişikliğin gerekçesi ve tarihi ayrıca yazılır; önceki hedef ve sonuç kaydı silinmez. Ayrıntılı kabul ve kontrol adımları 04 numaralı belgeye aktarılacak.

## Başlangıçta verilmiş iş kuralı

**BR-01:** Aynı doktor, tarih ve saat için iptal edilmemiş ikinci randevu oluşturulamaz. Bu prototipte Bekliyor kaydı saati Dolu, Tamamlandı kaydı saati Kapalı tutar. İptal edildi durumundaki kayıt o saati engellemez; aynı doktor, tarih ve saatte iptal edilmemiş kayıt yoksa saat Uygun olur. Kontrol aynı açık sayfanın mevcut veri durumu içindir; çoklu sekme/cihaz garantisi değildir.

**BR**, iş kuralı kimliğidir. FR-02 randevu oluşturma işlevini anlatır; BR-01 bu işlevin uyması gereken kayıt koşulunu belirtir. Aynı kural birden fazla işlevde etkili olabilir.

- **BR-01 hangi işlevleri etkiliyor?** Doğrudan FR-01, FR-02, FR-03 ve FR-05'i etkiler. FR-04 ve FR-06, ortaya çıkan kayıt durumlarını ve sayılarını gösterir; çakışmayı engelleyen işlemin kendisi değildir.
- **Bu kural için paydaşa soracağımız soru:** Aynı doktor, tarih ve saate birden fazla iptal edilmemiş randevu verilmesinin istisnası var mı? Tamamlanmış randevunun saati her durumda kapalı mı kalmalı? Gerçek paydaş yanıtı henüz alınmadı; başlangıç prototipinde istisna tanımlı değil.
- **Gözlemlediğimiz başka kural:** Hasta rolünde yalnız seçili hastanın kendi Bekliyor kaydı için iptal işlemi sunulur; işlem onaylanırsa iptal edilir, vazgeçilirse kayıt korunur. Dayanak: G-02, G-03-T3, G-04 ve başlangıç paketinin rol koşulları. Bu mevcut prototip kuralı, gerçek kurumun onaylanmış yetki kuralı olarak sunulmaz.

### İşlevlere etkisi

| İlgili işlev | BR-01 ile bağlantısı |
|---|---|
| FR-01 — Saatleri listeleme | Aynı doktor, tarih ve saatte Bekliyor veya Tamamlandı kaydı varsa saat yeniden seçime açılmaz; durum sırasıyla Dolu veya Kapalı gösterilir. |
| FR-02 — Randevu oluşturma | Oluşturma sırasında aynı doktor, tarih ve saatte iptal edilmemiş kayıt bulunuyorsa yeni kayıt oluşturulmaz. Hasta adının farklı olması bu engeli kaldırmaz. |
| FR-03 — İptal | İptal edilen kayıt saat doluluğu hesabından çıkar. O saatte iptal edilmemiş başka kayıt yoksa saat yeniden uygun olur. Vazgeçme kaydın durumunu değiştirmez. |
| FR-05 — Tamamlama | Tamamlandı da iptal edilmemiş bir durumdur; muayenenin tamamlanması saati yeniden açmaz. |
| FR-04 / FR-06 — Liste ve toplamlar | İptal edilmiş kayıtlar geçmişte görünmeye ve toplam kayıt sayısına dahil olmaya devam eder. Saatin uygunluğu ile toplam kayıt sayısı ayrı bilgilerdir. |

### Aynı doktor, tarih ve saat için durumları okuyalım

| O saatteki mevcut kayıt durumu | Saatin görünümü | BR-01 açısından yeni kayıt |
|---|---|---|
| Bekliyor kaydı var. | Dolu | Oluşturulamaz. |
| Tamamlandı kaydı var. | Kapalı | Oluşturulamaz. |
| Yalnız İptal edildi kayıtları var veya hiç kayıt yok; iptal edilmemiş kayıt yok. | Uygun | Bu kural engellemez; rol, seçim ve diğer oluşturma koşulları da sağlanmalıdır. |

**Öğretmen denemesindeki örnek:** Deniz Arı / 12 Kasım 2030 / 09:00 için Ece'nin R011 kaydı Bekliyor durumundadır. Hasta Kaan olarak değiştirildiğinde 09:00 yine Dolu görünmüştü (G-04). Çünkü saat kontrolünün anahtarı doktor + tarih + saattir; hasta değişikliği mevcut doktor randevusunu kaldırmaz. Aynı 09:00 saatinde R001, R009 ve R010 gibi eski iptal kayıtlarının bulunması, R011'in engelini ortadan kaldırmaz.

R002 / 10:00 Tamamlandı olduğunda saat Kapalı kaldı (G-05-B). R008 / 09:30 iptal edildiğinde ise bu saatte iptal edilmemiş kayıt kalmadığı için saat Uygun oldu (G-02). Bu iki sonuç, tamamlanma ile iptalin saat üzerinde farklı etkileri olduğunu gösterir.

**Kuralın sınırı:** Doktor veya tarih değiştiğinde başka bir doktor–tarih–saat birleşimi değerlendirilir. Bu kural tek başına aynı hastanın farklı doktorlardan aynı saate randevu almasını engellemez; bunun istenip istenmediği ayrı bir ihtiyaç sorusudur. Aynı açık sayfanın mevcut verisine dayanır; farklı sekme veya cihazların eşzamanlı işlemleri bu denemede doğrulanmadı.

**Kanıtın sınırı:** Saat durumlarının değişmesi ve hasta değişince 09:00'ın dolu kalması önceki gözlemlere dayanır. Oluşturma sırasında ikinci kayıt kontrolünün bulunduğu `index.html` kodunda görüldü; bu adımda yeni bir çakışma veya eşzamanlı işlem testi yapılmadı. BR-01 için olumlu ve engellenen durumlar 04 numaralı belgede kabul koşullarına dönüştürülecek.

## Belirsiz ifadeyi düzeltme

- **Belirsiz ifade:** “Sistem hızlı olmalı.”
- **Daha açık, kontrol edilebilir ifade:** “Resepsiyon rolünde doktor seçimi onaylandığında B1 saatler, B2 günlük randevu listesi ve B3 günlük toplamlar, yeni doktor ve seçili tarihe ait doğru içerikle en fazla 1 saniyede güncellenmeli. Ölçüm aynı bilgisayar ve tarayıcı sürümünde, tek sekmede ve en fazla 20 örnek kayıtla yapılmalı. 12 Kasım 2030 için Deniz Arı ve Selin Kaya arasında yapılan 10 seçim değişikliğinin tamamı bu süre sınırını sağlamalı.”
- **Eksik bilgi / doğrulama sorusu:** Bir saniyelik ders hedefi kullanıcı beklentisi için yeterli mi? Ölçümde kullanılacak bilgisayar, işletim sistemi, tarayıcı sürümü ve ekran kaydının kare hızı ne olacak? Bu ortam bilgileri ölçüm sırasında kaydedilecek; gerçek kullanıcı beklentisi ayrıca doğrulanacak. Yirmi kayıt üzerindeki veri miktarları ve farklı cihazlar için değerlendirme ayrı planlanacak.

Bu metin, yukarıdaki **NFR-02** hedefinin açık ifadesidir; yeni veya farklı bir performans hedefi oluşturmaz. Açık onay penceresi ve geliştirici araçlarında yavaşlatma olmaması dahil bütün ölçüm koşulları NFR-02 tablosundaki gibi korunur. Bir saniye, ders için önerilen hedef olmaya devam eder; henüz ölçülmüş sonuç değildir.

### İfadeyi nasıl netleştirdik?

| Açıklığa kavuşturulan nokta | Gereksinimdeki karşılığı |
|---|---|
| Hangi kullanıcı rolü? | Resepsiyon. |
| Hangi işlem? | Doktor seçiminin değiştirilmesi ve onaylanması. |
| Süre ne zaman başlar? | Seçimin tıklama veya Enter ile onaylandığı anda. |
| Hangi sonuç görünmeli? | Saatler, günlük liste ve toplamların yeni doktor ve seçili tarihe ait doğru içeriği. |
| Ne kadar sürede? | En fazla 1 saniyede. |
| Hangi ortam ve veri? | Aynı bilgisayar/tarayıcı, tek sekme, en fazla 20 örnek kayıt; NFR-02'deki diğer koşullar. |
| Kaç deneme yeterli sayılacak? | Belirlenen 10 seçim değişikliğinin tamamı süre sınırını sağlamalı. |
| Nasıl ölçülecek? | Ekran kaydında seçimin onaylandığı an ile üç alanın doğru güncellendiği an arasındaki süre. |

“Hızlı” ifadesi tek başına işlemi, süreyi ve ortamı belirtmiyordu. Yeni metin kontrol edilecek davranışı ve değerlendirme sınırını açıklıyor. Hızlı görünen yanlış içerik bu gereksinimi karşılamaz; doğru içerik ile süre birlikte kontrol edilir. Kullanıcının seçim yapmadan önce düşünmesi bu yanıt süresine dahil değildir.

**Mevcut doğrulama durumu:** On süre henüz ölçülmedi. Her denemenin süresi ve içerik doğruluğu daha sonra ayrı kaydedilecek. Bir deneme sınırı aşarsa veya yanlış içerik gösterirse bu örnek hedef, o ölçüm setinde sağlanmamış olur. Ölçüm belirsizliği varsa sonuç başarılı olarak işaretlenmez; belirsizlik kaydı korunarak ölçüm uygun yöntemle tekrarlanır.

**Belgeden sonraki adım:** `04-kabul-kriterleri.md` dosyasında gereksinimler başlangıç durumu, kullanıcı eylemi ve beklenen sonuçla açıklanacak. Kalite hedeflerinin ölçüm adımları da ilişkilendirilecek. Beklenen sonuç, gerçek çalıştırma sonucu ve henüz yapılmamış kontrol durumu ayrı tutulacak.

Dayanak dosyalar: `01-vizyon-kapsam.md`, `02-paydaslar.md`, `08-prototip-gozlemleri.md`, başlangıç paketindeki `README.md` ve `index.html`.
