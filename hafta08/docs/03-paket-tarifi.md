# 8. hafta / 3. basamak — Paket içeriğini tanımladık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Bir klasörü rastgele sıkıştırmak yerine hangi dosyaların teslim edileceğini tanımlıyoruz. Bu pakette index.html, dört JavaScript dosyası, lisans, kullanım yönergesi, sürüm bilgisi ve özet listesi bulunur. Öğrencinin tarayıcısındaki randevu verisi kaynak dosya değildir ve bu ZIP’e aktarılmaz.

## Ekranda göster ve uygula

Üretim aracındaki izinli dosya listesini ve aday tanımını açın. Arşivin sıralı üretildiğini, zaman damgasının sabit olduğunu ve sıkıştırmasız ZIP kullanıldığını gösterin. Bu seçimlerin dosya içeriğini değil, paketleme değişkenliğini azaltmak için yapıldığını açıklayın.

- [03-paket-tarifi.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/03-paket-tarifi.md)
- [build_candidate.py](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/scripts/build_candidate.py)

## Öğrenciye soru

**Yalnız index.html dosyasını göndermek yeterli mi?**

Beklenen açıklama: Hayır. H5’ten beri JavaScript dört src dosyasından yüklenir. HTML tek başına tam uygulama değildir.

## Grubun yapacağı iş

Kendi paketin için açık içerik listesi oluştur. Geçici dosyaları, kişisel veriyi ve gereksiz çıktıları dışarıda tut.

Kontrol: Paketin her dosyasının amacı açıklanıyor ve eksik src dosyası yakalanıyor mu?

## Hazırlığın gerçek durumu

9 dosyalı çevrimdışı çalışma paketi. Gerçek tarayıcı verisi pakete alınmaz.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## Dokuz dosyanın görevi

| Dosya | Görev |
|---|---|
| index.html | Ekran, stil ve yerel script yükleme |
| src/demo-data.js | Sentetik başlangıç verisi |
| src/repository.js | Ortak veriye erişim ve saklama |
| src/rules.js | İş kuralları |
| src/ui.js | Arayüz ve saat yardımı |
| LICENSE | Mevcut MIT lisansı |
| README.md | Paketi açma ve kapsam yönergesi |
| SURUM.json | Aday adı, kaynak commit'i, kaynak özetleri |
| SHA256SUMS.txt | Diğer sekiz dosyanın SHA-256 özetleri |

Kaynak dışı destek yönergesi `hafta08/config/PAKET_README.md` dosyasından gelir ve özeti dış aday tanımında sabittir. Paket yalnız uygulama içindir; ders PDF'leri, test araçları ve eski ders belgeleri bu ZIP'in parçası değildir. Arşiv sıralaması, 1980-01-01 sabit zamanı, Unix 100644 dosya modu ve ZIP_STORED yöntemi tanımlıdır.
