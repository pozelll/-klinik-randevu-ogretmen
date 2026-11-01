# 4. hafta — Mimari karar

Tarih: 1 Kasım 2026

Durum: Dördüncü ve beşinci basamakların öğretmen örneği hazır.
Seçim: Tek tarayıcıda katmanlı/modüler yapı ve sınırlı bir Randevu Deposu
(Repository) uyarlaması. Kodda uygulama ve bağımsız ekip incelemesi bekliyor.

İncelenen uygulama: Üçüncü hafta sonu `index.html`,
`da3ce51798344a6fafaee89cce42aa9aba90de17` commit'i.
Dördüncü hafta dalında uygulama kodu bu sürümle aynıdır.

## Senaryo ve gereksinim

**Senaryo:** Hasta, kendi Bekliyor randevusunun iptalini onaylar veya işlemden vazgeçer.
Bu senaryo üçüncü haftadaki açıklama ve onay metni çalışmasını sürdürür.
Yeni bir randevu, gerçek hesap girişi, sunucu veya ortak veritabanı eklemiyoruz.

| Kaynak | Bu çizimde korunacak davranış |
|---|---|
| [FR-03](../../docs/03-gereksinimler.md) | Yalnız Hasta rolü, seçili hastaya ait Bekliyor kaydını onayla iptal eder. Tamamlandı ve İptal edildi kayıtlarına yeni iptal uygulanmaz. |
| [FR-01 ve BR-01](../../docs/03-gereksinimler.md) | Saatin durumu doktor + tarih + saate göre belirlenir. İptal edilmiş kayıt saati engellemez; başka iptal edilmemiş kayıt varsa saat uygun sayılmaz. |
| [AC-03](../../docs/04-kabul-kriterleri.md) | Onaylanan iptalde kayıt silinmez, İptal edildi durumuyla listede kalır. Koşullar uygunsa saat yeniden Uygun görünür. |
| [ALT-01](../../docs/04-kabul-kriterleri.md) | Onay penceresindeki İptal seçeneği işlemden vazgeçirir; Bekliyor durumu ve saat korunur. |
| [H3-AC01–H3-AC05](../../hafta-03/docs/04-kabul-ve-dod.md) | İptal koşulları, Tamamlandı sınırı ve onay seçeneklerinin açıklaması korunur. İptalde toplam kayıt sayısı değişmez. |

Bu kaynaklardaki eski gözlemler yeniden çalıştırılmış test sonucu değildir.
Aşağıdaki değerlendirme kaynak kodun okunmasına ve mevcut belgelere dayanır.

## Mevcut kod ile öneri arasındaki fark

**Mevcut durum:** Arayüz, iş kuralları ve kayıt işlemleri aynı [index.html](../../index.html)
içindedir. `cancelAppointment` kaydı bulur, `canCancel` ile koşulu denetler,
`window.confirm` ile onay sorar, durumu değiştirir, `saveData` ve `render` çağırır;
son olarak `notify` ile mesaj verir. `saveData` da `renderStorage` çağırarak ekrana
ulaşır. Dolayısıyla bugün üç bağımsız bileşen oluşturulmuş değildir.

**Seçilen tasarım:** Aynı tarayıcı uygulamasında üç sorumluluğun sınırını belirliyoruz.
Arayüz kullanıcıyla konuşacak; iş kuralları işlemin uygunluğunu ve sonucunu
belirleyecek; veri erişimi okuma ve saklamayı yürütecek. Okların gösterdiği çağrı
ve sonuçlar henüz uygulanmış bir API değildir. Beşinci basamakta bu yapıyı
seçtik; gerekçesi aşağıdadır. Koda aktarım beşinci haftanın çalışmasıdır.

## Sorumlulukların ayrılması

