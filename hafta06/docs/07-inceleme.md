# 6. hafta / 7. basamak - İnceleme paketini açtık

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

İnceleyen, değerlendirdiği içeriğin yazarı veya ortak yazarı olmamalıdır. İnceleme; gereksinim, kod farkı, test beklentisi ve kanıt arasındaki uyumu kapsar. Bu çalışmadaki otomatik kontroller bağımsız insan onayı olarak yazılmadı.

## Ekranda ne açacağım, ne yapacağım?

PR #16’nın Files changed sekmesini açın. H6’nın H5 üzerine eklediği test ve belgeleri gösterin. Bekleyen inceleme formunda gerçek kişinin adı ve kontrol ettiği commit için boş alan bırakıldığını anlatın. Bir bulgu çıkarsa dosya, etki, düzeltme commit’i ve yeniden kontrol sonucunu yazın.

- [07-inceleme.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/docs/07-inceleme.md)
- [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16)
- [Görev #14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14)

## Kontrol sorusu

Yapılmayan inceleme onay gibi sunulmuş mu? PR hedefi doğru mu? H4, H5 ve H6 işleri birbirinin yerine kapatılmış mı?

**Öğrenciye soru:** Yazarı olduğum testi tekrar çalıştırmam bağımsız inceleme olur mu?

**Beklenen açıklama:** Tekrar test olur; bağımsız inceleme olmaz. İncelemeyi içeriğin yazımına katılmamış kişi yapmalıdır.

## Öğrencinin yapacağı iş

Başka üyeye belirli bir dosya ve kontrol kapsamı ver. Gerçek inceleme sonucunu, varsa bulguyu ve düzeltmeyi kaydet.

## Öğretmen örneğinin gerçek durumu

Taslak PR #16 açık; hedef H5 dalı. İnceleyen kişi ve onay henüz yok.

Görev: [#14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · İnceleme paketi: [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.

## Gerçek inceleme formu

| Alan | Durum |
|---|---|
| İnceleyen adı / hesabı | Bekliyor |
| Yazıma katılmadığının kaydı | Bekliyor |
| İncelenen commit / tarih | Bekliyor |
| Dosya ve test kapsamı | Bekliyor |
| Bulgu / önem / düzeltme | Henüz bağımsız inceleme yapılmadı |
| Düzeltme commit'i / yeniden kontrol | Gerekirse doldurulur |
| Karar / gerçek GitHub review bağlantısı | Bekliyor |

Bağımlılık sırası: #7 → #11 → #12 → #15 → #16. Önceki PR'lar incelenip birleştirilirken sonraki PR'ın hedefi ve farkı yeniden kontrol edilir. H6'nın hedefi şu an H5 dalıdır; main'e birleştirilmiş değildir.
