# İlk dört hafta
Öğrenci takip rehberi

Klinik Randevu projesi | 19 öğrenci | G01-G03: 5 kişi, G04: 4 kişi
Önce gözlemle, sonra açıkla, planla, uygula ve gerçek sonucu kaydet.

## Bu yeni sürümde ne var?

İlk üç dersin 29 Ekim tarihli 33 sayfalık rehberi korunmuştur. Sonuna dördüncü haftanın sekiz basamaklı uygulaması eklenmiştir. İlk üç haftayı tamamlayan gruplar yeniden başlamaz; kendi dolu proje klasörüyle H4 bölümüne geçer.

| Bu PDF’de | İçerik |

| --- | --- |

| Sayfa 1-2 | Kullanım ve paket haritası |

| Sayfa 3-35 | Önceki 33 sayfalık ilk üç ders rehberi |

| Sayfa 36-49 | Dördüncü hafta: sekiz basamak, çalışma formları ve teslim |

Bu PDF rehberdir. Asıl çalışmanızı ZIP’teki uygulama ve düzenlenebilir Markdown belgelerinde yapın. Her grup kendi deposunu kullanır. Öğretmenin puanını, test sonucunu, kayıt kimliğini veya inceleme durumunu kendi grubunuzun gerçekleşmiş sonucu gibi yazmayın.

H4 öğretmen örneği: https://github.com/pozelll/-klinik-randevu-ogretmen/tree/docs/h4-mimari-plan
H4 kod ayrımı bu hafta uygulanmaz; tasarım ve sonraki uygulama planı hazırlanır.



# ZIP’ten hangi klasörü kullanacağım?

| Klasör / dosya | Ne zaman, nasıl? |

| --- | --- |

| BASLA.md | Önce okuyun; devam eden ve yeni başlayan grup akışını ayırır |

| klinik-randevu-ogrenci/ | Sıfırdan başlayan grup için 1-2. hafta uygulaması ve boş belgeler |

| 3-derste-eklenecek/hafta-03/ | Üçüncü haftada kendi kök projenize eklenecek eski şablonlar, kod parçaları ve alıştırma |

| 4-haftada-eklenecek/hafta04/ | Dördüncü haftada eklenecek boş 00-04 belgeleri, çizim taslağı, plan girdileri ve kart |

| Ilk_4_Hafta_Ogrenci_Takip_Rehberi.pdf | Bu rehberin paketin içindeki kopyası |

**Devam eden grup:** Kendi dolu projenizi yedekleyin. Yalnız ihtiyacınız olan yeni hafta klasörünü ekleyin. Eski docs, diagrams, hafta-03 ve index.html üzerine boş başlangıç dosyası yazmayın. Zaten bir hafta04 klasörünüz varsa dosyaları karşılaştırarak ekleyin; dolu alanları koruyun.

**Yeni başlayan grup:** klinik-randevu-ogrenci klasöründen başlayın. Üçüncü hafta eklerini o projenin köküne alın. H3 kod parçalarını kendiniz uygulayın; referans uygulama hazır karşılaştırma içindir. H4’te yalnız yeni belge klasörünü ekleyin.

Eski 33 sayfanın “3-derste-eklenecek” yolları hâlâ geçerlidir. “Ders” başlıkları bu dört haftalık sıralamadaki oturumları anlatır. Gözlem kimliklerini kendi docs/08’inizle eşleştirin; örneğin öğrenci G-06 yenileme alıştırması, öğretmen G-06 kaydından farklı bağlamdadır.

Dosya kopyası tarayıcı kayıtlarını taşımaz. Kendi bilgisayarınızda aynı dosya yolu, tarayıcı, rol, doktor ve tarih koşullarını kaydedin.



# 4. haftada ne yapacağız?

Üçüncü haftanın çalışan uygulamasından devam edeceğiz. Kodun nasıl sorumluluklara ayrılacağını tasarlayacak, uygulama görevlerini planlayacak ve değişiklik gelince süre/emeğin neden değiştiğini açıklayacağız.

| Basamak | Çıktı |

