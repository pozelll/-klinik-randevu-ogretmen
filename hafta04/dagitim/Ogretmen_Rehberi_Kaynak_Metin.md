# İlk dört hafta
Öğretmen çalışma rehberi

**Neyi, nerede, neden yaptık?**
Dersi yeniden çalışmak, dosyaları sınıfta açıp göstermek ve öğrencilerin sorularını yanıtlamak için açıklamalı rehber.

## Bu rehberi nasıl kullanmalısınız?

Önce ilgili haftanın açıklamasını okuyun. Sonra “Göster” veya “Kaynak” satırındaki dosyayı kendi proje klasörünüzde açın. Öğretmen örneğini öğrencilere gösterdikten sonra aynı gerekçeyi kendi çalışmalarında açıklamalarını isteyin. Hazır örnek, grubun kendi gözlem ve inceleme kaydı yerine geçmez.

| Hafta | Temel soru | Ürettiğimiz çıktı |

| --- | --- | --- |

| 1 | Ne görüyoruz, kimin ihtiyacı var? | Gözlem, kapsam, paydaş ve risk kayıtları |

| 2 | Davranışı nasıl açık ve kontrol edilebilir yazarız? | Gereksinim, kabul koşulu, model ve izlenebilirlik |

| 3 | Küçük bir iyileştirmeyi nasıl planlar ve doğrularız? | İptal açıklığı değişikliği, iş listesi, test ve PR |

| 4 | Bir sonraki uygulamayı nasıl tasarlar ve planlarız? | Mimari karar, sorumluluk diyagramı, ilk/güncel plan |

**Hazırlık tamamlandı; inceleme süreci açık.** İlk dört haftanın öğretmen dosyaları GitHub çalışma dallarında bulunuyor. H4 tasarım ve planlama hazırlığı tamamlandı. Yazardan farklı kişinin incelemesi, önceki PR bağımlılıkları ve main’e birleştirme henüz tamamlanmadı. Beşinci haftanın kod ayrımı uygulanmadı.

Kaynak sürüm: 8b668fbed7e348fc25a7e5ffa6c69d3ae9f14f3b
Hazırlık tarihi: 1 Kasım 2026. İlk iki haftanın kaynak paketi birleşiktir; bu rehber gözlem ve modelleme çalışmalarını iki oturum halinde anlatır.



# Hızlı erişim ve çalışma sırası

| Sayfa | Konu | Derste açılacak yer |

| --- | --- | --- |

| 3-6 | Başlangıç, uygulama ve ilk hafta | index.html; docs/01, 02, 06, 07, 08, 09 |

| 7-10 | Gereksinim, kabul, modeller ve bağlantılar | docs/03, 04, 05; diagrams/ |

| 11 | GitHub kavramları ve mevcut durum | PR #7, #11, #12 |

| 12-17 | Üçüncü hafta: hedef, plan, kod, test, değerlendirme | hafta-03/docs; index.html |

| 18-25 | Dördüncü hafta: sekiz adım, tasarım, hesap, inceleme | hafta04/docs; diagrams; planlar; kartlar |

| 26-28 | Soru-cevap ve sınıf gösterimi | İlgili dosya yolları her yanıtta |

| 29-30 | Dosya bulma dizini ve kaynaklar | Bütün haftaların dosya haritası |

## Bir soruyu cevaplarken üç cümle kurun

1. **Ne?** İptal edilen kayıt silinmiyor; durumu değişiyor.
2. **Neden?** İşlem geçmişi ve sayım tutarlılığı korunuyor.
3. **Nerede gösteririm?** index.html içindeki cancelAppointment ve hafta-03/docs/08-test-kaydi.md içindeki T06 tablosu.

## Durumları karıştırmayın

“Planlandı”, “kodda var”, “denendi”, “inceleyen onayladı” ve “main’e alındı” farklı durumlardır. Eski belgelerin sonundaki “henüz yapılmadı” cümleleri o belgenin tarihli aşamasını anlatabilir. Güncel genel durumu H4’ün 00 ve 04 belgelerinden, kodu doğru daldan kontrol edin. Tarihsel kayıtların yerine yeni bir başarı hikâyesi yazmadık.

Öğrencilerin önceki rehberi 29 Ekim tarihli 33 sayfalık belgedir. Yeni öğrenci PDF’i bu bölümü koruyup H4 yönergelerini ekler. Öğretmen gözlem kimliğiyle öğrenci alıştırma kimliği aynı olsa bile açıklama ve dosya bağlamı esas alınır.



# Başlangıç: hangi dosyadan devam ediyoruz?

Projenin çalışan dosyası kökteki **index.html**. Dördüncü hafta için ikinci bir ana uygulama oluşturmadık. Üçüncü haftanın son sürümünü koruyup yeni tasarım belgelerini hafta04 klasörüne ekledik. Böylece kod değişikliği ile belge hazırlığını ayırt edebiliyoruz.

| Konum | Ne var? | Neden ayrı? |

| --- | --- | --- |

| index.html | Çalışan tek dosyalı eğitim uygulaması | Davranışı göstermek ve küçük metin değişikliği yapmak |

| docs/ ve diagrams/ | İlk iki haftanın belgeleri ve modelleri | İhtiyaç ve kabul dayanağını korumak |

| hafta-03/docs/ | İyileştirme planı, değişiklik, test ve değerlendirme | Üçüncü haftanın çalışmasını ayrı izlemek |

| hafta04/ | Yaklaşım, mimari, plan ve inceleme | Sonraki uygulamanın tasarımını koddan ayırmak |

## Bilgisayarda açma

ZIP’in tamamını çıkarın; ZIP içinden çalışmayın. Kök index.html dosyasını tarayıcıda, .md dosyalarını metin editöründe açın. Dosya uzantılarını görünür yapın: index.html.txt hatalıdır. GitHub’daki kod sayfası uygulamanın canlı ekranı değildir.

## Kopyalamak neden gerekli, neden yeterli değil?

H3 yedeği karşılaştırma noktasıdır. H4 çalışma kopyası üzerinde ilerlerken eski dosyalar korunur. Fakat dosya kopyası tarayıcının localStorage verisini taşımaz. Aynı tarayıcı ve dosya yoluyla çalışın; mevcut deneme verisini sıfırlamayın. Yeni bir deneme kopyası açtıysanız başlangıç verisinin farklı olabileceğini yazın.

Göster: hafta04/docs/00-baslangic-ve-surum.md. H3 başlangıcı: da3ce51798344a6fafaee89cce42aa9aba90de17. Yerel bilgisayarınızdaki dosya yolu ayrıca kaydedilmelidir.



# Uygulamanın çalışma mantığı

| Rol | Yapabildiği işler | Yapamadığı işler |

| --- | --- | --- |

| Hasta | Saat görme, kendi adına oluşturma, kendi Bekliyor kaydını iptal | Başkasının kaydını görme/iptal; tamamlama |

| Resepsiyon | Seçili hasta adına oluşturma; doktor/gün listesi ve toplamlar | İptal veya tamamlama |

| Doktor | Görevli seçili doktorun listesini/toplamlarını görme; Bekliyor kaydı tamamlama | Yeni randevu oluşturma veya iptal |

