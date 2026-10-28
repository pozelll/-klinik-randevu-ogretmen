# 05 — İzlenebilirlik

Ekip: Öğretmen denemesi  
Hazırlık tarihi: 28.10.2026  
Sürüm: 0.8 — docs/izlenebilirlik dalına aktarılacak öğretmen çalışma metni  
Dosyanın yeri: docs/05-izlenebilirlik.md  
Aktarım öncesi hazırlık durumu: Altı FR için bağlantı satırları hazırlandı. Kullanıcı görüntülerindeki 03 / FR-01, 04 / AC-01 ve 08 / G-04 içerikleri öğretmen çalışma metinleriyle karşılaştırıldı ve birbiriyle uyumlu bulundu. docs/izlenebilirlik dalı oluşturuldu. Bu daldaki 05 dosyası 28.10.2026 tarihli görüntüde boş başlangıç şablonu olarak açıldı; bu çalışma metni onun güncellenmesi için hazırlandı. Diğer FR satırlarının karşılaştırılması, değişiklik commit'inin doğrulanması, pull request ve bağımsız inceleme henüz tamamlanmadı. Son görev listesi görüntüsünde ilk kutu boş, ikinci kutu işaretliydi; kutuların gerçekleşen işle eşleştirilmesi istendi, düzeltme sonucu henüz görülmedi. Yeni prototip testi yapılmadı.

## Amaç ve kaynaklar

Kullanıcı ihtiyacından gereksinime, kabul koşuluna, gerçek gözleme ve işi takip eden GitHub kartına ulaşmak. Değişiklik incelemeye açıldığında gerçek pull request bağlantısı da aynı satıra eklenecek.

Bu taslak, hazırladığımız öğretmen dosyalarına dayanır:

- [03-gereksinimler.md](03-gereksinimler.md) — belge sürümü 0.4.
- [04-kabul-kriterleri.md](04-kabul-kriterleri.md) — belge sürümü 1.0.
- [08-prototip-gozlemleri.md](08-prototip-gozlemleri.md) — 26–27.10.2026 tarihli öğretmen gözlemleri.

Issue numaraları ve adresleri, kullanıcının gönderdiği altı gerçek GitHub kart ekranından doğrulandı. Bu hazırlık, GitHub'da yüklü her belgenin bütün içeriğinin incelendiği anlamına gelmez. Kayıt kimlikleri öğretmen denemesine aittir; öğrenciler kendi gözlemlerini ve gerçek bağlantılarını kullanır.

## Proje bağlantıları

