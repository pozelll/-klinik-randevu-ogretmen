# 9. hafta / 3. basamak - Çakışmayı anlamıyla çöz

## Derste anlat
Git bir çakışma gösterdiğinde ürün kararını bizim vermemiz gerekir. Sadece bir tarafı kabul etmek diğer ekibin ihtiyacını kaybettirebilir. Bu örnekte duyuru iki hedefi de anlatmalı; hasta ve personel notları ayrı ayrı korunmalıdır. Çözümden sonra geçerli JSON, doğru içerik ve birleştirme geçmişini birlikte kontrol ederiz.

## Ekranda göster ve uygula
Ham çakışma dosyasında HEAD ve develop bölümlerini gösterin. komut-kaydi.json içinde merge çıkışının 1, çözülmemiş yolun panel/surum.json olduğunu bulun. 03-cozum.json ile karşılaştırın. Çözüm commit’ini git show ile açın; iki ebeveyn içerdiğini gösterin. H9-G03–G05 çakışmanın oluştuğunu, hatalı dosyanın reddedildiğini ve iki notun korunduğunu doğrular.

- [Çakışmanın ham kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/kanitlar/cakisma-oncesi-cozulmemis.txt)
- [40 · Çözüm ve kontrol](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/docs/40-feature-ve-cakisma-yonetimi.md)

## Öğrenciye soru
**Çakışma işaretleri silindi ve JSON okunuyor. İş bitti mi?**

Beklenen açıklama: Henüz değil. İki ihtiyacın da korunması gerekir. Biçim doğruluğu ile içerik doğruluğu farklı kontrollerdir.

## Grubun yapacağı iş
İki katkıyı koruyan bir çözüm yazın. Neden bu metni seçtiğinizi ve kontrol sonucunu kaydedin.

Kontrol: İşaret yok, JSON geçerli, iki not korunmuş; çözüm gerekçesi mevcut.

## Hazırlığın durumu
Çözüm: iki ebeveyn, iki katkı. Yalnız işaretleri silmek yetmez.

[Görev #20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) · [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21). Öğretmen örneği; gerçek öğrenci katkısı veya bağımsız inceleme iddiası değildir.