B1 saatleri, B2 randevu listesini, B3 günlük toplamları gösterir. Hasta B2’de kendi kayıtlarını görür; yetkili günlük liste seçili doktor ve günün bütün örnek hastalarını kapsar. B3, Hasta rolünde gösterilmez. Liste kapsamını ve sayım kapsamını aynı sanmayın.

## Sabit örnek koşul

Başlangıç seçimi Hasta / Ece Yılmaz / Deniz Arı / 12 Kasım 2030’dur. Temiz başlangıçta R001 09:00 Bekliyor, R002 10:00 Bekliyor, R003 11:00 Tamamlandı, R004 13:00 İptal edildi; 09:30 uygundur. Bunlar başlangıç verisidir. Öğretmenin ilerlemiş oturumundaki sayılar aynı değildir; R013 görmek için sıfırlama yapılmaz.

## İki önemli sınır

Rol düğmesi bir simülasyondur; gerçek hesap girişi veya güvenli sunucu yetkilendirmesi değildir. Veriler sentetiktir. Uygulama sunucuya bağlanmaz; izin varsa tarayıcıya kaydeder. Saklama başarısız olursa oturum belleğinde çalışabilir. Başka cihazla ortak veri ve eşzamanlama garantisi yoktur.

Kaynak: README.md, BILINEN_KISITLAR.md; index.html içindeki state, canBook, canCancel, canComplete, renderSummary ve saveData.



# 1. hafta: “Çalıştı” yerine gözlem yazmak

Önce uygulamadaki davranışı gördük; sonra onu belgeye çevirdik. Gözlem, yalnız ekran görüntüsü değildir. Başlangıç koşulu, yapılan eylem ve gerçek sonuç birlikte yazılırsa başka biri deneyi tekrar kurabilir.

| Kayıt alanı | İptalden vazgeçme örneği |

| --- | --- |

| Koşul | Hasta, Ece, Deniz, 12.11.2030; kendi Bekliyor kaydı ve Dolu saat |

| Eylem | Kartta İptal et; açılan pencerede İptal / Cancel |

| Beklenen | Kayıt Bekliyor ve saat Dolu kalır |

| Gerçek sonuç | Gerçekte gördüğünüz kayıt, saat ve varsa sayım |

| Kanıt | Tarih, sürüm, dosya yolu, ekran/mesaj ve deneyen kişi |

## Neden yanlış denemeyi silmedik?

Vazgeçmek isterken pencerede Tamam seçilirse uygulama iptali onaylar. Bu olay “vazgeçme çalışmıyor” kanıtı değildir; yapılan eylem farklıdır. Gerçek iptal kaydını koruduk ve yeni Bekliyor kayıtla ayrı deneme yaptık. Böylece gözlemle yorumu ayırdık. H3’teki açıklık iyileştirmesinin gerekçesi bu karışıklığın öğretimde görünür olmasıydı.

## Göster ve sor

docs/08-prototip-gozlemleri.md dosyasında G-03 kayıtlarını açın. “Beklenen görev neydi, gerçekte hangi düğmeye basıldı?” diye sorun. Ardından başlangıç koşulu kurulmadan test sonucu yazılamayacağını açıklayın.

Kimlik notu: Eski öğrenci rehberindeki G-06 yenileme alıştırmasıdır; öğretmen docs/08 içindeki G-06 resepsiyon karşılaştırmasıdır. Bağlantıyı yalnız G-06 adına göre değil dosya + senaryo açıklamasıyla kurun.



# 1. hafta: ihtiyaç, kapsam ve ekip

Vizyon belgesi “hangi kullanıcıya nasıl fayda?” sorusunu yanıtlar. Kapsam ise bu çalışmanın sınırıdır. “SMS güzel olur” demek SMS’i mevcut ürüne eklemez; bir aday olarak yazılır ve kapsam kararı gerekir.

| Dosya | Ne yazdık? | Neden? |

| --- | --- | --- |

| docs/01 | Problem, vizyon, kapsam içi/dışı | Her öneriyi zorunlu iş sanmamak |

| docs/02 | Paydaş, beklenti, sorular ve senaryo yanıtları | Ekranda görülenle kullanıcı ihtiyacını ayırmak |

| docs/06 | Risk, neden, etki, önlem, sorumlu | Sorunu çıkmadan yönetebilmek |

| docs/07 | Gerçek toplantı, karar, sonraki iş | Kararın kiminle ve neden alındığını izlemek |

| docs/09 | Gerçek üye ve görev dağılımı | Katkıyı ve kontrol sorumluluğunu açık tutmak |

## Aktör, paydaş ve ekip üyesi

Hasta uygulamayla etkileşen aktördür. Öğretmen eğitim çıktılarıyla ilgili bir paydaştır ama randevu uygulamasının bir ekran rolü olmak zorunda değildir. Öğrencinin koordinatör olması da uygulamadaki Doktor rolü değildir. Aynı kişi sınıf senaryosunda farklı bakış açılarını canlandırabilir; bu gerçek hasta görüşmesi sayılmaz.

19 kişilik düzen: G01, G02, G03 beşer; G04 dört kişi. Her grup bütün çıktıları üretir. Dört kişilik grupta görevler birleştirilir; kontrol kaldırılmaz. Kendi yazdığı parçanın bağımsız incelemesini aynı kişi yapmaz.

Göster: docs/01-vizyon-kapsam.md, 02-paydaslar.md, 06-riskler.md, 07-toplanti-notu.md, 09-ekip-rolleri.md.



# 2. hafta: gereksinimi doğru yazmak

Gereksinim düğmenin adı değil, sistemin koşullu davranışıdır. “İptal düğmesi olsun” yerine “Hasta yalnız kendi Bekliyor kaydını onaylayarak iptal edebilmeli” dedik. Bu cümle aktörü, önkoşulu, işlemi ve sonucu sınırlar.

| Kimlik | Davranış | Önemli sınır |

| --- | --- | --- |

| FR-01 | Saatleri listele | Hasta değişince başka hastanın ayırdığı saat boşalmaz |

| FR-02 | Randevu oluştur | Hasta/Resepsiyon; uygun saat; yeni Bekliyor kayıt |

| FR-03 | Kendi kaydını iptal | Hasta + sahiplik + Bekliyor + onay |

| FR-04 | Günlük listeyi göster | Resepsiyon/Doktor; seçili doktor ve tarih |

| FR-05 | Randevuyu tamamla | Doktor; Bekliyor kayıt; saat Kapalı kalır |

| FR-06 | Günlük toplamları göster | Yetkili görünüm; iptal edilen kayıt toplama dahil |

## BR-01 neden ayrı bir iş kuralı?

Aynı doktor + tarih + saat için iptal edilmemiş ikinci kayıt oluşturulamaz. Bekliyor ve Tamamlandı saati kapatır; İptal edildi kaydı tek başına saati kapatmaz. Bu kural oluşturma, saat gösterimi ve iptalin sonucunu birlikte etkiler. Birden fazla gereksinime dokunduğu için ortak kimlikle izlenir.

“İptalden sonra saat her zaman açılır” ifadesi fazla geneldir. Aynı doktor/tarih/saatte başka iptal edilmemiş kayıt yoksa açılır. Normal arayüz zaten çift kaydı engeller; yine de kuralı doğru koşulla tanımlarız.

