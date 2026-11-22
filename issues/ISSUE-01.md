# FR-01: uygun saat gereksinimini doğrula ve izlenebilirliğini tamamla

Güncelleme: 28.10.2026 — kaynak belge sürümü 1.0.  
Gerçek kart: [Issue #1](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/1).  
Durum: Belge karşılaştırması tamamlandı; PR #7 açık, bağımsız inceleme ve son teslim kontrolü bekliyor.

Bu dosya, depodaki görev kaynak metnidir. Aşağıdaki işaretler yapılan işin durumunu kaydeder; çevrim içi Issue gövdesinin veya kutularının otomatik güncellendiği anlamına gelmez.

## Amaç

Kullanıcının seçili doktor ve tarihte hangi saatlerin uygun olduğunu doğru anlamasını sağlayan FR-01 gereksinimini, kabul koşulunu ve gözlem kanıtını birbirine bağlamak.

Öğretmen belgelerinin çalışma metinleri hazır. Bu kart, gereksinim–kabul koşulu–gözlem bağlantısının kontrolünü, izlenebilirlik kaydını ve değişikliğin incelemesini takip eder.

## Gereksinim ve kabul koşulu

FR-01: Seçili doktor ve tarihin saatleri gösterilmelidir. İptal edilmemiş kayıt yoksa Uygun, Bekliyor kaydı varsa Dolu, Tamamlandı kaydı varsa Kapalı görünmelidir. Saatleri üç rol de görür; Doktor randevu oluşturmak için saat seçemez.

AC-01 — Hasta değişince saat doluluğunun korunması:

- Verilen: Hasta rolünde Ece Yılmaz, doktor Deniz Arı ve 12.11.2030 seçilidir. Ece'nin 09:00 saatindeki R011 kaydı Bekliyor durumundadır.
- Ne zaman: Örnek hasta Kaan Demir olarak değiştirilir.
- O zaman: Doktor ve tarih aynı kalırken 09:00 Dolu kalmalıdır. Hasta değişimi doktorun ayrılmış saatini boşaltmamalıdır.

## Mevcut kanıt

docs/08-prototip-gozlemleri.md içindeki G-04: Kaan seçildiğinde 09:00 Dolu kaldı. AC-01'in sonucu bu önceki öğretmen gözlemine dayanır; bugün yeni test yapılmadı.

AC-01, FR-01'in bir senaryosudur; bütün rollerin ve bütün saat durumlarının eksiksiz sınandığı anlamına gelmez. Öğrenciler kendi denemelerinde gerçek kayıt kimliklerini ve sonuçlarını yazar.

## Yapılacaklar

- [x] GitHub'daki docs/03-gereksinimler.md içindeki FR-01, docs/04-kabul-kriterleri.md içindeki AC-01 ve docs/08-prototip-gozlemleri.md içindeki G-04 metinlerini karşılaştır.
- [x] docs/05-izlenebilirlik.md içinde FR-01 satırına AC-01, G-04, ilgili dosyalar ve bu kartın oluşturulduktan sonraki gerçek bağlantısını ekle.
- [x] İlk izlenebilirlik değişikliğini ayrı dalda kaydet ve PR aç — docs/izlenebilirlik, a4bc1fc ve [PR #7](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7) ile gerçekleşti. Bu kaynak dosyanın güncellemesi aynı PR kapsamında izlenecek.
- [ ] Değişikliğin yazarı olmayan bir kişinin incelemesini al; bulguları işle ve gerekiyorsa yeniden kontrol et.
- [ ] Oluşan gerçek pull request bağlantısını izlenebilirlik kaydına ekle; son dosyanın erişilebilirliğini kontrol et.

### Yapılan belge kontrolünün kaydı

28.10.2026: Kullanıcının gönderdiği docs/izlenebilirlik ZIP kopyasında FR-01 → AC-01 → G-04 birlikte okundu; açıklamalar ve önceki gözlem sonuçları tutarlı. 03, 04 ve 08 dosyaları güncel öğretmen kopyalarıyla birebir aynı. İncelenen commit: a4bc1fc89061f2b136bdaab085887acda62a0933.

05'in a4bc1fc ile kaydedilen 0.8 sürümünde bu FR'nin gerçek Issue bağlantısı ve eşleşmesi bulunuyor. Toplu güncellemedeki 1.0 sürümünde PR #7 ve bu kontrolün sonucu da var. Son güncellemenin GitHub'a aktarımı ve erişimi doğrulanmadan son görev işaretlenmez. Yeni prototip denemesi veya bağımsız kişi incelemesi yapılmadı.

## Takip

- Sorumlu: Pınar — öğretmen uygulaması; gerçek kartta pozelll ataması önceki kullanıcı ekranından doğrulandı.
- İnceleyen: Henüz belirlenmedi; bağımsız inceleme yapılmadı.
- Öncelik: Yüksek; ilk gereksinim–kabul koşulu–kanıt bağlantısını kuruyoruz.
- Hedef tarih: Henüz belirlenmedi.
- İlgili kimlikler: FR-01, AC-01, BR-01, G-04.
- Bağımlılık: İlgili belgelerin güncel içeriğine erişim ve kartın gerçek bağlantısı.
- Pull request: [#7 — Açık](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7); docs/izlenebilirlik → main. Bu belge değişikliğiyle ilgili; üçüncü haftanın kod değişikliği PR'ı değildir.

## Tamamlandı ölçütü

FR-01, AC-01 ve G-04 bağlantısı tutarlı olmalı; gerçek Issue ve pull request bağlantıları kaydedilmeli; bağımsız inceleme tamamlanmalı; engelleyici bulgular giderilip kontrol edilmeli ve son belgeye erişilebilmelidir. Kartın açılması bu işlerin tamamlandığı anlamına gelmez.