| Sorumluluk | Bu senaryoda ne yapar? | Neyi başka bileşene bırakır? |
|---|---|---|
| **Arayüz** | Rol/hasta seçimini ve randevu kimliğini alır. Uygunluk sonucuna göre işlemi gösterir, onayı sorar. Vazgeçmede değişiklik isteği göndermez. Sonuca göre listeyi, saati, izin verilen toplamları ve kaydetme durumunu gösterir. | İptal yetkisini ve durum geçişini kendisi kararlaştırmaz; doğrudan kayıt değiştirmez veya localStorage yazmaz. |
| **İş kuralları / randevu işlemleri** | Kaydı veri erişiminden ister. Kayıt var mı, rol Hasta mı, kayıt seçili hastanın mı ve Bekliyor mu denetler. Onaylı istekte koşulları yeniden kontrol eder; uygunsa Bekliyor → İptal edildi değişimini hazırlar ve saklama ister. BR-01'e göre saat durumunu, liste kapsamını ve ilgili sayıları hesaplar. | Onay penceresi açmaz, DOM çizmez; localStorage ayrıntısını bilmez. Kaydetmenin kalıcılık sonucunu veri erişiminden alır. |
| **Veri erişimi** | Randevu verisini okur; onaylanmış değişikliği oturum verisine uygular ve mümkünse tarayıcının localStorage alanına yazar. Okuma/yazma ve kalıcılık durumunu döndürür. | Kimin iptal edebileceğine karar vermez; onay veya bildirim göstermez, saat uygunluğu kuralını belirlemez. |

Buradaki rol ve hasta kimliği eğitim simülasyonundan gelir. Bu ayrım gerçek kimlik
doğrulaması veya sunucu tarafında erişim güvenliği sağlamaz.

### Mevcut işlevlerin önerilen karşılıkları

| Bugünkü kod | Önerilen sorumluluk | Ayrılırken dikkat edilecek nokta |
|---|---|---|
| Olay dinleyicisi, `window.confirm`, `notify`, `render*` | Arayüz | İşlem sonucu ve görünüm verisini kullanır. DOM üretirken iş kuralı tekrar yazılmaz. |
| `canCancel`, `cancelAppointment` içindeki koşul ve durum geçişi | İş kuralları | `cancelAppointment` bütünüyle tek kutuya taşınmaz; onay, kayıt ve çizim işleri ayrılır. Düğmenin gizlenmesi tek kontrol değildir. |
| `occupiedAt`, `scopedAppointments`; görünüm işlevlerindeki kapsam, durum ve sayı hesapları | İş kuralları | Saatin doluluğu, hastanın listesi ve doktor/tarih toplamları farklı kapsamlardır. Sonucu arayüz gösterir. |
| `loadData`, `saveData`, bellek içindeki `data` | Veri erişimi | `saveData` içindeki ekran çağrısı ayrılır. Saklama durumu sonuç olarak üst bileşene bildirilir. |
| `validateData` | Veri erişiminde okuma kontrolü ve iş kuralları | Bugünkü işlev hem veri biçimini hem iptal edilmemiş çakışan kayıtları kontrol ediyor. Biçim kontrolü veri erişiminde; BR-01 denetimi ortak iş kuralında kalmalı. |

İş kuralları için veri erişiminden gelen kayıt üzerinde değişiklik hazırlamak,
reddedilen bir istekte paylaşılan kaydı yanlışlıkla değiştirmemelidir. Beşinci
basamakta seçilen erişim sözleşmesi aşağıda açıklanır; kesin dosya adları ve
yükleme düzeni uygulama aşamasında belirlenecektir.

## Bileşen diyagramı ve okların anlamı

![Seçilen tasarım — randevu iptalinde sorumluluk ayrımı](../diagrams/01-bilesen.png)

[Düzenlenebilir çizim](../diagrams/01-bilesen.drawio) ·
[Düzenleme ve kontrol notu](../diagrams/README.md)

| Yön | Taşınan bilgi |
|---|---|
| Arayüz → İş kuralları | Uygunluk sorgusu; onay verilirse randevu kimliği ve simülasyon rol/hasta bilgisiyle iptal isteği. |
| İş kuralları → Arayüz | Uygunluk/ret gerekçesi; işlem sonrası görünüm verisi ve saklamanın kalıcılık durumu. |
| İş kuralları → Veri erişimi | Gerekli kayıtları oku; yalnız geçerli ve onaylı iptal için hazırlanmış değişikliği sakla. |
| Veri erişimi → İş kuralları | Kayıtlar; saklama işleminin sonucu ve kalıcılık bilgisi. |

Düz ok çağrı, kesik ok geri dönen sonuç/veridir. Bunlar aynı uygulamanın içindeki
mantıksal iletişimi gösterir; HTTP, ayrı sunucu veya çoklu cihaz eşzamanlaması
anlamına gelmez. Veri erişiminden arayüze doğrudan çizim çağrısı önerilmiyor.

## Aynı senaryonun üç sonucu

1. **Onay:** Uygunluk denetlenir, arayüz onay sorar. Onaylı istek iş kurallarında
   yeniden denetlenir. Kayıt silinmeden İptal edildi durumuna geçirilir; saklama
   sonucu alınır. Arayüz güncel listeyi ve BR-01'e göre hesaplanan saati gösterir.