Göster: docs/03-gereksinimler.md; kodda occupiedAt, bookAppointment ve canCancel. Bunlar istemci tarafındaki eğitim kontrolleridir.



# Kabul koşulu ve kalite hedefi

Kabul koşulu bir gereksinimi belirli başlangıç ve eylemle sınanabilir hale getirir. Beklenen sonuç testten önce yazılır; gözlenen sonuç deneme yapıldıktan sonra eklenir. Bir tabloyu doldurmak test çalıştırmak değildir.

## FR-03 için iki ayrı senaryo

**AC-03:** Verilen kendi Bekliyor kaydım; ne zaman iptali onaylarsam; o zaman kayıt İptal edildi olarak kalır, toplam kayıt değişmez, saat BR-01’e göre belirlenir.
**ALT-01:** Aynı başlangıçta onay penceresinden vazgeçersem; kayıt ve saat değişmeden kalır. Başarılı iptal, başarılı vazgeçmenin kanıtı değildir.

| Kalite hedefi | Ders için önerilen ölçüt | Durum |

| --- | --- | --- |

| NFR-01 kullanılabilirlik | 4 kişiden en az 3’ü iki görevi de doğru, yardımsız ve her görevde en çok 60 saniyede yapar | Ölçülmedi |

| NFR-02 yanıt süresi | En çok 20 kayıt; aynı ortamda 10 doktor değişiminin tümünde B1/B2/B3 doğru ve en çok 1 saniyede güncellenir | Ölçülmedi |

| NFR-03 klavye | Oluşturma, vazgeçme, iptal, tamamlama; görünür odak ve klavye tuzağı olmadan | Ölçülmedi |

Bu eşikler öğretim hedefidir; evrensel standardın zorunlu sayıları değildir. Öğretmenin yönlendirilmiş denemeleri bağımsız kullanılabilirlik ölçümü sayılmaz. “Hızlı görünüyor” ifadesi kronometreli ve koşulları belirli ölçüm yerine geçmez.

Göster: docs/03-gereksinimler.md NFR bölümü ve docs/04-kabul-kriterleri.md. AC-07 çift kayıt engeli, ALT-01 ise vazgeçme alternatifidir.



# Üç diyagram neden birbirinin yerine geçmez?

| Model | Sorduğu soru | Dosya |

| --- | --- | --- |

| Bağlam | Sistemin dışında kim var, hangi bilgi alışverişi var? | diagrams/01-baglam.drawio |

| Kullanım durumu | Hangi aktör hangi kullanıcı amacını yerine getirir? | diagrams/02-kullanim-durumlari.drawio |

| Bileşen / sorumluluk | İçeride hangi parça hangi işi üstlenecek? | hafta04/diagrams/01-bilesen.drawio |

Bağlam çiziminde Hasta, Resepsiyon ve Doktor dışarıda; sistem tek sınır içindedir. Kullanım durumu çiziminde altı amaç sistem sınırının içindedir. Dördüncü haftada ise tek uygulamanın iç sorumluluklarını ayırırız. B1/B2/B3 ekran panellerini dış aktör yapmayız.

## Kullanım durumu bağlantılarını nasıl kontrol ederim?

Hasta: UC-01, UC-02, UC-03. Resepsiyon: UC-01, UC-02, UC-04, UC-06. Doktor: UC-01, UC-04, UC-05, UC-06. Bir rolü bir amaca bağlamak, gereksinim tablosundaki yetkiyle tutarlı olmalıdır. Örneğin Resepsiyona UC-03 iptal bağlantısı eklemek mevcut kapsamı değiştirir.

## Çizim dosyası ile görüntü

PNG kolay okunur ve belgeye konur; .drawio kutu ve okların düzenlenebilir kaynağıdır. İkisini birlikte saklarız. Çizim değişirse PNG de yenilenir. Enter çizimi kaydetmez; metin düzenlemesini bitirip dosyayı ayrıca kaydetmek gerekir. H4 çiziminin XML/PNG kontrolü yapıldı; diagrams.net içinde gerçek düzenleme kontrolü bekliyor.

Göster: kök diagrams klasörü ile hafta04/diagrams klasörünü yan yana açın. Eski modelleri H4 diyagramıyla değiştirmeyin.



# İzlenebilirlik: bir sorudan kanıta gitmek

İzlenebilirlik tablosu “bu değişikliği neden yaptık?” sorusuna tek yerden yanıt buldurur. Kimliklerin amacı metni çoğaltmak değil, bağlantıları korumaktır. Gereksinim değişirse hangi kabul koşulu, test ve görev etkilenecek görebiliriz.

| Halka | FR-03 örneği |

| --- | --- |

| İhtiyaç | Hasta randevusunu anlaşılır biçimde yönetebilsin |

| Gereksinim / model | FR-03; UC-03; BR-01 ile ilişki |

| Kabul koşulu | AC-03 onaylı iptal; ALT-01 vazgeçme |

| İlk gözlem | G-02 iptal; G-03-T3 vazgeçme, öğretmen docs/08 içinde |

| Belgeleme görevi | Öğretmen Issue #3; belge değişikliği PR #7 |

| H3 iyileştirmesi | H3-01 / #8 açıklama; H3-02 / #9 onay metni |

| Yeni kanıt | H3 T01-T06; kapsamları hafta-03/docs/08’de |

| H4 tasarım | H4-MK-01; üç sorumluluk; H4-P0/P1 |

## Sınıfta nasıl gösterilir?

Önce docs/05-izlenebilirlik.md içindeki FR-03 satırını açın. AC-03 ve ALT-01’e, ardından gerçek gözlem dosyasına geçin. “Bu görüntü iki senaryonun ikisini de kanıtlıyor mu?” diye sorun. H3’te kod değişikliğinin ayrı Issue numaralarıyla izlendiğini gösterin.

FR-03, H3-01 ve GitHub #8 farklı kimlik türleridir. Öğrencinin H3-01 görevi kendi deposunda #8 olmak zorunda değildir. Her grup kendi gerçek Issue/PR bağlantısını yazar. Bir bağlantının varlığı işin tamamlandığını göstermez.

Kaynak: docs/05-izlenebilirlik.md, hafta-03/docs/03-product-backlog.md ve 08-test-kaydi.md.



# GitHub: yüklemek, incelemek, birleştirmek

| Kavram | Basit açıklama | Karıştırılmaması gereken |

| --- | --- | --- |

| Depo | Proje dosyaları ve değişiklik geçmişi | Canlı uygulama ekranı değildir |

| Dal | Çalışmanın ayrı ilerleyen sürüm hattı | Klasör adı değildir |

| Commit | Dosya değişikliklerinin kayıt noktası | Tek başına inceleme veya onay değildir |

| Issue / pano | İşin tanımı ve ilerleme takibi | Dosya yüklemek otomatik Issue açmaz |

| PR | Bir daldaki değişikliği hedef dala alma önerisi | Açılması birleştirildi demek değildir |

| Review / merge | İnceleme kararı / hedef dala alma işlemi | Viewed yalnız okuma takibidir |

## Öğretmen deposunun mevcut zinciri

