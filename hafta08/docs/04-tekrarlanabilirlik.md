# 8. hafta / 4. adım - Tekrarlanabilir üretim

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Aynı tanımlı girdilerden üretilen iki paketin baytlarını ve SHA-256 özetlerini karşılaştırın. Sabit dosya sırası ve arşiv zamanı, aynı içeriğin aynı paketle üretilmesini destekler.

## Grup çalışması

1. Kendi kaynak commit'inizi, aday tanımınızı ve üretim ortamınızı kaydedin.
2. Paketi iki ayrı çıktı dosyasına üretin.
3. İki dosyanın baytlarını ve özetlerini karşılaştırın. Fark varsa kaynak, araç veya paket metaverisindeki değişikliği araştırın.
4. Yeni denemenizin komutlarını, tarihini ve gerçek sonuçlarını kaydedin.

## Teslim edilecek çıktı

İki üretimin dosya adları, kaynak bilgileri, SHA-256 özetleri, karşılaştırma sonucu ve varsa farkın açıklaması. Eşit özet, insan onayı veya dijital imza anlamına gelmez.

## H8 örneğini çalıştırma

Örnek komutlar `release/h8-surum-adayi` dalının depo kökünde çalıştırılır. Aşağıdaki H8-P01 sonucu ve ilk CI bulgusu 22 Kasım 2026 tarihli kayıtlara aittir.

```bash
python scripts/check_candidate.py
python scripts/build_candidate.py build --output kendi-ciktilarim/aday-a.zip
python scripts/build_candidate.py build --output kendi-ciktilarim/aday-b.zip
```

`check_candidate.py` iki ayrı geçici dosya üretir, baytlarını ve özetlerini karşılaştırır. Deneme çıktıları geçicidir; dağıtım ZIP'inin üzerine yazmaz. Gerçek H8-P01 sonucu: her iki özet `36822b44675d5df7d1613f9605f907e18fe3656cc74b64e614d19c277bde2dc5`. Yeni denemeyi kaydetmek için `--evidence kendi-ciktilarim/paket-sonuclari.json` verin.

Kaynak dosya veya paket yönergesi aday tanımından farklıysa üretim durur. Yeni sürüm istendiğinde değişikliği inceleyip yeni commit ve aday tanımı oluşturun; kontrolü geçmek için gelişigüzel özet değiştirmeyin.

## Hazırlık sırasında yakalanan gerçek bulgu

İlk CI koşusunda lisansın yerel kopyasına eklenmiş bir satır sonu nedeniyle kaynak özeti uyuşmadı ve üretim durdu. Özgün uzak lisans değiştirilmedi; sabit commit'teki dosya baytları korunarak yeniden alındı. Aday tanımı ve paket bu gerçek kaynağa göre yeniden üretildi, yeni CI geçti. [İlk bulgu kaydı](../kanitlar/ilk-ci-bulgusu.json) ile [başarılı koşuyu](../kanitlar/ci-kaydi.json) karşılaştırın. Bir bayt farkının bile göz ardı edilmemesi, kontrolün amacını gösterir.

[Kontrol aracı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/scripts/check_candidate.py) · [Tarihli paket sonuçları](../kanitlar/paket-kontrolleri.json)

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