| --- | --- |

| 1-2 | Başlangıç sürümü, yedek, H4 dalı ve klasörler |

| 3 | Üç yaklaşımın karşılaştırması ve gerekçeli seçim |

| 4 | Arayüz, iş kuralları ve veri erişimi diyagramı |

| 5 | İki mimari seçenek ve tasarım kalıbı kararı |

| 6 | İlk iş planı, ağ, kritik yol, kaynak ve risk |

| 7 | Yeni kartla güncel plan; ilk plan korunur |

| 8 | Farklı kişinin incelemesi, PR ve teslim kaydı |

## Görevleri gerçek isimlerle paylaşın

Beş kişilik grupta bir üye sürüm/teslimi, biri yaklaşımı, biri mimari/diyagramı, biri hesabı, biri çapraz kontrolü koordine edebilir. Dört kişilik grupta sürüm/teslim ile yaklaşım koordinasyonu birleşebilir. Her parçayı yazan kişiden farklı kişi o parçayı inceler; kontrol eden kendi yazdığı bölümü bağımsız onaylamaz.

Bunlar önerilen iş paylaşımlarıdır; üyeleri 00 belgesine gerçek adlarla yazın. Öğretmenin örnek U1-U4 planı gelecekteki kod uygulaması içindir; H4 belgesinin gerçek inceleyenini otomatik belirlemez.

Kayıt: hafta04/docs/00-baslangic-ve-surum.md. Bu hafta “kod modüllere ayrıldı” veya “A-I işleri bitti” yazmayın.



# Önce kendi çalışmanızı koruyun

1. Üçüncü haftada kullandığınız index.html dosyasının tam yolunu bulun. Aynı dosyanın açıldığını doğrulayın.
2. Dolu proje klasörünü ayrı bir yedek konuma kopyalayın. Kaynak dal ve tam commit kimliğini 00’a yazın.
3. 4-haftada-eklenecek içindeki hafta04 klasörünü kendi proje kökünüze ekleyin. Mevcut dolu dosyanın üstüne yazmayın.
4. Kendi deponuzda H3 değişikliklerinin bulunduğu tabanı belirleyin; docs/h4-mimari-plan dalını bu tabandan oluşturun. H3 main’de değilse gerçek tabanı öğretmenle netleştirip kaydedin.

| Kontrol | Ne görmelisiniz? |

| --- | --- |

| Kök | index.html, docs, diagrams, hafta-03 ve hafta04 birlikte |

| H4 docs | 00, 01, 02, 03, 04 boş çalışma formları |

| H4 diagrams | Düzenlenebilir başlangıç taslağı ve açıklama |

| H4 planlar/kartlar | İlk planı koruma alanı, örnek girdiler, değişiklik kartı |

Tarayıcı kayıtları yedek ZIP’in içinde değildir. Yeni dosya konumunda örnek kayıtlar farklı görünürse önce saklama koşulunu kontrol edin. Veriyi öğretmenin ekranına benzetmek için sıfırlamayın.

## Bu adım bitince

00 belgesinde kaynak yol, yedek yol, kaynak dal/commit, H4 dalı, üyeler ve açık kalan işler dolu olmalı. Başka bir üye doğru projeyi açabildiğinizi kontrol etsin. Yeni test yapmadıysanız yapılmış test sonucu yazmayın.



# Çalışma yaklaşımını seçin

**Amaç:** Bir yaklaşımı adı popüler olduğu için değil, kendi proje koşullarınıza uyduğu için seçmek.
**Açın:** hafta04/docs/01-yasam-dongusu-secimi.md; kök docs/01 ve 03; hafta-03/docs/05 ve 06.

1. Önceki çalışmadan iki somut durum bulun: değişen kapsam, geri bildirim, belirsizlik veya kalite riski.
2. Şelale, artırımlı ve çevik yaklaşımları değişiklik, geri bildirim, ilk kullanılabilir sonuç, risk ve proje uygunluğu açısından karşılaştırın.
3. Seçiminizi yazın; iki gerekçeyi gerçek dosya/bölümle ilişkilendirin.
4. Seçmediğiniz bir yaklaşımın hangi koşulda daha uygun olacağını ve seçiminizin zayıf yanını açıklayın.