PR #7: docs/izlenebilirlik → main.
PR #11: feat/h3-iptal-acikligi → docs/izlenebilirlik.
PR #12: docs/h4-mimari-plan → feat/h3-iptal-acikligi.
1 Kasım kontrolünde üçü de açıktı; H4 PR’ı taslaktı. Bu nedenle main’de bütün yeni dosyaları göremeyebilirsiniz. H4 dalını seçince önceki çalışmalarla birlikte güncel hazırlığı görürsünüz.

Bağımlı PR açmamızın nedeni önceki çalışmayı korurken yeni haftanın farkını ayrı göstermek. Öncekiler birleştirilince hedef dal ve farklar tekrar kontrol edilir. Öğrenci deposunda önceki işler main’deyse yeni dal main’den başlar; öğretmenin geçici dal zinciri körlemesine kopyalanmaz.

Göster: https://github.com/pozelll/-klinik-randevu-ogretmen/pull/12
İnceleme yapılmadığı için otomatik olarak Done, Closed veya onaylı teslim demiyoruz.



# 3. hafta: küçük bir kullanıcı sorununa odaklanmak

Hedefimiz “bir sürü özellik eklemek” değil, hastanın iptali onaylamak ile işlemden vazgeçmek arasındaki farkı anlamasına yardımcı olmaktı. Ürün hedefi kullanıcıya faydayı; haftalık hedef bu faydaya yönelik küçük artımı tanımlar.

| İş | İlk / güncel puan | Neden bu sırada? |

| --- | --- | --- |

| H3-01 görünür iptal açıklaması | 2 / 3 | İşlemden önce koşulu ve sonucu açıklamak |

| H3-02 onay penceresini açıklama | 3 / 3 | Karar anında iki seçeneğin farkını göstermek |

| H3-03 saat seçimi yardımı | 3 / 3 | Faydalı ama iptal açıklığı için zorunlu değil |

| H3-04 taşıma, H3-05 SMS, H3-06 özet | 8, 8, 5 / değişmedi | Gelecek adayları; yeni karar ve kapsam gerektirir |

## Neden bütün adayları yapmadık?

Ürün iş listesi yapılabilecek işleri taşır; çalışma planı o dönemin seçimini taşır. Bir fikrin listede bulunması uygulandığını veya taahhüt edildiğini göstermez. H3-04/05/06 bu derste uygulanmadı. H3-03 ertelendi; silinmedi veya tamamlandı sayılmadı.

Sınıfta Product Owner fayda ve sıralamayı; Scrum Master çalışma düzeni ve engelleri; Developers planı ve kaliteyi takip eder. Bu kısa etkinlik bir öğrenme simülasyonudur; yalnız rol isimleri kullanmak tam Scrum uygulandığını kanıtlamaz.

Göster: hafta-03/docs/01-ekip-hedef.md, 02-gozlem.md ve 03-product-backlog.md. Puanlar saat, not veya başarı yüzdesi değildir.



# 3. hafta: 8 → 9 → 6 hesabı

İlk seçim H3-01, H3-02 ve H3-03’tü. Ders varsayımı olarak kapasite 8 puandı. Yeni kart, ana açıklamada “Tamamlandı durumundaki randevular iptal edilemez” ifadesinin açıkça görünmesini istedi. Ürün zaten bu sınırı uyguluyordu; açıklama ve kontrol kapsamı genişledi.

| Durum | Hesap | Anlam |

| --- | --- | --- |

| İlk plan | 2 + 3 + 3 = 8 | Başlangıç seçimi kapasiteye sığıyor |

| Aynı kapsam, yeni tahmin | 3 + 3 + 3 = 9 | H3-01 büyüdü; kapasite 1 puan aşıldı |

| Güncel seçim | 3 + 3 = 6 | H3-01/02 kaldı; H3-03 ertelendi |

| Ayrılmamış kapasite | 8 - 6 = 2 | 3 puanlık işi eklemeye yetmez |

## “İki puan boş kaldı; yanlış plan mı?”

Hayır. Kapasiteyi doldurmak amaç değildir. Hedefi koruyan ve kalite koşullarını yerine getirebilen kapsam seçilir. İşi zorla küçük gösterip eklemek tahmini bozabilir. Gerçek bir ekip işi bağımsız parçalara ayırmayı ayrıca değerlendirebilir; bu örnekte H3-03’ü erteledik.

## “6/8 = %75 başarı mı?”

Hayır. Bu oran kapasiteye göre seçilen göreli kapsamı anlatır; öğrencinin notu veya tamamlanmış iş yüzdesi değildir. Tamamlanan puana yalnız Bitti Tanımı koşullarını sağlayan iş girer. Test yapılmış ama bağımsız inceleme bekliyorsa işin bu durumu ayrıca görünür kalır.

Göster: hafta-03/docs/05-sprint-plani.md, 06-degisiklik-karti.md ve 12-metrikler.md. İlk tahminler güncel değerlerle silinmedi.



# 3. hafta: kodda tam olarak neyi değiştirdik?

| Yer | Değişiklik | Amaç |

| --- | --- | --- |

| index.html; main-grid öncesi açıklama | Kendi Bekliyor kaydı, Tamamlandı sınırı, kaydın kalması ve koşullu saat açılması | Kullanıcının işlemden önce sonucu anlaması |

| index.html; cancelAppointment içindeki window.confirm | Kayıt/tarih/saat; Tamam iptali onaylar, İptal işlemden vazgeçirir | Karar anındaki anlam karışıklığını azaltmak |

Bu metin değişiklikleri Hasta rolünün yetkisini genişletmedi. Resepsiyon veya Doktora iptal yetkisi eklenmedi. Tarayıcının kendi düğme adları değiştirilmedi; özel pencere geliştirilmedi. H4 boyunca aynı index.html korundu.

## Kodu okurken izlenecek sıra

1. canCancel: rol Hasta mı, kayıt seçili hastanın mı, durum Bekliyor mu?
2. cancelAppointment: kayıt bulunamazsa veya uygun değilse işlemi reddeder.
3. window.confirm: kullanıcı vazgeçerse değişiklikten önce döner.
4. Onay varsa status = cancelled olur; saveData ve render çağrılır. Kayıt diziden silinmez.

## Sınırı dürüstçe gösterin

Mevcut başarı bildirimi “İlgili saat yeniden uygun” diyor; ana açıklama ve onay metni doğru BR-01 koşulunu içeriyor. H4 tasarımında sonuç mesajının da kurala bağlı olması gerektiği belirtilmiştir; bu sonraki uygulama işidir. Kalıcı yazma hatasında önceki bellek değişimi otomatik geri alınmıyor. Tasarım kararını uygulanmış düzeltme gibi anlatmayın.

Göster: index.html içinde Ctrl+F ile main-grid, canCancel, cancelAppointment ve saveData. Kod satır numarası yerine bu adları aramak sürüm değişimlerinde daha dayanıklıdır.



# 3. hafta: altı test neyi kanıtlıyor?

| Test | Kontrol | Kayıtlı sonucun sınırı |

| --- | --- | --- |

| T01 | Yeni ana açıklama | Ekranda dört anlam görünür; kullanılabilirlik ölçümü değil |

| T02 | Vazgeçme | R012 Bekliyor, saat Dolu; kullanıcı bildirimi ve son ekran |

| T03 | Onaylı iptal | R011 İptal edildi; yanlış Tamam seçimi iptal olarak kaydedildi |

