# 9. hafta / 4. basamak - Release ve etiket

## Derste anlat
Release dalı sürüm hazırlığını ayırır. Commit bir içerik anını, dal ilerleyen bir referansı, etiket seçilmiş sürüm noktasını gösterir. Açıklamalı etiketin mesajı da vardır; yine de etiket tek başına kalite onayı değildir. Bu laboratuvarda kusurun geç fark edilmesini canlandırmak için 0.9.0 eğitim etiketi oluşturulur. Gerçek klinik yayın kararı bundan ayrıdır.

## Ekranda göster ve uygula
41 belgesindeki release kaydını açın. Deney deposunda git show egitim-hafta09-v0.9.0 komutuyla mesajı ve hedefi inceleyin. git cat-file -t egitim-hafta09-v0.9.0 çıktısı tag olmalıdır. GitHub PR #21’in hâlâ açık olduğunu gösterin: yerel main birleşmesi, gerçek ders deposunun main dalının birleştiği anlamına gelmez.

- [41 · Sürüm kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/docs/41-release-ve-surum-kaydi.md)
- [Gitflow sonuçları](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/kanitlar/gitflow-sonuclari.json)

## Öğrenciye soru
**Etiket atılmış olması sürümün tüm kalite koşullarını geçtiğini kanıtlar mı?**

Beklenen açıklama: Hayır. Etiket bir sürüm noktasını işaretler. Test, inceleme, ölçüm ve kabul kayıtları ayrıca değerlendirilir.

## Grubun yapacağı iş
Sürüm kapsamı, tam commit, etiket mesajı ve açık riskleri kendi sürüm kaydınıza yazın.

Kontrol: Etiket türü ve hedefi doğrulanmış; eğitim yayını ile ürün kararı ayrı.

## Hazırlığın durumu
Yerel etiket: v0.9.0 senaryosu. GitHub üretim yayını yapılmadı.

[Görev #20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) · [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21). Öğretmen örneği; gerçek öğrenci katkısı veya bağımsız inceleme iddiası değildir.