| Kavram | Düşünmek için kısa açıklama |

| --- | --- |

| Şelale | Aşamaları ve çıktıları daha önceden belirgin planlama |

| Artırımlı | Kullanılabilir kapsamı parça parça büyütme |

| Çevik | Kısa geri bildirimle öğrenme ve planı uyarlama |

Artırımlı ve çevik birbirini dışlamak zorunda değildir. “Çevik, o yüzden belge yok” demeyin. Kararın ve kanıtın nerede tutulacağını açıklayın. Sınıf etkinliğindeki rol isimleri tek başına tam Scrum uygulandığını göstermez.

## Kontrol sorusu

Başka bir üye “Sizin projenizde hangi olay bu seçimi destekliyor?” diye sorsun. Yanıtınız yalnız “daha hızlı” ise somutlaştırın. Gerçek geri bildirimi 01’in sonuna yazın.



# Üç sorumluluğu çizin

**Amaç:** Ekranın, iş kararının ve saklamanın görevlerini karıştırmamak.
**Açın:** hafta04/docs/02-mimari-karar.md ve hafta04/diagrams/01-bilesen.drawio.

1. İptal veya oluşturma senaryosunu seçin; ilgili FR ve kabul koşulunu yazın.
2. Arayüz hangi isteği alır ve neyi gösterir? İş kuralları hangi kararı verir? Veri erişimi neyi okur/yazar? Tabloyu doldurun.
3. Çizim taslağındaki boş sorumlulukları kendi cümlelerinizle değiştirin. Çağrı ve sonuç oklarını ekleyin; yön ve taşıdıkları bilgiyi etiketleyin.
4. Başlıkta “Önerilen tasarım” deyin. Tek uygulama içindeki ayrımın sunucu ayrımı olmadığını belirtin.
5. .drawio dosyasını kaydedin, PNG dışa aktarın; ikisini yeniden açıp okunabilirliği kontrol edin.

| İptal için düşünün | Nerede açıklayacaksınız? |

| --- | --- |

| Kullanıcı pencereden vazgeçerse? | Değişiklik isteği ve veri akışı |

| Rol/sahiplik/durum uygun değilse? | Kuralın karar sınırı |

| İptal kaydı siler mi; saat ne olur? | Durum geçişi ve BR-01 |

| Kalıcı yazma başarısızsa? | Bellek ile kalıcılık sonucunun ayrımı |

PNG hazır olmadığı için taslak pakette verilmedi. Kendi düzenlediğiniz çizimden üretin. Kök diagrams klasöründeki ilk iki modelin üzerine bu çizimi kaydetmeyin.

Kaydet: hafta04/diagrams/01-bilesen.drawio ve 01-bilesen.png. 02 belgesinde her okun anlamı açıklanmalı.



# İki seçenek ve bir kalıp kararı

**Açın:** hafta04/docs/02-mimari-karar.md.
Mevcut düzeni sürdürme ile sorumlulukları ayırma seçeneklerini aynı ölçütlerle karşılaştırın. Farklı bir alternatif öneriyorsanız kapsamını açık yazın.

| Ölçüt | Cevaplamanız gereken |

| --- | --- |

| Açıklık | Bir kuralı hangi yerde bulabiliyoruz? |

| Değişiklik etkisi | Açıklama, kural veya saklama değişince nereler etkileniyor? |

| Test edilebilirlik | Kuralı ekranın tamamını çalıştırmadan kontrol edebilecek miyiz? |

| Maliyet | Kaç yeni bağlantı/kavram ve ne kadar bakım yükü doğacak? |

| Uygunluk | Bu küçük eğitim projesinin gerçekten ihtiyacı var mı? |

Bir tasarım kalıbını değerlendirin. Öğretmen örneği Randevu Deposu / Repository’dir. Hangi somut sorunu çözmesini beklediğinizi, yararını ve ek karmaşıklığını yazın. Sadece kalıbın adını eklemek gerekçe değildir. Kullanma veya kullanmama kararınız tutarlı gerekçeyle açıklanmalı.