| T04 | Tamamlandı sınırı | R003’te iptal düğmesi yok, 11:00 Kapalı; görünüm kontrolü |

| T05 | Hasta süzme | Kaan görünümünde Ece kaydı yok; gerçek kimlik doğrulama testi değil |

| T06 | Oluştur-vazgeç-iptal sayımı | R013 ve dört aşama; ekranlar ile kullanıcı bildirimleri ayrı |

28 Ekim’deki öğretmen kaydı bu altı kontrolü belirtilen kapsamlarıyla Geçti olarak içerir. Bu yeni PDF için testler yeniden çalıştırılmadı. “Altı test geçti” demek tüm olası durumlar, kalite hedefleri ve bağımsız inceleme tamamlandı demek değildir.

## A ve B sürümünü neden ayırdık?

İlk metin değişiklikli A sürümünde R011 iptal ve R012 vazgeçme denendi. Tamamlandı cümlesi eklenen B sürümünde görünüm kontrolleri ve ek T06 kaydı vardı. JavaScript bloğunun A ile aynı olduğu dosya karşılaştırmasıyla kontrol edilmişti. Her kanıtın hangi sürüme ait olduğu test kaydında açıklanır.

Bir ekran yoksa ekran kanıtı varmış gibi yazılmaz. T06 vazgeçme sayımı kullanıcı bildirimiyle doğrulandı; yeni ekranı yoktu. Öğrenci kendi denemesini gerçek kayıt, saat, sürüm ve sonuçla doldurur.

Göster: hafta-03/docs/08-test-kaydi.md. Kaynak ortam Windows/Chrome; ayrıntılı sürüm numarası kaydedilmemiştir. Bu sınırlılığı sonradan tahminle doldurmadık.



# T06: iptal neden toplamı azaltmıyor?

| Aşama | Bekleyen | Tamamlanan | İptal | Toplam |

| --- | --- | --- | --- | --- |

| Başlangıç | 1 | 2 | 6 | 9 |

| R013 oluşturuldu | 2 | 2 | 6 | 10 |

| Pencereden vazgeçildi | 2 | 2 | 6 | 10 |

| İptal onaylandı | 1 | 2 | 7 | 10 |

Oluşturma yeni kayıt ekler: toplam +1. Vazgeçme veri değiştirmez. İptal aynı kaydın durumunu değiştirir: Bekleyen -1, İptal +1; toplam sabit. Toplam, bekleyen iş sayısı değildir; üç durumdaki bütün kayıtların sayısıdır.

Genel başlangıç B, T, I, N ise oluşturma sonrası B+1, T, I, N+1; vazgeçme sonrası aynı; iptal sonrası B, T, I+1, N+1 olur. Bu ilişki öğrencinin farklı başlangıç sayılarıyla da kullanılabilir.

## Sınıfta gösterim

Hasta rolünde gerçek kaydı takip edin; sayıları aynı doktor ve tarihle Resepsiyon görünümünden okuyun. Hasta listesi ve yetkili günlük toplam farklı kapsamda olabilir. Rol değişiminde doktor/tarih de değişmişse iki ekranın sayısını doğrudan karşılaştırmayın.

Öğretmenin R013 sayısını taklit etmek için kayıt silmek veya veriyi sıfırlamak gerekmez. Öğrencinin kaydı R008 veya R014 olabilir. Önemli olan aynı kaydın aşamalarını ve toplamın neden değiştiğini açıklamasıdır.

Göster: hafta-03/kanitlar/h3-t06-baslangic-toplamlar-20261028.png; h3-t06-olusturma-toplamlar-20261028.png; h3-t06-iptal-toplamlar-20261028.png. Vazgeçmenin ayrı yeni ekranı yoktur.



# Review, retrospektif ve Bitti Tanımı

| Etkinlik | Soru | Kayıt |

| --- | --- | --- |

| Ürün değerlendirmesi | Ortaya çıkan açıklama kullanıcıya nasıl yardım ediyor? | hafta-03/docs/10-review-retro.md |

| Retrospektif | Bir sonraki çalışmada iş yapışımızı nasıl iyileştireceğiz? | Aynı dosyada ayrı bölüm |

| PR incelemesi | Değişiklik, kabul koşulları ve kanıt tutarlı mı? | 09-pr-inceleme.md ve gerçek review |

| Bitti Tanımı | Bir işi hangi ortak kalite koşullarıyla bitmiş sayıyoruz? | 04-kabul-ve-dod.md |

| Metrik / bireysel açıklama | Ne seçildi, ne gerçekten bitti; ben ne yaptım? | 12-metrikler.md; 13-cikis-bileti.md |

Bu etkinlikler birbirinin yerine geçmez. Arkadaşın ürünü kullanırken yorum yapması, kod farkını incelediği anlamına gelmez. Bir PR’ı açmak da gerçek review değildir. Yazardan veya ortak yazardan farklı kişi somut bulguyu ve değerlendirdiği sürümü kaydeder.

## Öğrenciye verilecek örnek geri bildirim

“03 belgesinde puan 2 kalmış; değişiklik kartında güncel değer 3. İlk tahmini koruyup güncel sütunu düzelt.” Bu ifade somut ve uygulanabilirdir. “Güzel olmuş” tek başına hangi kapsamın kontrol edildiğini göstermez.

Retrospektif sonucu da somut olmalı: “Bir sonraki denemeden önce bir üye rol/doktor/tarih koşulunu sesli okuyacak; test kaydında eksik koşul kalıp kalmadığını kontrol edeceğiz.” Gerçek katılımcı ve tarih sonradan uydurulmaz.

Öğretmen örneğinde bağımsız inceleme ve nihai teslim bekliyor. Öğrenciler kendi gerçek durumlarıyla formu doldurur; öğretmenin açık PR durumu onların işini otomatik bekletmez.



# 4. hafta: sekiz basamağın mantığı

| Adım | Yaptığımız iş | Neden? |

| --- | --- | --- |

| 1 | H3 son sürümünü ve yedeği belirledik | Neyi değiştirdiğimizi karşılaştırabilmek |

| 2 | H4 dalı, klasörleri ve boş şablonlar | Eski çalışmayı koruyarak ilerlemek |

| 3 | Yaklaşımları karşılaştırıp seçim yaptık | Çalışma biçimini proje koşuluna dayandırmak |

| 4 | İptal sorumluluklarını çizdik | Ekran, kural ve saklamayı ayırmak |

| 5 | İki mimari ve Repository kararını yazdık | Tercihin yarar ve maliyetini görünür kılmak |

| 6 | İlk planı ve kritik yolu hesapladık | Bağımlılık ve kaynakla gerçekçi plan kurmak |

| 7 | Kartla planı güncelledik, ilkini koruduk | Yeni kapsamın etkisini göstermek |

| 8 | İnceleme formu ve taslak PR hazırladık | Gerçek inceleme ve teslimi izlemek |

Bu haftanın ana işi kodu yeniden yazmak değil, sonraki uygulamayı tasarlamak ve planlamaktır. H3’ün index.html dosyası aynıdır. “Kod değişmediyse iş yapmadık mı?” sorusuna: hangi parçanın ne yapacağına ve değişiklik maliyetine karar verdik; bunlar uygulamanın girdileridir, diye cevap verin.

