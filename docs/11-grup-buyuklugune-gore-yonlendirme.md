# Grup büyüklüğüne göre çalışma ve inceleme

22 Kasım 2026 öğrenci yönlendirmesi. Sınıfta toplam 19 öğrenciden oluşan altı grup vardır: iki grup iki kişilik, bir grup üç kişilik, üç grup dört kişiliktir. Haftalık işler bu gerçek büyüklüklere göre paylaşılır. Öğretmen örneğindeki dört kişilik U1–U4 planı bütün gruplara aynen atanmaz.

Bu belge ortak çalışma yöntemini açıklar. Gerçek görev sahipleri, GitHub hesapları ve kendi depo bağlantıları grubun çalışma kaydında tutulur. Bu ortak öğretmen deposunda kişiler yerine Üye 1, Üye 2 gibi rol adları kullanılır. Aşağıdaki dağılımlar öneridir; yapılmış katkı, onay veya sabit kişi ataması değildir.

## Her üyenin anlamlı katkısı

Her öğrenci bir ihtiyacı, dosyayı, davranışı veya doğrulama işini sahiplenir; ne yaptığını açıklayabileceği gerçek bir çıktı üretir. Bu çıktı gereksinim ve kabul koşulu, küçük kod değişikliği, düzenlenebilir mimari çizim, hesaplanmış plan, yürütülmüş test veya gerekçeli inceleme kaydı olabilir. Yalnız adını yazmak veya biçim değişikliğiyle commit sayısını artırmak katkının kanıtı değildir.

İşe başlamadan görev sahibi, incelenecek kapsam, beklenen çıktı ve kontrol eden belirlenir. İş bittikten sonra dosya, commit, test veya inceleme bağlantısı ve gerçek sonuç kaydedilir. Birlikte yazılan bölümün bütün yazarları belirtilir. Haftalar arasında görevler değiştirilir; aynı kişi sürekli yalnız dosya yükleyen veya yalnız izleyen rolde kalmaz.

## İki kişilik grup

Üye 1 ile Üye 2 küçük işleri paylaşır. Örneğin biri kullanıcı hedefini ve bir uygulama değişikliğini, diğeri ayrı bir kabul senaryosunu ve başka bir değişikliği hazırlayabilir. Her öğrenci yazmadığı veya birlikte yazmadığı parçayı inceleyebilir. İnceleme, yalnız gerçekten değerlendirilen dosya ve sürüm için geçerlidir.

İkisinin birlikte yazdığı bölüm için iki üye de bağımsız inceleyen sayılmaz. İkisinin katkı verdiği PR'ın tamamı veya ortak hazırlanan son paket bağımsız olarak değerlendirilecekse başka gruptan bir öğrenci ya da öğretim elemanı belirlenir. Erişim, kapsam ve uygun zaman sağlanana kadar bu inceleme bekliyor olarak kalır. Ortak yazılan testin başka üye tarafından yalnız yeniden çalıştırılması, test tasarımının bağımsız incelemesi değildir.

Aynı öğrenciye iki farklı uygulama işi aynı zaman aralığında atanmaz. Örneğin Üye 1 hem veri erişimini hem iş kurallarını yazacaksa, bu işler sıraya konur ve diğer üyenin arayüz işiyle gerçek bağımlılıkları gösterilir. İnceleme ve düzeltme süresi planın dışına çıkarılmaz.

## Üç kişilik grup

İki üye uygulama işlerini paylaşırken üçüncü üye, yazımına katılmadığı kapsamın incelemesini ve kabul kontrollerini üstlenebilir. Bir öğrenci veri erişimi ile iş kurallarını, diğeri arayüzü üstleniyorsa aynı kişiye düşen işler sıralanır. Üç mantıksal sorumluluk, üç kişinin eşzamanlı kod yazmasını zorunlu kılmaz.

Üçüncü üye de incelenecek belgeyi, kodu veya testi birlikte yazarsa o parçanın inceleyeni yeniden seçilir. Gerekirse grup dışından destek alınır. İnceleyen; tekrar üretim adımları, bulgular, düzeltme sonrası kontrol ve kullandığı commit bilgisiyle somut katkı üretir. Bu görevin kendisi, incelemediği diğer parçaların onayı değildir.

## Dört kişilik grup

Öğretmen örneğine benzeyen bir dağılımda Üye 1 veri erişimini, Üye 2 iş kurallarını, Üye 3 arayüzü, Üye 4 ise yazımına katılmadığı kapsamın incelemesini üstlenebilir. Bu dağılım özellikle beşinci haftadaki uygulama için bir seçenektir; dördüncü haftada hazırlanan belgelerin incelemesi ayrıca planlanır.

Üye 4 bir parçanın yazımına da katılmışsa o parça için başka inceleyen gerekir. Diğer üyeler de birbirlerinin ayrı hazırladığı parçaları inceleyebilir; inceleme kapsamları kayıtta açıkça ayrılır. Öğretmen örneğindeki süreler, dört kişilik bir grubun gerçek çalışma hızını veya müsaitliğini kanıtlamaz.

## İnceleme kaydında bulunması gerekenler

