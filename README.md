# YAZ325 - Klinik Randevu öğretmen projesi

1–9. haftaların birikimli öğretmen çalışma kaynağı. Sekiz PR’dan oluşan zincir main'e birleştirildi. Kapanış güncellemesi: [PR #22](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/22).

## Derste aç

- [Güncel uygulama paketi: 0.3.0-rc.2](hafta09/dagitim/Klinik_Randevu_0.3.0-rc.2.zip). ZIP'in tamamını ayıklayıp index.html'i açın; src klasörü yanında kalsın.
- [Teknik kapanış, ölçümler ve merge kayıtları](hafta09/docs/49-kapanis-raporu.md).
- [İnsan kabul oturumu ve boş formlar](hafta09/docs/50-insan-kabul-oturumu.md).

| Hafta | Ders dosyaları |
|---|---|
| 1–2 | [Gereksinimler ve izlenebilirlik](docs/03-gereksinimler.md) |
| 3 | [Scrum ve kontrollü değişiklik](hafta-03/docs/05-sprint-plani.md) |
| 4 | [Mimari ve iş planı](hafta04/README.md) |
| 5 | [Modüler uygulama](hafta05/README.md) |
| 6 | [Test, karar tablosu ve CI](hafta06/README.md) |
| 7 | [Saat seçimi yardımı](hafta07/README.md) |
| 8 | [Tarihsel rc.1 paket üretimi](hafta08/README.md) |
| 9 | [Gitflow, release ve hotfix](hafta09/README.md) |

Eski PDF ve haftalık belgeler hazırlandıkları sürümün kayıtlarıdır. Oradaki “PR açık / ölçülmedi” ifadeleri için güncel durum 49 numaralı rapordadır. 0.9.x Gitflow paneli ayrı eğitim laboratuvarıdır; klinik uygulama sürümü değildir.

## Çalıştırma ve kontrol

Uygulamanın kendisi için sunucu/Node gerekmez. Testler için Node.js, Python ve Playwright gerekir.

```bash
node --test tests/*.test.cjs
python -m unittest discover -s hafta09/tools -p test_surum_kontrol.py -v
python scripts/check_candidate.py --profile h9
python tests/browser_smoke.py
python tests/performance_checks.py
xvfb-run -a python tests/keyboard_acceptance.py --native-dialog --evidence-dir klavye-kanit
```

CI bu kontrolleri main ve değişiklik PR'larında çalıştırır. Native klavye için Linux Xvfb, xdotool ve scrot gerekir; kurulum workflow dosyasında kayıtlıdır. Gitflow paneli JSON yükler: depo kökünde python -m http.server 8000 çalıştırıp http://localhost:8000/hafta09/panel/ açın.

## Kabul durumu

Otomatik işlev, paket, Gitflow ve klavye kontrolleri başarılı; 7/20/100/1000 kayıtla yerel performans ölçümü yapıldı. Dört gerçek katılımcılı NFR-01, NFR-02'nin özgün ekran-kare değerlendirmesi ve bağımsız insan/alıcı kabulü [#20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) kapsamında açık. AI teknik incelemesi insan onayı yerine yazılmadı. Nihai klinik yayın yapılmadı.

Tüm örnek veriler sentetiktir. Rol seçimi gerçek kimlik doğrulama değildir; saklama tek tarayıcıya aittir, çoklu cihaz/eşzamanlı kullanım kapsam dışıdır.

[Tarihsel başlangıç ve haftalık README kayıtları](docs/10-tarihsel-readme-kaydi.md).
