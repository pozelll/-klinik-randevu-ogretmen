# 8. hafta / 3. adım - Paket tarifi

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Hangi dosyaların teslim edileceğini ve her dosyanın görevini tanımlayın. Uygulamanın çalışması için gereken dosyalar birlikte paketlenir; geçici çıktılar ve kişisel veriler pakete alınmaz.

## Grup çalışması

1. Kendi uygulamanızın çalışması için gereken dosyaları listeleyin.
2. Kullanım yönergesi, lisans, sürüm bilgisi ve özet listesi gibi destek dosyalarını belirleyin.
3. [Örnek üretim aracındaki](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/scripts/build_candidate.py) izinli dosya listesini [aday tanımıyla](../config/surum-adayi.json) karşılaştırın.
4. Arşiv sırası, zaman bilgisi ve dosya modu gibi paketleme tercihlerini kaydedin.
5. Eksik uygulama dosyasını yakalayacak kontrolü teslim listenize ekleyin.

## Teslim edilecek çıktı

Dosya yolu, görevi ve kaynağı bulunan paket içerik listesi. Tarayıcıdaki randevu kayıtları uygulama kaynak dosyası değildir; örnek ZIP'e aktarılmaz.

## 22 Kasım 2026 tarihli örnekteki dokuz dosya

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

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
