# 40 - Feature ve çakışma yönetimi

> 22 Kasım 2026 tarihli teknik hazırlık kaydı: Bu belge Gitflow eğitim deneyini ve klinik 0.3.0-rc.1 başlangıcını anlatır. Dal, hedef ve açık/taslak PR bilgileri birleştirme öncesindeki duruma aittir. [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21) aynı gün main'e birleştirilmiştir; bu işlem bağımsız insan incelemesi veya kabulü yerine geçmez. Güncel 0.3.0-rc.2 sonuçları [kapanış raporunda](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md), açık insan kabul işleri [kabul oturumu ve formlarında](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/50-insan-kabul-oturumu.md) bulunur.

## Beklenen ihtiyaçlar

| Alan | Hasta katkısı | Personel katkısı | Birleşik karar |
|---|---|---|---|
| duyuru | Hastanın randevu durumunu izlemesi | Personelin uygun saatleri izlemesi | İki ihtiyacı aynı duyuruda anlat |
| hasta_notu | Hasta açıklaması | Ortak tabandaki metin | Hasta katkısını koru |
| personel_notu | Ortak tabandaki metin | Personel açıklaması | Personel katkısını koru |

İki feature ortak `f19236c` tabanından ayrıldı. Hasta katkısı develop'a alındıktan sonra develop, personel dalına birleştirilmeye çalışıldı. Git gerçekten 1 çıkışı ve `panel/surum.json` için çözülmemiş durum verdi. [Ham çakışma](../kanitlar/cakisma-oncesi-cozulmemis.txt) saklandı. Bu beklenen hata başarılı deneyin bir parçasıdır; başarısız sonucu gizlemek değildir.

## Ekranda inceleme

Deney tamamlandığında `feature/personel-bilgi` dalı çözüm commit'ine ilerlemiş olur. Başlangıçtaki ortak tabanı incelemek için dal adları yerine kendi deney raporunuzdaki `commits.patient` ve `commits.staff` kimliklerini kullanın. Depo kökünde aşağıdaki komut bu iki kimliği ve karşılaştıracağınız `commits.baseline` değerini gösterir:

```bash
python -c "import json; from pathlib import Path; c=json.loads(Path('h9-deneyim/gitflow-sonuclari.json').read_text(encoding='utf-8'))['commits']; print('patient:', c['patient']); print('staff:', c['staff']); print('baseline:', c['baseline'])"
```

Sonraki komutta `HASTA_COMMIT` ve `PERSONEL_COMMIT` yerlerine bu çıktıda gördüğünüz tam kimlikleri yazın. `merge-base` sonucu kendi raporunuzdaki `baseline` kimliğiyle aynı olmalıdır.

```bash
git -C h9-deneyim/lab-deposu merge-base HASTA_COMMIT PERSONEL_COMMIT
git -C h9-deneyim/lab-deposu log --graph --decorate --oneline --all
git -C h9-deneyim/lab-deposu show feature/personel-bilgi:panel/surum.json
git -C h9-deneyim/lab-deposu rev-list --parents -n 1 feature/personel-bilgi
```

Yerel kayıtlı örnekte çözüm commit'i `0ed1026d0804ac7d3e17eb0bbab1fb01b62582b4`; iki ebeveyni vardır. Yeni denemenin kimliklerini kendi raporundan okuyun.

Çözüm: “Hastalar randevu durumunu, personel uygun saatleri izleyebilir.” Hasta ve personel notları ilgili feature dosyalarıyla aynı tutuldu. [03-cozum.json](../senaryolar/03-cozum.json) sonuç metnidir. Her iki tarafı bütünüyle kabul etme yerine alan bazında karar verildi.

Kontroller: H9-G03 gerçek çakışma; G04 çözülmemiş dosyanın reddi; G05 iki ebeveyn, birleşik duyuru ve iki notun korunması. Beş yapısal kontrol, iptal cümlesinin anlamını henüz doğrulamaz. Anlam açığı 42 belgesinde ele alınır.

Öğrenci uygulaması: kendi iki ihtiyacını seç, aynı alanda farklı düzenleme yap, çakışmayı oluştur, karar gerekçesini yaz ve iki katkıyı kontrol et. Öğretmenin otomatik commit'lerini kendine ait katkı diye sunma.