Repository veri tabanı veya yeni sunucu demek değildir. Öğretmen örneğinde veri erişimi sınırı içinde önerilen küçük uyarlamadır. Kodda uygulanmamış bir sözleşmeyi “çalışıyor” diye yazmayın.

## Kontrol

Başka üye kararın diyagram ve gereksinimle uyumunu okusun. Arayüze iş kuralı, veri erişimine rol kararı konduysa gerekçeyi yeniden tartışın. Beşinci haftaya bırakılan kod işleri açık olsun.



# İlk planın girdilerini hazırlayın

**Açın:** hafta04/docs/03-is-plani-ve-riskler.md. Önce kapsam, süre birimi, kişiler, öncüller ve çıktıların anlamını yazın. Aşağıdaki tablo öğretmenin verdiği alıştırma girdisidir; tamamlanmış iş veya grubun ölçülmüş tahmini değildir.

| İş | Çıktı | Öncül | Kişi | Blok |

| --- | --- | --- | --- | --- |

| A | Sözleşme ve koşullar | - | U1+U2 | 2 |

| B | Randevu Deposu | A | U1 | 4 |

| C | İş kuralları | A | U2 | 3 |

| D | Arayüz | A | U3 | 3 |

| E | Bütünleştirme | B,C,D | U1+U2+U3 | 2 |

| F | Kabul/sınır denemeleri | E | U2+U3 | 3 |

| G | Bağımsız kod incelemesi | F | U4 | 2 |

| H | Sınırlı düzeltme ve tekrar | G | U1+U2 | 2 |

| I | Son kontrol ve paket adayı | H | U1+U4 | 1 |

Bir blok 30 dakika; t=0 net çalışma başlangıcı. Her atanan kişi iş boyunca o işe katılır. B/C/D farklı kişilerle paralel olabilir; E üçünü bekler. U4 yazarlardan farklı inceleyen varsayımıdır. Gerçek grup farklı görev/kaynak seçerse kendi hesabını yapar.

Beşinci üye varsa somut görevini ve zamanını yazın; yalnız kişi sayısını artırmak süreyi otomatik azaltmaz. H4 belge incelemesinin kişileri ile gelecekteki uygulama planının kişilerini ayırın.

Tablo dosyası: hafta04/planlar/00-ornek-plan-girdileri.md. Ana kaydınız: docs/03. Üçüncü haftanın puanını saate dönüştürmeyin.



# Kritik yolu nasıl bulacağız?

1. İşleri ve “öncül bitsin, sonraki başlasın” oklarını çizin.
2. Her işin erken başlangıcını öncüllerin en büyük erken bitişinden bulun; süreyi ekleyin.
3. Son bitişten geriye gidin: geç bitiş ardılların en küçük geç başlangıcı; süreyi çıkarın.
4. Bolluk = geç başlangıç - erken başlangıç. Bu tarih kısıtı olmayan örnekte sıfır bolluklu zinciri ve yol toplamlarını karşılaştırın.
5. Her kişinin aynı zaman aralığında iki işte bulunmadığını kontrol edin.

## Yöntemi öğrenmek için küçük örnek

P: 2 blok. P’den sonra Q: 3 ve R: 2 blok paralel. Son S: 1 blok; Q ve R’yi bekler. Q 2-5, R 2-4 aralığında çalışır. S max(5,4)=5’te başlar ve 6’da biter. P-Q-S kritik yoldur; R’nin 1 blok bolluğu vardır. Bu örnek, A-I ödevinin cevabı değildir.

| Ölçü | Nasıl hesaplanır? |

| --- | --- |

| İş sürelerinin toplamı | Bütün süreler; paralellik indirilmez |

| Net geçen süre | Ağın ve uygun kaynak atamalarının bitişi |

| Emek | Her işin saat süresi × kişi sayısı; sonra toplam |

| Takvim tarihi | Gerçek çalışma günleri, molalar ve dış beklemelerle ayrıca |

