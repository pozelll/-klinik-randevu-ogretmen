# 4. hafta — Yaşam döngüsü ve geliştirme yaklaşımı seçimi

Tarih: 1 Kasım 2026

Durum: Doldurulmuş öğretmen örneği; bağımsız ekip incelemesi bekliyor.

Çalışma: Klinik Randevu — üçüncü basamak

İncelenen uygulama başlangıcı: `da3ce51798344a6fafaee89cce42aa9aba90de17`

## Bu basamakta neye karar veriyoruz?

Klinik Randevu projesini **kısa geri bildirim döngüleriyle, küçük artımlar halinde
ilerleten çevik bir çalışma düzeniyle** sürdüreceğiz. Seçimimiz ders projesinin
mevcut koşullarına dayanır; her proje için geçerli tek doğru yöntem iddiası değildir.

Burada “artırımlı” ve “çevik” birbirini dışlayan seçenekler değildir. Artırımlı
geliştirme, ürüne kullanılabilir parçalar ekleme biçimini; çevik yaklaşım,
öğrendiklerimize göre işbirliği içinde yönümüzü ayarlamayı anlatır. Yinelemeli
çalışmada önceki çözümü gözden geçirip iyileştiririz. Scrum, bu fikirleri kullanan
belirli bir çerçevedir; çevik kavramıyla eş anlamlı değildir. [K2–K4]

Üçüncü haftadaki çalışma, Scrum kavramlarından yararlanan bir ders alıştırmasıdır.
Yalnız Sprint ve iş listesi adlarını kullanmış olmamız, eksiksiz bir Scrum
uygulaması gerçekleştirdiğimizi göstermez.

## 1. Önceki dosyalardan ne öğrendik?

Aşağıdaki bağlantılar, bu dosyanın bulunduğu klasörden ilgili belgelere gider.

| Projemizdeki durum | Dayanak | Seçimimize etkisi |
|---|---|---|
| Çalışan bir başlangıç uygulamamız var. Saatleri gösterme, randevu oluşturma, iptal, günlük liste, tamamlama ve toplamlar aynı örnekte inceleniyor. | [Vizyon ve kapsam](../../docs/01-vizyon-kapsam.md), [FR-01–FR-06 ve BR-01](../../docs/03-gereksinimler.md) | Mevcut uygulamayı koruyarak küçük bir ihtiyacı seçip sonucunu gözleyebiliriz. |
| İptali onaylamak ile işlemden vazgeçmek arasındaki farkın açıklanmasına ihtiyaç duyulmuş. | [H3 başlangıç gözlemi](../../hafta-03/docs/02-gozlem.md), [iş listesi](../../hafta-03/docs/03-product-backlog.md) | Tüm ürünü yeniden yazmak yerine aynı kullanıcı sorununa odaklanan iki küçük iyileştirmeyi ele alabiliriz. |
| Derste verilen yeni bilgi, Tamamlandı sınırının ana açıklamada da yazılmasını istemiş. | [Değişiklik kartı](../../hafta-03/docs/06-degisiklik-karti.md) | İlk tahmini koruyup değişikliğin kapsam ve kapasite etkisini değerlendirmemiz gerekiyor. |
| Aynı kapsamın tahmini kapasiteyi aşınca H3-03 ertelenmiş; H3-01 ve H3-02 korunmuş. | [İlk ve güncel plan](../../hafta-03/docs/05-sprint-plani.md) | Hedefi koruyarak kapsamı yeniden seçmek, bu projenin çalışma biçimine uyuyor. |
| T01–T06 için sonuçlar kaydedilmiş; bağımsız inceleme ve bazı kalite ölçümleri ayrı tutulmuş. | [Test kaydı](../../hafta-03/docs/08-test-kaydi.md), [Bitti Tanımı](../../hafta-03/docs/04-kabul-ve-dod.md) | Küçük değişiklikten sonra kontrol yapacağız; yalnız kod yazıldığı için işi bitmiş saymayacağız. |
| Başlangıç prototipinde sunucu, ortak veritabanı, gerçek hesap girişi ve SMS bulunmuyor. | [Kapsam dışı işler](../../docs/01-vizyon-kapsam.md) | Aday fikirleri doğrudan bu haftanın teslimine katmayacağız; önce ihtiyaç ve bağımlılıklarını inceleyeceğiz. |