İlk yedi adımın öğretmen hazırlığı ve sekizinci adımın incelemeye sunulacak paketi hazır. Sekizinci adımın bağımsız insan incelemesi ve nihai teslimi açık. A-I plan görevleri de henüz yapılmış işler değildir.

Göster: hafta04/README.md ve docs/00-baslangic-ve-surum.md. Öğrenci yeni boş şablonları kendi dolu H3 projesine ekler.



# Yaklaşım seçimi: neden küçük artımlar?

| Yaklaşım | Yarar | Sınır / dikkat |

| --- | --- | --- |

| Şelale | Aşamaları ve teslimlerini baştan belirginleştirir | Geç geri bildirim değişiklik maliyetini artırabilir; her projede değişiklik yasak demek değildir |

| Artırımlı | Kullanılabilir kapsamı küçük parçalarda sunar | Parçaların bütünleşmesi ve ortak kurallar korunmalı |

| Çevik çalışma | Kısa geri bildirimle öğrenme ve planı uyarlama | Düzenli iletişim, açık kalite koşulları ve kayıt gerektirir |

Seçimimiz kısa geri bildirim döngüleriyle küçük artımlar halinde çevik çalışma. H3’te küçük açıklama değişikliğini uygulayıp denedik; yeni kart geldiğinde planı güncelledik. Bu proje deneyimleri seçimi gerekçelendirir. Artırımlı geliştirme ile çevik çalışma birbirini dışlayan seçenekler değildir.

## Alternatif ne zaman daha uygun olabilir?

Gereksinimleri çok daha sabit, aşama onayları belirgin bir işte daha plan odaklı yaklaşımın yararı artabilir. Bizim küçük öğrenme projemizde hızla görülebilen bir ürün parçası ve geri bildirim var. Bunun karşılığında kapsam dağılmasını iş listesi, Bitti Tanımı ve izlenebilirlik ile yönetiyoruz.

“Çevikse belge gerekmez” yanlış. Bu projede kararın nedenini ve testin kapsamını yazmak sonraki değişikliği daha güvenilir kılar. Gereksiz tekrar azaltılabilir; ihtiyaç, karar ve kanıt kaydı kaldırılmaz.

Göster: hafta04/docs/01-yasam-dongusu-secimi.md. Bu seçim tek başına tam Scrum uygulandığı iddiası değildir.



# Mimari ve tasarım kalıbı: kararın gerekçesi

Seçenek A mevcut tek HTML içindeki bağlı düzeni sürdürmek; Seçenek B aynı tarayıcıda arayüz, iş kuralları ve veri erişimini ayırmak. H4-MK-01 ile B’yi seçtik. Küçük proje için ek kavram ve bağlantı maliyeti var; karşılığında kuralı ekrandan bağımsız açıklamak ve denemek kolaylaşabilir. Bu yarar uygulama ve testle daha sonra doğrulanacak.

| Parça | Sorumluluk | Buraya koymayacağımız karar |

| --- | --- | --- |

| Arayüz | İstek alır, onay sorar, sonucu gösterir | Rol/sahiplik/durum uygunluğunu tek başına belirleme |

| İş kuralları | İptal uygunluğu, durum geçişi, BR-01 sonucu | HTML üretme veya localStorage ayrıntısı |

| Veri erişimi | Kaydı okuma, güncelleme, kalıcılık sonucu | Kimin iptal edebileceğine karar verme |

## Repository burada neyi çözüyor?

Kayıtları farklı yerlerde doğrudan değiştirip saklama ayrıntılarını dağıtmak yerine tek veri erişim sınırı öneriyoruz. findById bağımsız kopya veya null; list kopyalar; update var olan kaydın güncelleme ve kalıcılık sonucunu verir. Bunlar önerilen sözleşmelerdir; mevcut kodda uygulanmış API değildir.

Repository dördüncü bir katman değildir; üçüncü sorumluluk içinde sınırlı uyarlamadır. Yeni sunucu, veritabanı veya gerçek kullanıcı hesabı eklemiyoruz. localStorage anahtarı, schema ve nextId korunmalı; oluşturma/tamamlama aynı güncel veriyi görmelidir.

Göster: hafta04/docs/02-mimari-karar.md. Mimari daha geniş sorumluluk düzenidir; kalıp belirli bir tekrarlanan soruna yaklaşımı anlatır.



# Diyagramı anlatma provası

Görsel: hafta04/diagrams/01-bilesen.png

Yukarıdan aşağıya: kullanıcı onaylı isteği verir; kurallar uygunluğu belirler; veri erişimi kaydı saklar. Kesik oklar sonuç/veri dönüşüdür. Vazgeçme halinde değişiklik isteği gönderilmez. Üç kutu üç sunucu anlamına gelmez.

Bu çizim önerilen tasarımdır. Dosya: hafta04/diagrams/01-bilesen.drawio ve PNG. Kaynak kod hâlâ tek index.html içindedir. Görseldeki 5/8 etiketi kararın hazırlandığı basamağı gösterir.



# İlk plan: görev, süre, bağımlılık ve kaynak

Plan H4-P0, mimari kararın beşinci haftada uygulanmasına ilişkin öğretim örneğidir. Bir blok 30 dakika net çalışmadır. t=0 başlangıç anını temsil eder; takvim günü, mola veya dış onay beklemesi değildir. U1-U4 gerçek kişi ataması değildir.

| İş | Çıktı | Öncül | Kişiler | Blok |

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

A bitmeden B/C/D başlayamaz; ortak sözleşme önce belirlenir. B/C/D farklı kişilerle paralel hazırlanır. E hepsini bekler. G bağımsız incelemedir; U4’ü kod yazımına kaydırmak bu niteliği değiştirebilir. H’nin iki bloğu sınırlı düzeltme payıdır; her hatayı bir saatte çözeceğimiz garantisi değildir.

Göster: hafta04/planlar/01-ilk-is-plani.md. Sürelerin toplamı 22 bloktur; paralellik nedeniyle net bitiş 22 blok değildir.



# Kritik yol hesabını tahtada açıklamak

**İleri hesap:** erken başlangıç = öncüllerin en büyük erken bitişi; erken bitiş = başlangıç + süre. **Geri hesap:** geç bitiş = ardılların en küçük geç başlangıcı; geç başlangıç = bitiş - süre. **Bolluk:** geç başlangıç - erken başlangıç.

| İş | Erken başla/bitir | Geç başla/bitir | Bolluk |

| --- | --- | --- | --- |

| A | 0 / 2 | 0 / 2 | 0 |

| B | 2 / 6 | 2 / 6 | 0 |

| C | 2 / 5 | 3 / 6 | 1 |

| D | 2 / 5 | 3 / 6 | 1 |

| E | 6 / 8 | 6 / 8 | 0 |

| F | 8 / 11 | 8 / 11 | 0 |

| G | 11 / 13 | 11 / 13 | 0 |

| H | 13 / 15 | 13 / 15 | 0 |

| I | 15 / 16 | 15 / 16 | 0 |

E başlangıcı max(6,5,5)=6. B kolundan yol 16 blok, C ve D kollarından 15 blok. Kritik yol A-B-E-F-G-H-I; net süre 16×0,5=8 saat. C ve D’nin birer blok bolluğu, ikisini atlayabileceğimiz veya projeye bir saat ekleyebileceğimiz anlamına gelmez.

