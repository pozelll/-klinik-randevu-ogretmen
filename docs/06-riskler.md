# 06 — Riskler

Ekip: Öğretmen çalışma örneği; öğrenci grubu henüz atanmadı.  
Tarih: 27.10.2026  
Sürüm: 1.0 — Çalışma metni tamamlandı; önlemlerin uygulanması ve ölçümler takipte.  
Kapsam: Klinik Randevu başlangıç prototipi ve ilk üç dersin proje çalışması.

## Amaç ve kullanım

Bu dosyada, proje hedefini veya ders çalışmasını ileride olumsuz etkileyebilecek durumları, bunların erken işaretlerini ve alınacak önlemleri kaydederiz. Gerçekleşmiş olayı 08-prototip-gozlemleri.md içinde kanıtıyla tutarız; ele alınacak mevcut sorunu ayrıca bir görev/issue ile izleriz. Henüz açılmamış bir GitHub kaydı için bağlantı üretmeyiz.

RSK-01 gibi kimlikler risk kaydını belirtir. Uygulamadaki R011 gibi randevu numaralarıyla aynı şey değildir.

Olasılık değerleri düşük/orta/yüksek biçimindeki ilk nitel değerlendirmelerdir; ölçülmüş oran veya yüzde değildir. Etki de aynı üç düzeyle ve gerekçesiyle yazılır. Bu taslakta puan hesabı yapılmaz. Sorumlular önerilen ekip görevleridir; 09 numaralı ekip belgesinde gerçek öğrenci adlarıyla eşleştirilecektir.

## Risk listesi

| Kimlik | Risk ve nedeni | Olasılık: düşük/orta/yüksek | Etki | Erken işaret | Önlem | Sorumlu |
|---|---|---|---|---|---|---|
| RSK-01 | İptal onayındaki ifadelerin karıştırılması nedeniyle, işlemden vazgeçmek isteyen kullanıcının randevuyu istemeden iptal etmesi. Karttaki İptal et ile onay kutusundaki İptal farklı sonuçlara karşılık gelir. | Orta — öğretmen denemelerinde karışıklık görüldü; diğer kullanıcılar için sıklık ölçülmedi. | Yüksek — korunmak istenen randevu iptal olabilir ve saati yeniden uygun görünebilir. | Kullanıcının hangi düğmeyi seçmesi gerektiğini sorması; vazgeçme görevinde Tamam seçmesi. | Üçüncü derste görünür iptal açıklamasını ve onay metnini netleştirmek; AC-03 ile ALT-01 akışlarını yeniden kontrol etmek; NFR-01'i dört farklı katılımcıyla ölçmek. | Kullanılabilirlik kontrolünü üstlenen üye — adı atanacak. |
| RSK-02 | Tarayıcıya bağlı yerel saklamanın kullanılamaması veya temizlenmesi nedeniyle çalışma kayıtlarının yenileme/kapatma sonrasında kaybolması; dersin aynı kayıtlarla sürdürülememesi. | Orta — ortam koşullarına bağlı nitel varsayım; veri kaybı deneyi yapılmadı. | Yüksek — gözlem yeniden kurulabilir, ancak ders zamanı ve önceki kayıtlarla karşılaştırma kaybedilebilir. | Kalıcı saklamanın kullanılamadığına ilişkin uyarı; aynı koşullardaki yenileme öncesi ve sonrası referans kayıtların farklı görünmesi. | Aynı dosya, tarayıcı ve tek sekmeyle çalışmak; rol ve seçimleri eşitleyerek referans kayıtları karşılaştırmak; gözlem ve ekran kanıtlarını proje dosyalarında saklamak. Saklama sınırlarını ayrıca denemek gerekirse mevcut öğretmen kayıtları yerine ayrı test ortamı kullanmak. | Çalışma ortamı ve kanıt kaydını üstlenen üye — adı atanacak. |
| RSK-03 | Gereksinim, kabul kriteri ve diyagramın ayrı ayrı güncellenmesi nedeniyle aynı role farklı belgelerde farklı görevler verilmesi; yanlış işin geliştirilmesi veya değerlendirilmesi. | Orta — birden çok belge birlikte tutuluyor; şu anda yeni bir çelişki saptandığı iddia edilmiyor. | Orta — düzeltme ve yeniden inceleme gerekir; kapsam veya test beklentisi karışabilir. | Örneğin bir belgede Resepsiyona iptal/tamamlama görevi eklenirken FR-03 ve FR-05'in değişmemesi; seçili doktor/tarih sınırının bir çizimde unutulması. | FR kimlikleriyle 03, 04 ve iki diyagramı karşılaştırmak; değişiklikte ilgili belgeleri birlikte güncellemek; çizen/yazan dışındaki üyeye inceletmek. | Belge tutarlılığı kontrolünü üstlenen üye — adı atanacak. |