Örnek: bir saatlik işe üç kişi katılırsa üç kişi-saat emek oluşur. Bir saatlik süre üç saate dönüşmez. Bollukları toplayıp projenin sonuna eklemeyin.

Kaydet: docs/03 içindeki erken/geç tablo, ağ ve açıklamalar. Sayıları yazmak yetmez; bir birleşme noktasındaki max hesabını açıklayın.



# İlk planı dondurun ve riski yazın

Hesabı bitirince docs/03’ün ilk planını, varsayımlarını, ağını, sonuçlarını ve risklerini hafta04/planlar/01-ilk-is-plani.md dosyasına karşılaştırma kopyası olarak alın. Tarih ve kaynak commit’i ekleyin. Sonraki kart geldiğinde bu dosyayı yeni değerlerle değiştirmeyin.

| İlk plan kontrolü | Grubunuzun kaydı |

| --- | --- |

| Kapsam ve bitiş çıktısı | Hangi teslim adayı planlanıyor? |

| Süre / kaynak | Birim ve gerçek isimler veya açık örnek varsayım |

| Ağ ve hesap | Öncüller, yollar, erken/geç ve bolluk |

| Çakışma | Aynı kişi aynı anda iki farklı işte mi? |

| Risk | Neden, etki, önlem, sorumlu ve işaret |

| Sürüm | İlk planı gösteren commit ve korunan dosya |

## Risk örneği nasıl yazılır?

“İnceleyen G sırasında uygun olmayabilir; bitiş gecikebilir. Uygunluğu önceden doğrula; değişirse takvimi yeniden hesapla.” Bu yapı, yalnız “zaman riski” yazmaktan daha kullanışlıdır. Kendi grubunuzun en az ilgili somut risklerini ve sorumlusunu belirleyin; burada yeni bir puanlama eşiği verilmez.

Bir üye hesabı okuyup anlaşılmayan bir varsayımı sorsun. Gerçek geri bildirimi docs/03’e yazın. Bu hazırlık kontrolü gelecekteki kod testleri çalıştırıldı demek değildir.



# Yeni kart: karar tablosu ve kanıt

İlk plan korununca kartı açın: hafta04/kartlar/01-karar-tablosu-ve-kanit.md. Mevcut iptal koşulları için yedi ayrı durum ve her durum için yalıtılmış başlangıç/kanıt isteniyor. Bu ders senaryosu yeni yetki veya ürün davranışı eklemiyor.

| Satır | Koşul | Beklenen |

| --- | --- | --- |

| K01 | Kayıt yok | Ret; veri değişmez |

| K02 | Resepsiyon; kendi Bekliyor kayıt | Ret; rol uygun değil |

| K03 | Doktor; kendi Bekliyor kayıt | Ret; rol uygun değil |

| K04 | Hasta; başka hastanın Bekliyor kaydı | Ret; sahiplik uygun değil |

| K05 | Hasta; kendi Tamamlandı kaydı | Ret; durum korunur |

| K06 | Hasta; kendi İptal edildi kaydı | İkinci iptal yok |

| K07 | Hasta; kendi Bekliyor kaydı; onay var | Silmeden iptal; toplam aynı; BR-01 |

Örnek A-I planında C: 3 → 5 blok; F: 3 → 4 blok. Diğer süre/öncül/kişiler aynı kabul edilir. Bu yeni girdilerle hesabı siz yapacaksınız. Başka ilk plan kullandıysanız kartın etkisini kendi işlerinize eşleyin.

Bu hafta beklenen sonucu yazın; çalıştırılmamış duruma Geçti yazmayın. Vazgeçme, kalıcı yazma hatası ve diğer işlemlerle ortak veri kontrolleri kapsamda kalır. Tek başarılı iptal görüntüsü yedi durumun kanıtı olamaz.



# Güncel planı karşılaştırın