2. **Vazgeçme:** Onay penceresindeki İptal seçilir. Arayüz değişiklik isteği
   göndermez; kayıt Bekliyor ve saat Dolu kalır. Kayıt sayıları değişmez.
3. **Reddedilen istek:** Kayıt yoksa veya rol, sahiplik ya da durum koşulu
   sağlanmıyorsa iş kuralları ret döndürür. Durum değiştirilmez, kaydetme yapılmaz.

Başarılı durum değişiminde yeni kayıt oluşmaz: bekleyen bir azalır, iptal edilen
bir artar; tamamlanan ve toplam kayıt sayısı korunur. Günlük toplamlar mevcut
uygulamada Doktor/Resepsiyon görünümünde gösterilir; Hasta görünümüne yeni toplam
alanı eklemiyoruz. Kontroller farklı rollere geçilerek planlanabilir.

### Saklama sınırı

Bugünkü `saveData` kalıcı yazma başarısız olduğunda `storageAvailable` değerini
kapatır; daha önce yapılmış bellek değişikliğini geri almaz. Öneride de sonuç,
“durum bu oturumda değişti” ile “kalıcı kaydedildi” bilgisini ayırmalı; arayüz
buna göre kaydetme durumunu göstermelidir. Başarısız yazmada otomatik geri alma
veya cihazlar arasında kalıcılık bu çalışmada vaat edilmez.

### Sonraki uygulamada korunacak açıklık

Mevcut onay metni saatin açılmasını “başka iptal edilmemiş kayıt yoksa” koşuluyla
anlatırken son başarı mesajında koşulsuz “İlgili saat yeniden uygun.” yazıyor.
Normal geçerli veri akışı çakışmayı zaten engelliyor; yine de önerilen arayüz
sonuç metnini iş kurallarının hesapladığı gerçek saat durumundan üretmelidir.
Bu basamakta başarı mesajı veya uygulama kodu değiştirilmedi.

## İki mimari seçeneğin karşılaştırılması

**Seçenek A — Mevcut tek dosya ve ortak durumla devam:** `index.html` içindeki
`data`/`state` ve mevcut işlev bağlantıları korunur; yeni işler aynı düzene eklenir.
Bu seçeneğin avantajı, küçük prototipi açmanın ve bütün kodu birlikte görmenin
kolay olmasıdır. Her tek dosyalı programın kötü tasarlandığını söylemiyoruz;
burada karşılaştırdığımız, bizim mevcut kodumuzdaki bağlantılardır.

**Seçenek B — Katmanlı/modüler tek tarayıcı uygulaması:** Arayüz, randevu
işlemleri/kuralları ve veri erişimi belirli işlevler üzerinden haberleşir.
Katmanlar mantıksal sorumluluklardır; üçünün ayrı makinede çalışması gerekmez.
Bu seçim aynı tarayıcıda çalışacak bir yapıdır. [K1, K3]

| Ölçüt | Seçenek A: Mevcut düzen | Seçenek B: Sorumlulukları ayrılmış düzen |
|---|---|---|
| Sorumlulukların açıklığı | `cancelAppointment` onay, kural, durum değişimi, kaydetme ve gösterimi birlikte yürütüyor. | Onay/gösterim arayüzde; karar randevu işlemlerinde; saklama veri erişiminde. |
| İptal açıklaması değişirse | `cancelAppointment` ve görünüm kodundaki metinler incelenir; bu sırada iş akışıyla aynı bölümde çalışılır. | Metin değişikliği arayüzde ele alınır; mevcut işlem sonuçlarının anlamı korunur. |
| İptal koşulu değişirse | `canCancel` ve onu kullanan görünüm/işlem akışı birlikte kontrol edilir. | Koşul randevu işlemlerinde tek yerde değiştirilir; arayüz aynı uygunluk sonucunu kullanır. Kabul koşulları ve testler yine güncellenir. |
| Kaydetme biçimi değişirse | `saveData`, paylaşılan `data` ve `renderStorage` bağlantısı birlikte incelenir. | Aynı erişim sözleşmesi korunabiliyorsa değişim veri erişiminde tutulabilir. Sözleşme değişirse diğer bileşenler de etkilenebilir. |
| Test edilebilirlik | Dışarıya açılmamış işlevleri, ortak durumu ve ekran çağrılarını ayırmak ek düzenleme gerektiriyor. | Randevu işlemleri, örnek kayıt döndüren bir depo ile DOM ve localStorage olmadan sınanabilir. Tarayıcıdaki bütün akış ayrıca kontrol edilir. |
| Ek kod ve kavram yükü | Yeni bir bağlantı düzeni gerektirmez; başlangıçta daha az hazırlık vardır. | Sözleşme, bileşenleri bağlayan başlangıç kodu ve veri kopyalama kuralları gerekir. |
| Küçük ders projesine uygunluk | Kısa tanıtım ve ilk gözlem için yeterli; sorumluluk sınırlarını uygulayarak öğrenme hedefini sınırlıyor. | Mevcut iptal senaryosuyla sınırlandığında bakım ve kontrol sorumluluklarını görünür kılıyor. |

