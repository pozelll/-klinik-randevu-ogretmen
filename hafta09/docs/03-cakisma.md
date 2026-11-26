# 9. hafta / 3. adım - Çakışmayı anlamıyla çöz

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Çakışmayı iki ihtiyacı da koruyacak biçimde çözün. Dosyanın biçimini, içerik kararını ve birleştirme geçmişini birlikte doğrulayın.

## Grup çalışması

1. Kendi deney klasörünüzdeki `cakisma-oncesi-cozulmemis.txt` dosyasını açın. İki tarafın değiştirdiği alanı ve çakışma işaretlerini belirleyin. [Paylaşılan ham kayıt](../kanitlar/cakisma-oncesi-cozulmemis.txt) karşılaştırma örneğidir.
2. Aynı koşunun `komut-kaydi.json` dosyasında çakışmaya yol açan merge komutunu, `1` çıkış kodunu ve çözülmemiş `panel/surum.json` yolunu bulun.
3. [Çözüm senaryosunu](../senaryolar/03-cozum.json) önceki iki katkıyla karşılaştırın. Duyurunun kapsamını, hasta notunu ve personel notunu ayrı ayrı kontrol edin.
4. Aşağıdaki komutlarla çözüm commit'inin ebeveynlerini ve dosya içeriğini inceleyin. H9-G03–G05 sonuçlarını kendi koşunuzun raporuyla eşleştirin.

```bash
git -C h9-deneyim/lab-deposu rev-list --parents -n 1 feature/personel-bilgi
git -C h9-deneyim/lab-deposu show feature/personel-bilgi:panel/surum.json
```

5. Grubunuzun iki katkısından doğan çakışmayı çözün. Seçtiğiniz metnin gerekçesini yazın; iki ihtiyacın korunmasını ve geçerli JSON oluşmasını kontrol ettikten sonra çözümü commit olarak kaydedin.

## Teslim edilecek çıktı

Çakışan dosya kaydı, çözülmüş dosya, çözüm gerekçesi, merge commit'i ve doğrulama sonuçları.

## Çıktı kontrolü

- Çakışma işareti kalmamıştır; JSON okunabilir.
- Hasta ve personel katkıları korunmuştur.
- Çözüm merge commit'inin iki ebeveyni ve gerekçesi kayıtlıdır.

[Çözümün teknik kaydı](40-feature-ve-cakisma-yonetimi.md)

[Önceki adım](02-feature.md) · [Sonraki adım: Release ve etiket](04-release.md)