- Depo: [pozelll/-klinik-randevu-ogretmen](https://github.com/pozelll/-klinik-randevu-ogretmen).
- Pano: [Klinik Randevu - Öğretmen Görev Panosu](https://github.com/users/pozelll/projects/1/views/1).
- Çalışma dalı: [docs/izlenebilirlik](https://github.com/pozelll/-klinik-randevu-ogretmen/tree/docs/izlenebilirlik). 28.10.2026 tarihli kullanıcı ekranında bu dal seçili ve 2 Branches bilgisi görünür. Dal main ile güncel; son commit ilk yüklemenin 63aa3fa kaydı, toplam 1 Commit. Bu belge değişikliği için yeni commit veya PR henüz yok.
- 28.10.2026 tarihli son pano ekranı: Todo 5, In Progress 1, Done 0. FR-01 / Issue #1 kartı In Progress sütununda görüldü. Bu çalışma durumu, dosyaların GitHub'a aktarıldığı veya incelemenin tamamlandığı anlamına gelmez.

Pano durumu bu belgedeki anlık gözlem kaydıdır. Çalışma ilerledikçe gerçek pano ve ilgili kayıtlar güncellenir. Bir kartın açılması veya panoya alınması, karttaki işin tamamlandığını göstermez.

## Gereksinim–kabul koşulu–kanıt–görev tablosu

Tabloda her FR için ana eşleşme yer alır. İlgili ek senaryolar ve kapsam sınırları aşağıda açıklanmıştır. İlgili dosya sütunundaki 03, 04 ve 08, yukarıda bağlantısı verilen numaralı dosyalardır.

| Kullanıcı ihtiyacı | Gereksinim | Kabul koşulu | Gözlem kanıtı | GitHub Issue | İlgili dosya / bölüm | Pull request |
|---|---|---|---|---|---|---|
| Kullanıcı, seçili doktor ve tarihte hangi saatin uygun olduğunu anlayabilmeli. Hasta seçiminin değişmesi başka hastaya ayrılmış saati boşaltmamalı. | FR-01 — Saatleri listeleme | AC-01 — Hasta değişince saat doluluğunun korunması | G-04: Kaan seçildiğinde Deniz Arı / 12.11.2030 / 09:00 Dolu kaldı. | [#1 — FR-01](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/1) | 03: FR-01; 04: AC-01; 08: G-04 | Henüz oluşturulmadı. |
| Hasta veya resepsiyon uygun saate doğru kişi ve zaman bilgileriyle randevu oluşturabilmeli. Ana kanıt Hasta rolünün başarılı akışına aittir. | FR-02 — Randevu oluşturma | AC-02 — Uygun saate randevu oluşturma | G-01: Ece / Deniz / 12.11.2030 / 09:30 için R008 Bekliyor oluştu; saat Dolu oldu. | [#2 — FR-02](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/2) | 03: FR-02; 04: AC-02; 08: G-01 | Henüz oluşturulmadı. |
| Hasta kendi bekleyen randevusunu onaylayarak iptal edebilmeli; vazgeçerse randevusu korunmalı. | FR-03 — Kendi randevusunu iptal etme | AC-03 — İptali onaylama; ALT-01 — Vazgeçme | AC-03 → G-02: R008 İptal edildi, 09:30 Uygun. ALT-01 → G-03-T3: R011 Bekliyor, 09:00 Dolu kaldı. | [#3 — FR-03](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/3) | 03: FR-03; 04: AC-03 ve ALT-01; 08: G-02, G-03-T3 | Henüz oluşturulmadı. |
| Doktor ve resepsiyon, seçili doktorun seçili gündeki bütün örnek hasta kayıtlarını ve durumlarını birlikte izleyebilmeli. | FR-04 — Günlük liste | AC-04A — Doktor görünümü; AC-04B — Resepsiyonda hasta seçiminin listeyi daraltmaması | AC-04A → G-05: Ece ve Kaan, üç durumla listelendi. AC-04B → G-06: Kaan seçiliyken Ece'nin R011 kaydı da görüldü. | [#4 — FR-04](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/4) | 03: FR-04; 04: AC-04A/B; 08: G-05, G-06 | Henüz oluşturulmadı. |
| Doktor biten muayeneyi tamamlanmış olarak işaretleyebilmeli; kayıt, saat ve sayılar tutarlı değişmeli. | FR-05 — Randevuyu tamamlama | AC-05 — Doktorun bekleyen randevuyu tamamlaması | Sonuç G-05-B: R002 Tamamlandı, 10:00 Kapalı; düğme kalktı; sayılar 1/2/5/8 oldu. Başlangıç G-05: 2/1/5/8. | [#5 — FR-05](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/5) | 03: FR-05; 04: AC-05; 08: G-05, G-05-B | Henüz oluşturulmadı. |
| Doktor ve resepsiyon, seçili doktor ve tarihin günlük akışını doğru durum ve toplam kayıt sayılarıyla okuyabilmeli. | FR-06 — Günlük toplamlar | AC-06 — Doktordan Resepsiyona geçişte toplamların korunması | Sonuç G-06: 1/2/5/8 korundu. Başlangıç G-05-B; kayıt dökümü G-05 ve R002'nin sonraki durum değişimiyle açıklanır. | [#6 — FR-06](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/6) | 03: FR-06; 04: AC-06; 08: G-06, G-05-B, G-05 | Henüz oluşturulmadı. |

## İlk satırı birlikte okuma — FR-01

1. **İhtiyaç:** Kullanıcı uygun saati doğru anlamalı. Başka bir hastanın ayrılmış saati, hasta seçimi değişince boşalmamalı.
2. **FR-01:** 03 numaralı dosyada saatlerin hangi koşullarda Uygun, Dolu ve Kapalı gösterileceğini anlatır.
3. **AC-01:** 04 numaralı dosyada belirli bir durum seçer: Ece'den Kaan'a geçerken doktor ve tarih değişmez; 09:00 Dolu kalmalıdır.
4. **G-04:** 08 numaralı dosyada bu önceki denemenin gerçek sonucunu kaydeder. Beklenen sonuçla gözlenen sonuç burada karşılaştırılır.
5. **Issue #1:** Bu belge bağlantısının kontrolünü ve kalan değişiklik/inceleme işlerini takip eder.
6. **Pull request:** Henüz yok. Değişiklik gerçekten incelemeye açılınca oluşan bağlantı eklenecek.

Bu satırın hazır olması bütün FR-01 senaryolarının sınandığı veya Issue #1'in tamamlandığı anlamına gelmez. FR-01, AC-01 ve G-04 için aşağıda kaydedilen içerik karşılaştırması tamamlandı; gerçek değişikliğin depoya kaydı ve incelemesi sırada.

## GitHub'da içerik karşılaştırması — FR-01

28.10.2026 tarihli kullanıcı ekranında main dalındaki docs/03-gereksinimler.md dosyasının Preview görünümü ve FR-01 satırının tamamı okunuyor. Görünen satır, öğretmen çalışma kopyasının 0.4 sürümündeki FR-01 ile uyumlu bulundu.

| Kontrol edilen içerik | Görüntüdeki sonuç |
|---|---|
| Kapsam | Seçili doktor ve örnek tarihin sabit saatleri. |
| Saat durumu | İptal edilmemiş kayıt yoksa Uygun; Bekliyor varsa Dolu; Tamamlandı varsa Kapalı. |
| Saat seçimi | Hasta veya Resepsiyon uygun saat seçince seçili saat ayırt edilir. |
| Rol sınırı | Üç rol saatleri görür; Doktor randevu oluşturmak için saat seçemez. |
| Seçim değişikliği | Doktor veya tarih değişince saatler o seçime göre güncellenir. |
| Öncelik | Yüksek; uygun saati belirleme ve dolu/tamamlanmış saate yönelmeme gerekçesi açıklanmış. |

Bu karşılaştırmada FR-01 satırında düzeltme gerektiren fark bulunmadı. Ekranda belge başlığındaki sürüm alanı görünmedi; 03 belgesinin tüm içeriği veya sürüm etiketi doğrulanmış sayılmadı. Kanıt: sunum hazırlığı için saklanan kanitlar/github-fr01-gereksinim-kontrol-20261028.png.

### AC-01 bölümünün karşılaştırılması

28.10.2026 tarihli sonraki kullanıcı ekranında main / docs / 04-kabul-kriterleri.md dosyasının Preview görünümündeki AC-01 bölümü okundu. Başlık, FR-01 ve BR-01 bağlantısını açıklayan giriş, beş satırlık tablo, gerekçe ve örneğe özgü veri açıklaması öğretmen çalışma kopyasıyla uyumlu bulundu.

| Alan | GitHub'da görülen içerik |
|---|---|
| Verilen | Hasta / Ece Yılmaz / Deniz Arı / 12 Kasım 2030; Ece'nin R011 / 09:00 kaydı Bekliyor. |
| Ne zaman | Örnek hasta Kaan Demir olarak değiştirilir. |
| O zaman | Doktor ve tarih aynı kalırken B1'de 09:00 Dolu kalmalı; hasta değişimi saati Uygun yapmamalı. |
| Gerçek sonuç | G-04'te Kaan seçilince 09:00 Dolu kalmış; doktor ve tarih korunmuş. |
| Durum | Geçti — önceki G-04 gözlemine göre. Bu adımda yeniden çalıştırılmadı. |

Alt açıklama, saat uygunluğunun doktor + tarih + saat üzerinden değerlendirildiğini ve öğretmen örneğindeki kayıt kimliği yerine öğrencinin kendi gerçek verisini yazacağını açıkça belirtiyor. AC-01 bölümünde düzeltme gerektiren fark bulunmadı. Kanıt: sunum hazırlığı için saklanan kanitlar/github-ac01-kabul-kriteri-kontrol-20261028.png. Belgenin üstteki sürüm alanı bu karede görünmüyor; diğer kabul koşulları bu görüntüyle doğrulanmış sayılmadı.

### G-04 kaydının karşılaştırılması ve üç belgenin sonucu

28.10.2026 tarihli sonraki kullanıcı görüntüsünde G-04 satırının tamamı okunuyor. Satırın içeriği, 08-prototip-gozlemleri.md öğretmen çalışma kopyasındaki G-04 ile uyumlu. Bu son kare yalnız tabloyu gösteriyor; dosya yolu ve dal adı görünmüyor. Değerlendirme, istenen G-04 satırına yanıt olarak gönderilen görünür içeriğe dayanıyor.

| Alan | Görülen içerik ve karşılaştırma sonucu |
|---|---|
| Rol ve seçimler | Hasta / Kaan Demir / Deniz Arı / 12.11.2030. |
| Yapılan işlem | Hasta Ece yerine Kaan seçilmiş; doktor Deniz Arı ve 12 Kasım 2030 korunmuş. AC-01'deki eylemle uyumlu. |
| Beklenen | Kaan'ın kendi kayıtları görünmeli; hasta seçimi doktorun dolu saatlerini boşaltmamalı. |
| Gözlenen | Kaan'ın R002 / 10:00 Bekliyor ve R004 / 13:00 İptal edildi kayıtları görünmüş; Ece'nin kayıtları kendi listesinde görünmemiş. B1'de 09:00 ve 10:00 Dolu, 13:00 Uygun. |
| FR-01 / AC-01 için ana kanıt | Ece için ayrılmış 09:00, Kaan seçilince Dolu kalmış. |
| Sınır | Prototipin arayüz davranışı gözlemi; gerçek kimlik doğrulaması veya veri güvenliği testi değil. |

Sonuç: FR-01'in saat durumunu doktor/tarih üzerinden tanımlaması, AC-01'in hasta değişirken doktor/tarihi sabit tutması ve G-04'te 09:00'ın Dolu kalması birbirini destekliyor. Bu üç içerikte düzeltme gerektiren fark bulunmadı. Kanıt görüntüsü: kanitlar/github-g04-gozlem-kontrol-20261028.png. G-04'teki R002 / Bekliyor bilgisi önceki denemeye aittir; sonraki G-05-B'de tamamlanan kaydın bugünkü durumuyla değiştirilmez.

Issue #1'in ilk maddesindeki üç belgeyi karşılaştırma işi tamamlandı. İlk kutuyu işaretleme yönergesinden sonra gelen 28.10.2026 tarihli görev listesi görüntüsünde ilk kutu boş, ikinci kutu işaretli; üçüncü, dördüncü ve beşinci kutular boş. Bu kare yalnız Yapılacaklar ve Takip bölümünün başını gösterir; Issue başlığı/adresi görünmez. Kanıt: kanitlar/github-fr01-gorev-kutulari-20261028.png.

İşaretli ikinci kutu, 05 dosyasındaki bağlantıları ekleme maddesidir. Hazırlanan çalışma kopyası mevcut; ancak kullanıcının yerel kopyası ve GitHub'a aktarımı bu görüntüyle doğrulanmıyor. Kullanıcıya tamamlanan karşılaştırma için ilk kutuyu işaretlemesi ve ikinci kutuyu aktarım doğrulanana kadar şimdilik boş bırakması söylendi. Düzeltme sonucu henüz görülmedi. Diğer teslim ve inceleme işleri bekliyor. Yeni prototip testi yapılmadı; son görülen pano durumu In Progress olarak korunur.

## Ek bağlantılar ve kanıt kapsamı

- **FR-01'in durum değişimleri:** AC-02 / G-01 oluşturma sonrası Dolu, AC-03 / G-02 iptal sonrası Uygun, AC-05 / G-05-B tamamlama sonrası Kapalı durumuna destek verir. Her gözlem kendi rolü, başlangıcı ve eylemiyle değerlendirilir.
- **BR-01 ve reddedilen işlem:** AC-07, FR-01 ve FR-02 ile ilişkilidir. G-07'de kullanıcı, Resepsiyon / Kaan / Deniz / 12.11.2030 seçimlerinde 09:00 Dolu saatinin seçilemediğini, onayın pasif kaldığını, yeni kayıt oluşmadığını ve R011'in değişmediğini yazılı doğruladı. Bu adım için ekran görüntüsü yok; doğrudan ikinci oluşturma isteği veya eşzamanlı erişim testi yapılmış sayılmaz. İlgili görevler #1 ve #2'dir.
- **FR-02:** Resepsiyon rolünde oluşturma henüz elle denenmedi. R008, G-01'de oluşturuldu; daha sonraki G-02'de iptal edildi. Sonraki durum önceki başarılı oluşturma gözlemini değiştirmez.
- **FR-03'ün liste kapsamı:** G-04, Hasta rolünde Kaan'ın kendi kayıtlarının görünmesine destek verir. Gerçek kimlik doğrulaması veya sunucu güvenliği sonucu değildir. İptal sonrası saatin açılması, aynı doktor/tarih/saatte başka iptal edilmemiş kayıt bulunmaması koşuluna bağlıdır.
- **FR-04:** G-06, seçili hastadan başka bir hastanın da listelendiğini gösterir; bütün satırların yeniden tek tek denetlendiğini göstermez. G-05 ile G-06 arasında R002, G-05-B'de tamamlanmıştır. Durum farkı rol değişiminden kaynaklanmaz.
- **FR-05:** Yalnız Doktor rolü tamamlar; öğretmenin R002 kaydı zaten tamamlanmıştır. Yeni deneme yapılacaksa uygun Bekliyor başlangıcı ayrı belirlenir; bu belge için mevcut veriler sıfırlanmaz.
- **FR-06:** İptal edilen kayıtlar toplamda sayılır. AC-06 yalnız belirtilen rol geçişini kapsar. Hasta rolünde toplamların gizlenmesine ilişkin ayrı elle yapılmış gözlem yoktur; başka doktor/tarih ve bütün güncelleme yolları bu tek koşulla doğrulanmaz.

## Kalite gereksinimlerinin plan bağlantıları

Bu satırlarda ölçüm planı hazırdır; gerçek ölçüm kanıtı yoktur. Altı FR kartı açılması bu ölçümleri tamamlamaz.

| Gereksinim | Planın yeri | Gerçek ölçüm kanıtı | Ayrı Issue / pull request |
|---|---|---|---|
| NFR-01 — İptal ve vazgeçme görevlerinin kullanılabilirliği | 03: NFR-01; 04: AC-NFR-01 | Ölçülmedi. Önceki yönlendirilmiş öğretmen denemeleri dört katılımcılı ölçüm yerine geçmez. | Henüz oluşturulmadı. |
| NFR-02 — Doktor seçimi sonrası doğru içeriğin yanıt süresi | 03: NFR-02; 04: AC-NFR-02 | Ölçülmedi. On denemelik süre kaydı yok. | Henüz oluşturulmadı. |
| NFR-03 — Dört görevin klavyeyle yürütülmesi | 03: NFR-03; 04: AC-NFR-03 | Ölçülmedi. Gerçek klavye denemesi kaydı yok. | Henüz oluşturulmadı. |

## Kontrol

- [x] Her FR için en az bir kabul koşulu çalışma tablosunda yer alıyor.
- [ ] Altı FR kartı ile GitHub'daki ilgili belge ve gözlem içerikleri birlikte karşılaştırıldı. FR-01 karşılaştırması tamamlandı; FR-02–FR-06 bekliyor.
- [x] Gerçek Issue bağlantıları kullanıldı; oluşmamış PR alanlarına Henüz oluşturulmadı yazıldı.
- [ ] İlgili değişiklik, yazar veya ortak yazar olmayan kişinin incelemesinden geçti.

Bu kutular bağlantı tablosu ve inceleme durumunu gösterir; bütün işlev veya kalite testlerinin tamamlandığı anlamına gelmez.

## Çalışma ve inceleme durumu

| Kontrol | Bu taslaktaki durum |
|---|---|
| Her FR için ana kabul koşulu ve önceki gözlem eşleşmesi | Öğretmen çalışma dosyalarından hazırlandı. |
| Altı Issue'nun gerçek adresleri | Kullanıcı ekranlarından doğrulandı. |
| Görev panosu bağlantısı | Kullanıcının oluşturma sonrası ekranından alındı. |
| 03, 04 ve 08 içeriklerinin karşılaştırılması | FR-01 → AC-01 → G-04 için tamamlandı; kullanıcı görüntülerindeki içerikler uyumlu. Diğer FR satırları bekliyor. 03 ve 04'ün sürüm alanları, son G-04 karesinde ise dosya yolu/dal görünmüyor. |
| Issue #1'deki kontrol kutuları | Son kullanıcı görüntüsünde ilk kutu boş, ikinci kutu işaretli; diğer üçü boş. İçerik karşılaştırmasına karşılık ilk kutunun işaretlenmesi, aktarım doğrulanana kadar ikinci kutunun boş bırakılması istendi. Düzeltme sonucu bekliyor. |
| Dalda açılan 05 dosyasının mevcut içeriği | 28.10.2026 tarihli kullanıcı ekranında docs/izlenebilirlik dalında açıldı: 22 satır, 818 Bytes, FR-01–FR-06 için boş şablon alanları, son dosya commit'i 63aa3fa. |
| Bu dosyanın ve doldurulmuş ISSUE metinlerinin depoya güncellenmesi | Bu sürüm aktarım öncesinde hazırlandı; kaydetme sonucu henüz görülmedi. Doldurulmuş ISSUE kaynak metinleri ayrıca güncellenecek. |
| Gerçek çalışma dalı | docs/izlenebilirlik oluşturuldu ve seçili; kullanıcı ekranında 2 Branches ve main ile güncel bilgisi görüldü. Bağlantı Proje bağlantıları bölümünde. |
| Bu belge değişikliğine ait commit / pull request | Henüz oluşturulmadı. Dalın son kaydı ilk yüklemenin 63aa3fa commit'i; dal oluşturma yeni dosya değişikliği değildir. |
| Yazar veya ortak yazar olmayan kişinin incelemesi | Yapılmadı; inceleyen henüz belirlenmedi. |
| İnceleme bulgularının giderilmesi ve yeniden kontrolü | Gerçek inceleme sonrasında kaydedilecek. |

Asistanın belge eşleştirme hazırlığı, bağımsız öğrenci/arkadaş incelemesi olarak sayılmadı. İlgili değişiklik aynı pull request içinde birden fazla FR'yi kapsayabilir; ancak bağlantı her satırın gerçek değişikliğiyle ilişkili olmalıdır.

## Kaydetme ve sonraki güncelleme

1. Dosyayı bilgisayardaki projenin docs klasörüne 05-izlenebilirlik.md adıyla kaydet. Mevcut boş taslak yerine bu sürüm kullanılabilir; kendi ek notların varsa koru.
2. FR-01 → AC-01 → G-04 içerik karşılaştırması tamamlandı. Issue #1'in ilk kontrol maddesini işaretle; ikinci maddeyi dosyanın depoya aktarımı doğrulanınca tamamla. Diğer satırlar hazırlanmış taslaktır; kendi karşılaştırma ve inceleme kayıtları bekler.
3. GitHub'a aktarımı oluşturulan docs/izlenebilirlik dalında yapacağız; ardından gerçek değişiklik commit'i ve pull request kaydedilecek. Yerelde kaydetmek GitHub dosyasını değiştirmez.
4. Yeni bir test, inceleme veya pull request gerçekleşirse ilgili satırı gerçek kanıtla güncelle. Bekleyen alanlara örnek sonuç veya tahmini bağlantı yazma.