Değişiklik kartı bir eğitim senaryosudur. Gerçek klinik görüşmesi veya kullanıcı
şikâyeti olarak sunulmaz. Eski belgelerdeki ilerleme ifadeleri yazıldıkları anı
yansıtır; güncel başlangıç sürümü [00 belgesinde](00-baslangic-ve-surum.md) kayıtlıdır.

## 2. Üç yaklaşımı karşılaştırma

Bu tablo temel eğilimleri karşılaştırır. Uygulamada bir proje farklı yaklaşımları
birleştirebilir; seçimi gerekçelendirmek gerekir. [K1–K4]

| Ölçüt | Şelale ağırlıklı düzen | Artırımlı geliştirme | Çevik çalışma |
|---|---|---|---|
| İşlerin düzeni | Gereksinim, tasarım, uygulama ve kontrol aşamaları sırayla ilerler. | Her geliştirme parçası öncekinin üzerine yetenek ekler. | Kısa döngülerde sonucu değerlendirip planı uyarlarız. |
| Yeni gereksinim | Önceki kararlar ve değişiklik etkisi yeniden değerlendirilir. | İlgili veya sonraki parçanın kapsamı gözden geçirilir. | Öncelik ve kapsam, hedef ve kapasiteyle birlikte yeniden ele alınır. |
| Geri bildirim | Belge ve aşama gözden geçirmelerinde alınabilir. | Her kullanılabilir parçanın ardından alınabilir. | Geliştirme boyunca düzenli işbirliği ve geri bildirim amaçlanır. |
| İlk kullanılabilir sonuç | Genellikle ana geliştirme ve bütünleştirme sonrasında ortaya çıkar. | Bütün kapsam bitmeden bir parça kullanılabilir. | Erken kullanılabilir sonuçlarla öğrenme amaçlanır. |
| Dikkat edilecek nokta | Geç keşfedilen ihtiyaçlar önceki aşamalarda yeniden çalışma doğurabilir. | Parçalar birbiriyle uyumlu olmalı; her parçanın kontrolü yapılmalı. | Sürekli değişiklik, odak ve kalite koşullarını aşındırmamalı. |

Şelalede değişiklik “yasak” değildir. Çevik çalışmada plan ve belge “gereksiz”
değildir. Artırımlı geliştirme de ürünü rastgele dosyalara bölmek değildir. [K1–K3]

## 3. Aynı Klinik Randevu örneğinde nasıl görünürdü?

Aşağıdaki örnekler yaklaşımları öğretmek için yapılmış karşılaştırmalardır;
uygulanmış üç ayrı proje veya ölçülmüş başarı sonucu değildir.

| Yaklaşım | İptal açıklığını iyileştirme işini nasıl ele alabilirdik? |
|---|---|
| Şelale ağırlıklı | İptal koşullarını ve metinleri önce ayrıntılı tanımlar, tasarımı gözden geçirir, sonra uygular ve kontrol ederdik. Tamamlandı cümlesi sonradan gelirse ilgili gereksinim, tasarım ve test kayıtlarını etkisiyle birlikte değiştirirdik. |
| Artırımlı | Çalışan uygulamaya iptal açıklığı gibi sınırlı bir yetenek ekler; açıklama, onay metni ve mevcut davranışların birlikte çalışmasını kontrol ederdik. Saat yardımı ayrı bir sonraki geliştirme parçası olabilirdi. |
| Çevik | Önce hangi kullanıcı sorununu çözeceğimizi belirlerdik. Yeni bilgi gelince hedefi koruyarak kapsamı yeniden seçer, sonucu inceleyip sonraki işlere karar verirdik. Küçük artımlar bu düzenin içinde kullanılabilirdi. |

Bu projenin mevcut koşullarında üçüncü sütundaki çalışma düzenini ve küçük
artımlarla ilerleme biçimini birlikte seçiyoruz.

## 4. Seçimimizin somut gerekçesi: 8 → 9 → 6

Bu sayılar üçüncü haftanın öğretim için verilmiş göreli tahminleridir.
Saat, dakika, öğrenci notu veya ölçülmüş ekip hızı değildir.