Bu tablo, kaynak kod üzerinden yaptığımız öğretmen değerlendirmesidir. B seçeneği
için hız, hata azalması veya süre kazancı ölçmedik. Katmanlı düşünmenin genel
modülerlik gerekçesi K1'de; tabloya özgü sonuçlar bu proje için yorumumuzdur.

## Mimari karar ve gerekçesi

**H4-MK-01: Seçenek B ile devam edeceğiz.** Mevcut davranışları koruyup iptal
akışındaki sorumlulukları ayıracağız. Üç somut gerekçemiz var:

1. Üçüncü hafta onay metnini değiştirirken durum değiştiren işlevin içinde
   çalıştık. Metin ve karar sorumluluklarını ayırmak sonraki incelemeyi kolaylaştırır.
2. `saveData` bugün `renderStorage` çağırıyor. Kaydetme sonucunu veri olarak
   döndürmek, saklama kodunun ekranı tanımasına duyulan ihtiyacı kaldırır.
3. FR-03 ve BR-01 kurallarını kontrollü örneklerle sınamak istiyoruz. İş kurallarını
   tarayıcı ekranından bağımsız çağırabilmek bu hedefe uygundur.

Ödediğimiz bedel, birkaç yeni işlev sınırı ve bunları bağlayan kodun anlaşılmasıdır.
Aynı kodu üç dosyaya bölmek tek başına yeterli olmaz: arayüz doğrudan kayıt
değiştirmemeli, veri erişimi ekran çizmemeli, iş kuralları onay penceresi açmamalıdır.

Bu kararı geçersiz kılabilecek yeni koşullar; gerçek hesap girişi, ortak sunucu
verisi veya eşzamanlı cihaz kullanımıdır. Böyle bir ihtiyaç doğarsa mimariyi
ve güvenlik gereksinimlerini yeniden değerlendiririz. Bugünkü ayrımı yapmak,
bu ihtiyaçları çözmüş olmak anlamına gelmez.

## Tasarım kalıbı: Repository — Randevu Deposu

**Kalıbın fikri:** Uygulama, saklama ayrıntılarına doğrudan ulaşmak yerine kayıtları
bir koleksiyon gibi sunan erişim noktasıyla çalışır. Repository, veri erişimi
kalıbıdır. Kaynaktaki kapsamlı nesne/veritabanı eşleme yapısını bu küçük derse
taşımıyoruz; koleksiyon benzeri erişim sınırını uyarlıyoruz. [K2]

Buradaki “depo”, randevu kayıtlarını bulan ve güncelleyen yazılım bileşenidir;
GitHub'daki proje deposuyla karıştırılmamalıdır. Diyagramdaki üçüncü kutu bu
sorumluluğu üstlenir; dördüncü bir katman eklemiyoruz.

**Çözmek istediğimiz somut sorun:** İptal işlevi bugün `data.appointments` dizisine
doğrudan erişiyor ve `saveData` çağırıyor. Randevu işlemlerine küçük bir depo
nesnesi vererek kayıt arama ve saklama ayrıntılarını bu nesnenin içinde tutacağız.
Gerçek kullanımda tarayıcı deposu, kontrollü denemede aynı işlemleri sağlayan
bellek deposu kullanılabilir. Ayrı bir kütüphane veya sınıf hiyerarşisi gerekmiyor.

### İptal senaryosu için planlanan küçük sözleşme

Aşağıdaki adlar tasarım örneğidir; henüz çalışan kod değildir. Sözleşme bugünkü
tek sayfalı, eşzamanlı tarayıcı akışı içindir.