**Emek:** Her görevin saat süresi × katılan kişi sayısı toplanır: 17 kişi-saat. E bir saat, üç kişi: 3 kişi-saat emek ama bir saat geçen süre. 17’yi dört kişiye bölerek bitiş bulunmaz; öncüller ve kişi uygunluğu korunmalıdır. Her blokta çifte atama kontrol edilir.

Göster: hafta04/docs/03-is-plani-ve-riskler.md H4-P0 hesap tablosu. Kritik yol burada süre ve bağımlılıklardan türetilir; “en önemli görevler listesi” değildir.



# Değişiklik geldi: neden 8 saat 9 oldu?

H4-DK-01, mevcut iptal kuralları için yedi satırlı karar tablosu ve her satıra ayrı başlangıç/kanıt istedi. Yeni iptal yetkisi eklenmedi. Ek işi planladık: C 3’ten 5 bloğa; F 3’ten 4 bloğa çıktı. Diğer süre, öncül ve kişiler aynı kabul edildi; gerçek işte bu varsayım yeniden sınanır.

| Ölçü | P0 | P1 |

| --- | --- | --- |

| C / F süresi | 3 / 3 blok | 5 / 4 blok |

| B / C / D bitişi | 6 / 5 / 5 | 6 / 7 / 5 |

| E başlangıcı | 6 | 7 |

| Kritik yol | A-B-E-F-G-H-I | A-C-E-F-G-H-I |

| Net bitiş | 16 blok / 8 saat | 18 blok / 9 saat |

| İş sürelerinin toplamı | 22 blok / 11 saat | 25 blok / 12,5 saat |

| Toplam emek | 17 kişi-saat | 19 kişi-saat |

C’nin +2 bloğunun ilki eski 1 blok bolluğu kullanır; ikincisi E’yi 1 blok geciktirir. F’nin +1 bloğu ortak son zinciri 1 blok daha uzatır. Net artış 2 blok = 1 saattir. Emek artışı C’de 1 kişi×1 saat; F’de 2 kişi×0,5 saat: toplam 2 kişi-saat.

P1’de B’nin bolluğu 1, D’nin 2, C’nin 0 bloktur. Yeni kritik kol C’dir. İlk planı silseydik değişikliğin gerçek etkisini göremezdik. Seçimimiz ek kapsamı koruyup süre artışını kabul etmek; inceleme ve testi kısaltarak 8 saate sığmış gibi göstermemektir.

Göster: hafta04/kartlar/01-karar-tablosu-ve-kanit.md ve docs/03 H4-P1. İlk planın sabit kopyası değişmeden planlar/01-ilk-is-plani.md içinde.



# H4 incelemesi ve beşinci haftaya devir

| Karar tablosu satırı | Beklenen; henüz yürütülmüş kanıt değil |

| --- | --- |

| K01 kayıt yok | Ret; veri değişmez |

| K02 Resepsiyon / K03 Doktor | Rol uygun değil; veri korunur |

| K04 başka hastanın kaydı | Sahiplik uygun değil; veri korunur |

| K05 Tamamlandı | İptal uygulanmaz |

| K06 İptal edildi | İkinci iptal uygulanmaz; sayılar korunur |

| K07 Hasta + kendi + Bekliyor + onay | Kayıt silinmeden iptal; toplam aynı; BR-01 saat sonucu |

Her satır ayrı sentetik başlangıçla denenir. Bir satırın değişmiş verisi sonraki satıra taşınırsa yanlış sonuç alınabilir. Ret durumunu yalnız düğme gizli diye geçmiş saymayız; sonraki uygulamada kontrollü istekle iş kuralı da sınanır. Vazgeçme, saklama hatası ve diğer randevu işlemleriyle tutarlılık kontrolleri ayrıca kalır.

## Sekizinci basamakta hazırladığımız kayıt

04-inceleme-ve-teslim.md: hangi dosyanın inceleneceği, hazırlık kontrolleri, gerçek inceleyen/commit formu, bulgu-düzeltme tablosu ve birleştirme koşulları. İnsan incelemesi yapılmadığı için bu alanlar bekliyor. GitHub PR #12 taslak olarak açıldı.

H4 belge incelemesi ile P0/P1’deki gelecekte yapılacak G kod incelemesi farklıdır. H4 onayı gelecekte yazılacak kodu onaylamaz. Beşinci hafta öncesinde gerçek kişi, takvim, sözleşme ve açılış yöntemi netleşir; sonra uygulama ve gerçek testler yapılır.

Göster: hafta04/docs/04-inceleme-ve-teslim.md. Eski PR bağımlılıkları çözülünce hedef dal ve fark tekrar kontrol edilmelidir.



# Sık sorular: ilk iki hafta

## Hazır uygulama varsa gereksinimi neden yazıyoruz?

Var olan davranışı gözleyip açık ve kontrol edilebilir ihtiyaçlara çevirmeyi öğreniyoruz. Prototipte bulunması paydaşın onayladığı ihtiyaç olduğu anlamına gelmez. Göster: docs/03 ve docs/08.

## Gereksinim, kabul koşulu ve test aynı mı?

Gereksinim sistem davranışını; kabul koşulu belirli durumda bekleneni; test kaydı yapılan denemenin gerçek sonucunu anlatır. Göster: FR-03 → AC-03/ALT-01 → G kayıtları.

## İptal edilen kayıt niye listede duruyor?

İptal silme değildir. Geçmişi ve günlük sayımı koruyoruz. Göster: B2, B3 ve T06.

## Tamamlanan saat neden yeniden açılmıyor?

BR-01 iptal edilmemiş kaydı engel sayar; Tamamlandı iptal edilmiş değildir. Göster: R003/11:00 ve docs/03 BR-01.

## Yenilemede Hasta rolüne dönmek veri kaybı mı?

Tek başına değil. Seçimler başlangıca dönebilir; kayıtlar ayrı saklanır. Aynı doktor/tarihi yeniden seçip kayıt kimliğini karşılaştırın.

## Dosyayı arkadaşımın bilgisayarına taşıdım, kayıtlar neden aynı değil?

Dosya kopyası localStorage verisi değildir. Tarayıcı, dosya yolu ve saklama izni etkilidir. Ortak sunucu yoktur.

## PNG göndermek yeterli mi?

Hayır; düzenlenebilir .drawio kaynağını da teslim ediyoruz. PNG yalnız görünümü gösterir.



# Sık sorular: üçüncü ve dördüncü hafta

## Tamam neden iptal ediyor, İptal neden koruyor?

Pencere “Randevunuzu iptal etmek istiyor musunuz?” sorusunu sorar. Tamam bu işlemi onaylar; İptal penceredeki işlemden vazgeçer. H3’te bu anlamı açıklama metnine yazdık.

## Üçüncü hafta puanı dördüncü hafta saate çevirebilir miyiz?

Hayır. H3 puanı göreli tahmin; H4 bloğu açıkça 30 dakika net süredir. Farklı ölçülerdir.

## Repository veritabanı mı?

Hayır. Burada kayıt erişiminin sınırıdır; oturum verisi ve mümkünse localStorage kullanımı önerilir. Sunucu eklenmedi.

## Üç katman üç dosya veya üç sunucu mu demek?

