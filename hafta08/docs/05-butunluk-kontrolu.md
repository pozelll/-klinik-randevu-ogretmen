# 8. hafta / 5. adım - Paket bütünlüğü

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Doğrulayıcının sağlam paketi kabul ettiğini ve beklenen içeriğe uymayan paketi reddettiğini sınayın. İç özet listesiyle birlikte dış aday tanımını da kontrol edin.

## Grup çalışması

1. Sağlam teslim paketini ve başlangıç SHA-256 özetini kaydedin.
2. Deneme için ayrı bir kopya oluşturun; yalnız bu kopyada kontrollü eksik dosya denemesi yapın.
3. Beklenen reddi ve gerçekten oluşan sonucu ayrı yazın.
4. Sağlam paketi yeniden doğrulayın ve başlangıç özetinin korunduğunu kontrol edin.

Denemeler geçici kopyalarda yapılır. Teslim ZIP'ini veya asıl kaynak dosyalarını deneme amacıyla bozmayın. [Örnek kontrol aracı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/scripts/check_candidate.py) bu denemeleri ayrı çalışma kopyalarında yürütür.

## Teslim edilecek çıktı

Sağlam paketin özeti, deneme kopyasına yapılan değişiklik, beklenen sonuç, gerçek doğrulama çıktısı ve sağlam paketin son kontrolü.

## 22 Kasım 2026 tarihli sekiz örnek kontrol

Aşağıdaki sonuçlar [örnek paket kontrol kaydına](../kanitlar/paket-kontrolleri.json) aittir. Kendi denemenizin sonucunu ayrıca üretin. Doğrulama komutu `release/h8-surum-adayi` dalının depo kökünde çalıştırılır.

| Kimlik | Gerçek kontrol | Sonuç |
|---|---|---|
| H8-P01 | İki üretimin baytları ve SHA-256 aynı | PASS |
| H8-P02 | Dış aday tanımına uygun dokuz dosya | PASS |
| H8-P03 | ui.js içinde aynı uzunlukta bir bayt değiştirildi | Beklenen ret |
| H8-P04 | rules.js çıkarıldı | Beklenen ret |
| H8-P05 | Beklenmeyen dosya eklendi | Beklenen ret |
| H8-P06 | ui.js ile iç özet listesi birlikte değiştirildi | Dış tanım sayesinde ret |
| H8-P07 | Yerel kaynak dosya değiştirildi | Üretim başlamadan ret |
| H8-P08 | Güvenli ayıklama, dokuz dosya ve dört script yolu | PASS |

```bash
python scripts/build_candidate.py verify hafta08/dagitim/Klinik_Randevu_0.3.0-rc.1.zip
```

Doğrulama için depo kökündeki kaynak dosyalar, dış aday tanımı ve yönerge bulunmalıdır. SHA256SUMS.txt kendi kendisini özetlemez. İçerik eşitliği kontrol edilir; bu mekanizma dijital imza veya tedarik zinciri güvenlik sertifikası değildir.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
