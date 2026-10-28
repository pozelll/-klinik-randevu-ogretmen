# FR-05: randevu tamamlama gereksinimini doğrula ve izlenebilirliğini tamamla

Güncelleme: 28.10.2026 — kaynak belge sürümü 1.0.  
Gerçek kart: [Issue #5](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/5).  
Durum: Belge karşılaştırması tamamlandı; PR #7 açık, bağımsız inceleme ve son teslim kontrolü bekliyor.

Bu dosya, depodaki görev kaynak metnidir. Aşağıdaki işaretler yapılan işin durumunu kaydeder; çevrim içi Issue gövdesinin veya kutularının otomatik güncellendiği anlamına gelmez.

## Amaç

Doktorun bekleyen muayeneyi tamamlanmış kayıttan ayırmasını sağlayan FR-05 gereksinimini, kabul koşulunu ve gözlem kanıtını birbirine bağlamak. Kaydın, saatin ve günlük toplamların tutarlı değişmesi birlikte ele alınır.

Öğretmen belgelerinin çalışma metinleri hazır. Bu kart, gereksinim–kabul koşulu–gözlem bağlantısının kontrolünü, izlenebilirlik kaydını ve değişikliğin incelemesini takip eder.

## Gereksinim

FR-05: Yalnız Doktor rolü, görevli olarak seçili doktorun seçili tarihteki Bekliyor kaydını tamamlayabilmelidir. İşlem sonrası kayıt Tamamlandı olmalı, ilgili saat Kapalı görünmeli ve aynı kayda yeniden tamamlama işlemi sunulmamalıdır. Durum değişikliği günlük toplamlara yansımalıdır. Hasta ve Resepsiyon tamamlama yapamaz.

Tamamlandı kaydı BR-01 açısından iptal edilmemiş kayıttır; o saat yeni randevuya açılmaz.

## Kabul koşulu

AC-05 — Doktorun bekleyen randevuyu tamamlaması:

- Verilen: Doktor rolü, Deniz Arı ve 12.11.2030 seçilidir. Kaan Demir'in R002 / 10:00 kaydı Bekliyor, saat Dolu durumundadır; kayıtta Tamamlandı işlem düğmesi vardır. Günlük toplamlar 2 bekleyen, 1 tamamlanan, 5 iptal edilen ve 8 toplam kayıttır.
- Ne zaman: Doktor, R002 kartındaki Tamamlandı düğmesine bir kez basar.
- O zaman: R002, Tamamlandı etiketiyle listede kalmalı; bu kaydın tamamlama düğmesi kalkmalıdır. 10:00 Kapalı olmalıdır. Günlük toplamlar 1 bekleyen, 2 tamamlanan, 5 iptal edilen ve 8 toplam kayıt olmalıdır.

Genel sayı ilişkisi: Bekleyen bir azalır, tamamlanan bir artar; iptal edilen ve toplam kayıt sayısı değişmez. Sayılanlar seçili doktor ve tarihin randevu kayıtlarıdır.

## Mevcut kanıt ve sınırı

docs/08-prototip-gozlemleri.md içindeki G-05, başlangıçtaki R002 kaydını ve 2 / 1 / 5 / 8 sayılarını gösterir. G-05-B'de R002 Tamamlandı, 10:00 Kapalı ve tamamlama düğmesi kaldırılmış olarak görülmüştür. Sayılar 1 / 2 / 5 / 8 olmuştur. AC-05 bu önceki gözleme dayanır.

Bugün yeni deneme yapılmadı. R002 mevcut öğretmen verisinde zaten Tamamlandı durumundadır; geçmiş başlangıcı kurmak için kayıtlar sıfırlanmaz. Öğrenciler kendi Bekliyor kayıtlarıyla deneme yaptıklarında gerçek kimlikleri ve önce/sonra sayılarını yazar. R002 veya toplam 8, her öğrenci için zorunlu sonuç değildir.

Bu sonuç, belirtilen prototip senaryosunun gözlemidir; gerçek kimlik doğrulaması veya bütün yetkisiz işlem yollarının güvenlik testi değildir. Kaydın Tamamlandı işlem düğmesi, iptal onayı penceresindeki Tamam düğmesinden ayrı bir arayüz öğesidir.

## Yapılacaklar

- [x] GitHub'daki docs/03-gereksinimler.md içinde FR-05, docs/04-kabul-kriterleri.md içinde AC-05 ve docs/08-prototip-gozlemleri.md içindeki G-05-B metinlerini karşılaştır; G-05'teki başlangıçla tutarlılığını kontrol et.
- [x] docs/05-izlenebilirlik.md içindeki FR-05 satırına AC-05, sonuç kanıtı G-05-B, başlangıç dayanağı G-05, ilgili dosyalar ve bu kart açıldıktan sonraki gerçek bağlantısını ekle.
- [x] İlk izlenebilirlik değişikliğini ayrı dalda kaydet ve PR aç — docs/izlenebilirlik, a4bc1fc ve [PR #7](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7) ile gerçekleşti. Bu kaynak dosyanın güncellemesi aynı PR kapsamında izlenecek.
- [ ] Değişikliğin yazarı olmayan bir kişinin incelemesini al; özellikle yalnız Doktor rolü, saatin Kapalı olması, düğmenin kalkması ve toplamın korunmasını kontrol ettir. Bulguları işle ve gerekiyorsa yeniden kontrol et.
- [ ] Oluşan gerçek pull request bağlantısını izlenebilirlik kaydına ekle; son dosyanın erişilebilirliğini kontrol et.

### Yapılan belge kontrolünün kaydı

28.10.2026: Kullanıcının gönderdiği docs/izlenebilirlik ZIP kopyasında FR-05 → AC-05 → G-05-B; başlangıç G-05 birlikte okundu; açıklamalar ve önceki gözlem sonuçları tutarlı. 03, 04 ve 08 dosyaları güncel öğretmen kopyalarıyla birebir aynı. İncelenen commit: a4bc1fc89061f2b136bdaab085887acda62a0933.

05'in a4bc1fc ile kaydedilen 0.8 sürümünde bu FR'nin gerçek Issue bağlantısı ve eşleşmesi bulunuyor. Toplu güncellemedeki 1.0 sürümünde PR #7 ve bu kontrolün sonucu da var. Son güncellemenin GitHub'a aktarımı ve erişimi doğrulanmadan son görev işaretlenmez. Yeni prototip denemesi veya bağımsız kişi incelemesi yapılmadı.

## Takip

- Sorumlu: Pınar — öğretmen uygulaması; gerçek kartta pozelll ataması önceki kullanıcı ekranından doğrulandı.
- İnceleyen: Henüz belirlenmedi; bağımsız inceleme yapılmadı.
- Öncelik: Yüksek; muayenenin tamamlanma durumunu ve ilgili saatin yeniden kullanıma açılmamasını belgeliyoruz.
- Hedef tarih: Henüz belirlenmedi.
- İlgili kimlikler: FR-05, AC-05, G-05-B, G-05; saat için FR-01 ve BR-01, sayılar için FR-06.
- İlgili gerçek kart: [FR-04 — #4](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/4); işlemin yapıldığı günlük listeyle ilişki için.
- Bağımlılık: İlgili belgelerin güncel içeriğine erişim ve bu kartın gerçek bağlantısı.
- Pull request: [#7 — Açık](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7); docs/izlenebilirlik → main. Bu belge değişikliğiyle ilgili; üçüncü haftanın kod değişikliği PR'ı değildir.

## Tamamlandı ölçütü

FR-05, AC-05 ve G-05-B bağlantısı tutarlı olmalı; Doktor rolü sınırı, saat ve düğme sonucu, önce/sonra sayıları ve toplamın korunması doğru açıklanmalı; gerçek Issue ve pull request bağlantıları kaydedilmeli; bağımsız inceleme tamamlanmalı; engelleyici bulgular giderilip kontrol edilmeli ve son belgeye erişilebilmelidir. Kartın açılması veya belge görevinin tamamlanması, yeni prototip testi yapıldığı anlamına gelmez.
