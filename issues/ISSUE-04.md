# FR-04: günlük liste gereksinimini doğrula ve izlenebilirliğini tamamla

Güncelleme: 28.10.2026 — kaynak belge sürümü 1.0.  
Gerçek kart: [Issue #4](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/4).  
Durum: Belge karşılaştırması tamamlandı; PR #7 açık, bağımsız inceleme ve son teslim kontrolü bekliyor.

Bu dosya, depodaki görev kaynak metnidir. Aşağıdaki işaretler yapılan işin durumunu kaydeder; çevrim içi Issue gövdesinin veya kutularının otomatik güncellendiği anlamına gelmez.

## Amaç

Resepsiyon ve Doktor rollerinin seçili doktorun seçili gündeki randevularını ve durumlarını birlikte takip etmesini anlatan FR-04 gereksinimini, kabul koşullarını ve gözlem kanıtlarını birbirine bağlamak.

Öğretmen belgelerinin çalışma metinleri hazır. Bu kart, gereksinim–kabul koşulu–gözlem bağlantısının kontrolünü, izlenebilirlik kaydını ve değişikliğin incelemesini takip eder.

## Gereksinim

FR-04: Resepsiyon ve Doktor rollerinde seçili doktorun seçili tarihteki bütün örnek hasta kayıtları gösterilmelidir. Bekliyor, Tamamlandı ve İptal edildi durumları ayırt edilebilmelidir. Resepsiyondaki örnek hasta seçimi günlük listeyi tek hastaya daraltmamalıdır.

Kapsam yalnız seçili doktor ve tarihtir. Hasta rolü, FR-03 kapsamında kendi kayıtlarını görür. Bu rol seçimi prototip simülasyonudur; gerçek kimlik doğrulaması veya sunucu tarafında erişim denetimi değildir.

## Kabul koşulları

### AC-04A — Doktor görünümü

- Verilen: Hasta rolü, Kaan Demir, Deniz Arı ve 12.11.2030 seçilidir. Bu doktor ve tarihte Ece ile Kaan'ın kayıtları vardır. R011 ve R002 Bekliyor, R003 Tamamlandı; R001, R009, R010, R008 ve R004 İptal edildi durumundadır.
- Ne zaman: Simülasyon rolü Doktor yapılır.
- O zaman: Günlük listede seçili doktor ve tarihin Ece ve Kaan kayıtları birlikte görünmeli; üç kayıt durumu ayırt edilebilmelidir.

### AC-04B — Resepsiyonda hasta seçimi listeyi daraltmaz

- Verilen: Doktor rolü, Deniz Arı ve 12.11.2030 seçilidir. Örnek hasta seçimi Kaan Demir olarak korunmuştur. Ece'nin R011 / 09:00 kaydı Bekliyor, Kaan'ın R002 / 10:00 kaydı Tamamlandı durumundadır.
- Ne zaman: Simülasyon rolü Resepsiyon yapılır.
- O zaman: Kaan seçiliyken günlük listede Ece'nin R011 / 09:00 / Bekliyor kaydı da görünmelidir. Liste Kaan'ın kayıtlarıyla sınırlandırılmamalıdır.

## Mevcut kanıt ve sınırı

- G-05: Doktor görünümünde Ece ve Kaan'ın kayıtları, üç durumla birlikte görüldü. AC-04A bu önceki gözleme dayanır.
- G-06: Resepsiyon görünümünde Kaan seçiliyken Ece'nin kayıtları ve R011 / 09:00 / Bekliyor görüldü. AC-04B bu önceki gözleme dayanır; bu görüntü bütün kayıtların tek tek yeniden denetlendiği anlamına gelmez.
- G-05 ile G-06 arasında G-05-B işlemi yapıldı ve doktor R002'yi tamamladı. İki gözlemde R002'nin farklı durumda olmasının nedeni bu işlemdir; rol değişimi değildir.

Bugün yeni deneme yapılmadı. İki senaryo kendi başlangıç durumuyla değerlendirilir; mevcut kayıtlar eski başlangıcı yeniden kurmak için değiştirilmez. Öğrenciler kendi denemelerindeki gerçek kayıt kimliklerini ve durumları kullanır. Resepsiyonun listeyi görmesi, o rolde yeni randevu oluşturma işleminin de elle denendiğini göstermez.

## Yapılacaklar

- [x] GitHub'daki docs/03-gereksinimler.md içinde FR-04, docs/04-kabul-kriterleri.md içinde AC-04A ve AC-04B ile docs/08-prototip-gozlemleri.md içindeki G-05 ve G-06 kayıtlarını karşılaştır; doktor/tarih sınırını ve gözlemlerin zaman sırasını koru.
- [x] docs/05-izlenebilirlik.md içindeki FR-04 satırına AC-04A → G-05 ve AC-04B → G-06 eşleşmelerini, ilgili dosyaları ve bu kart açıldıktan sonraki gerçek bağlantısını ekle.
- [x] İlk izlenebilirlik değişikliğini ayrı dalda kaydet ve PR aç — docs/izlenebilirlik, a4bc1fc ve [PR #7](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7) ile gerçekleşti. Bu kaynak dosyanın güncellemesi aynı PR kapsamında izlenecek.
- [ ] Değişikliğin yazarı olmayan bir kişinin incelemesini al; özellikle Resepsiyondaki hasta seçiminin listeyi daraltmadığını ve iki gözlemin farklı başlangıçlarını kontrol ettir. Bulguları işle ve gerekiyorsa yeniden kontrol et.
- [ ] Oluşan gerçek pull request bağlantısını izlenebilirlik kaydına ekle; son dosyanın erişilebilirliğini kontrol et.

### Yapılan belge kontrolünün kaydı

28.10.2026: Kullanıcının gönderdiği docs/izlenebilirlik ZIP kopyasında FR-04 → AC-04A/G-05 ve AC-04B/G-06; aradaki G-05-B durum değişimi birlikte okundu; açıklamalar ve önceki gözlem sonuçları tutarlı. 03, 04 ve 08 dosyaları güncel öğretmen kopyalarıyla birebir aynı. İncelenen commit: a4bc1fc89061f2b136bdaab085887acda62a0933.

05'in a4bc1fc ile kaydedilen 0.8 sürümünde bu FR'nin gerçek Issue bağlantısı ve eşleşmesi bulunuyor. Toplu güncellemedeki 1.0 sürümünde PR #7 ve bu kontrolün sonucu da var. Son güncellemenin GitHub'a aktarımı ve erişimi doğrulanmadan son görev işaretlenmez. Yeni prototip denemesi veya bağımsız kişi incelemesi yapılmadı.

## Takip

- Sorumlu: Pınar — öğretmen uygulaması; gerçek kartta pozelll ataması önceki kullanıcı ekranından doğrulandı.
- İnceleyen: Henüz belirlenmedi; bağımsız inceleme yapılmadı.
- Öncelik: Yüksek; klinik çalışanlarının doğru günlük listeyi ve kayıt durumlarını görmesini belgeliyoruz.
- Hedef tarih: Henüz belirlenmedi.
- İlgili kimlikler: FR-04, AC-04A, AC-04B, G-05, G-06; zaman sırasını açıklayan G-05-B.
- İlgili gerçek kart: [FR-03 — #3](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/3); Hasta rolünün kendi kayıtlarını görme kapsamıyla karşılaştırma için.
- Bağımlılık: İlgili belgelerin güncel içeriğine erişim ve bu kartın gerçek bağlantısı.
- Pull request: [#7 — Açık](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7); docs/izlenebilirlik → main. Bu belge değişikliğiyle ilgili; üçüncü haftanın kod değişikliği PR'ı değildir.

## Tamamlandı ölçütü

FR-04'ün iki senaryosu doğru kabul koşulu ve kanıtla eşleşmeli; seçili doktor/tarih kapsamı, rol farkları ve gözlemlerin zaman sırası korunmalı; gerçek Issue ve pull request bağlantıları kaydedilmeli; bağımsız inceleme tamamlanmalı; engelleyici bulgular giderilip kontrol edilmeli ve son belgeye erişilebilmelidir. Kartın açılması veya belge görevinin tamamlanması, yeni prototip testi ya da gerçek erişim güvenliği doğrulaması yapıldığı anlamına gelmez.
