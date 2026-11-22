# 9. hafta / 6. basamak - Kanıtı yeniden üret

## Derste anlat
Bir ekran görüntüsü anı gösterir; komut, kaynak commit ve sonuç kaydı deneyi izlenebilir yapar. Git bundle dalları ve etiketleriyle geçmişi taşımamızı sağlar. Yeni klasörde açıp kimliği karşılaştırmak teslimin kontrolüdür. Yerel ve CI deneyleri ayrı Git geçmişleri üretir; zamanlar farklı olduğu için commit kimlikleri farklı olabilir. Her rapor kendi koşusunun kimlikleriyle okunur.

## Ekranda göster ve uygula
Yerel gitflow-sonuclari.json ile CI raporunun kaynak commit ve tarihini ayırt edin. GitHub Actions’ta 12 Gitflow ve son panelin 6 kontrolünü açın. Klinik koşusunda 30 Node, 14 kaynak tarayıcı, 8 paket ve 14 paket tarayıcı kontrolünü gösterin. Bundle’ı yeni klasöre git clone -b develop ile açın; kayıtlı develop SHA’sı ve panel metniyle karşılaştırın.

- [43 · Kanıt zinciri](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/docs/43-git-kanit-ve-izlenebilirlik.md)
- [GitHub Actions koşusu](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202073)

## Öğrenciye soru
**Panelin altı kontrolünün geçmesi, klinik randevu uygulamasının bütün testlerinin geçtiği anlamına gelir mi?**

Beklenen açıklama: Hayır. Panel, Gitflow süreci ve klinik uygulama farklı kapsamdır. Her biri kendi kaynak ve yürütüm kaydına bağlanır.

## Grubun yapacağı iş
Kendi denemenizi yeni klasörde çalıştırın. Koşu tarihi, komut, ortam, SHA ve sonuç dosyalarını kaydedin.

Kontrol: Başka klasörde açılan geçmiş aynı; her sonuç kendi kapsamına bağlı.

## Hazırlığın durumu
12/12 Gitflow · 6/6 panel. Klinik testleri ayrıca başarılı.

[Görev #20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) · [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21). Öğretmen örneği; gerçek öğrenci katkısı veya bağımsız inceleme iddiası değildir.
