# H8 — Kabul ve teslim kapıları

Bu tablo 22 Kasım 2026 tarihli H8 hazırlığının teknik sonuçlarını ve o hazırlık anındaki bekleyen işleri gösterir. Grubunuzun gerçek değerlendirmesini alttaki boş forma kaydedin. PR #19 aynı gün `main` dalına birleştirilmiştir; güncel inceleme ve birleştirme durumu [PR kaydından](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19) izlenir.

| Koşul | Hazırlığın gerçek durumu | Kanıt / sorumlu |
|---|---|---|
| Aday kaynağı sabit | Tamamlandı | config/surum-adayi.json |
| Paket iki üretimde aynı | Tamamlandı | H8-P01 |
| Tam içerik, bozulma ve kaynak kontrolü | Tamamlandı | H8-P02–P08 |
| İş kuralları | 30/30 Node geçti | CI kaydı |
| Kaynakta tarayıcı akışı | 14/14 geçti | kaynak-tarayici-sonuclari.json |
| Teslim ZIP'i yeniden üretimle aynı | Tamamlandı | CI cmp adımı |
| Ayıklanmış teslim paketinde davranış | 14/14 geçti | paket-tarayici-sonuclari.json |
| Sürüm notu, kullanım ve geri dönüş planı | Hazır | docs/02, 03 ve 07 |
| Bağımsız kişi incelemesi | Bekliyor | Gerçek kişi, commit ve bulgu derste kaydedilecek |
| NFR-01 / NFR-02 / NFR-03 | Ölçülmedi | Kullanılabilirlik / yanıt süresi / klavye |
| Gerçek alıcı cihazında erişim ve kabul | Bekliyor | Alıcı ve sonuç kaydedilecek |
| Önceki PR'ların çözümü ve merge | Bekliyor | #7 → #11 → #12 → #15 → #16 → #18 → #19 |
| Nihai yayın onayı / GitHub Release | Yapılmadı | Ders adayı olarak sunuldu |
| Geri dönüş tatbikatı | Yapılmadı | Yalnız plan hazır |

**Hazırlık kaydının sonucu:** Teknik kontrolleri tamamlanmış, incelenebilir ders sürüm adayı. Bu teknik kayıt, nihai kullanıcı kabulünün tamamlandığını göstermez. Görev #17 ve PR #19'un güncel durumları ilgili GitHub kayıtlarından kontrol edilir.

## Gerçek kabul kaydı — doldurulacak

| Alan | Gerçek değerlendirme sırasında doldurun |
|---|---|
| Alıcı / tarih / cihaz / tarayıcı | |
| Değerlendirilen ZIP SHA-256 | |
| Açılan uygulama / yapılan akış | |
| Beklenen ve gerçek sonuç | |
| Kabul kararı / açık bulgu | |
| Düzeltme sürümü / yeniden kontrol | |
