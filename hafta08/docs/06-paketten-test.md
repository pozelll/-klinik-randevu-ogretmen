# 8. hafta / 6. basamak — Teslim dosyasını sınadık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Çalışma klasörünün çalışması, teslim paketinin eksiksiz olduğunu tek başına göstermez. Bu nedenle paketi ayrı klasörde açıp aynı davranış senaryolarını çalıştırıyoruz. Tarayıcı raporundaki uygulama dosyası özetlerini aday tanımıyla karşılaştırarak testin doğru içeriğe ait olduğunu kontrol ediyoruz.

## Ekranda göster ve uygula

CI’da önce kaynak testlerini, sonra paket üretimini, ardından --app-dir ile ayıklanmış paketteki tarayıcı adımını gösterin. Kaynakta 14 ve pakette 14 senaryo vardır; bunlar 28 farklı senaryo değildir. Paket raporundaki beş kaynak özetini aday tanımıyla eşleştirin.

- [06-paketten-test.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/06-paketten-test.md)
- [Paket tarayıcı kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/kanitlar/paket-tarayici-sonuclari.json)
- [CI kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/kanitlar/ci-kaydi.json)

## Öğrenciye soru

**Paket testi ile kaynak testinin aynı olması neden yararlı?**

Beklenen açıklama: Aynı beklenen davranışların teslim edilen içerikte de çalıştığını gösterir; eksik dosya veya yanlış sürüm riskini azaltır.

## Grubun yapacağı iş

Kendi ZIP’ini yeni klasörde aç. En az bir uçtan uca akışı paket üzerinde tekrar çalıştır ve sürümü kaydet.

Kontrol: Tarayıcı gerçekten ayıklanan klasörü mü açmış? Test edilen içerik teslim ZIP’iyle aynı mı?

## Hazırlığın gerçek durumu

Kaynak ve paket: 14’er senaryo geçti. 30 Node testi kaynak üzerinde de geçti.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## Gerçek yürütüm ve yeniden çalıştırma

[GitHub Actions koşusu](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45021999531) · kaynak/test commit'i `6eb6088bdd8cdc9b8c3fe5b7ff1b703e2bd87fa2`.

```bash
node --test --test-reporter=tap tests/*.test.cjs
python scripts/check_candidate.py
python scripts/build_candidate.py extract hafta08/dagitim/Klinik_Randevu_0.3.0-rc.1.zip --target kendi-ciktilarim/aday-paket
python tests/browser_smoke.py --app-dir kendi-ciktilarim/aday-paket
```

Ayıklama hedefi boş olmalıdır; araç dolu hedefin üzerine yazmaz. Tarayıcı testi için Playwright ve Chromium gerekir; kurulum H7 test belgesindedir. Paketi normal kullanıcı olarak açmak için bu araçlar gerekmez.

CI: 30 Node, kaynakta 14 tarayıcı, 8 paket kontrolü, dağıtım ZIP'i ile yeniden üretilen ZIP'in bayt eşitliği ve ayıklanmış dağıtım paketinde 14 tarayıcı senaryosu geçti. İki tarayıcı yürütümü aynı senaryoların iki içerik konumunda kontrolüdür. Kayıtlar: `kaynak-tarayici-sonuclari.json`, `paket-tarayici-sonuclari.json`, `ci-paket-kontrolleri.json`, `ci-kaydi.json`.
