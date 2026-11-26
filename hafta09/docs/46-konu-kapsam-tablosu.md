# 46 - 14 konu kapsamı ve öğrenciye devir

> 22 Kasım 2026 kapanış güncellemesi: PR zinciri main’e birleştirildi; rc.2, gerçek klavye ve performans sonuçları [49 numaralı raporda](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md) bulunur. Aşağıdaki rc.1 hazırlık kayıtları ve açık PR durumları birleştirme öncesine aittir. Bağımsız insan incelemesi ve kabulü birleştirme işlemiyle tamamlanmış sayılmaz; açık işler [insan kabul oturumu ve formlarında](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/50-insan-kabul-oturumu.md) izlenir.

Bu tablo mevcut **öğretmen hazırlığına** aittir. “Kanıtlı örnek” öğrencinin kazanımı tamamladığı anlamına gelmez. Öğrenci kendi dosya, ölçüm, katkı ve değerlendirmesini ekler. “Kısmi” kapsamın bir bölümünde kanıt olduğunu, “eksik” uygulama kanıtı bulunmadığını belirtir.

| No / konu | Mevcut çıktı ve kanıt | Durum | Öğrenci görevi / açık iş |
|---|---|---|---|
| 1 Süreçlere giriş | [Vizyon/kapsam](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/docs/01-vizyon-kapsam.md), görev ve PR akışı | Kanıtlı örnek | Süreç adımını kendi çıktısına bağla |
| 2 Yaşam döngüsü | [H4 seçim](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta04/docs/01-yasam-dongusu-secimi.md) | Kanıtlı örnek | Alternatif modeli gerekçeyle karşılaştır |
| 3 Agile/Scrum | [H3 plan](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta-03/docs/05-sprint-plani.md), [retro](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta-03/docs/10-review-retro.md) | Kanıtlı örnek | Gerçek ekip planı ve uyarlama kaydı oluştur |
| 4 Gereksinim analizi | [FR/BR/NFR](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/docs/03-gereksinimler.md), kabul ve izlenebilirlik | Kanıtlı örnek | Paydaş ihtiyacını kabul koşuluna dönüştür |
| 5 Mimari ve tasarım kalıpları | [H4 karar](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta04/docs/02-mimari-karar.md), veri erişim sınırı | Kısmi | Mimari seçimini ve tasarım kalıbı alternatifini tartış |
| 6 Modülerlik/bağımlılık | [H5 sözleşme](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta05/docs/02-sozlesme.md), src ayrımı | Kanıtlı örnek | Değişikliğin bağımlılık etkisini göster |
| 7 Birim/bütünleşme/kabul testleri | [H6 izlenebilirlik](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta06/docs/09-izlenebilirlik.md), H9 klinik CI | Kısmi | Kendi senaryonu çalıştır; gerçek kullanıcı kabulünü ekle |
| 8 CI/CD stratejileri | [.github/workflows](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/.github/workflows/klinik-tests.yml), H8 paket | Kısmi | CI var; gerçek hedefe CD ve geri dönüş kararı eksik |
| 9 Gitflow/sürüm kontrolü | [39–43 belgeleri](39-gitflow-ve-dal-plani.md), gerçek bundle, 12 kontrol | Kanıtlı örnek | Kendi çakışma, release ve iki hedefli hotfix kanıtını üret |
| 10 İleri proje yönetimi | [H4 plan](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta04/planlar/01-ilk-is-plani.md), [45](45-plan-gerceklesen.md) | Kısmi | Gerçek sorumlu, emek ve sapma verisini kaydet |
| 11 Güvence/güvenlik/gizlilik/güvenilirlik | Sentetik veri, rol kuralı testleri, paket/geri dönüş kaydı | Kısmi | Gerçek kimlik güvenliği, NFR ve toparlanma sınamalarını planla |
| 12 Metrikler ve kalite | Test sayıları, [44 kalite kapıları](44-surum-kalite-karari.md) | Kısmi | Test sayısından hizmet kalitesi sonucu çıkarma; eksik ölçümü yap |
| 13 Performans/ölçeklenebilirlik | Plan var; aynı adaya bağlı yük/p95/hata/iş hacmi kanıtı yok | Eksik | Mimariye uygun ölçüm planı, ham veri, grafik ve karar üret |
| 14 Gelecek/AI/otomasyon | AI destekli hazırlık ve çalışan CI/deney otomasyonu | Kısmi | AI önerisini bağımsız değerlendir; sorumluluk ve süreç etkisini tartış |

## 10–14. haftaya geçiş

Yeni grup projesi için kapsam, mimari, kabul koşulu, test, kalite kapısı, CI ve sürüm akışını seçin. Önce eksik kanıtı görevleştirin. Başarıyı öğretmen örneğinin çalışmasıyla değil grubun kendi yürütümü ve değerlendirmesiyle gösterin.

[Boş grup formu](../sablonlar/grup-kaydi.md). Önceki ders planında 10 kapsam/plan; 11 tasarım/ilk parça; 12 test/CI; 13 performans/hata/sürüm; 14 demo ve kanıtlı teslim olarak ayrılmıştır.