| Aşama | İş seçimi ve hesap | Ne anlama geliyor? |
|---|---|---|
| İlk plan | H3-01: 2 + H3-02: 3 + H3-03: 3 = **8 puan** | Verilen 8 puanlık kapasiteye eşitti. |
| Yeni bilgiyle aynı kapsam | H3-01: 3 + H3-02: 3 + H3-03: 3 = **9 puan** | Aynı işler artık varsayılan kapasiteyi 1 puan aşıyordu. |
| Güncel seçim | H3-01: 3 + H3-02: 3 = **6 puan** | İptal açıklığı hedefi korundu; saat seçimi yardımı H3-03 ertelendi. |
| Ayrılmamış kapasite | 8 − 6 = **2 puan** | 3 puanlık ertelenen işi bu alana sığmış sayamayız. |

**Birinci gerekçe — yeni bilgiye göre uyarlama:** Tamamlandı sınırının açık
yazılması işi genişletmiş. İlk planı silmeden yeni kapsamı hesaplayıp daha az
öncelikli işi ertelemişiz. Çalışma düzenimiz bu tür öğrenmeyi görünür kılmalı.

**İkinci gerekçe — kullanılabilir bir başlangıcın bulunması:** Zaten çalışan
randevu akışında bir açıklamayı iyileştirebiliyoruz. Böylece küçük bir değişikliğin
öncesini ve sonrasını karşılaştırabiliriz.

**Üçüncü gerekçe — sınırlı ders kapasitesi:** Her aday fikri aynı anda yapmak
yerine ortak kullanıcı hedefi etrafında iş seçmek gerekiyor. SMS ve randevu taşıma
gibi adaylar, iş listesinde bulunmaları nedeniyle otomatik olarak seçilmiş olmaz.

Bu gerekçeler proje kayıtlarından çıkardığımız öğretmen değerlendirmesidir;
yaklaşımın daha hızlı veya daha başarılı olduğunu gösteren karşılaştırmalı deney değildir.

## 5. Seçimin zayıf yönlerini nasıl yöneteceğiz?

| Olası sorun | Bu projede uygulayacağımız karşılık |
|---|---|
| Her yeni fikir kapsamı büyütür. | Önce hedefle ilişkisini, kapasiteyi ve bağımlılıklarını yazacağız; ertelenen işi açıkça kaydedeceğiz. |
| Küçük değişiklikler birbirinden kopar. | Dördüncü basamakta bileşen sorumluluklarını, beşinci basamakta ortak mimari kararı açıklayacağız. |
| Plan sürekli değiştiği için eski karar kaybolur. | İlk planı saklayıp yeni tahmini ve değişiklik gerekçesini ayrıca yazacağız. |
| “Çalışıyor” denilerek kalite kontrolü atlanır. | Kabul koşullarını, test kaydını ve yazardan farklı kişinin incelemesini ortak tamamlanma koşullarında tutacağız. |
| Sınıf içi görüş gerçek kullanıcı doğrulaması sayılır. | Görüşün öğretmen, öğrenci canlandırması veya gerçek paydaş kaynağını açıkça belirteceğiz. Yapılmayan ölçümü yapılmış yazmayacağız. |

Çevik yaklaşım kaliteyi düşürme gerekçesi değildir. Scrum bağlamında bir işin
kullanılabilir Increment sayılması, Definition of Done koşullarını karşılamasına
bağlıdır. Bizim dersimizdeki PR ve inceleme gereklilikleri de belirlediğimiz
tamamlanma koşullarının parçasıdır; her Scrum ekibi için aynı araç zorunluluğu
olduğu anlamına gelmez. [K4]

## 6. Başka bir yaklaşım ne zaman daha uygun olabilir?

Kapsamı ve kabul ölçütleri baştan ayrıntılı tanımlanmış, değişiklik olasılığı düşük,
aşama teslimleri açık bir çalışma için daha öngörücü bir düzeni tercih edebilirdik.
Örneğin özellikleri onaylanmış sabit bir veri aktarımı işini planlarken bu seçeneği
karşılaştırırdık. Bu bir öğretim örneğidir; böyle bir işin mutlaka şelale ile
yapılması gerektiği anlamına gelmez.