1. C ve F’nin hangi yeni çıktılar nedeniyle büyüdüğünü yazın.
2. Güncel sürelerle ileri ve geri hesabı baştan yapın. İlk planı değiştirmeyin.
3. Yeni kritik yolu, bollukları, net süreyi ve emeği bulun.
4. Kişi çakışmalarını ve inceleyenin yeni zamandaki uygunluğunu kontrol edin.
5. Kapsamı kabul etme veya erteleme seçeneklerini gerekçelendirin; kalite kontrolünü gizlice kaldırmayın.

| Karşılaştırma | İlk plan | Güncel plan | Gerekçe |

| --- | --- | --- | --- |

| C ve F süresi | Kendi hesabınız | Kendi hesabınız | Kartın etkisi |

| Net geçen süre | Kendi hesabınız | Kendi hesabınız | Birleşme noktası / kritik kol |

| Toplam emek | Kendi hesabınız | Kendi hesabınız | Süre × kişi |

| Kritik yol ve bolluk | Kendi hesabınız | Kendi hesabınız | Değişen en uzun yol |

| Risk ve kalite | İlk kaydı koru | Ek değerlendirme | Yeni durum |

## Tartışma soruları

Ek iş sürelerinin toplamı ile net gecikme neden aynı olmayabilir? C’nin ilk plandaki bolluğu neyi değiştirir? Yeni kritik kol hangisi? Bir kişi uygun değilse aynı bitişi savunabilir misiniz? İnceleme süresini azaltmak hangi kalite koşulunu etkiler?

Kaydet: docs/03 güncel plan bölümü. İlk dosya planlar/01-ilk-is-plani.md aynı kalmalı. Gerçek takvim henüz yoksa kesin teslim tarihi uydurmayın.



# Farklı kişi incelemesi ve PR

**Açın:** hafta04/docs/04-inceleme-ve-teslim.md.
Çalışma dalında 00-04 belgelerini, çizimleri, ilk/güncel planı ve kartı kaydedin. PR açıklamasına problemi, çıkan sonucu, yapılan kontrolleri ve açık kalanları yazın.

1. Doğru kaynak ve hedef dalı kontrol edin. Önceki çalışmalar main’deyse hedef main olabilir; açık bağımlılık varsa gerçek tabanı kaydedin.
2. İnceleyen, değerlendirdiği bölümün yazarı/ortak yazarı olmasın. Güncel tam commit kimliği ve tarihi yazsın.
3. Dosya farkını, gerekçeleri, diyagramı ve iki hesabı kontrol etsin. .drawio dosyasını açıp düzenlenebildiğini deneme kopyasında sınasın.
4. Bulguyu dosya/bölüm ve beklenen düzeltmeyle yazsın. Düzeltme varsa yeni commit ve yeniden kontrol kaydı ekleyin.

| Kayıt | Zorunlu anlam |

| --- | --- |

| İncelenen commit | Tam olarak hangi sürüme bakıldı? |

| İnceleyen / tarih | Kim gerçekten değerlendirdi? |

| Bulgu / karar | Neyi kontrol etti, ne eksik? |

| Düzeltme / yeniden kontrol | Yeni sürümde bulgu giderildi mi? |

İnceleyen yoksa “Bekliyor” yazın. Öğretmenin PR #12’si sizin PR numaranız değildir. Viewed, review ve merge farklı işlemlerdir. Kendi hesabınızdan yazılmış hazırlık metni başka kişinin gerçek görüşü sayılamaz.



# Teslimden önce dosya kontrolü

| Çıktı | Kontrol |

| --- | --- |

| 00 başlangıç kaydı | Kaynak/yedek yolu, dal, commit, üyeler ve açık işler |

| 01 yaklaşım | Üç yaklaşım, proje kanıtı ve gerekçeli seçim |

| 02 mimari | İki seçenek, kalıp kararı, sorumluluklar ve sınırlar |

| Çizimler | Düzenlenebilir .drawio ve aynı tasarımın okunur PNG’si |

| 03 iş planı | Görev, süre, öncül, kişi, ağ, hesap, risk; ilk/güncel karşılaştırma |

| Sabit ilk plan | Kart öncesi değerler değişmeden korunmuş |

| 04 inceleme | Gerçek kişi, commit, bulgu, düzeltme, son karar |

