# 8. hafta / 4. basamak — İki üretimi karşılaştırdık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Tekrarlanabilir üretim, aynı tanımlı girdilerden aynı çıktıyı elde etmeyi hedefler. Burada iki üretimin baytları eşit. Sabit dosya sırası ve arşiv zamanı bu sonucu destekler. Bu kontrol dosyaların iyi tasarlandığını veya paketin güvenilir bir kişi tarafından imzalandığını kanıtlamaz.

## Ekranda göster ve uygula

check_candidate.py aracını çalıştırın ve iki üretimin özetlerinin eşit olduğu satırı gösterin. Kaynak dosyaya yapılan kontrollü bir değişikliğin üretimi durdurduğunu okuyun. Daha önceki üretimin çıktısını aynı yeni denemenin sonucu gibi kaydetmemeyi vurgulayın.

- [04-tekrarlanabilirlik.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/04-tekrarlanabilirlik.md)
- [check_candidate.py](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/scripts/check_candidate.py)
- [Paket sonuçları](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/kanitlar/paket-kontrolleri.json)

## Öğrenciye soru

**ZIP’in saatini her üretimde bugüne ayarlasaydık ne olurdu?**

Beklenen açıklama: Kaynak aynı olsa bile arşiv baytları değişebilirdi. Bu nedenle paket metaverisi de tanımlanır.

## Grubun yapacağı iş

Kendi paketini iki kez üret. Özetleri karşılaştır ve fark varsa hangi girdinin değiştiğini araştır.

Kontrol: Eşitlik sonucu iki gerçek üretimden mi geliyor? Kaynak tanımı değişirse kontrol duruyor mu?

## Hazırlığın gerçek durumu

İki üretim aynı paket içeriğini verdi. Eşit özet, insan onayı veya imza değildir.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## Çalıştırma — depo kökünde

```bash
python scripts/check_candidate.py
python scripts/build_candidate.py build --output kendi-ciktilarim/aday-a.zip
python scripts/build_candidate.py build --output kendi-ciktilarim/aday-b.zip
```

`check_candidate.py` iki ayrı geçici dosya üretir, baytlarını ve özetlerini karşılaştırır. Deneme çıktıları geçicidir; dağıtım ZIP'inin üzerine yazmaz. Gerçek H8-P01 sonucu: her iki özet `36822b44675d5df7d1613f9605f907e18fe3656cc74b64e614d19c277bde2dc5`. Yeni denemeyi kaydetmek için `--evidence kendi-ciktilarim/paket-sonuclari.json` verin.

Kaynak dosya veya paket yönergesi aday tanımından farklıysa üretim durur. Yeni sürüm istendiğinde değişikliği inceleyip yeni commit ve aday tanımı oluşturun; kontrolü geçmek için gelişigüzel özet değiştirmeyin.

## Hazırlık sırasında yakalanan gerçek bulgu

İlk CI koşusunda lisansın yerel kopyasına eklenmiş bir satır sonu nedeniyle kaynak özeti uyuşmadı ve üretim durdu. Özgün uzak lisans değiştirilmedi; sabit commit'teki dosya baytları korunarak yeniden alındı. Aday tanımı ve paket bu gerçek kaynağa göre yeniden üretildi, yeni CI geçti. [İlk bulgu kaydı](../kanitlar/ilk-ci-bulgusu.json) ile [başarılı koşuyu](../kanitlar/ci-kaydi.json) karşılaştırın. Bir bayt farkının bile göz ardı edilmemesi, kontrolün amacını gösterir.