Sorumluluk ayrımıdır. Fiziksel dosya düzeni ve dağıtım ayrı karardır. Şu anda çalışan kod tek HTML dosyasıdır.

## Bütün görev sürelerini toplasam teslim süresini bulur muyum?

Paralel görevler varsa hayır. Öncüllerle en uzun yolu ve kaynak uygunluğunu kontrol etmelisiniz. P0’da toplam 11 saat; net geçen süre 8 saat.

## Beşinci kişi gelince süre otomatik kısalır mı?

Hayır. Hangi işi üstleneceği, bağımlılık ve beceri belirlenmelidir. 17 kişi-saati kişi sayısına bölmek kritik yol hesabı değildir.

## Testler geçti; PR neden hâlâ taslak?

H4’te yeni davranış testi yapılmadı; hazırlık kontrolleri yapıldı. Gerçek bağımsız inceleme ve önceki PR bağımlılıkları bekliyor. Yükleme, onay ve birleştirme farklıdır.



# Sınıfta 15 dakikalık tekrar gösterimi

| Süre | Göster | Sorulacak soru |

| --- | --- | --- |

| 0-2 dk | index.html; Hasta/Ece/Deniz/12.11.2030 | Rol seçimi gerçek giriş mi? B2 ile B3 aynı kapsam mı? |

| 2-4 dk | Kendi Bekliyor kaydında önce vazgeçme | Penceredeki İptal hangi işlemden vazgeçiriyor? |

| 4-6 dk | Onaylı iptal ve aynı doktor/gün toplamı | Neden toplam azalmadı? |

| 6-8 dk | docs/05 FR-03 satırı | Bu davranışın kabul koşulu ve kanıtı nerede? |

| 8-10 dk | H3 değişiklik kartı | 8 → 9 → 6 neyi gösteriyor? |

| 10-12 dk | H4 bileşen diyagramı | Kimin iptal edebileceğine hangi parça karar veriyor? |

| 12-14 dk | H4 ilk ve güncel plan | C büyürken neden net artış 1 saat? |

| 14-15 dk | PR #12 ve inceleme kaydı | Hazırlıkla nihai tamamlanma arasındaki eksik adım ne? |

Bu süreler sınıfta tekrar için öneridir; resmi ders süresi veya öğrenci performans eşiği değildir. Canlı gösterim yeni veri değişikliği yapar. Başlangıç kaydını not edin; eski T06 sonucunun üstüne yeni sayı yazmayın. Uygun Bekliyor kayıt yoksa yeni kayıt hazırlığını açıkça kaydedin.

## Öğrencinin açıklamasını değerlendirme

Öğrenci yalnız sonucu söylemesin: dosyayı bulsun, gerekçeyi açıklasın, kanıtın sınırını söylesin. “Kritik yol C oldu” yanıtının devamında C’nin 1 blok bolluğunu ve E başlangıcındaki değişimi açıklamasını isteyin. Ezber sayılar yerine kendi grubunun koşullarını kullanmasını bekleyin.

Bu rehber hazır nottur; öğrencilerin hesapları, katkıları ve gerçek inceleme kayıtları kendi projelerinde oluşur.



# Dosya bulma dizini: ilk üç hafta

| Yol / dosya | Aradığınız bilgi |

| --- | --- |

| docs/01-vizyon-kapsam.md | Problem, vizyon, kapsam sınırı |

| docs/02-paydaslar.md | Aktör, paydaş, sorular |

| docs/03-gereksinimler.md | FR-01-06, NFR, BR-01 |

| docs/04-kabul-kriterleri.md | AC, ALT-01, kalite ölçüm planı |

| docs/05-izlenebilirlik.md | İhtiyaç-kabul-gözlem-Issue-PR bağlantısı |

| docs/06-riskler.md | Risk, önlem, sorumlu |

| docs/07-toplanti-notu.md | Gerçek kararlar ve görüşmeler |

| docs/08-prototip-gozlemleri.md | G koşulları ve gerçek sonuçlar |

| docs/09-ekip-rolleri.md | Üyeler, görevler, katkı düzeni |

| hafta-03/docs/01 ve 02 | Hafta hedefi ve başlangıç gözlemi |

| hafta-03/docs/03 ve 04 | İş listesi; kabul ve Bitti Tanımı |

| hafta-03/docs/05 ve 06 | İlk/güncel plan; değişiklik kararı |

| hafta-03/docs/07 ve 08 | Pano/günlük; gerçek test kaydı |

| hafta-03/docs/09 ve 10 | PR incelemesi; review/retrospektif |

| hafta-03/docs/11, 12 ve 13 | Teslim, metrik, bireysel çıkış bileti |

Kök ders-testi.html ilk iki dersin kısa alıştırmasıdır. Eski öğrenci paketindeki hafta-03/ders-testi.html üçüncü dersin ek alıştırmasıdır. Sonuçları otomatik gönderilmiş veya kalıcı kaydedilmiş sanmayın; ilgili çalışma belgesine aktarın.



# Dosya bulma dizini: H4 ve kaynaklar

| H4 yolu | Aradığınız bilgi |

| --- | --- |

| docs/00-baslangic-ve-surum.md | Başlangıç, yedek, dal ve durum |

| docs/01-yasam-dongusu-secimi.md | Üç yaklaşım ve gerekçeli seçim |

| docs/02-mimari-karar.md | Sorumluluklar, seçenekler, Repository sözleşmesi |

| diagrams/01-bilesen.drawio ve .png | Önerilen tasarımın çizimi |

| docs/03-is-plani-ve-riskler.md | P0/P1 tabloları, kritik yol, emek ve risk |

| planlar/01-ilk-is-plani.md | Değişiklik öncesi sabit P0 |

| kartlar/01-karar-tablosu-ve-kanit.md | H4-DK-01 ve yedi durum |

| docs/04-inceleme-ve-teslim.md | İnceleyen, bulgu, PR ve teslim koşulları |

| sablonlar/01, 02, 03 | Öğrenci için boş ana belgeler |

## Doğru sürümü açmak

Öğretmen deposu: https://github.com/pozelll/-klinik-randevu-ogretmen
H4 dalı: docs/h4-mimari-plan
PR: https://github.com/pozelll/-klinik-randevu-ogretmen/pull/12
Bu rehberin proje dayanağı: 8b668fbed7e348fc25a7e5ffa6c69d3ae9f14f3b

Kavramların kaynakları proje belgelerinde bağlantılıdır: Çevik Manifesto ve Scrum Guide (01); Fowler’ın Presentation Domain Data Layering ve Repository açıklamaları ile Microsoft N-tier rehberi (02); GAO Schedule Assessment Guide GAO-16-89G (03). Bunlar kavramsal dayanaklardır; proje tahminleri ve rol atamaları öğretim varsayımlarımızdır.

Öğrenci rehberinin ilk üç ders bölümü, 29 Ekim 2026 tarihli 33 sayfalık dağıtım rehberinden korunmuştur. H4 bölümü ve bu öğretmen rehberi 1 Kasım’da eklendi. Eski tarihli aşama notları güncel sonuç gibi okunmamalıdır. Yeni PDF hazırlanırken uygulama testleri yeniden yürütülmedi.

Öğrenci grupları kendi adlarını, katkılarını ve gerçek bağlantılarını kullanır.


