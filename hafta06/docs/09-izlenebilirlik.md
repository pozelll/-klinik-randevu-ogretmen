# H6 - Gereksinimden kanıta izlenebilirlik

Hazırlık: 22 Kasım 2026. Sonuçlar öğretmen örneğinin otomatik kontrolleridir.

| Gereksinim / koşul | Test | Gerçek kanıt |
|---|---|---|
| FR-03: kayıt, rol, sahiplik, durum sınırı | DK-K01–DK-K07 | [7 ayrı önce/sonra kaydı](../kanitlar/karar-tablosu-sonuclari.json) |
| AC-03: onaylı iptal; silmeden durum değişimi | H5-S01, DK-K07, H3-T03 | [Node](../kanitlar/node-test-sonuclari.tap), [tarayıcı](../kanitlar/tarayici-sonuclari.json) |
| ALT-01: iptalden vazgeçme | H3-T02 | [Tarayıcı](../kanitlar/tarayici-sonuclari.json) |
| FR-01 / BR-01: dolu saat, iptal sonrası uygunluk | H5-S03, H5-S04, H6-R04, H6-R14, H3-T03–T04 | Node ve tarayıcı kayıtları |
| FR-02 / FR-05: oluşturma ve tamamlama ortak veri | H5-S04, H6-R10–R13, H6-B07 | Node ve tarayıcı kayıtları |
| FR-04: liste kapsamı | H5-S05, H3-T05 | Node ve tarayıcı kayıtları |
| FR-06: günlük toplam; iptalde toplam korunur | H6-R09, H3-T06 | Node ve tarayıcı kayıtları |
| H4 depo sözleşmesi: kopya, bulunmayan kayıt | H5-S02, H6-R05 | Node kayıtları |
| Saklama sınırı / hata | H5-S06, H6-R01–R07, H6-B08 | Node ve tarayıcı kayıtları |
| H3 açıklama metni / Tamamlandı sınırı | H3-T01, H3-T04 | Tarayıcı kayıtları |
| 390 px görünüm | H6-B09 | Tarayıcı kaydı; kapsamlı erişilebilirlik ölçümü değil |
| NFR-01 kullanılabilirlik, NFR-02 yanıt süresi, NFR-03 klavye | Ayrı ölçüm planları | Bu çalışmada ölçülmedi |
| Bağımsız kod/kanıt incelemesi | PR #15 ve #16 | Bekliyor; otomatik test bunun yerine geçmez |

Toplam Node testi 30'dur: 8 H5 + 7 karar + 15 regresyon. Tarayıcıdaki 9 senaryo bunlardan ayrı bir kümedir. Satır sayısı test kapsam yüzdesi değildir.

Kaynak uygulama commit'i: `2d11826f7d00baa245613305f5efa87c81902dc4`.
H6 test/CI commit'i: `5b18dbfeef9229f66859d74a3a379e96602e53f6`.
Tarayıcı ve karar tablosu JSON'larında uygulama kaynaklarının SHA-256 özetleri bulunur.
