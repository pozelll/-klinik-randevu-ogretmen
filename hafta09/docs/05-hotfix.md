# 9. hafta / 5. basamak - Hotfix’i iki dala taşı

## Derste anlat
Paneldeki kasıtlı yanlış cümle, iptal edilen kaydın silindiğini söylüyor. Oysa klinik örnekte kayıt geçmişte kalır, saat açılır. Beş yapısal kontrol bu anlam hatasını yakalamaz. Eklenen A01 kontrolü yanlış metni reddeder. Hotfix teslim dalından çıkar; hem teslim geçmişine hem gelecek sürümün dalına taşınır. Böylece bir sonraki sürüm aynı hatayı geri getirmez.

## Ekranda göster ve uygula
04-release.json için surum_kontrol.py komutunu önce normal, sonra --anlam ile çalıştırın: 5/5 geçer, 5/6 başarısız olur. 05-hotfix.json ile 6/6 geçtiğini gösterin. Deney deposunda hotfix/0.9.1’in main ve develop için atalık kontrolünü yapın. Son panel içeriklerini de karşılaştırın. 0.9.0 etiketi değiştirilmeden 0.9.1 etiketi eklenmiştir.

- [42 · Hotfix ve eşitleme](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/docs/42-hotfix-ve-senkronizasyon.md)
- [Son panel verisi](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/panel/surum.json)

## Öğrenciye soru
**Düzeltme yalnız main’e taşınırsa sonraki sürümde hangi risk doğar?**

Beklenen açıklama: develop eski metni taşıyorsa hata yeniden gelebilir. Düzeltmenin geçmişte bulunması ve son içerikte korunması birlikte denetlenir.

## Grubun yapacağı iş
Hotfix gerekçesini yazın; iki hedef için atalık ve içerik kontrolünün gerçek çıktısını kaydedin.

Kontrol: İki atalık çıkışı 0; son içerik aynı; eski etiket hedefi değişmedi.

## Hazırlığın durumu
İki atalık kontrolü geçti. Eski etiket yerinde korundu.

[Görev #20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) · [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21). Öğretmen örneği; gerçek öğrenci katkısı veya bağımsız inceleme iddiası değildir.