## RSK-01 — Birlikte okuyacağımız ilk kayıt

- **Dayanak:** 08 numaralı belgede G-03-T1 ve G-03-T2 sırasında vazgeçme görevi planlanmışken onay kutusunda Tamam seçildi ve ilgili randevular iptal edildi. G-03-T3'te İptal seçilince R011 Bekliyor kaldı; 09:00 Dolu olarak korundu.
- **Geçmiş olay ile riskin ayrımı:** Önceki karışıklıklar gözlem kaydıdır. Buradaki risk, benzer karışıklığın sonraki kullanımda yeniden yaşanmasıdır. Tamam seçiminin iptali gerçekleştirmesi tek başına yazılımın işlevsel olarak bozuk olduğunu göstermez; ifadelerin anlaşılabilirliği ayrıca değerlendirilir.
- **Bugünkü durum:** Açık — önlem planlandı; üçüncü dersin metin değişiklikleri ve NFR-01 ölçümü henüz yapılmadı.
- **Önemli sınır:** Bu prototip yerel onay penceresini kullanır. Üçüncü ders planı açıklama ve onay metnini iyileştirir; tarayıcının Tamam/İptal düğmelerini özel düğmelerle değiştirme işi bu değişikliğin kapsamında değildir.
- **Risk ne zaman yeniden değerlendirilecek?** Metin iyileştirmesi uygulanıp işlev kontrolleri ve NFR-01 ölçümü yapıldıktan sonra. Tek bir doğru öğretmen denemesi riski kapatmak için yeterli sayılmaz.

## RSK-02 — Yerel kayıt, ekran seçimi ve gözlem kanıtı

**Risk cümlesi:** Tarayıcıya bağlı yerel saklamanın kullanılamaması veya temizlenmesi nedeniyle randevu kayıtları yenileme/kapatma sonrasında kaybolabilir; ders aynı kayıtlarla sürdürülemeyebilir.

**Dayanak:** Başlangıç paketindeki BILINEN_KISITLAR.md, saklamanın tarayıcı koşullarına bağlı olduğunu ve kalıcı saklama başarısızsa uygulamanın bellekte devam ettiğini açıklar. 08-prototip-gozlemleri.md içindeki Kayıt davranışı bölümünde ise önceki gerçek yenileme denememiz bulunur.

| Önceki denemede görülen durum | Doğru yorum |
|---|---|
| Yenileme sonrasında rol Hasta olarak açıldı. | Ekrandaki rol seçimi başlangıç değerine döndü. Bu tek başına randevu verisinin silindiğini göstermez. |
| Resepsiyon yeniden seçilince R011 Bekliyor, R002 Tamamlandı görünüyordu. | Kontrol edilen iki kaydın durumu o yenilemede korundu. |
| Günlük toplamlar 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıttı. | Seçili doktor ve tarih için önceki toplamlar korundu. Yalnız toplamların eşit olması bütün kayıtların tek tek aynı olduğunu kanıtlamaz. |

Bu kayıtlar öğretmen denemesinin sonucudur. Her grubun kayıt numarası ve sayılarının aynı olması gerekmez. Yeni bir karşılaştırma yapılırsa grup kendi başlangıç kayıtlarını, durumlarını, rolünü, doktorunu ve tarihini kaydeder; son durumu bunlarla karşılaştırır. Bu adımda yeni bir yenileme veya veri silme deneyi istenmez.

**Önlem planının anlamı:** Aynı dosya ve tarayıcıda, tek sekmeyle çalışmak farklı çalışma ortamlarını karıştırma ihtimalini azaltır; kalıcı saklama garantisi sağlamaz. Aynı rol, doktor ve tarih seçilerek referans kayıtlar karşılaştırılır. Gözlem belgesi ile ilgili ekran kanıtları ayrıca saklanır. Saklama başarısızlığı veya veri temizleme davranışı ileride denenecekse mevcut öğretmen verileri yerine ayrı test ortamı kullanılır.

