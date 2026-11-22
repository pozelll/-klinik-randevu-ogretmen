# 3. hafta — Teslim kontrolü

Tarih: 28.10.2026  
Sürüm: 0.2 — 01–13 hazır; son sürüm yüklemesi ve kapanış bekliyor  
Uygulayan: Pınar Kızıloğlu — öğretmen uygulaması  
Konum: hafta-03/docs/11-teslim.md

## Teslimin amacı ve mevcut durum

Bu dosya yapılan işlere, kanıtlara ve eksiklere ulaşmayı sağlayan teslim dizinidir. Tek başına onay veya tamamlanma belgesi değildir. Kod değişiklikleri ve altı kontrol tamamlandı; bağımsız inceleme, birleştirme ve son teslim kontrolü bekliyor.

## Bağlantılar ve sürüm

| Alan | Kayıt |
|---|---|
| Depo | https://github.com/pozelll/-klinik-randevu-ogretmen |
| Pano | https://github.com/users/pozelll/projects/1/views/1 |
| H3 PR | https://github.com/pozelll/-klinik-randevu-ogretmen/pull/11 |
| Önceki belge PR'ı | https://github.com/pozelll/-klinik-randevu-ogretmen/pull/7 |
| Ana dal | main |
| Çalışma dalı | feat/h3-iptal-acikligi |
| PR #11 mevcut tabanı | docs/izlenebilirlik |
| Son ekranla doğrulanan çalışma commit'i | c0bff15; tam hash kaydedilmedi. |
| Sonraki belge yüklemesi | Kullanıcı 07/08/09 dosyalarını yüklediğini bildirdi; yeni commit kimliği ve uzak içerik ayrıca doğrulanmadı. |
| Merge commit | Yok; birleştirme doğrulanmadı. |

#7'nin inceleme ve birleştirmesi tamamlandıktan sonra #11'in main hedefi, farkları ve kontrolleri yeniden değerlendirilecek. Şimdiki docs/izlenebilirlik hedefine H3 değişiklikleri birleştirilerek önceki belge PR'ının kapsamı genişletilmeyecek.

## Teslim kontrol listesi

- [x] İlk ve güncel plan, kapsam artışı ve erteleme gerekçesi 05/06 belgelerinde kayıtlı.
- [x] H3-01 ana açıklama ve H3-02 onay metni uygulandı; PR içindeki index.html farkı birlikte okundu.
- [x] T01–T06 gerçek sonuçları, sınırları ve kanıt türleri 08-test-kaydi.md içinde kayıtlı.
- [x] Üç sayım PNG dosyası önceki paketle GitHub'a yüklendi; test belgesinden göreli bağlantıları yazıldı.
- [x] Gerçek H3 görevleri #8, #9 ve #10 bağlantıları kaydedildi.
- [x] H3 PR #11 açıldı; birlikte okuma 09-pr-inceleme.md içinde kayıtlı.
- [ ] Doldurulmuş 13 Markdown belgesinin son sürümleri teslimde mevcut. 01–13 hazırlandı; 10–13 belgelerinin GitHub yüklemesi henüz doğrulanmadı.
- [ ] Yazardan/ortak yazardan farklı gerçek kişinin incelemesi ve bulguların kapanışı.
- [ ] Eski başarı bildirimindeki koşulsuz saat ifadesi hakkında inceleme kararı/düzeltme.
- [ ] #7 bağımlılığının çözülmesi ve #11'in uygun hedefe birleştirilmesi.
- [ ] Birleştirme sonrası kısa kontrol ve son commit kaydı.
- [ ] Teslimi alacak kişinin özel depoya ve panoya erişiminin ayrı ayrı doğrulanması.
- [ ] Bireysel çıkış bileti ve ölçüm kayıtları. Kayıt yokluğu sıfır puan veya başarı sayılmaz.

Kutular yalnız açıklanan kapsamda tamamlanmayı gösterir. Testlerin geçmesi bütün Definition of Done koşullarını tamamlamaz; #8/#9 için son doğrulanan durum Open/In Progress, #10 için Open/Todo'dur.

## Görev kapsamı ve öğretmen örneğinin sınırı

Gerçek görevler: [#8](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/8), [#9](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/9), [#10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10).

Eski şablonda altı gerçek H3 Issue bağlantısı isteniyordu. Bu öğretmen uygulamasında üç gerçek Issue var; H3-04/05/06 ürün iş listesinde aday olarak kaldı. Altı kart oluşturulduğu iddia edilmez. Bu kapsam farkı öğrenci teslim şablonu dağıtılmadan önce açıkça uyumlandırılacak.

## Dosyalara erişim

- 01–06: Ekip/hedef, gözlem, iş listesi, kabul/Done koşulları, plan ve değişiklik kararı.
- [07-pano-ve-gunluk.md](07-pano-ve-gunluk.md): Son doğrulanan görev durumları ve kalan işler.
- [08-test-kaydi.md](08-test-kaydi.md): Altı kontrol ve üç sayım kanıtına bağlantılar.
- [09-pr-inceleme.md](09-pr-inceleme.md): PR bilgileri, birlikte okuma ve bekleyen bağımsız inceleme.
- [10-review-retro.md](10-review-retro.md): Ürün değerlendirmesi ve süreç iyileştirme taslağı; gerçek toplantı yapılmış sayılmaz.
- [12-metrikler.md](12-metrikler.md) hazır; [13-cikis-bileti.md](13-cikis-bileti.md) boş bireysel yanıt formu olarak hazır. Gerçek yanıtlar henüz alınmadı.

## Kaynak ve yapay zekâ desteği beyanı

Başlangıç malzemesi dersin Klinik Randevu prototipi ve ders şablonlarıdır. ChatGPT; adım adım yönlendirme, metin/kod düzenleme, belge hazırlama ve paylaşılan ekranları yorumlama desteği verdi. Uygulamayı yerel bilgisayarında çalıştıran, işlemleri yapan ve GitHub yüklemelerini gerçekleştiren kişi Pınar Kızıloğlu'dur. Sonuçlar ekranla doğrulananlar ve kullanıcı bildirimleri olarak ayrılmıştır. Asistanla ortak okuma bağımsız arkadaş incelemesi değildir. Yapılmayan kullanıcı, güvenlik veya performans ölçümleri yapılmış gösterilmez.

## Sınıfta kullanım

19 öğrenci üç beş kişilik ve bir dört kişilik grupta çalışır. Her grup kendi depo, pano, PR ve kanıt bağlantılarını teslim eder. Öğretmen örneğinin hesap adı, test sonuçları ve katkıları öğrencilerin gerçek çalışması yerine kopyalanmaz. Grup tesliminin yanında bireysel çıkış bileti ayrıca alınır.

Öğretmen konuşma notu: “Teslim dosyası, çalışmayı devralacak kişinin nereden başlayacağını gösterir. Kod nerede, hangi sürüm kontrol edildi, hangi kanıt var ve ne eksik? Eksikleri açık yazmak teslimi tamamlanmış saymak değildir; çalışmanın gerçek durumunu görünür kılar.”

## Kaydetme

Bu dosyayı hafta-03/docs içine kaydedin. Henüz GitHub'a yüklenmedi. Kalan kapanış belgeleri hazırlandıktan sonra birlikte yükleme yapılabilir.
