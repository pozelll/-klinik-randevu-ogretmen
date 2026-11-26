# 9. hafta / 2. adım - İki feature, ortak taban

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

İki katkının hangi ortak başlangıçtan ayrıldığını commit kimlikleriyle doğrulayın. Her katkının değiştirdiği alanı ve karşıladığı ihtiyacı kaydedin.

## Grup çalışması

1. [Hasta senaryosunu](../senaryolar/01-hasta.json) ve [personel senaryosunu](../senaryolar/02-personel.json) karşılaştırın. `duyuru`, `hasta_notu` ve `personel_notu` alanlarındaki değişiklikleri yazın.
2. Birinci adımda oluşan `h9-deneyim/gitflow-sonuclari.json` dosyasından `commits.patient`, `commits.staff` ve `commits.baseline` değerlerini alın.
3. Aşağıdaki `HASTA_COMMIT` ve `PERSONEL_COMMIT` yerlerine bu koşunun tam commit kimliklerini yazıp komutu çalıştırın. Sonucu aynı rapordaki `baseline` ve H9-G02 kaydıyla karşılaştırın.

```bash
git -C h9-deneyim/lab-deposu merge-base HASTA_COMMIT PERSONEL_COMMIT
```

4. Dal uçları birleştirme sırasında ilerler. İlk ortak tabanı incelerken ilk iki katkının sabit commit kimliklerini kullanın; deney sonundaki dal adlarını ilk katkı kimlikleriyle karıştırmayın.
5. Grubunuzun ayrı çalışma deposunda aynı başlangıçtan iki küçük katkı oluşturun. Gerçekte katkıyı yapan üyeyi, değiştirdiği alanları ve commit'ini [grup formuna](../sablonlar/grup-kaydi.md) yazın.

## Teslim edilecek çıktı

İki katkının amacı, yazarları ve tam commit'leri; ortak ata komutu ve çıktısı; korunması gereken alanların listesi.

## Çıktı kontrolü

- İlk katkı commit'lerinin ortak atası kayıtlı başlangıçla eşleşir.
- Her katkı için ayrı bir ihtiyaç ve gerçek değişiklik gösterilir.
- Otomatik deneyin commit'leri grubun insan katkısı olarak sunulmaz.

[Feature ve çakışma kaydı](40-feature-ve-cakisma-yonetimi.md) · [Örnek Git geçmişi](../kanitlar/git-gecmisi.txt)

[Önceki adım](01-baslangic.md) · [Sonraki adım: Çakışma çözümü](03-cakisma.md)