**Neyi kaydetmiş oluyoruz?** 06-riskler.md dosyasını kaydetmek risk metnini, 08-prototip-gozlemleri.md dosyasını kaydetmek gözlem kaydını korur. HTML dosyasını kopyalamak uygulamanın kaynak kodunu korur. Bu işlemler tarayıcıdaki randevuların otomatik yedeğini oluşturmaz; prototipte randevu verisini dışa aktarma işlevi yoktur. Başka tarayıcıda kayıtların görünmemesi de ilk tarayıcıdaki kayıtların silindiğini tek başına göstermez; bu prototipte cihazlar ve tarayıcılar arasında eşzamanlama bulunmaz.

**Bugünkü değerlendirme:** Olasılık Orta, etki Yüksek; nitel öğretmen taslağı. Durum Açık. Önceki yenileme gözleminde kontrol edilen veriler korundu; saklamanın başarısız olduğu koşullar denenmedi. Risk gerçekleşmiş olarak işaretlenmedi ve bütün ortamlarda veri korunacağı sonucuna varılmadı.

**Bu adımın çalışma çıktısı:** RSK-02'nin nedenini, etkisini, önlemini ve dayanağını okuyup ayırmak. Kullanıcının kendi dosyasında kaydetmesi veya öğrencilerin bu incelemeyi yapması henüz doğrulanmadı.

## RSK-03 — Belgeler aynı davranışı anlatıyor mu?

**Risk cümlesi:** Gereksinim, kabul kriteri ve diyagram ayrı ayrı güncellenirse aynı rolün görevi farklı belgelerde farklı anlatılabilir; ekip yanlış işi geliştirebilir veya doğru davranışı yanlış beklentiyle değerlendirebilir.

**Örnek erken işaret:** Gereksinimde randevuyu yalnız Doktor tamamlayabilir denirken diyagramda Resepsiyon da bu işleve bağlanmış olabilir. Bu, olası bir çelişki örneğidir; mevcut öğretmen diyagramında böyle bir bağlantı bulunmamaktadır.

### Birlikte karşılaştırma — FR-05

| Bakılacak yer | Kontrol edeceğimiz anlam | Öğretmen örneğinde görülen |
|---|---|---|
| docs/03-gereksinimler.md → FR-05 | Kim, hangi kaydı, hangi koşulla tamamlayabilir? | Yalnız Doktor; görevli seçilen doktorun seçili tarihteki Bekliyor kaydı. Sonuç Tamamlandı, ilgili saat Kapalı; günlük toplamlar güncellenir. |
| docs/04-kabul-kriterleri.md → AC-05 | Bu gereksinimin beklenen sonucu nasıl kontrol edilir? | Doktor rolünde Bekliyor kaydı tamamlanır; kayıt Tamamlandı olur, tamamlama düğmesi kalkar, saat Kapalı kalır ve günlük sayılar değişir. |
| diagrams/02-kullanim-durumlari.drawio → FR-05 ovali | Bu işleve hangi aktör bağlı? | Randevuyu tamamlama ovalinin yalnız Doktor ile bağlantısı vardır. Alttaki koşul notu görevli doktor, seçili tarih ve Bekliyor durumunu hatırlatır. |

**Karşılaştırmanın sonucu:** 27.10.2026 tarihinde hazırlanan öğretmen dosyalarında bu üç noktadaki FR-05/AC-05 açıklamaları ile aktör bağlantısı arasında çelişki saptanmadı. Bu sınırlı belge kontrolü, bütün gereksinimlerin yeniden incelendiği veya uygulama testlerinin yeniden çalıştırıldığı anlamına gelmez. AC-05'in önceki çalışma sonucu G-05-B kaydına dayanır.

**Neden aynı cümleleri kullanmıyoruz?** Gereksinim, sistemden beklenen davranışı; kabul kriteri, bu davranışı hangi başlangıç ve sonuçla kontrol edeceğimizi; diyagram, rolün işleve katılımını anlatır. Aynı anlamı korumaları gerekir, kelimesi kelimesine aynı metin olmaları gerekmez. Ayrıntılı koşulların tamamı ovalin içine yazılmaz.

**Önlem planı:** Her değişiklikte ilgili FR kimliğini bulup kabul kriteri ve diyagramlarla karşılaştırmak; etkilenen belgeleri birlikte güncellemek; yazan/çizen dışındaki bir üyeye inceletmek. Bir çelişki bulunursa hangi belgenin doğru olduğunu gelişigüzel seçmek yerine kapsam ve gereksinim kararına dönmek, gerekiyorsa açık soruyu veya değişiklik kararını kaydetmek. Gerçek GitHub görev ve inceleme bağlantıları oluştuktan sonra 05 numaralı izlenebilirlik belgesine eklenir.

