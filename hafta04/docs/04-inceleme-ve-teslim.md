# 4. hafta — İnceleme ve teslim kaydı

Tarih: 1 Kasım 2026 · Sekizinci basamak · Öğretmen çalışma kopyası

**Durum: İncelemeye hazırlık tamamlandı; gerçek bağımsız inceleme bekliyor.**
[H4 taslak PR'ı](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/12) ve çalışma paketi hazırdır. Main'e birleştirme
ve nihai teslim henüz yapılmadı. Bu belge bir onay veya yapılmış öğrenci çalışması değildir.

## 1. İncelenecek paket

| Çıktı | İnceleme odağı |
|---|---|
| [00 — Başlangıç kaydı](00-baslangic-ve-surum.md) | H3 başlangıcı, yedek, dal ve önceki PR'larla ilişki. |
| [01 — Yaşam döngüsü seçimi](01-yasam-dongusu-secimi.md) | Üç yaklaşımın karşılaştırması ve projeye dayalı tercih. |
| [02 — Mimari karar](02-mimari-karar.md) | İki seçenek, H4-MK-01, üç sorumluluk ve sınırlı Repository uyarlaması. |
| [Düzenlenebilir diyagram](../diagrams/01-bilesen.drawio) ve [PNG](../diagrams/01-bilesen.png) | Çağrı/sonuç yönleri; mevcut kod ile önerilen tasarımın ayrımı. |
| [03 — İş planı ve riskler](03-is-plani-ve-riskler.md) | Görevler, süre/bağımlılık/kaynak hesabı, H4-P0 / H4-P1 farkı. |
| [Sabit ilk plan](../planlar/01-ilk-is-plani.md) | Değişiklik öncesi varsayımlar ve hesap korunmuş mu? |
| [H4-DK-01 kartı](../kartlar/01-karar-tablosu-ve-kanit.md) | Yedi karar satırı; ek kanıt işinin C ve F üzerindeki etkisi. |
| [01](../sablonlar/01-yasam-dongusu-secimi.md), [02](../sablonlar/02-mimari-karar.md), [03](../sablonlar/03-is-plani-ve-riskler.md) boş şablonları | Öğrencinin kendi projesi için dolduracağı kopyalar. |

GitHub çalışma dalı: `docs/h4-mimari-plan`.
PR hedefi: `feat/h3-iptal-acikligi`; bu dal H3 çalışmasını içerir.
[Güncel tam çalışma ZIP'i](https://drive.google.com/file/d/1NQCBc6oMpXIZTIMRXOEr_2cBx15foto4/view)
önceki haftaların dosyalarını da içerir; yalnız H4 klasöründen oluşmaz.
Bu bağlantı ilerledikçe güncellenir; inceleyen kendi kontrol ettiği commit'i ayrıca kaydeder.

## 2. Hazırlık sırasında yapılan kontroller

Aşağıdakiler ChatGPT desteğiyle yapılan hazırlık kontrolleridir; bağımsız kişinin
değerlendirmesi, GitHub onayı veya uygulamanın davranış testi değildir.
İncelenen plan ve diyagram içeriği `95d6ac2` hazırlık sürümündeki içeriktir;
sekizinci basamakta bu içeriklere inceleme bağlantıları ve teslim kaydı eklenmiştir.

| Kontrol | Sonuç ve sınırı |
|---|---|
| Başlangıç korunuyor mu? | H3'teki 42 dosya sabit `da3ce51798344a6fafaee89cce42aa9aba90de17` sürümüyle bayt düzeyinde aynı. `index.html` değişmedi. |
| İlk plan ve boş şablonlar | H4-P0 sabit kopyası, 03 belgesinin ilk plan gövdesi ve üç öğrenci şablonu altıncı basamak sürümüyle aynı. |
| İlk plan hesabı | Tablolardan yeniden hesaplandı: A–B–E–F–G–H–I; 16 blok / 8 saat; 17 kişi-saat. |
| Güncel plan hesabı | Tablolardan yeniden hesaplandı: A–C–E–F–G–H–I; 18 blok / 9 saat; 19 kişi-saat. |
| Zamanlar ve kaynaklar | İki planın erken/geç zamanları ve bollukları tutarlı; örnek atamalarda aynı kişiye eşzamanlı iki görev düşmüyor. Gerçek ekip uygunluğu doğrulanmadı. |
| Değişiklik etkisi | C +2, F +1 blok; toplam iş süresi +3 blok, net bitiş +2 blok, emek +2 kişi-saat. C'nin eski 1 blok bolluğu açıklamada korunuyor. |
| Diyagram | XML yeniden okundu: 44 hücre, dört geçerli bağlantı; PNG görsel olarak kontrol edildi. diagrams.net içinde açma/düzenleme denemesi yapılmadı. |
| Bağlantılar ve kapsam | H4 belgelerinin yerel dosya bağlantıları çözümleniyor. Uygulama kodunda değişiklik yok; dosya farkı H4 klasörüyle sınırlı. |

`index.html` SHA-256:
`a8efb6ed40b5fb10cd09aded207e13f6a92ea2b1263a3fafcf2a1585518721f5`

Sabit H4-P0 kopyasının SHA-256 değeri:
`76dacb1dd550f09563c165cb23e27a809f4a0bbdc92971c9dbaffa56646a42bf`

H3'ün T01–T06 sonuçları kendi tarihli kayıtlarında kalır; bu hafta yeniden
çalıştırılmış test diye sunulmaz. NFR ölçümü yapılmadı. H4-DK-01 satırları
beklenen sonuçları tanımlar; gerçek yürütüm kanıtı henüz yoktur.

## 3. Bağımsız inceleyen için kontrol sırası

İnceleyen, değerlendirdiği içeriğin yazarı veya ortak yazarı olmamalıdır.
Örnek plandaki U4 rolü, bu belgelere atanmış gerçek bir kişi değildir.

1. PR'ın güncel tam head SHA'sını kaydedin. H3'e göre dosya farkında yalnız
   `hafta04` dosyalarının bulunduğunu ve `index.html`in korunmasını doğrulayın.
2. 01 belgesindeki tercihi projenin önceki kayıtlarıyla karşılaştırın. Öğretmen
   varsayımı, gerçek gözlem ve öğrenci tarafından doldurulacak alanları ayırın.
3. 02 belgesi ve diyagramda başarılı iptal, vazgeçme, rol/sahiplik/durum reddi,
   BR-01 saat koşulu ve başarısız kalıcı yazma sınırlarını izleyin. Repository
   önerisinin ek sunucu veya uygulanmış kod gibi anlatılmadığını kontrol edin.
4. `.drawio` dosyasını diagrams.net'te açın; ayrı kutu ve bağlantının
   düzenlenebildiğini bir deneme kopyasında kontrol edin. Tarih ve sonucu yazın.
   Asıl çizim değişirse PNG'yi de güncelleyin.
5. P0 ve P1 için ileri/geri hesabı kendiniz yapın. 8 → 9 saat ve 17 → 19
   kişi-saat farkını; C'nin eski bolluğunu ve yeni kritik yolu açıklayın.
   Öğrenci grubu gerçek isim, takvim ve kendi tahminlerini ayrıca tamamlasın.
6. Bulguları dosya/bölüm, gerekçe ve beklenen düzeltmeyle kaydedin. Bulgu
   çıkmadıysa yalnız gerçekten kontrol ettiğiniz kapsam için bunu belirtin.
7. Düzeltme varsa yeni commit'i ve yeniden kontrol sonucunu kaydedin. Son
   kararınızı GitHub incelemesi veya bağlantısı verilmiş gerçek inceleme
   kaydıyla belgeleyin; boş formu ya da otomatik kontrolü onay saymayın.

## 4. Gerçek inceleme kaydı — bekliyor

| Alan | Mevcut durum |
|---|---|
| İnceleyen adı / GitHub hesabı | Henüz belirlenmedi. |
| İncelenen içeriğin yazımına katılmadığının kaydı | Henüz yok. |
| İnceleme tarihi ve tam commit SHA | Henüz yok. |
| İnceleme bağlantısı ve incelenen kapsam | Henüz yok. |
| diagrams.net açma/düzenleme sonucu | Kontrol bekliyor. |
| İlk değerlendirme | İnceleme bekliyor. |
| Düzeltmelerden sonraki commit ve karar | Henüz yok. |

Bulgu oluştuğunda aşağıdaki tabloya gerçek satır ekleyin. Boş olması,
inceleme yapıldığı veya sorun bulunmadığı anlamına gelmez.

| Bulgu ID | Dosya / bölüm | Bulgu ve önemi | Beklenen düzeltme | Sorumlu / düzeltme commit'i | Yeniden kontrol eden / sonuç |
|---|---|---|---|---|---|
| — | — | İnceleme henüz yapılmadı. | — | — | — |

## 5. PR bağımlılıkları ve birleştirme koşulları

1 Kasım 2026 kontrolünde [#7](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7)
ve [#11](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/11) açık ve
birleştirilmemişti; ikisinin GitHub inceleme listesi de boştu.
#7 açıklamasındaki belge işleri ve bağımsız inceleme; #11'in inceleme/son kontrol
işleri kendi kapsamlarında sonuçlandırılmalıdır. H4 hazırlığı bunları kapatmaz.

Bağımlılık sırası **#7 → #11 → H4**. H4, önceki iki PR çözülene kadar
H3 dalına karşı taslak olarak incelenebilir. Önceki PR'lar tamamlanınca gerçek
birleştirme biçimini ve güncel dalları kontrol edin; gerekirse H4 hedefini
`main` olarak değiştirin. Eski haftaların değişiklikleri tekrar farkta görünürse
dal geçmişini uygun biçimde düzenleyip kapsamı yeniden kontrol edin.

H4 için şu koşullar henüz tamamlanmış sayılmaz:

- [ ] Gerçek bağımsız inceleyen, kapsamı ve incelediği tam commit'i kaydetti.
- [ ] Diyagramın düzenleyicide açılması/düzenlenmesi kontrol edildi.
- [ ] Engelleyici bulgular giderildi; ilgili düzeltmeler yeniden incelendi.
- [ ] Önceki PR bağımlılıkları çözüldü; doğru hedef dal, güncel fark ve varsa çakışmalar kontrol edildi.
- [ ] Son head üzerindeki gerekli kontroller tamamlandı; koşullar sağlanınca taslak PR incelemeye hazır duruma alındı.
- [ ] Gerçek birleştirme yapıldı; birleştirme commit'i ve ana sürüm kontrolü kaydedildi.
- [ ] Son paket doğru sürümden üretildi; teslim bağlantısı ve alıcının erişimi doğrulandı.

Son PR head'i değişirse önceki incelemenin yeni içeriği kapsayıp kapsamadığını
yeniden kontrol edin. GitHub'ın bir dalı teknik olarak birleştirebilmesi, bu
dersin inceleme ve teslim koşullarının karşılandığı anlamına gelmez.

## 6. Beşinci haftaya geçiş

Bu haftanın çıktısı tasarım ve planlama belgeleridir. A–I uygulama görevleri
henüz yapılmadı; 8 veya 9 saat gerçekleşmiş çalışma süresi değildir. Beşinci
haftada H4-MK-01 ve H4-P1 temel alınır; önce gerçek görev sahipleri, takvim ve
tahminler netleştirilir. Kod ayrımı, gerçek testler ve uygulama incelemesi o
çalışmanın kayıtlarına yazılır. H4'ün bağımsız belge incelemesi ayrıca izlenir.

Öğrenciler kendi dolu projelerini korur; öğretmenin sonuçları ve bu durum kaydı
kendi incelemeleri yerine geçmez. Kendi PR/commit ve gerçek inceleme bilgileriyle
benzer bir kayıt oluştururlar.
