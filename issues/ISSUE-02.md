# FR-02: randevu oluşturma gereksinimini doğrula ve izlenebilirliğini tamamla

Güncelleme: 28.10.2026 — kaynak belge sürümü 1.0.  
Gerçek kart: [Issue #2](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/2).  
Durum: Belge karşılaştırması tamamlandı; PR #7 açık, bağımsız inceleme ve son teslim kontrolü bekliyor.

Bu dosya, depodaki görev kaynak metnidir. Aşağıdaki işaretler yapılan işin durumunu kaydeder; çevrim içi Issue gövdesinin veya kutularının otomatik güncellendiği anlamına gelmez.

## Amaç

Uygun saate doğru hasta, doktor, tarih ve saat bilgileriyle randevu oluşturulmasını anlatan FR-02 gereksinimini, kabul koşulunu ve gözlem kanıtını birbirine bağlamak.

Öğretmen belgelerinin çalışma metinleri hazır. Bu kart, gereksinim–kabul koşulu–gözlem bağlantısının kontrolünü, izlenebilirlik kaydını ve değişikliğin incelemesini takip eder.

## Gereksinim ve kabul koşulu

FR-02: Hasta kendi canlandırdığı örnek kişi adına, Resepsiyon seçili örnek hasta adına uygun saati seçip onayladığında yeni randevu oluşturulmalıdır. Kayıt doğru hasta, doktor, tarih ve saat bilgileriyle Bekliyor görünmeli; saat Dolu olmalıdır. Aynı doktor, tarih ve saatte iptal edilmemiş başka kayıt varsa ikinci kayıt oluşturulmamalıdır (BR-01). Doktor rolü randevu oluşturamaz.

AC-02 — Hasta rolünde uygun saate randevu oluşturma:

- Verilen: Hasta rolü, Ece Yılmaz, Deniz Arı ve 12.11.2030 seçilidir. 09:30 için iptal edilmemiş başka kayıt yoktur; kullanıcı uygun olan 09:30 saatini seçmiştir.
- Ne zaman: Kullanıcı Randevuyu onayla düğmesine bir kez basar.
- O zaman: Randevularım alanında bu hasta, doktor, tarih ve saate ait yeni kayıt Bekliyor görünmeli; 09:30 Dolu olmalıdır.

## Mevcut kanıt ve sınırı

docs/08-prototip-gozlemleri.md içindeki G-01: R008 kaydı Ece Yılmaz / Deniz Arı / 12.11.2030 / 09:30 bilgileriyle Bekliyor olarak oluştu; 09:30 Dolu oldu. AC-02'nin sonucu bu önceki öğretmen gözlemine dayanır; bugün yeni test yapılmadı.

R008 daha sonraki G-02 denemesinde iptal edildi. Şimdi İptal edildi görünmesi, önceki oluşturma gözlemini değiştirmez. Öğrencilerin kendi denemelerinde oluşan gerçek kayıt kimliği kullanılmalıdır.

G-01, Hasta rolünün başarılı oluşturma akışını kapsar. Resepsiyon rolünde oluşturma henüz elle denenmedi. Dolu saate ikinci kayıt, eşzamanlı erişim ve yanıt süresi bu gözlemle doğrulanmış sayılmaz.

## Yapılacaklar

- [x] GitHub'daki docs/03-gereksinimler.md içindeki FR-02, docs/04-kabul-kriterleri.md içindeki AC-02 ve docs/08-prototip-gozlemleri.md içindeki G-01 metinlerini karşılaştır; gözlemin kapsam sınırını koru.
- [x] docs/05-izlenebilirlik.md içinde FR-02 satırına AC-02, G-01, ilgili dosyalar ve bu kartın oluşturulduktan sonraki gerçek bağlantısını ekle.
- [x] İlk izlenebilirlik değişikliğini ayrı dalda kaydet ve PR aç — docs/izlenebilirlik, a4bc1fc ve [PR #7](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7) ile gerçekleşti. Bu kaynak dosyanın güncellemesi aynı PR kapsamında izlenecek.
- [ ] Değişikliğin yazarı olmayan bir kişinin incelemesini al; bulguları işle ve gerekiyorsa yeniden kontrol et.
- [ ] Oluşan gerçek pull request bağlantısını izlenebilirlik kaydına ekle; son dosyanın erişilebilirliğini kontrol et.

### Yapılan belge kontrolünün kaydı

28.10.2026: Kullanıcının gönderdiği docs/izlenebilirlik ZIP kopyasında FR-02 → AC-02 → G-01 birlikte okundu; açıklamalar ve önceki gözlem sonuçları tutarlı. 03, 04 ve 08 dosyaları güncel öğretmen kopyalarıyla birebir aynı. İncelenen commit: a4bc1fc89061f2b136bdaab085887acda62a0933.

05'in a4bc1fc ile kaydedilen 0.8 sürümünde bu FR'nin gerçek Issue bağlantısı ve eşleşmesi bulunuyor. Toplu güncellemedeki 1.0 sürümünde PR #7 ve bu kontrolün sonucu da var. Son güncellemenin GitHub'a aktarımı ve erişimi doğrulanmadan son görev işaretlenmez. Yeni prototip denemesi veya bağımsız kişi incelemesi yapılmadı.

## Takip

- Sorumlu: Pınar — öğretmen uygulaması; gerçek kartta pozelll ataması önceki kullanıcı ekranından doğrulandı.
- İnceleyen: Henüz belirlenmedi; bağımsız inceleme yapılmadı.
- Öncelik: Yüksek; ürünün temel randevu oluşturma işini belgeliyoruz.
- Hedef tarih: Henüz belirlenmedi.
- İlgili kimlikler: FR-02, AC-02, BR-01, G-01; saat durumunun değişmesi için FR-01.
- İlgili gerçek kart: [FR-01 — #1](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/1). Bu ilişki, ilk kartın tamamlandığı anlamına gelmez.
- Bağımlılık: İlgili belgelerin güncel içeriğine erişim ve bu kartın gerçek bağlantısı.
- Pull request: [#7 — Açık](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7); docs/izlenebilirlik → main. Bu belge değişikliğiyle ilgili; üçüncü haftanın kod değişikliği PR'ı değildir.

## Tamamlandı ölçütü

FR-02, AC-02 ve G-01 bağlantısı tutarlı olmalı; kanıtın Hasta rolündeki başarılı akışla sınırlı olduğu belirtilmeli; gerçek Issue ve pull request bağlantıları kaydedilmeli; bağımsız inceleme tamamlanmalı; engelleyici bulgular giderilip kontrol edilmeli ve son belgeye erişilebilmelidir. Bu belge görevinin tamamlanması, henüz yapılmamış prototip denemelerinin geçtiği anlamına gelmez.