| İşlem | Beklenen sonuç | Sınır |
|---|---|---|
| `findById(id)` | Kaydın bağımsız kopyası veya bulunamadı sonucu. | Kopyayı değiştirmek saklanan kaydı kendiliğinden değiştirmez. |
| `list()` | Randevu kayıtlarının bağımsız kopyaları. | Hasta/rol görünürlüğünü, BR-01 saat sonucunu ve toplamları iş kuralları hesaplar. |
| `update(appointment)` | Var olan kaydı günceller; değişimin uygulanıp uygulanmadığını ve kalıcı mı yalnız bellekte mi olduğunu döndürür. | Yeni kayıt oluşturmaz, kayıt silmez, iptal yetkisine karar vermez. Bulunmayan kimlikte değişiklik yapmaz. |

Başarılı bellek güncellemesi ile kalıcı yazma ayrı sonuçlardır. Kalıcı yazma
başarısızsa mevcut uygulamadaki gibi bellek değişimi kalabilir; arayüz bunu
saklama durumunda gösterir. `update` sonucunu yalnız “başarılı/başarısız” diye
tek değere indirip bu ayrımı kaybetmeyeceğiz.

`localStorage` anahtarı `ygs-klinik-randevu-demo-v1`, `schema: 1`, `nextId` ve mevcut
randevu alanları korunacak. İptal güncellemesi `nextId` üretmez veya artırmaz.
Mevcut kayıtların yalnız uygulama dosyalarını kopyalayarak başka konuma taşınmış
sayılmaması gerektiği [başlangıç belgesinde](00-baslangic-ve-surum.md) açıklanır.

| Değerlendirme | Bu projedeki karşılığı |
|---|---|
| Beklenen yarar | İptal işlevi kaydın nasıl saklandığını bilmeden kayıt bulabilir ve güncelleme isteyebilir. Aynı sözleşmeye uyan deneme deposu ile kontrollü sonuç üretilebilir. |
| Ek maliyet | Üç erişim işlemi, kopya kayıtlar, saklama sonucu ve başlangıçta bileşenleri bağlayan kod hazırlanır. İşlem adları ve sonuçları tutarlı tutulur. |
| Risk | Aynı anda hem depo hem doğrudan `data` erişimi kullanılırsa iki ayrı yazma yolu oluşur. Kalıp adı verilmesi bu sorunu kendiliğinden çözmez. |
| Kullanma kararı | İptal akışı için sınırlı bir Repository uyarlaması kullanılacak. Somut yarar bağımsız kural kontrolüdür; bütün proje için genel amaçlı bir depo altyapısı kurulmayacak. |
| Yeniden değerlendirme | Sözleşme yalnız çağrı aktarıp anlamlı bir sınır sağlamıyorsa sadeleştirilecek. Uzak sunucu, asenkron işlem veya yeni veri gereksinimi gelirse sözleşme yeniden ele alınacak. |

Bu yararlar tasarım beklentisidir; yeni kod ve testlerle henüz doğrulanmadı.
Kalıp kullanmak bir amaç değildir. Bu örnekte onu, iptal kuralı ile tarayıcıda
saklama ayrıntısı arasında somut bir sınır oluşturduğu için seçiyoruz.

## Beşinci haftada koda aktarılacak sınırlar

| Alan | Uygulama sınırı | Kontrol edilecek sonuç |
|---|---|---|
| Arayüz | Olaylar, onay metni ve ekrana çizim burada kalır; randevu işlemlerinin sonucunu kullanır. | Onay, vazgeçme, liste, saat ve kaydetme bildirimi tutarlı görünür. |
| Randevu işlemleri | Rol, sahiplik, durum geçişi ve BR-01 burada kalır; doğrudan DOM/localStorage erişimi olmaz. | Uygun olmayan istek kayıt değiştirmez; onaylı iptal kayıt silmez. |
| Randevu Deposu | Okuma, kopya kayıt verme, güncelleme ve kalıcılık sonucu burada kalır; ekran çağrısı olmaz. | Reddedilen istekte yazma yapılmaz; yazma hatasının bellek/kalıcılık farkı görünür olur. |
| Başlangıç ve eski veri | Veri erişimi okunabilir veri biçimini kontrol eder. Randevu işlemleri BR-01 bütünlüğünü denetler; başlangıç akışı geçersiz veride mevcut örnek veriye dönüş davranışını sürdürür. | Bir alt bileşen ekranı veya üst iş katmanını doğrudan çağırmaz; eski kayıt biçimi ve açılış mesajları korunur. |
| Oluşturma ve tamamlama | İptal için aynı kayıtların ikinci bir kopyasını yöneten ayrı bir veri kaynağı oluşturulmaz. Diğer işlemler de aynı güncel veriyi görür. | İptal sonrası oluşturma/tamamlama eski veriyi yazıp değişikliği kaybettirmez. |

