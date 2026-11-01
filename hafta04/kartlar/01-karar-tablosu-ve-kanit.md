# H4-DK-01 — Karar tablosu ve ayrı kontrol kanıtı

Dördüncü hafta, yedinci basamak · 1 Kasım 2026

Bu kart ders için hazırlanmış bir senaryodur. Gerçek klinik talebi, ekip toplantısı
veya yapılmış test sonucu değildir. Beşinci haftadaki uygulama işlerine başlanmadan,
H4-P0 ilk planı hazırlandıktan sonra verildiği varsayılır; A–I işleri henüz başlamadı.

## Yeni bilgi

> Mevcut iptal koşulları yedi satırlık bir karar tablosuyla açıklansın. Her satır
> ayrı başlangıç verisiyle kontrol edilsin; kullanılan sürüm, veri, beklenen sonuç,
> gerçek sonuç ve kayıt değişimi ilgili satıra bağlansın. Bir başarılı iptal
> görüntüsü bütün satırların kanıtı olarak kullanılmasın.

İlk planda iptal, vazgeçme, rol/sahiplik/durum reddi ve saklama sınırları zaten
kontrol kapsamındaydı. Eklenen iş, **karar tablosu ve satır bazında izlenebilir
kanıt hazırlığıdır**. Yeni iptal yetkisi veya yeni ürün davranışı istenmiyor.
H4-MK-01 mimari kararı ve Randevu Deposu sözleşmesi korunuyor.

## Tabloya bağlanacak örnek durumlar

Bunlar beşinci haftada ayrılacak randevu işlemlerine yönelik beklenen sonuçlardır.
Ret durumları yalnız ekranda düğme gizli mi diye bakılarak geçilmiş sayılmaz;
kontrollü istek ve veriyle iş kuralı da sınanır. DK-K07 için onay verildiği varsayılır.

| Satır | Kayıt bulundu mu? | Simülasyon rolü | Kayıt seçili hastanın mı? | Başlangıç durumu | Beklenen sonuç |
|---|---|---|---|---|---|
| DK-K01 | Hayır | Hasta | Uygulanmaz | Uygulanmaz | İstek reddedilir; hiçbir kayıt değiştirilmez. |
| DK-K02 | Evet | Resepsiyon | Evet | Bekliyor | Rol koşulu sağlanmaz; kayıt ve veriler korunur. |
| DK-K03 | Evet | Doktor | Evet | Bekliyor | Rol koşulu sağlanmaz; kayıt ve veriler korunur. |
| DK-K04 | Evet | Hasta | Hayır | Bekliyor | Sahiplik koşulu sağlanmaz; kayıt ve veriler korunur. |
| DK-K05 | Evet | Hasta | Evet | Tamamlandı | Durum koşulu sağlanmaz; kayıt Tamamlandı kalır. |
| DK-K06 | Evet | Hasta | Evet | İptal edildi | İkinci iptal uygulanmaz; kayıt ve sayılar korunur. |
| DK-K07 | Evet | Hasta | Evet | Bekliyor | Onaylı iptal kaydı silmeden İptal edildi yapar; toplam kayıt sayısı aynı kalır. Saat sonucu BR-01'e göre belirlenir. |

Her satır kendi sentetik başlangıç verisiyle yürütülecek. Önceki satırın durum
değişikliği sonraki denemeye taşınmayacak. Ret satırlarında iptal isteği nedeniyle
Randevu Deposu'na güncelleme çağrısı yapılmadığı da kontrol edilecek. Bunlar
koşulları temsil eden örneklerdir; bütün olası birleşimlerin eksiksiz testi değildir.

ALT-01 vazgeçme, kalıcı yazma başarısızlığı, görünüm/saat/toplam tutarlılığı ve
diğer randevu işlemleriyle ortak veri kontrolleri ilk plandaki kapsamlarıyla sürer.
Gerçek sonuçlar ancak uygulama denendikten sonra yazılır.

## Öğretmen örneği için yeni tahminler

- **C: 3 → 5 blok.** Karar tablosunu hazırlama ve kurallara bağlama için bir;
  yalıtılmış başlangıç verileri ve beklenen değişimleri hazırlama için bir ek blok.
- **F: 3 → 4 blok.** Satır bazında yürütüm ve kanıt kaydını tamamlamak için bir ek blok.
- Diğer işlerin süreleri, öncülleri ve U1–U4 atamaları aynı kalır. Bir blok 30 dakikadır.
- A'nın iki bloğu sözleşme/koşul netleştirmesini, G'nin iki bloğu kısa tablo ve kanıtların
  incelemesini karşılayabilir varsayımı korunur. Gerçek işte yetmezse yeniden tahmin gerekir.
- Ek çalışma H düzeltme payından veya bağımsız incelemeden düşülmez.

Bunlar ders için verilen tahmin girdileridir; ölçülmüş süre veya gerçek ekip onayı değildir.

## Öğrencinin yapacağı iş

1. İlk planı değiştirmeden koru. Yeni bilgiyle hangi çıktıların büyüdüğünü açıkla.
2. Güncel süre, emek, başlangıç/bitiş, bolluk ve kritik yolu hesapla.
3. Aynı kişiye aynı anda iki farklı görev atanmadığını kontrol et.
4. İlk planla farkı ve seçtiğin yaklaşımın gerekçesini yaz; kalite koşullarını koru.

Öğretmen hesabı [03-is-plani-ve-riskler.md](../docs/03-is-plani-ve-riskler.md)
belgesinin H4-P1 bölümündedir. Gruplar kendi başlangıç planlarını kullanıyorsa
etkiyi o planın görev ve kaynaklarına göre değerlendirmelidir.
