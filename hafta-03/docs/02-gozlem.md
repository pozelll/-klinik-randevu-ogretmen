# 3. hafta — Başlangıç gözlemi ve geliştirme ihtiyacı

Çalışma: Klinik Randevu — Pınar Kızıloğlu öğretmen uygulaması  
Belgeleme tarihi: 28.10.2026  
Sürüm: 0.1  
Dosyanın projedeki yeri: hafta-03/docs/02-gozlem.md  
Durum: Önceki gerçek gözlemlerden başlangıç gerekçesi hazırlandı. Bu adımda yeni uygulama denemesi veya kod değişikliği yapılmadı.

## 1. Bu dosyanın amacı

01-ekip-hedef.md içinde hastanın iptali onaylamak ile işlemden vazgeçmek arasındaki farkı anlayabilmesini hedefledik. Burada bu hedefi hangi gözlemlere dayanarak seçtiğimizi açıklıyoruz.

**Gözlem**, yaptığımız işlem ve gördüğümüz sonuçtur. **Geliştirme ihtiyacı**, bu gözlemden hareketle kullanıcı için iyileştirmek istediğimiz noktadır. İkisinin ayrı yazılması, çözüm önerisini gerçekleşmiş sonuç gibi sunmamızı önler.

## 2. Başlangıç ve kanıt kaynağı

| Alan | Kayıt |
|---|---|
| Uygulama | Mevcut Klinik Randevu projesinin index.html dosyası. |
| Gözlemlerin sürümü | 0.1 — birleşik 1–2. hafta başlangıç prototipi; önceki gözlem belgesindeki sürüm bilgisi. |
| Tarayıcı | Önceki denemelerde Google Chrome. Tarayıcının sürüm numarası kaydedilmedi. |
| Kaynak belge | ../../docs/08-prototip-gozlemleri.md |
| Kaynak gözlemlerin tarihi | 26–27.10.2026. Bu dosyanın hazırlanma tarihiyle karıştırılmaz. |
| İlgili seçimler | Hasta / Ece Yılmaz / Deniz Arı / 12.11.2030. Son tarih prototipin örnek randevu tarihidir. |
| Yerel dosyanın tam yolu | Henüz kaydedilmedi. Kullanıcının bilgisayarındaki yol tahmin edilmedi. |

Bu belge önceki öğretmen denemelerini özetler; 28.10.2026 tarihinde aynı denemeler yeniden yapılmış sayılmaz. Önceki ayrıntılı kayıtlar 08 dosyasında korunur.

## 3. Ne yaptık, ne gördük?

| Kaynak | Gerçekleşen işlem | Gözlenen sonuç |
|---|---|---|
| G-02 | R008 / 09:30 için İptal et seçildi ve açılan pencerede iptal onaylandı. | R008 İptal edildi olarak listede kaldı; 09:30 Uygun oldu. |
| G-03-T1 ve G-03-T2 | Vazgeçme denemesi planlanmışken kullanıcı, onay penceresinde Tamam seçtiğini bildirdi. | R009 ve ardından R010 iptal edildi; her denemenin sonunda 09:00 Uygun oldu. Bu sonuç, yapılan Tamam seçimiyle uyumluydu. |
| G-03-T3 | R011 / 09:00 için İptal et seçildi; açılan pencerede İptal seçilerek işlemden vazgeçildi. | R011 Bekliyor, 09:00 Dolu kaldı. Kullanıcı bildirimi ve paylaşılan görüntüler bu sonucu doğruladı. |

İlk G-03 kaydında yalnız sonuç ekranı görüldüğü ve pencere seçimi doğrulanamadığı için o kayıt, vazgeçme davranışına kanıt olarak kullanılmaz. Son doğrulanan vazgeçme sonucu G-03-T3'tür.

## 4. Üç ifadenin farklı anlamı

