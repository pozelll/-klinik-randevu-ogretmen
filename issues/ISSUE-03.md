# FR-03: randevu iptali gereksinimini doğrula ve izlenebilirliğini tamamla

Güncelleme: 28.10.2026 — kaynak belge sürümü 1.0.  
Gerçek kart: [Issue #3](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/3).  
Durum: Belge karşılaştırması tamamlandı; PR #7 açık, bağımsız inceleme ve son teslim kontrolü bekliyor.

Bu dosya, depodaki görev kaynak metnidir. Aşağıdaki işaretler yapılan işin durumunu kaydeder; çevrim içi Issue gövdesinin veya kutularının otomatik güncellendiği anlamına gelmez.

## Amaç

Hastanın kendi bekleyen randevusunu onaylayarak iptal etmesini ve iptal işleminden vazgeçtiğinde randevusunun korunmasını anlatan FR-03 gereksinimini, iki akışın kabul koşullarını ve gözlem kanıtlarını birbirine bağlamak.

Öğretmen belgelerinin çalışma metinleri hazır. Bu kart, gereksinim–kabul koşulu–gözlem bağlantısının kontrolünü, izlenebilirlik kaydını ve değişikliğin incelemesini takip eder.

## Gereksinim

FR-03: Hasta görünümünde yalnız seçili hastanın seçili doktor ve tarihteki kayıtları gösterilmelidir. Hasta kendi Bekliyor kaydını iptal etmek istediğinde onay sorulmalıdır. Onay verirse kayıt İptal edildi durumuyla listede kalmalı; aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt yoksa saat Uygun olmalıdır. Vazgeçerse randevu Bekliyor ve saat Dolu kalmalıdır.

Tamamlandı veya İptal edildi durumundaki kayıt iptal edilemez. Resepsiyon ve Doktor bu prototipte iptal işlemi yapamaz.

## Kabul koşulları

### AC-03 — İptali onaylama

- Verilen: Hasta / Ece Yılmaz / Deniz Arı / 12.11.2030 seçilidir. R008 / 09:30 Bekliyor, saat Dolu durumundadır. Aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt yoktur. R008 kartındaki İptal et düğmesiyle açılmış onay penceresi ekrandadır.
- Ne zaman: Kullanıcı onay penceresinde Tamam düğmesine basar.
- O zaman: R008, İptal edildi durumuyla listede kalmalı; 09:30 Uygun olmalıdır.

### ALT-01 — İptal işleminden vazgeçme

- Verilen: Hasta / Ece Yılmaz / Deniz Arı / 12.11.2030 seçilidir. R011 / 09:00 Bekliyor, saat Dolu durumundadır. R011 kartındaki İptal et düğmesiyle açılmış onay penceresi ekrandadır.
- Ne zaman: Kullanıcı onay penceresinde İptal düğmesine basar.
- O zaman: Pencere kapanmalı; R011 Bekliyor, 09:00 Dolu kalmalıdır.

Karttaki İptal et pencereyi açar. Penceredeki Tamam randevuyu iptal eder; penceredeki İptal işlemden vazgeçirir.

## Mevcut kanıt ve sınırı

- G-02: R008, İptal edildi olarak listede kaldı; 09:30 Uygun oldu. AC-03 bu önceki gözleme dayanır.
- G-03-T3: Kullanıcı pencerede İptal'e bastığını belirtti; görüntülerde R011 Bekliyor ve 09:00 Dolu kaldı. ALT-01 bu önceki gözleme dayanır.
- G-04: Hasta Kaan olarak seçildiğinde yalnız Kaan'ın seçili doktor ve tarihteki kayıtları göründü. FR-03'ün kendi kayıtlarını görme sınırına destekleyici gözlemdir.

Bugün yeni deneme yapılmadı. R008 zaten iptal edilmiş durumdadır; geçmiş deneyin Verilen koşulu mevcut durum gibi kabul edilmemelidir. Öğrenciler kendi denemelerinde gerçek başlangıç verilerini ve kayıt kimliklerini kullanır. Bu gözlemler gerçek kimlik doğrulaması veya NFR-01 kullanılabilirlik ölçümü değildir.

## Yapılacaklar

- [x] GitHub'daki docs/03-gereksinimler.md içinde FR-03, docs/04-kabul-kriterleri.md içinde AC-03 ve ALT-01 ile docs/08-prototip-gozlemleri.md içindeki G-02 ve G-03-T3 kayıtlarını karşılaştır; rol ve saat koşullarını koru.
- [x] docs/05-izlenebilirlik.md içindeki FR-03 satırına AC-03 → G-02 ve ALT-01 → G-03-T3 eşleşmelerini, ilgili dosyaları ve bu kart açıldıktan sonraki gerçek bağlantısını ekle. G-04'ü destekleyici liste gözlemi olarak ayrı belirt.
- [x] İlk izlenebilirlik değişikliğini ayrı dalda kaydet ve PR aç — docs/izlenebilirlik, a4bc1fc ve [PR #7](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7) ile gerçekleşti. Bu kaynak dosyanın güncellemesi aynı PR kapsamında izlenecek.
- [ ] Değişikliğin yazarı olmayan bir kişinin incelemesini al; özellikle iki onay seçeneğinin anlamını kontrol ettir. Bulguları işle ve gerekiyorsa yeniden kontrol et.
- [ ] Oluşan gerçek pull request bağlantısını izlenebilirlik kaydına ekle; son dosyanın erişilebilirliğini kontrol et.

### Yapılan belge kontrolünün kaydı

28.10.2026: Kullanıcının gönderdiği docs/izlenebilirlik ZIP kopyasında FR-03 → AC-03/G-02 ve ALT-01/G-03-T3; destekleyici G-04 birlikte okundu; açıklamalar ve önceki gözlem sonuçları tutarlı. 03, 04 ve 08 dosyaları güncel öğretmen kopyalarıyla birebir aynı. İncelenen commit: a4bc1fc89061f2b136bdaab085887acda62a0933.

05'in a4bc1fc ile kaydedilen 0.8 sürümünde bu FR'nin gerçek Issue bağlantısı ve eşleşmesi bulunuyor. Toplu güncellemedeki 1.0 sürümünde PR #7 ve bu kontrolün sonucu da var. Son güncellemenin GitHub'a aktarımı ve erişimi doğrulanmadan son görev işaretlenmez. Yeni prototip denemesi veya bağımsız kişi incelemesi yapılmadı.

## Takip

- Sorumlu: Pınar — öğretmen uygulaması; gerçek kartta pozelll ataması önceki kullanıcı ekranından doğrulandı.
- İnceleyen: Henüz belirlenmedi; bağımsız inceleme yapılmadı.
- Öncelik: Yüksek; hastanın iptal etme ve randevuyu koruma kararlarının doğru uygulanmasını belgeliyoruz.
- Hedef tarih: Henüz belirlenmedi.
- İlgili kimlikler: FR-03, AC-03, ALT-01, BR-01, G-02, G-03-T3; destekleyici G-04.
- İlgili gerçek kartlar: [FR-01 — #1](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/1), [FR-02 — #2](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/2).
- Bağımlılık: İlgili belgelerin güncel içeriğine erişim ve bu kartın gerçek bağlantısı.
- Pull request: [#7 — Açık](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7); docs/izlenebilirlik → main. Bu belge değişikliğiyle ilgili; üçüncü haftanın kod değişikliği PR'ı değildir.

## Tamamlandı ölçütü

FR-03'ün iki akışı doğru kabul koşulu ve kanıtla eşleşmeli; rol sınırı, iptal edilen kaydın listede kalması ve saatin açılma koşulu korunmalı; gerçek Issue ve pull request bağlantıları kaydedilmeli; bağımsız inceleme tamamlanmalı; engelleyici bulgular giderilip kontrol edilmeli ve son belgeye erişilebilmelidir. Kartın açılması veya belge görevinin tamamlanması, yeni test ya da NFR ölçümü yapıldığı anlamına gelmez.