Klinik Randevu'da ise açık kapsam soruları ve ders boyunca verilecek yeni bilgiler
var. Bu nedenle mevcut seçimimizi geri bildirim ve kapsam uyarlaması üzerine kuruyoruz.
Gerçek hastane ürünü aşamasına geçilirse güvenlik, paydaş, mevzuat ve işletim
gereksinimleri ayrıca değerlendirilir; eğitim prototipinin sınırları ürün güvencesi
olarak kullanılamaz.

## 7. Öğrenci bu kararı nasıl açıklayacak?

Kendi cümleleriyle şu üç soruya yanıt verebilmeli:

1. Önceki hafta hangi yeni bilgi planı değiştirdi?
2. H3-03'ü ertelemek kullanıcı hedefini neden bozmadı?
3. Bir işi kodlamak, hangi eksikler varken onu tamamlanmış yapmaz?

Öğretmenin kısa anlatım örneği:

> Başlangıçta üç işe yer ayırmıştık. Yeni bilgiyle aynı işlerin toplamı kapasitemizi
> aştı. Amacımız iptal koşulunu ve onay seçeneklerini anlaşılır kılmaktı. Bu nedenle
> hedefe doğrudan hizmet eden iki işi koruduk, saat yardımını erteledik. Testi veya
> incelemeyi kaldırmadık. Dördüncü haftada da aynı uygulamayı inceleyip tasarım ve
> plan kararlarımızı gerekçeleriyle ilerleteceğiz.

Öğrenciler [boş seçim şablonunu](../sablonlar/01-yasam-dongusu-secimi.md) kendi
gruplarında doldurur. Bu öğretmen örneği öğrencinin gerçek gözlemi, toplantısı veya
bireysel yanıtı yerine kullanılmaz.

## 8. Kontrol ve sonraki adım

- [x] Üç yaklaşım karşılaştırıldı; artırımlı ve çevik çalışmanın birlikte kullanılabileceği açıklandı.
- [x] Seçim, önceki proje belgeleri ve değişiklik hesabıyla gerekçelendirildi.
- [x] İlk tahmin, yeni tahmin ve güncel kapsam birbirinden ayrıldı.
- [x] Yaklaşımın sınırlılıkları ve alternatif koşullar yazıldı.
- [ ] Yazardan farklı ekip üyesinin incelemesi ve geri bildirimi alındı.

Hazırlama desteği: ChatGPT; mevcut öğretmen proje kayıtları üzerinden oluşturulan çalışma metni.

Bağımsız inceleyen / görüşme katılımcısı: Henüz kaydedilmedi. Gerçek değerlendirme
[04-inceleme-ve-teslim.md](04-inceleme-ve-teslim.md) üzerinden izlenecek.

Bu adımda kod değişmedi ve uygulama testleri yeniden çalıştırılmadı.

Bu basamağı izleyen sorumluluk ayrımı ve bileşen diyagramı
[02-mimari-karar.md](02-mimari-karar.md) dosyasında yer alır.

## Kavram kaynakları

1 Kasım 2026'da erişilen kaynaklar. Genel kavramları destekler; Klinik Randevu için
seçim ve örnekler yukarıdaki proje kayıtlarına dayanan öğretim değerlendirmesidir.

- **K1:** NASA Software Engineering Handbook, SWE-019, “Software Life Cycle”, Ver B rehberi; özellikle standart şelale ve artırımlı yaşam döngüleri. [Kaynak](https://swehb.nasa.gov/spaces/SWEHBVB/pages/32604451/SWE-019%2B-%2BSoftware%2BLife%2BCycle). Kavramsal başvuru olarak kullanıldı; NASA proje kuralları bu derse zorunluluk olarak aktarılmadı.
- **K2:** [Çevik Yazılım Geliştirme Manifestosu — Türkçe](https://agilemanifesto.org/iso/tr/manifesto.html).
- **K3:** [Çevik Bildirinin Temelindeki İlkeler — Türkçe](https://agilemanifesto.org/iso/tr/principles.html).
- **K4:** [The 2020 Scrum Guide](https://scrumguides.org/scrum-guide.html), Scrum Theory, Increment ve Definition of Done bölümleri.