**Sorumlu:** Belge tutarlılığı kontrolünü üstlenen üye; gerçek öğrenci adı 09 numaralı ekip belgesinde atanacak. İnceleyen kişi kontrol ettiği dosya/sürümü ve bulgusunu kaydeder. Henüz yapılmamış arkadaş incelemesi tamamlandı olarak yazılmaz.

**Bugünkü değerlendirme:** Olasılık Orta, etki Orta; nitel öğretmen taslağı. Durum Açık — FR-05 için öğretmen örneği karşılaştırıldı; öğrenci ekiplerinin gerçek incelemesi ve sonraki değişikliklerde yeniden kontrol bekliyor. Bir örnekte uyum bulunması gelecekte belge ayrışması riskini ortadan kaldırmaz.

**Bu adımın çalışma çıktısı:** RSK-03'ün neyi önlemeye çalıştığını açıklamak ve FR-05 → AC-05 → diyagramdaki Doktor bağlantısını takip etmek. Hazır örneğe yanlış bağlantı ekleyerek yapay hata oluşturmak gerekmiyor.

## Bir riski gözden geçirme — mevcut durum ve izleme planı

Bu bölüm, mevcut belgelerden hazırlanan öğretmen çalışma örneğidir. Yeni bir uygulama testi veya öğrenci ekip incelemesi değildir. Riskin değerlendirmesi, yeni kanıt geldiğinde gerekçesiyle güncellenir; önceki değerlendirme silinmez.

### RSK-01 için bugünkü durum kaydı

| Alan | Kaydedilen bilgi |
|---|---|
| Kayıt tarihi ve türü | 27.10.2026 — öğretmen örneğinin belge üzerinden hazırlık durumu kontrolü. |
| İncelenen risk | RSK-01 — iptal ifadelerinin karıştırılması sonucu randevunun istemeden iptal edilmesi. |
| Önceki değerlendirme | Olasılık Orta, etki Yüksek; nitel ilk değerlendirme. |
| Mevcut kanıt | G-03-T1 ve G-03-T2'de vazgeçme görevi planlanmışken Tamam seçilerek iptal onaylandı. G-03-T3'te İptal seçilince R011 Bekliyor, 09:00 Dolu kaldı. Bunlar önceki öğretmen gözlemleridir. |
| İyileştirme sonrası yeni kanıt | Henüz yok. Üçüncü dersin açıklama/onay metni değişiklikleri uygulanmadı; değişiklik sonrası kontroller ve NFR-01 ölçümü yapılmadı. |
| Güncel karar ve gerekçe | Açık — önlem ve ölçüm bekleniyor. Riski azaltacak değişiklik ve etkisine ilişkin yeni kanıt olmadığı için olasılık Orta, etki Yüksek olarak korunuyor. |
| Yapılacak iş | Planlanan metin iyileştirmesini uygulamak; değiştirilen sürümde AC-03 ve ALT-01 akışlarını yeniden kontrol etmek; NFR-01'i belirlenen koşullarla ölçmek. |
| Takip sorumlusu | Kullanılabilirlik kontrolünü üstlenen üye; gerçek öğrenci adı 09-ekip-rolleri.md içinde atanacak. |
| Sonraki kontrol zamanı | Üçüncü dersin iyileştirme ve doğrulama adımları sonrası. Ölçüm yetişmezse risk açık tutulur; ekip gerçek sonraki kontrol tarihini belirler. |
| Gerçek uygulama/ölçüm bilgisi | Testi yapan kişi, uygulama sürümü, ölçüm tarihi ve sonuç bağlantıları henüz oluşmadı. Uygulandıktan sonra kaydedilecek. |

### Sonraki kontrolde hangi sonuçlar kullanılacak?

1. **AC-03 — İptali onaylama:** Kendi Bekliyor kaydı onay verilince İptal edildi olur ve listede kalır. Aynı doktor/tarih/saatte başka iptal edilmemiş kayıt yoksa saat Uygun olur.
2. **ALT-01 — Vazgeçme:** Onay penceresinde işlemden vazgeçilince aynı kayıt Bekliyor, saat Dolu kalır.
3. **NFR-01 — Anlaşılabilirlik ölçümü:** Dört farklı katılımcının en az üçü, iptal etme ve vazgeçme görevlerinin ikisini de doğru, görev çözümüne yönelik yardım verilmeden ve her görev ayrı ayrı en fazla 60 saniyede tamamlamalıdır. Bir kişi ancak iki görevin bütün koşullarını sağlarsa başarılı sayılır. Aynı kişinin dört denemesi dört katılımcı değildir. Ayrıntılı görev ve ölçüm koşulları 03-gereksinimler.md ve 04-kabul-kriterleri.md içinde korunur.

