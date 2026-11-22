# H5 / H6 - Yeniden çalıştırma

## Uygulama

1. GitHub'da `test/h6-karar-tablosu` dalını seçin.
2. Code > Download ZIP ile bütün depoyu indirin ve tamamen ayıklayın.
3. `index.html` ile `src/` aynı kökte kalmalı. `index.html` dosyasını tarayıcıda açın.
4. Sabit sentetik takvim 12–13 Kasım 2030'dur; bugünkü tarih seçilmez.
5. Örnek veriyi sıfırlama işlemi bu demodaki mevcut yerel değişiklikleri siler; önce gerekli gözlemleri kaydedin.

Uygulama klasik yerel betikler kullanır. Sunucu, Node.js, npm kurulumu veya API anahtarı gerektirmez. file:// adresindeki kalıcılık tarayıcıya bağlıdır; alt bölümde kaydetme durumunu okuyun.

## Node testleri

Node.js 24 kullanılarak doğrulandı. Projenin kökünde:

```bash
node --test tests/h5-smoke.test.cjs tests/h6-decision.test.cjs tests/h6-regression.test.cjs
```

Beklenen: 30 test, 30 başarılı, 0 başarısız. Beklenen sayıyı gerçek sonuç alanına otomatik yazmayın.
Karar satırlarının JSON kanıtını üretmek isteğe bağlıdır. Ubuntu/bash örneği:

```bash
EVIDENCE_DIR=sonuclar node --test tests/h6-decision.test.cjs
```

## Tarayıcı testleri

Python ve Playwright gerekir. Ubuntu'da `python3`, Windows'ta kurulumunuza göre `python` veya `py` kullanın.

```bash
python3 -m pip install playwright
python3 -m playwright install chromium
python3 tests/browser_smoke.py --evidence-dir sonuclar
```

GitHub runner Linux sistem bağımlılıklarını `python -m playwright install --with-deps chromium` ile kurar.
Beklenen: 9 PASS. Betik varsayılan çalıştırmada kanıt dosyalarını değiştirmez; yalnız `--evidence-dir` verildiğinde çıktı yazar.

## İnsan kontrolü

- PR Files changed: doğru dal ve yalnız beklenen dosyalar.
- Kural ve depo testlerinin beklentileri gereksinime uygun mu?
- Onay metni, vazgeçme ve gerçek saat sonucu kullanıcıya açık mı?
- Veri kapsamı, saklama sınırı ve ölçülmeyen NFR'ler doğru belirtilmiş mi?
- İnceleyen kişi, tarih ve incelenen commit kayıtlı mı?

## Kavram kaynakları

- [GitHub: Pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests)
- [Node.js: Test runner](https://nodejs.org/api/test.html)
- [MDN: Window.localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

Kaynaklar 22 Kasım 2026'da kontrol edildi. Proje kararları, testler ve sentetik örnekler bu ders çalışmasına aittir.
