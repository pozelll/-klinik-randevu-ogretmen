# 5. hafta / 2. adım - Bileşen sözleşmesi

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Veri erişimi bileşeninin hangi işlemleri sunduğunu ve işlem sonuçlarının nasıl yorumlanacağını tanımlamak.

Buradaki randevu deposu, uygulama verisini okuyan ve güncelleyen bileşendir. Sözleşme, bu bileşene gönderilen istekleri ve dönen sonuçları tanımlar.

| İşlem / alan | Anlamı |
|---|---|
| `findById` | Kimliğe göre bulunan kaydın bağımsız kopyasını döndürür. |
| `list` | Kayıtları bağımsız kopyalar halinde sunar. |
| `update` | Var olan kaydı günceller; bulunmayan kimlik için `applied:false` döner. |
| `add` | Aynı veri kaynağına yeni randevu ekler. |
| `reset` | Aynı veri kaynağını başlangıç durumuna getirir. |
| `applied` | İşlemin oturum verisine uygulanıp uygulanmadığını bildirir. |
| `persistent` | Sonucun kalıcı saklamaya yazılıp yazılmadığını bildirir. |

`applied:true` ve `persistent:false` birlikte dönebilir. Bu durumda oturum verisi değişmiş, kalıcı yazma başarısız olmuştur; değişiklik sayfa yenilendiğinde korunmayabilir. Okuma işleminden alınan kopyayı değiştirmek, kayıtlı veriyi doğrudan güncellemez.

## Grup çalışması

1. Kendi veri erişimi bileşeninizin okuma ve güncelleme işlemlerini tanımlayın.
2. Başarılı güncelleme, reddedilen istek ve saklama hatası için beklenen sonuç alanlarını ayrı yazın.
3. Okuma işleminin döndürdüğü kopyanın kayıtlı veriden bağımsız olduğunu kendi çalışmanızda sınayın.
4. Sözleşmeyi ve çalıştırdığınız kontrolün sonucunu [grup kaydına](../sablonlar/grup-kaydi.md) bağlayın.

## Örnek uygulama

22 Kasım 2026 tarihli H5 çalışmasında bu sözleşme `src/repository.js` içinde uygulanmıştır. H5-S02, dönen kopya değiştirildiğinde kayıtlı R001'in durumunun korunmasını sınar.

## Kaynaklar

- [src/repository.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/repository.js)
- [H5 dalındaki sözleşme yönergesi](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/02-sozlesme.md)
- [Görev #13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13)
- [PR #15 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15)