Önceki yönlendirmeli öğretmen denemeleri yeni sürümün kontrolü veya bu dört katılımcılı ölçümün sonucu yerine kullanılamaz. Kayıtlarda gerçek süre, sonuç, yardım durumu, uygulama sürümü ve gözlem bağlantısı bulunmalıdır.

### Yeni kanıt gelince karar nasıl değişir?

Aşağıdaki satırlar koşullu karar rehberidir; gerçekleşmiş sonuçlar değildir.

| Sonraki kontroldeki durum | Kayda geçirilecek karar |
|---|---|
| Metin değişikliği veya gerekli ölçüm henüz yapılmadı. | Açık; tamamlanmayan iş ve sonraki kontrol zamanı yazılır. Yeni ölçüm sonucu uydurulmaz. |
| Metin değişti, ancak iptal/vazgeçme kontrolü ya da NFR-01 hedefi sağlanmadı. | Açık; gerçek bulgu kaydedilir, ek iyileştirme ve yeniden kontrol planlanır. |
| İşlev kontrolleri ve NFR-01 hedefi sağlandı. | Sonuçlar sürüm ve kanıtlarıyla kaydedilir; kalan risk, olasılık ve takip ihtiyacı gerekçeyle yeniden değerlendirilir. Otomatik olarak risk sıfırlandı veya kapandı yazılmaz. |

Başarılı bir kullanılabilirlik ölçümü, yanlış iptalin gerçekleşme ihtimalini yeniden değerlendirmemize yardımcı olabilir. Yanlış iptal gerçekleşirse doğacak etkinin otomatik olarak azaldığını göstermez. Değerlendirme güncellenirse önceki Orta/Yüksek kaydı korunur; yeni tarihli karar ayrıca eklenir. Bu küçük sınıf ölçümü bütün kullanıcılar için genellenmiş bir sonuç değildir.

### Üç riskin mevcut takip durumu

| Risk | Durum | Bekleyen takip |
|---|---|---|
| RSK-01 | Açık | Metin iyileştirmesi, değişiklik sonrası işlev kontrolleri ve NFR-01 ölçümü. |
| RSK-02 | Açık | Ortam koşullarını ve referans kayıtları izlemek; saklama başarısızlığı koşulları ayrıca denenecekse ayrı test ortamında planlamak. Önceki yenileme gözlemi genel kalıcılık garantisi değildir. |
| RSK-03 | Açık | Gerçek ekip incelemesi ve her değişiklikte ilgili belgelerin yeniden karşılaştırılması. Öğretmen örneğinde yalnız belirtilen FR-05 karşılaştırması güncel kontrol olarak kayıtlıdır. |

## Kaydetme ve çalışma durumu

Bu dosya projenin docs/06-riskler.md yoluna kaydedilir. Başlangıçtaki boş risk şablonunun doldurulmuş öğretmen örneğidir; yeni bir belge türü değildir. Dosyanın amacı, üç riskin açıklamaları ve gözden geçirme bölümüyle çalışma metni tamamlandı. Bu, risklerin kapatıldığı veya bütün önlemlerin uygulandığı anlamına gelmez. Gerçek öğrenci sorumluları, uygulama tarihleri ve ölçüm sonuçları oluştukça güncellenecek.

Son kaydetme adımı: Güncel dosyayı docs/06-riskler.md olarak saklayın; kendiniz ek not yazdıysanız koruyun. Dosyayı yeniden açıp sürümün 1.0 olduğunu, üç riskin bulunduğunu ve RSK-01 için Açık — önlem ve ölçüm bekleniyor kararının korunduğunu kontrol edin. Bu dosyayı diagrams klasörüne koymayın.

27.10.2026 tarihli önceki kullanıcı görüntüsünde 06-riskler.md dosyası VS Code'da docs altında açık ve RSK-01–RSK-03 satırları görünür durumdadır. Görüntüde sürüm satırı ve dosyanın tamamı açık değildir; bu 1.0 sürümünün kullanıcı tarafından indirildiği/kaydedildiği sonucuna varılmaz.

Gerçek GitHub issue, kod değişikliği, yeni prototip testi, NFR ölçümü veya öğrenci incelemesi bu dosya hazırlanırken yapılmış sayılmaz.