| Alan | Kaydedilecek bilgi |
|---|---|
| İş ve çıktı | Hangi ihtiyaç, dosya veya davranış inceleniyor? |
| Yazarlar | Bu kapsamı kim veya kimler hazırladı? |
| İnceleyen | Bu kapsamın yazımına katılmayan kişi kim? |
| Sürüm | İncelenen tam commit SHA'sı ve PR bağlantısı. |
| Kontrol | İzlenen adımlar, kullanılan örnek veri ve beklenen sonuç. |
| Gerçek sonuç | Bulgu, kontrol edildiği kapsamda bulgu bulunmadığı veya henüz incelenmediği. |
| Düzeltme | Bulgunun düzeltme commit'i ve ilgili yeniden kontrol sonucu. |

Bir PR açmak, otomatik kontrollerin yeşil olması veya teknik olarak merge edilebilmesi gerçek kişi incelemesinin yerine geçmez. Yeni commit ilgili içeriği değiştirirse inceleyen son sürümü de kontrol eder. Birleştirme sonrasında hedef dalın doğru dosyaları içerdiği ve uygulamanın o sürümden açıldığı ayrıca doğrulanır.

## Dördüncü hafta planını kendi grubuna uyarlama

[Öğretmen planındaki](../hafta04/docs/03-is-plani-ve-riskler.md) P0 ve P1, dört kişilik bir örnek ekibin varsayımlarıdır. P0 için 8 saat ve 17 kişi-saat, P1 için 9 saat ve 19 kişi-saat tarihsel öğretim hesabı olarak korunur. Bunlar öğrenci gruplarının tamamlanma süresi veya gerçekleşmiş emeği değildir.

1. Kendi projenizin işlerini ve teslim koşullarını yazın. Her işe gerçek bir sorumlu ve süre tahmini verin. Gerekli öğrenme ve ortam hazırlığını ayrıca hesaba katın.
2. Bir işin hangi iş bittikten sonra başlayabileceğini gösterin. Bütünleştirme, test, yazardan farklı kişi incelemesi, düzeltme ve teslim işlerini plana katın.
3. Her kişinin zaman çizelgesini kontrol edin. Aynı kişiye atanan işler çakışıyorsa bunları sıraya koyun veya kapsamı gerekçesiyle yeniden paylaşın. Gruba kişi eklenmiş gibi davranmayın.
4. Kaynakların uygunluğunu dikkate aldıktan sonra başlangıç, bitiş, toplam net süre ve kritik yolu yeniden hesaplayın. Toplam kişi-saati kişi sayısına bölmek, tek başına projenin bitiş süresini vermez.
5. İlk planı P0 olarak saklayın. [Yeni koşul kartı](../hafta04/kartlar/01-karar-tablosu-ve-kanit.md) gelince P1'i ayrı kaydedin; değişen iş, tahmin, sorumlu ve bitiş etkisini açıklayın. İnceleme veya düzeltme işini silerek yeni işe yer açmayın.
6. Gerçek çalışma başlayınca gerçekleşen süreyi tahminden ayrı kaydedin. Ders araları, dış inceleme bekleme süresi ve net çalışma süresi birbirine karıştırılmamalı.

Üçüncü haftanın göreli iş puanları saat değildir. [Ürün iş listesindeki](../hafta-03/docs/03-product-backlog.md) örnek 8 → 9 → 6 puan kararını kendi grubunuzun kapasitesiyle gerekçelendirin; aynı sayıları otomatik olarak teslim sözüne çevirmeyin.

## NFR ölçümünde ekip sayısı ile katılımcı sayısı

[NFR-01](03-gereksinimler.md) için hedef değişmez: dört farklı gerçek katılımcının en az üçü, iki görevin ikisini de doğru, yardımsız ve her biri en fazla 60 saniyede tamamlamalıdır. İki veya üç kişilik ekip kurulması bu ölçümü iki veya üç katılımcıya indirmez. Aynı kişinin tekrarları yeni katılımcı sayılmaz.

Gerektiğinde farklı gruplardan katılımcı seçilir. Görev metni, başlangıç verisi, uygulama sürümü, önceki deneyim, süre ve yardım ihtiyacı gerçek oturumda kaydedilir. Otomatik test, öğretmen rehberi veya yapılması planlanan deneme, dört kişinin ölçümü yerine sonuç olarak yazılmaz. Diğer NFR hedefleri ve özgün ölçüm yöntemleri de ekip büyüklüğü nedeniyle kendiliğinden değişmez.

## Haftalık kullanım

| Hafta | Grubun kaydedeceği kendi çıktı |
|---|---|
| 3 | Kullanıcı ihtiyacı, seçilen küçük değişiklik, iş listesi, kabul, test ve PR kanıtı. |
| 4 | Yaşam döngüsü ve mimari gerekçesi, düzenlenebilir çizim, P0/P1 planları ve belge incelemesi. |
| 5 | Sorumlulukları ayrılmış kod, gerçek katkılar ve korunmuş davranış kontrolleri. |
| 6 | Karar satırları, test kodu, gerçek yürütüm ve yazardan farklı kişi incelemesi. |
| 7 | Değişikliğin kapsamı, etki değerlendirmesi, uygulama ve regresyon kanıtı. |
| 8 | Doğru sürümden paket, bütünlük ve paket üzerinden kontrol; alıcının gerçek erişim sonucu. |
| 9 | Üyelerin kendi dal katkıları, çakışma gerekçesi, release/hotfix ve sürüm kararı kanıtı. |

Öğretmen sonuçları örnek olarak okunur. Her grup kendi deposunu, gerçek katkısını ve gerçekten yaptığı kontrolleri kaydeder; başlanmayan veya tamamlanmayan işler açık bırakılır.
