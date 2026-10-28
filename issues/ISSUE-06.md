# FR-06: günlük toplam gereksinimini doğrula ve izlenebilirliğini tamamla

Güncelleme: 28.10.2026 — kaynak belge sürümü 1.0.  
Gerçek kart: [Issue #6](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/6).  
Durum: Belge karşılaştırması tamamlandı; PR #7 açık, bağımsız inceleme ve son teslim kontrolü bekliyor.

Bu dosya, depodaki görev kaynak metnidir. Aşağıdaki işaretler yapılan işin durumunu kaydeder; çevrim içi Issue gövdesinin veya kutularının otomatik güncellendiği anlamına gelmez.

## Amaç

Resepsiyon ve Doktor rollerinin günlük randevu akışını doğru sayılarla takip etmesini sağlayan FR-06 gereksinimini, kabul koşulunu ve gözlem kanıtını birbirine bağlamak.

Öğretmen belgelerinin çalışma metinleri hazır. Bu kart, gereksinim–kabul koşulu–gözlem bağlantısının kontrolünü, izlenebilirlik kaydını ve değişikliğin incelemesini takip eder.

## Gereksinim

FR-06: Resepsiyon ve Doktor rollerinde, seçili doktor ve tarihin Bekleyen, Tamamlanan, İptal edilen ve Toplam kayıt sayıları gösterilmelidir. Toplam kayıt sayısı üç durumun toplamına eşit olmalıdır. Randevu oluşturma, durum değişimi veya doktor/tarih seçimi değiştiğinde sayılar mevcut kayıtlarla tutarlı güncellenmelidir. Hasta rolünde bu sayılar gösterilmemelidir.

İptal edilen kayıtlar toplam kayıt sayısına dahildir. Sayılanlar randevu kayıtlarıdır; toplam kayıt sayısı farklı hasta sayısı veya dolu saat sayısı değildir.

## Kabul koşulu

AC-06 — Doktordan Resepsiyona geçişte günlük toplamların korunması:

- Verilen: Doktor rolü, Deniz Arı ve 12.11.2030 seçilidir; örnek hasta seçimi Kaan olarak korunmuştur. G-05-B sonrasında R011 Bekliyor, R002 ve R003 Tamamlandı; R001, R004, R008, R009 ve R010 İptal edildi durumundadır. Günlük toplamlar 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıttır.
- Ne zaman: Kullanıcı doktoru, tarihi ve kayıtları değiştirmeden Resepsiyon rolüne geçer.
- O zaman: Günlük toplamlar 1 / 2 / 5 / 8 olarak kalmalı ve seçili doktor/tarihin kayıtlarıyla uyuşmalıdır. Kaan seçili olması sayıları yalnız Kaan'ın kayıtlarıyla sınırlandırmamalıdır.

İki kontrol birlikte yapılır: Her durumun sayısı ilgili kayıtlara eşit olmalı ve üç durumun toplamı Toplam kayıt değerini vermelidir. Öğretmen örneği: 1 + 2 + 5 = 8.

## Mevcut kanıt ve sınırı

docs/08-prototip-gozlemleri.md içindeki G-05-B'de doktor görünümünün toplamları 1 / 2 / 5 / 8'dir. G-06'da Resepsiyon rolünde, Kaan seçiliyken aynı toplamlar görülmüştür. AC-06 bu önceki rol geçişi gözlemine dayanır.

Kayıt dökümü G-05'teki kimlikler ve G-05-B'deki R002 durum değişimiyle açıklanır. G-06'da bütün liste satırlarının yeniden tek tek incelendiği iddia edilmez; doğrudan sonuç kanıtı görünen günlük toplam değerleridir.

Bugün yeni deneme yapılmadı. Bu senaryo, başka doktor/tarih, boş liste, oluşturma veya iptal sonrası bütün güncelleme yollarını kapsamaz. Hasta rolünde sayıların gizlenmesi gereksinimde ve kodda vardır; bu konuda ayrı elle yapılmış gözlem henüz kaydedilmedi. Öğrenciler kendi başlangıç kayıtlarını sayar; toplamlarının 8 olması zorunlu değildir.

## Yapılacaklar

- [x] GitHub'daki docs/03-gereksinimler.md içinde FR-06, docs/04-kabul-kriterleri.md içinde AC-06 ve docs/08-prototip-gozlemleri.md içindeki G-06 metinlerini karşılaştır; G-05-B başlangıcını ve G-05 kayıt dökümünü dikkate al.
- [x] docs/05-izlenebilirlik.md içindeki FR-06 satırına AC-06, sonuç kanıtı G-06, başlangıç dayanağı G-05-B, ilgili dosyalar ve bu kart açıldıktan sonraki gerçek bağlantısını ekle.
- [x] İlk izlenebilirlik değişikliğini ayrı dalda kaydet ve PR aç — docs/izlenebilirlik, a4bc1fc ve [PR #7](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7) ile gerçekleşti. Bu kaynak dosyanın güncellemesi aynı PR kapsamında izlenecek.
- [ ] Değişikliğin yazarı olmayan bir kişinin incelemesini al; özellikle doktor/tarih kapsamını, iptallerin toplama dahil olmasını ve kanıtın kapsam sınırını kontrol ettir. Bulguları işle ve gerekiyorsa yeniden kontrol et.
- [ ] Oluşan gerçek pull request bağlantısını izlenebilirlik kaydına ekle; son dosyanın erişilebilirliğini kontrol et.

### Yapılan belge kontrolünün kaydı

28.10.2026: Kullanıcının gönderdiği docs/izlenebilirlik ZIP kopyasında FR-06 → AC-06 → G-06; başlangıç G-05-B ve kayıt dökümü G-05 birlikte okundu; açıklamalar ve önceki gözlem sonuçları tutarlı. 03, 04 ve 08 dosyaları güncel öğretmen kopyalarıyla birebir aynı. İncelenen commit: a4bc1fc89061f2b136bdaab085887acda62a0933.

05'in a4bc1fc ile kaydedilen 0.8 sürümünde bu FR'nin gerçek Issue bağlantısı ve eşleşmesi bulunuyor. Toplu güncellemedeki 1.0 sürümünde PR #7 ve bu kontrolün sonucu da var. Son güncellemenin GitHub'a aktarımı ve erişimi doğrulanmadan son görev işaretlenmez. Yeni prototip denemesi veya bağımsız kişi incelemesi yapılmadı.

## Takip

- Sorumlu: Pınar — öğretmen uygulaması; gerçek kartta pozelll ataması önceki kullanıcı ekranından doğrulandı.
- İnceleyen: Henüz belirlenmedi; bağımsız inceleme yapılmadı.
- Öncelik: Orta; günlük akışın hızlı okunmasını sağlar, ayrıntılar günlük listede de bulunur. Başlangıç sürümünün kapsamındadır.
- Hedef tarih: Henüz belirlenmedi.
- İlgili kimlikler: FR-06, AC-06, G-06; başlangıç için G-05-B ve kayıt dökümü için G-05.
- İlgili gerçek kartlar: [FR-04 — #4](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/4), [FR-05 — #5](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/5).
- Bağımlılık: İlgili belgelerin güncel içeriğine erişim ve bu kartın gerçek bağlantısı.
- Pull request: [#7 — Açık](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7); docs/izlenebilirlik → main. Bu belge değişikliğiyle ilgili; üçüncü haftanın kod değişikliği PR'ı değildir.

## Tamamlandı ölçütü

FR-06, AC-06 ve G-06 bağlantısı tutarlı olmalı; seçili doktor/tarih kapsamı, üç durumun sayımı, iptallerin toplamda yer alması ve gözlemin sınırları doğru açıklanmalı; gerçek Issue ve pull request bağlantıları kaydedilmeli; bağımsız inceleme tamamlanmalı; engelleyici bulgular giderilip kontrol edilmeli ve son belgeye erişilebilmelidir. Kartın açılması veya belge görevinin tamamlanması, bütün güncelleme yollarının test edildiği anlamına gelmez.
