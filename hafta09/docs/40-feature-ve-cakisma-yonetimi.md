# 40 - Feature ve çakışma yönetimi

## Beklenen ihtiyaçlar

| Alan | Hasta katkısı | Personel katkısı | Birleşik karar |
|---|---|---|---|
| duyuru | Hastanın randevu durumunu izlemesi | Personelin uygun saatleri izlemesi | İki ihtiyacı aynı duyuruda anlat |
| hasta_notu | Hasta açıklaması | Ortak tabandaki metin | Hasta katkısını koru |
| personel_notu | Ortak tabandaki metin | Personel açıklaması | Personel katkısını koru |

İki feature ortak `f19236c` tabanından ayrıldı. Hasta katkısı develop'a alındıktan sonra develop, personel dalına birleştirilmeye çalışıldı. Git gerçekten 1 çıkışı ve `panel/surum.json` için çözülmemiş durum verdi. [Ham çakışma](../kanitlar/cakisma-oncesi-cozulmemis.txt) saklandı. Bu beklenen hata başarılı deneyin bir parçasıdır; başarısız sonucu gizlemek değildir.

## Ekranda inceleme

```bash
git -C h9-deneyim/lab-deposu merge-base feature/hasta-bilgi feature/personel-bilgi
git -C h9-deneyim/lab-deposu log --graph --decorate --oneline --all
git -C h9-deneyim/lab-deposu show feature/personel-bilgi:panel/surum.json
git -C h9-deneyim/lab-deposu rev-list --parents -n 1 feature/personel-bilgi
```

Yerel kayıtlı örnekte çözüm commit'i `0ed1026d0804ac7d3e17eb0bbab1fb01b62582b4`; iki ebeveyni vardır. Yeni denemenin kimliklerini kendi raporundan okuyun.

Çözüm: “Hastalar randevu durumunu, personel uygun saatleri izleyebilir.” Hasta ve personel notları ilgili feature dosyalarıyla aynı tutuldu. [03-cozum.json](../senaryolar/03-cozum.json) sonuç metnidir. Her iki tarafı bütünüyle kabul etme yerine alan bazında karar verildi.

Kontroller: H9-G03 gerçek çakışma; G04 çözülmemiş dosyanın reddi; G05 iki ebeveyn, birleşik duyuru ve iki notun korunması. Beş yapısal kontrol, iptal cümlesinin anlamını henüz doğrulamaz. Anlam açığı 42 belgesinde ele alınır.

Öğrenci uygulaması: kendi iki ihtiyacını seç, aynı alanda farklı düzenleme yap, çakışmayı oluştur, karar gerekçesini yaz ve iki katkıyı kontrol et. Öğretmenin otomatik commit'lerini kendine ait katkı diye sunma.