Kesin dosya adları ve tarayıcıda yükleme yöntemi beşinci haftanın uygulama
başlangıcında belirlenecek. Uygulamayı açma biçimi değişirse yönerge de
güncellenecek. Bu basamakta yeni JavaScript dosyası veya yeni özellik eklenmedi.

Koda aktarıldığında AC-03, ALT-01 ve H3 kabul koşulları yeniden kontrol edilecek;
rol/sahiplik/durum reddi, yazma hatası ve diğer randevu işlemleriyle veri tutarlılığı
ayrıca sınanacak. Bunlar yapılmış test sonucu değildir. Altıncı basamakta bu
sınırları görev, süre ve bağımlılıklara dönüştüreceğiz.

## Öğrencinin kararı anlatma örneği

> Mevcut uygulamamızda iptal işlevi hem onay soruyor hem kaydı değiştiriyor hem
> ekranı yeniliyor. Bu işleri üç sorumluluğa ayırmayı seçtik. Randevu Deposu
> kaydı bulacak ve değişikliği saklayacak; kimin iptal edebileceğine iş kuralları
> karar verecek. Böylece kuralları kontrollü verilerle inceleyebileceğiz. Bunun
> karşılığında bileşenleri bağlayan ek kod yazacağız. Bu hafta kararı verdik;
> uygulamayı henüz bu yapıya dönüştürmedik.

Öğrenci kendi projesinden bir değişiklik seçip hangi bileşenlerin etkileneceğini
anlatmalı; öğretmenin kararını gerekçesiz kopyalamamalıdır.

## Kavram kaynakları

Kaynaklar kavramları destekler; Klinik Randevu'ya ilişkin tercih ve sözleşme
bu ders için oluşturduğumuz öğretmen yorumudur. Erişim: 1 Kasım 2026.

- **K1:** Martin Fowler, [Presentation Domain Data Layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html). Sunum, iş mantığı ve veri erişimini ayırma; küçük programlarda modülerlik ve test sınırları.
- **K2:** Edward Hieatt ve Rob Mee, [Repository — Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/repository.html). Koleksiyon benzeri veri erişim sınırı. Buradaki küçük uyarlama kaynağın tam altyapı örneği değildir.
- **K3:** Microsoft Learn, [N-tier architecture style](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier). Mantıksal katman ile fiziksel dağıtım katmanı ayrımı. Azure dağıtımı bu projenin kapsamına alınmadı.

## Kontrol

- [x] Diyagramdaki sorumluluklar FR-03, BR-01, AC-03 ve ALT-01 ile karşılaştırıldı.
- [x] Çağrı ve sonuç oklarının yönleri ve taşıdığı bilgi açıklandı.
- [x] Mevcut tek dosya ile önerilen sorumluluk ayrımı ayrı belirtildi.
- [x] `.drawio` XML yapısı ve bağlantı uçları okunarak kontrol edildi; PNG görsel olarak incelendi.
- [ ] diagrams.net arayüzünde açma/düzenleme kontrolü ve yazardan farklı kişinin incelemesi.
- [x] İki mimari seçenek aynı ölçütlerle karşılaştırıldı; seçim gerekçelendirildi.
- [x] Repository uyarlamasının sorunu, yararı, maliyeti ve kullanma kararı açıklandı.
- [x] Beşinci hafta uygulama sınırları ve yapılacak kontroller belirtildi.
- [ ] Seçilen tasarımın kodda uygulanması ve davranış kontrolleri — henüz yapılmadı.

Hazırlık: Öğretmen için kaynak kod ve önceki belgelerden oluşturulmuş örnek.
Bağımsız inceleyen / geri bildirim: Henüz yok;
[04-inceleme-ve-teslim.md](04-inceleme-ve-teslim.md) üzerinden izlenecek.
Uygulamanın T01–T06 davranış testleri bu basamakta yeniden çalıştırılmadı.

Öğrenciler [boş 02 şablonunu](../sablonlar/02-mimari-karar.md) kendi gruplarında
kullanır ve kendi diyagramlarını üretir. Açıklamaları aynen kopyalamak yerine
her okun hangi bilgiyi taşıdığını ve hangi bileşenin durum değişikliğine karar
verdiğini kendi örnekleri üzerinden anlatır.
