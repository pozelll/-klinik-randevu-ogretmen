# 4. hafta — Mimari, tasarım kalıpları ve iş planlama

Durum: İlk yedi basamağın öğretmen hazırlığı hazır. H4-P0 korundu; H4-DK-01 kartıyla H4-P1 hazırlandı. Dört kişilik örnek ekip ve dokuz görev için net süre 8 → 9 saat, emek 17 → 19 kişi-saat oldu. Sekizinci basamağın bağımsız incelemesi/teslimi ve beşinci haftanın kod uygulaması bekliyor. Süreler ders varsayımıdır.
Hazırlık tarihi: 1 Kasım 2026
Öğretmen çalışma dalı: `docs/h4-mimari-plan`

## Nereden devam ediyoruz?

Üçüncü hafta sonunda iptal açıklaması ve onay metni geliştirilmiş Klinik Randevu
uygulamasından devam ediyoruz. Uygulamayı proje kökündeki `index.html` ile açın.
Bu klasörde ikinci bir ana uygulama dosyası yoktur.

İlk iki haftanın `docs` ve `diagrams` klasörleri ile `hafta-03` çalışması
proje kökünde korunur. Bu haftanın belgeleri `hafta04/docs`, çizimleri
`hafta04/diagrams` altında tutulur. Klasör adını `hafta04` olarak kullanın.

## Sekiz basamak

| Basamak | Yapılacak iş | Kayıt |
|---|---|---|
| 1 | Başlangıç sürümünü belirle ve yedeği koru. | Ayrı üçüncü hafta yedeği |
| 2 | Çalışma dalını ve dördüncü hafta klasörlerini hazırla. | Bu klasör ve 00 belgesi |
| 3 | Şelale, artırımlı ve çevik yaklaşımları karşılaştır. | docs/01-yasam-dongusu-secimi.md |
| 4 | Arayüz, iş kuralları ve veri erişiminin sorumluluklarını çiz. | diagrams/01-bilesen.drawio ve PNG |
| 5 | İki mimari seçeneği ve bir tasarım kalıbını değerlendir. | docs/02-mimari-karar.md |
| 6 | Görevleri, süreleri, bağımlılıkları ve kritik yolu planla. | docs/03-is-plani-ve-riskler.md |
| 7 | Değişiklik kartıyla planı güncelle; ilk planı koru. | 03 belgesinin güncelleme bölümü |
| 8 | Başka kişinin incelemesini al; koşullar sağlanınca teslim et. | 00 belgesindeki inceleme/teslim kaydı |

## Şimdi yapılacak işlem

1. `kartlar/01-karar-tablosu-ve-kanit.md` kartını ve `docs/03-is-plani-ve-riskler.md` içindeki H4-P0 / H4-P1 karşılaştırmasını okuyun. `planlar/01-ilk-is-plani.md` ilk planı değişmeden korur.
2. Öğrenci grupları `sablonlar` altındaki 01, 02 ve 03 belgelerini kendi `hafta04/docs` klasörlerine alır. Kendi gerekçelerini, görev sahiplerini ve sürelerini yazar; kendi diyagram ve kritik yol hesaplarını oluşturur.
3. Sıradaki sekizinci basamakta yazardan farklı kişinin incelemesi, H4 PR hazırlığı ve teslim koşulları ele alınacak. Gerçek inceleme yapılmadan tamamlanmış teslim kaydı yazılmayacak.

`[Doldurulacak]` yazıları öğrenci/öğretmen çalışması için ayrılmış alanlardır.
Şablonun var olması, içindeki görevin tamamlandığı anlamına gelmez.

## Çalışma kopyasını kullanma

Öğretmen için hazırlanan tam çalışma kopyası üçüncü haftanın mevcut dosyalarını içerir.
Öğrenciler kendi gruplarının dolu projesine bu haftanın yönerge ve boş şablonlarını ekler;
mevcut dolu dosyalarının üzerine yazmaz. Öğretmenin doldurduğu 01, 02 ve 03 belgelerinin yerine
`sablonlar` altındaki boş 01, 02 ve 03 şablonlarını kendi `hafta04/docs` klasörlerinde kullanırlar.
Öğretmenin sonuçları ve belgeleri öğrencinin kendi çalışması yerine geçmez.

Klasörü yeni bir konuma kopyalamak tarayıcıdaki randevu kayıtlarını taşımaz.
Eski çalışma klasörünü ve tarayıcı verilerini koruyun; karşılaştırmada gerçek
dosya yolunu, doktoru, tarihi ve rolü kaydedin.

Bu hafta tasarım ve planlama yapacağız. Kodun modüllere ayrılması beşinci haftanın çalışmasıdır.
