# 9. hafta / 2. basamak - İki feature, ortak taban

## Derste anlat
İki ekip üyesinin aynı başlangıçtan çalışması, aynı satırı farklı amaçlarla değiştirebilecekleri anlamına gelir. Hasta dalı hasta notunu, personel dalı personel notunu geliştirir; ikisi de ortak duyuruyu değiştirir. Dalların isimlerine bakmak ortak geçmişi kanıtlamaz. merge-base ile iki çalışmanın ortak atasını buluruz.

## Ekranda göster ve uygula
Senaryolar klasöründeki 01-hasta.json ile 02-personel.json dosyalarını yan yana açın. Yalnız duyuruya değil, korunması gereken iki özel nota da bakın. Deney deposunda git merge-base feature/hasta-bilgi feature/personel-bilgi komutunu çalıştırın. Çıkan kimliği gitflow-sonuclari.json içindeki baseline ile karşılaştırın. H9-G02 bu eşitliği gerçekten kontrol etti.

- [40 · Feature ve çakışma](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/docs/40-feature-ve-cakisma-yonetimi.md)
- [Gerçek Git geçmişi](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/kanitlar/git-gecmisi.txt)

## Öğrenciye soru
**İki dalın adı farklıysa içerikleri mutlaka çakışmadan birleşir mi?**

Beklenen açıklama: Hayır. Ayrı dallar aynı ortak tabandaki aynı satırı farklı değiştirebilir; isim farkı içerik uyumu sağlamaz.

## Grubun yapacağı iş
Ortak tabandan iki küçük katkı oluşturun. Her dalın değiştirdiği alanları ve katkı amacını yazın.

Kontrol: İki commit var; ortak ata doğru; her katkının amacı açıklanabiliyor.

## Hazırlığın durumu
Ortak taban doğrulandı. Dallar aynı duyuru alanını değiştirir.

[Görev #20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) · [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21). Öğretmen örneği; gerçek öğrenci katkısı veya bağımsız inceleme iddiası değildir.