| Nerede? | Seçenek | Ne yapıyor? |
|---|---|---|
| Randevu kartında | İptal et | Randevuyu iptal etmek için onay penceresini açıyor. |
| Açılan küçük pencerede | Tamam | İptali onaylıyor; ilgili randevu İptal edildi durumuna geçiyor. |
| Açılan küçük pencerede | İptal | İptal işleminden vazgeçiyor; randevu mevcut durumunda kalıyor. |

Bu adlar önceki Türkçe tarayıcı ekranlarımızdaki adlardır. Özellikle karttaki İptal et ile penceredeki İptal aynı işlemi yapmaz. Öğretmen denemesinde bu ayrımı ayrıca açıklamak gerekti.

## 5. Geliştirme ihtiyacı ve öneri

**İhtiyaç:** Hasta, işlemden önce hangi seçeneğin randevuyu iptal edeceğini, hangisinin randevuyu koruyacağını ve onaylanan iptalin sonucunu anlayabilsin.

Bu ihtiyaca karşılık iki küçük değişiklik öneriyoruz:

1. Ana ekranda görünür açıklama: Hasta kendi Bekliyor randevusunu iptal edebilir; iptal edilen kayıt listede kalır. Aynı doktor, tarih ve saatte başka iptal edilmemiş kayıt yoksa saat yeniden uygun olur.
2. Onay penceresinde açık metin: Tamam'ın randevuyu iptal edeceği, İptal'in işlemden vazgeçip randevuyu koruyacağı açıklanır. İptalin kayıt ve saat üzerindeki sonucu da belirtilir.

Metinlerin son hâli, iş listesi ve kabul koşullarını hazırlarken netleştirilecek. Bu iki değişiklik henüz koda uygulanmadı. Tarayıcının kendi onay düğmelerinin adları bu çalışmada değiştirilmez.

## 6. İlgili gereksinim ve risk

| Bağlantı | Bu çalışmayla ilişkisi |
|---|---|
| FR-03 — ../../docs/03-gereksinimler.md | Hastanın kendi bekleyen randevusunu onayla iptal etmesi. |
| AC-03 ve ALT-01 — ../../docs/04-kabul-kriterleri.md | İptal onaylanınca beklenen sonuç ve vazgeçilince kaydın korunması. |
| BR-01 — ../../docs/03-gereksinimler.md | Aynı doktor, tarih ve saatin iptal edilmemiş başka kayıtla çakışmaması. |
| RSK-01 — ../../docs/06-riskler.md | İptal ve vazgeçme ifadelerinin karışması riski. |

## 7. Henüz doğrulanmayan varsayım

**Daha açık açıklamalar, kullanıcının istediği seçeneği bulmasını kolaylaştırabilir.**

Bu bir iyileştirme varsayımıdır. Henüz yeni metinle kullanıcı denemesi yapılmadı; hata oranı veya süre ölçülmedi. Önceki öğretmen denemelerinden bütün kullanıcıların aynı güçlüğü yaşayacağı sonucu çıkarılamaz. Yeni metnin işlevi bozmaması ile kullanıcıya daha anlaşılır gelmesi ayrı kontrol konularıdır.

## 8. Kaydetme ve sonraki adım

1. Bu dosyayı, kaydettiğiniz 01-ekip-hedef.md ile aynı hafta-03/docs klasörüne koyun.
2. Adını 02-gozlem.md olarak koruyun; .md.txt olmamasını kontrol edin.
3. Üç ifadenin farklı anlamı tablosunu okuyun. Bu adım için uygulamada yeniden iptal denemesi veya veri sıfırlama gerekmez.

Beklenen çıktı: Kullanıcı ihtiyacının dayanağını açıklayan başlangıç gözlemi kayıtlıdır.

Sonraki belge: 03-product-backlog.md. İyileştirme önerilerini yapılacak işler listesine dönüştürüp önceliklerini açıklayacağız. Gerçek GitHub görev bağlantıları ancak görevler oluşturulduğunda yazılacak.
