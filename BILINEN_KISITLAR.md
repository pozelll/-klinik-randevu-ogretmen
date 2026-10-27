# Çalışan özellikler ve bilinen sınırlar

## Bu sürümün kapsamı

Bu sürüm, tarayıcıda açılan tek dosyalı eğitim demonstratörüdür. FR-01–FR-06 için gözlenebilir örnek davranış sağlar. Öğrencinin yazacağı gereksinim belgesi veya daha sonraki C#/Java MVC projesinin tamamlandığı anlamına gelmez.

## Çalışan davranışlar

- Doktor ve sabit örnek güne göre uygun/dolu/kapalı saatler.
- Hasta ve Resepsiyon rollerinde seçili hasta adına yeni randevu.
- Aynı açık sayfanın mevcut veri durumunda BR-01 kontrolü: aynı doktor, tarih ve saat için iptal edilmemiş ikinci kayıt reddedilir. Dolu saat düğmesi de seçilemez.
- Hasta rolünde yalnız kendi Bekliyor kaydını iptal etme; iptal için onay penceresi.
- Resepsiyon ve Doktor rollerinde seçili doktor/tarihin günlük listesi.
- Yalnız görevli Doktor rolünde kendi Bekliyor kaydını Tamamlandı yapma.
- Yetkili rolün günlük sayılarını işlemden sonra güncelleme.
- localStorage kullanılabiliyorsa yerel kayıt; kullanılamıyorsa oturum belleğinde devam etme.
- Bozuk veya beklenmeyen yerel kayıtta uyarı ve bilinen başlangıç verisine dönüş.
- Örnek veriyi sıfırlamadan önce kullanıcı onayı.
- Tüm CSS ve JavaScript dosyanın içinde; dış kaynağa ağ isteği yok.

## Gerçek güvenlik değildir

Hasta, Resepsiyon ve Doktor seçenekleri **simülasyon rolüdür**. Gerçek giriş, parola, sunucu tarafı yetkilendirme veya oturum güvenliği yoktur. Doktor seçicisini değiştirmek başka bir örnek doktoru canlandırmayı sağlar. Yerel dosya ve istemci kodu kullanıcı tarafından incelenebilir veya değiştirilebilir. Bu sınırlamalar öğretimde rol ile gerçek güvenlik arasındaki farkı tartışmak içindir.

## Kayıt ve eşzamanlılık

- Veriler yalnız bu tarayıcıda tutulur; merkezi veya paylaşımlı veritabanı yoktur.
- İki sekme, iki tarayıcı veya iki cihazın aynı saati eşzamanlı ayırmasını engelleme garantisi yoktur. Sekmeler arası canlı eşzamanlama yapılmaz; bir sekme diğerinin verisini sonradan üzerine yazabilir.
- Sekme kapandığında kalıcı kayıt garantisi verilmez. Dosya adresi, tarayıcı ayarı, özel gezinme ve saklama kotası davranışı etkileyebilir.
- Kalıcı saklama başarısız olursa uygulama bellekte çalışır; yenileme değişiklikleri kaybettirir.
- Bu küçük gösterim en fazla 1.000 randevu kaydı tutar. İptal edilmiş kayıtlar bu sayıya dahildir.

## Takvim ve işlem sınırları

- Yalnız 12 ve 13 Kasım 2030; iki doktor, iki hasta ve sabit saatler.
- Geçmiş tarih/saat, saat dilimi, tatil, çalışma takvimi ve farklı randevu süresi kuralları yoktur.
- Hasta, seçili doktor ve gün için kendi kayıtlarını görür; başka günün randevusu için tarihi değiştirmelidir.
- Resepsiyon bu sürümde kayıt açar ve günlük liste/toplam görür; iptal ve tamamlama yapmaz.
- Tamamlandı kaydı iptal edilmez ve saati tekrar açılmaz. İptal edilen kayıt yeniden Bekliyor yapılmaz; o saatte yeni kayıt açılabilir.
- Arama, randevu taşıma, bildirim, ödeme, sağlık verisi, dışa aktarma ve gerçek kurum entegrasyonu yoktur.
- Toplamlar yalnız seçili doktor ve tarih içindir; bütün klinik veya bütün günler için rapor değildir.

## Derste nasıl kullanılmalı?

Mevcut davranışı gözlemleyin, varsayımınızı yazın ve paydaş sorusuna dönüştürün. Bulduğunuz her sınırı doğrudan hata ilan etmeyin: kapsam dışı iş, eksik gereksinim ve gerçek kusur farklıdır. Bir iddiayı kabul koşulu ve yeniden uygulanabilir gözlemle destekleyin.
