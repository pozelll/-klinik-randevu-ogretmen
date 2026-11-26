# H7 — Değişiklik izlenebilirliği

Bu tablo 22 Kasım 2026 tarihli örnek uygulamanın test kayıtlarını gösterir. Sonuçlar belirtilen kaynak commit'e aittir; grubunuzun kendi yürütüm sonuçları değildir. Öğrenci yönergesi güncellemesi: 26 Kasım 2026.

| Gereksinim / risk | Görev / karar | Ürün dosyası | Kontrol | Gerçek kanıt |
|---|---|---|---|---|
| FR-01 uygun saatler | #10 / H7-DK-01 | index.html, src/ui.js | H7-B01, B03 | ../kanitlar/tarayici-sonuclari.json: PASS |
| FR-02 onayla oluşturma | #10 / H7-DK-01 | src/ui.js | H7-B02 | 7 → 7 → 8 kayıt, PASS |
| Rol ile yardım tutarlılığı | #10 / H7-DK-01 | src/ui.js | H7-B04 | Doktor kapalı; resepsiyon Kaan adına oluşturdu, PASS |
| Dar ekran riski | #10 / H7-DK-01 | index.html | H7-B05 | 390 px, taşma yok, PASS |
| Önceki iptal ve saklama akışı | H6'dan korunan davranış | rules.js, repository.js | H3-T01–T06, H6-B07–B09 | 9/9 PASS |

Kaynak commit: `bd5fa3fb2c35d1c11864eed982fdbc20d539d58a`.
[Gerçek CI koşusu](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45020807054).

Bu tarihli H7 çalışmasında NFR-01 kullanılabilirlik, NFR-02 yanıt süresi ve NFR-03 klavye kullanımı ölçülmedi. Beş yeni tarayıcı senaryosu bu ölçümlerin yerine geçmez. PR #18 aynı gün main dalına birleştirilmiştir; güncel inceleme durumu [PR kaydından](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18) izlenir.
