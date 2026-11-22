# 8. hafta / 5. basamak — Bozuk paketi yakaladık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Bir doğrulayıcının doğru paketi kabul etmesi yeterli değildir; yanlış paketi reddettiğini de göstermeliyiz. İki ayrı kopyada bir dosyayı değiştiriyor ve bir dosyayı çıkarıyoruz. Deneme kopyaları geçicidir. Teslim edilen ZIP bozulmaz. İç özet listesine tek başına güvenmek yerine dıştaki aday tanımı da kontrol edilir.

## Ekranda göster ve uygula

Paket kontrollerindeki değiştirilmiş dosya, eksik dosya ve ek dosya sonuçlarını gösterin. Ardından sağlam dağıtım ZIP’ini verify komutuyla doğrulayın. SHA256SUMS.txt dosyasının kendisini özetlememesinin döngüsel bağımlılığı önlediğini açıklayın.

- [05-butunluk-kontrolu.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/05-butunluk-kontrolu.md)
- [check_candidate.py](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/scripts/check_candidate.py)

## Öğrenciye soru

**Saldırgan ZIP’i ve iç özetleri birlikte değiştirirse iç liste yeterli midir?**

Beklenen açıklama: Hayır. Güvenilen dış kaynak/manifest gerekir. Bu dersin özeti bir dijital imza veya kimlik doğrulama sistemi değildir.

## Grubun yapacağı iş

Paket kopyasında kontrollü eksik dosya denemesi yap. Beklenen ret ile gerçek sonucu kaydet.

Kontrol: Negatif denemede beklenen ret gerçekten oluşuyor mu? Sağlam paket özeti değişmeden duruyor mu?

## Hazırlığın gerçek durumu

Kontrollü bozulmalar reddedildi. Beklenen içerik, dış aday tanımından gelir.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## Sekiz anlamlı kontrol

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
