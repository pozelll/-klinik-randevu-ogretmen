# YAZ325 - 6. hafta: Karar Tablosundan Test Kanıtına

Öğrenci çalışma rehberi. Güncelleme: 26 Kasım 2026.

Bu hafta 5. haftadaki modüler uygulamayı kullanarak test kapsamını, karar tablosunu, otomatik kontrolleri ve test kanıtlarını hazırlayacaksınız. Her grup kendi deposunda çalışır ve kendi çalıştırma sonuçlarını kaydeder.

Örnek çalışma dalı: `test/h6-karar-tablosu` · [Görev #14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16) 22 Kasım 2026'da `main` dalına birleştirilmiştir.

## Çalışma adımları

| Basamak | Çalışma | Grubun üreteceği çıktı |
|---|---|---|
| 1 | [Test planı](docs/01-test-plani.md) | Gereksinim, başlangıç verisi, test düzeyi ve beklenen sonuç. |
| 2 | [Karar tablosu](docs/02-karar-tablosu.md) | Her koşul için ayrı başlangıç ve sonuç kaydı. |
| 3 | [İş kuralı testleri](docs/03-kural-testleri.md) | Sonuç kodu, önce/sonra veri ve yazma sayısı. |
| 4 | [Bütünleşme ve regresyon](docs/04-butunlesme.md) | Ortak veri üzerinde ardışık işlemlerin test sonuçları. |
| 5 | [Tarayıcı testleri](docs/05-tarayici.md) | Vazgeçme, onaylı iptal ve ekran akışı kayıtları. |
| 6 | [Sürekli bütünleştirme (CI)](docs/06-ci.md) | Çalıştırma bağlantısı, commit ve gerçek kontrol sonucu. |
| 7 | [Kod ve kanıt incelemesi](docs/07-inceleme.md) | İnceleyen, kapsam, bulgular ve varsa düzeltme kaydı. |
| 8 | [İzlenebilirlik ve teslim](docs/08-teslim.md) | Gereksinimden test kanıtına ulaşan teslim paketi. |

## Grubun iş bölümü

İki, üç ve dört kişilik gruplar karar tablosu, test yazımı, test yürütümü ve kanıt incelemesini [grup büyüklüğüne göre](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşır. Her üye anlamlı bir çıktı ve gerçek katkı kaydı üretir; yazımına katılmadığı içeriği inceler. Ortak yazılan bölüm için gerekirse grup dışından inceleyen belirlenir. Sorumluları, tarihleri ve sonuçları [grup kaydına](sablonlar/grup-kaydi.md) yazın.

## Kaynaklar

- [Tek sayfalık süreç infografiği](dagitim/YAZ325_Hafta_06_Surec_Infografik_Aktif_Linkli.pdf)
- [Gereksinim-test-kanıt eşleştirmesi](docs/09-izlenebilirlik.md)
- [İndirme, açma ve test komutları](docs/10-yeniden-calistirma.md)
- [Boş grup kayıt formu](sablonlar/grup-kaydi.md)

## Örnek sonuçların kullanımı

22 Kasım 2026 tarihli örnek çalışma kayıtlarında 30 Node testi (8 H5 + 7 karar + 15 regresyon) ve 9 Chromium senaryosu başarılıdır. Bu kayıtlar kendi grubunuzun çalıştırma sonucu değildir. Kendi sürümünüzün commit'ini, araç sürümünü, tarihi ve gerçek sonucunu ayrıca kaydedin.

Otomatik test, kod incelemesi ve kullanılabilirlik/performans/klavye ölçümleri ayrı çalışmalardır. 4. haftadaki 9 saat / 19 kişi-saat planlama tahmini, gerçekleşmiş grup emeği veya otomatik test süresi olarak kullanılamaz.