| GitHub ve erişim | Gerçek depo/PR/commit bağlantıları; öğretmen erişimi |

| Önceki haftalar | Dolu dosyalar korunmuş; H4 nedeniyle kod değiştirilmemiş |

Gerekli inceleme ve düzeltmeler tamamlanınca doğru hedef dala birleştirin; ana sürümde dosyaları ve bağlantıları yeniden kontrol edin. Önceki PR bağımlılıkları sürüyorsa bunları açık yazın. Paketin hazır olması nihai teslimin bütün koşullarının sağlandığını göstermez.

## Kısa grup gösterimi

Seçiminizi söyleyin; diyagramda bir isteğin yolunu gösterin; ilk planla yeni plan arasındaki farkı açıklayın; inceleme kaydını açın. Her üye kendi katkısının yerini ve nedenini gösterebilsin. Başka grubun veya öğretmenin sonucunu kendi kanıtınız gibi sunmayın.



# Kendi kendinizi sınayın

Aşağıdaki sorular H4’ü tekrar etmek için önerilen alıştırmadır; ayrı zorunlu notlandırma kuralı eklemez. Yanıtları kendi sözcüklerinizle yazın; öğretmen örneğine bakmadan dosyanın yerini bulmayı deneyin.

1. İlk H3 dosyasını neden koruduk? Kopyalamak tarayıcı verisini de taşır mı?

2. Çevik ve artırımlı yaklaşım birlikte kullanılabilir mi? Kendi projenizden gerekçe verin.

3. İptal uygunluğuna arayüz mü, iş kuralları mı karar verir? Saklama nereye aittir?

4. Repository kullanmak hangi sorunu çözebilir, hangi ek maliyeti getirir?

5. Bir işin süresi ile kişi-saat emeği arasındaki farkı örnekleyin.

6. Kritik yol ve bolluk ne demek? Kendi planınızda E benzeri birleşme noktasını açıklayın.

7. Yeni kartta hangi süreler değişti? Net gecikme neden toplam ek süreyle aynı olmak zorunda değil?

8. PR açılması, dosya yüklenmesi ve gerçek inceleme hangi farklı bilgileri gösterir?

Paket içindeki isteğe bağlı tekrar-sorulari.md dosyasını kullanabilirsiniz. Üçüncü haftanın her öğrenci için ayrı çıkış bileti gerekliliği önceki rehberdeki haliyle devam eder.



# Hızlı yardım ve tamamlanma sınırı

| Durum | Ne yapmalısınız? |

| --- | --- |

| main’de H4 yok | Önce doğru çalışma dalını seçin; yükleme ile merge’i ayırın |

| Boş şablon dolu dosyaya denk geliyor | Üzerine yazmayın; karşılaştırıp yalnız yeni dosyaları ekleyin |

| Çizim resim gibi düzenlenmiyor | PNG yerine .drawio kaynağını açın |

| Kritik yol farklı çıktı | Süre, öncül, birim ve kaynak varsayımlarını karşılaştırın |

| Emek ile süre eşit değil | Birlikte çalışan kişi sayılarını ve paralel işleri kontrol edin |

| Öğretmenin R013 kaydı bende yok | Kendi gerçek kayıt kimliğinizi kullanın |

| İnceleyen yok / erişemiyor | Engeli ve bekleyen işi yazın; tamamlandı olarak işaretlemeyin |

| Kod ayrımı isteniyor mu? | H4’te tasarım/plan; uygulama beşinci haftanın işidir |

**Öğretmen örneğinin durumu, 1 Kasım 2026:** H4 hazırlık dosyaları GitHub’da; PR #12 taslak. Gerçek bağımsız inceleme ve ana dala birleştirme bekliyor. Bu durum sizin grubunuzun incelemesini otomatik yapmaz veya engellemez; kendi kayıtlarınızı tutun.

Örnek depo: https://github.com/pozelll/-klinik-randevu-ogretmen
H4 dalı: docs/h4-mimari-plan
Yardım için önce README.md ve hafta04/README.md dosyalarını okuyun.


