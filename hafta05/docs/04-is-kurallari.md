# 5. hafta / 4. adım - İş kuralları

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Bir işlemin yapılmasına ilişkin kararları arayüz kodundan ayırmak ve reddedilen isteğin veriyi değiştirmediğini göstermek.

Örnek uygulamada `cancelEligibility`, kayıt varlığını, rolü, sahipliği ve `Bekliyor` durumunu denetler. `cancel`, kullanıcı onayından sonra güncel kayıt üzerinde bu koşulları yeniden denetler. Böylece ilk uygunluk sorgusuyla işlem arasında değişen durum değerlendirilir; bu mekanizma çoklu cihaz eşzamanlaması sağlamaz.

| Ret kodu | İlgili denetim |
|---|---|
| `NOT_FOUND` | Kayıt varlığı |
| `ROLE` | Kullanıcı rolü |
| `OWNER` | Kaydın kullanıcıya ait olması |
| `STATUS` | Kaydın iptale uygun durumda olması |

`occupiedAt`, BR-01 kapsamında ilgili saatte başka iptal edilmemiş kayıt bulunup bulunmadığını hesaplar. İş kuralları bileşeni kararlarını veri erişimi üzerinden uygular; ekran çizimi ve kullanıcı onayı arayüzde kalır.

## Grup çalışması

1. Kendi uygulamanızdaki bir iş kuralını ekran kodundan ayırın.
2. Kurala uygun bir istek ve kurala uymayan bir istek hazırlayın.
3. Her iki isteğin sonucunu ve önce/sonra verisini kaydedin.
4. Reddedilen istekte veri güncellemesi yapılmadığını gösteren sonucu tesliminize ekleyin.

## Örnek uygulama kaydı

22 Kasım 2026 tarihli H5 çalışmasında reddedilen istekler veri yazımına ilerlemez; uygun iptal isteği kayıt durumunu günceller. H5-S08, ilk uygunluk kontrolünden sonra durum değiştiğinde iptal isteğinin reddedilmesini sınar.

## Kaynaklar

- [src/rules.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/rules.js)
- [H5 dalındaki iş kuralları yönergesi](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/04-is-kurallari.md)
- [Görev #13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13)
- [PR #15 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15)
