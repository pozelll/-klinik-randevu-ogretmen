# 8. hafta / 6. adım - Paketten test

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Teslim ZIP'ini ayrı bir klasöre ayıklayıp uygulamanın davranışlarını bu içerik üzerinde sınayın. Test edilen dosyaların özetlerini aday tanımıyla eşleştirin.

## Grup çalışması

1. Kendi teslim ZIP'inizi ve SHA-256 özetini kaydedin.
2. Paketi yeni ve boş bir klasöre ayıklayın.
3. Kaynak uygulamada kullandığınız en az bir uçtan uca akışı ayıklanmış paket üzerinde tekrar çalıştırın.
4. Testin açtığı uygulama yolunu, kaynak sürümünü, beklenen davranışı ve gerçek sonucu kaydedin.
5. Kaynak ile paket sonuçlarını karşılaştırın; aynı senaryonun iki yürütümünü iki farklı senaryo olarak saymayın.

## Teslim edilecek çıktı

Paket kimliği, ayıklama konumu, test edilen dosya özetleri, komutlar, ortam, tarih ve gerçek sonuçlar. Test kanıtı teslim ettiğiniz ZIP'in içeriğiyle eşleşmelidir.

## Tarihli örnek yürütüm ve yeniden çalıştırma

Aşağıdaki CI sonuçları 22 Kasım 2026 tarihli H8 çalışmasına aittir. Örnek komutları `release/h8-surum-adayi` dalının depo kökünde çalıştırın.

[GitHub Actions koşusu](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45021999531) · kaynak/test commit'i `6eb6088bdd8cdc9b8c3fe5b7ff1b703e2bd87fa2`.

```bash
node --test --test-reporter=tap tests/*.test.cjs
python scripts/check_candidate.py
python scripts/build_candidate.py extract hafta08/dagitim/Klinik_Randevu_0.3.0-rc.1.zip --target kendi-ciktilarim/aday-paket
python tests/browser_smoke.py --app-dir kendi-ciktilarim/aday-paket
```

Ayıklama hedefi boş olmalıdır; araç dolu hedefin üzerine yazmaz. Tarayıcı testi için Playwright ve Chromium gerekir; kurulum H7 test belgesindedir. Paketi normal kullanıcı olarak açmak için bu araçlar gerekmez.

CI: 30 Node, kaynakta 14 tarayıcı, 8 paket kontrolü, dağıtım ZIP'i ile yeniden üretilen ZIP'in bayt eşitliği ve ayıklanmış dağıtım paketinde 14 tarayıcı senaryosu geçti. İki tarayıcı yürütümü aynı senaryoların iki içerik konumunda kontrolüdür. Kayıtlar: `kaynak-tarayici-sonuclari.json`, `paket-tarayici-sonuclari.json`, `ci-paket-kontrolleri.json`, `ci-kaydi.json`.

- [H7 test ortamı kurulumu](../../hafta07/docs/06-test-kaniti.md)
- [Kaynak tarayıcı sonuçları](../kanitlar/kaynak-tarayici-sonuclari.json)
- [Paket tarayıcı sonuçları](../kanitlar/paket-tarayici-sonuclari.json)
- [CI paket kontrolleri](../kanitlar/ci-paket-kontrolleri.json)
- [CI kaydı](../kanitlar/ci-kaydi.json)

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
