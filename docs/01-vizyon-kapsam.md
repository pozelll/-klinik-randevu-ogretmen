# 01 — Vizyon ve kapsam

Ekip: Öğretmen denemesi  
Tarih: 27.10.2026  
Sürüm: Belge 0.1 — doldurulmuş öğretmen örneği  
Durum: İlk çalışma metni hazır; paydaş doğrulaması ve açık soruların yanıtları bekleniyor.  
İlgili issue / PR: Henüz oluşturulmadı.

Bu belge, Yazılım Geliştirme Süreçleri dersinin birleşik 1–2. haftasında kullanılan Klinik Randevu v0.1 eğitim prototipi için hazırlanmıştır. Başlangıç sürümünün kapsamını tanımlar; sonraki haftaların bütün özelliklerini bu sürüme yüklemez. Gerçek klinik paydaşlarıyla görüşülmediği için problem tanımı bir ders senaryosu varsayımı, kapsam ise görüşmeye açılacak taslaktır.

## Problem

Hastalar, seçtikleri doktorun hangi saatlerde uygun olduğunu ve kendi randevularının güncel durumunu takip etmekte zorlanmaktadır. Resepsiyon ve doktor, günlük randevuların kime ait olduğunu ve hangi aşamada bulunduğunu izlerken aynı saate birden fazla kayıt açılması ve kayıt durumlarının karıştırılması riskiyle karşılaşmaktadır.

## Kullanıcıya sağlayacağı değer

**Vizyon:** Hastaların uygun bir saate randevu alabildiği, klinik çalışanlarının günlük randevu akışını anlaşılır ve tutarlı biçimde izleyebildiği bir randevu yönetimi deneyimi sunmak.

- **Hasta:** Uygun saatleri ve kendi randevularının durumunu görerek randevusunu planlayabilir. Kendi bekleyen randevusunu iptal edebilmesi, plan değişikliğini yönetmesini sağlar.
- **Resepsiyon:** Seçilen hasta adına randevu oluşturabilir. Seçili doktorun o günkü kayıtlarını ve toplamlarını birlikte görerek bekleyen, tamamlanan ve iptal edilen randevuları takip edebilir.
- **Doktor:** Günlük listesinden bekleyen muayeneleri takip edebilir. Muayenesi biten randevuyu Tamamlandı olarak işaretleyerek bekleyen ve biten işleri ayırt edebilir.

Bu ifadeler hedeflenen kullanıcı faydasını açıklar. Zaman kazancı veya hata azalması gibi sayısal etkiler için ayrıca ölçüm yapılması gerekir.

Başlangıç prototipi bu akışları örnek kişilerle canlandırır. Dersteki amacımız, çalışan davranışları inceleyerek kullanıcı ihtiyacını, iş kurallarını ve kabul koşullarını yazmayı öğrenmektir.

## Kapsam içinde

Bu sürümde **FR**, işlevsel gereksinim; **BR**, iş kuralı kimliği olarak kullanılır. Kimlikler, sonraki belgelerde aynı davranışı takip etmemizi sağlar.

- **FR-01 — Uygun saatleri gösterme:** Seçili doktor ve örnek tarihe göre saatleri Uygun, Dolu veya Kapalı olarak listelemek.
- **FR-02 — Randevu oluşturma:** Hasta veya Resepsiyon rolünde uygun bir saat seçerek örnek hasta adına Bekliyor durumunda randevu oluşturmak.
- **FR-03 — Hastanın kendi randevusunu iptal etmesi:** Hastanın seçili doktor ve tarihteki kendi kayıtlarını göstermesi; kendi Bekliyor kaydını onay vererek iptal edebilmesi. Onay penceresinde vazgeçilirse randevu korunur. İptal onaylanırsa kayıt İptal edildi durumuyla listede kalır ve saat yeniden uygun olur.
- **FR-04 — Günlük listeyi gösterme:** Resepsiyon ve Doktor rollerinde seçili doktorun seçili gündeki bütün örnek hasta kayıtlarını göstermek.
- **FR-05 — Randevuyu tamamlama:** Doktor rolünde, görevli olarak seçili doktorun Bekliyor kaydını Tamamlandı durumuna geçirmek. Tamamlanan randevunun saati yeniden açılmaz.
- **FR-06 — Günlük toplamları gösterme:** Resepsiyon ve Doktor rollerinde seçili doktor ve tarih için bekleyen, tamamlanan, iptal edilen ve toplam kayıt sayısını göstermek.

**BR-01 — Aynı saate ikinci aktif kayıt açılmaması:** Aynı açık sayfanın mevcut veri durumunda, aynı doktor, tarih ve saat için iptal edilmemiş ikinci randevu oluşturulamaz. Bekliyor ve Tamamlandı kayıtları o saatin yeniden seçilmesini engeller; İptal edildi kaydı saati serbest bırakır. Bu kuralın bu sürümdeki gösterimi tek sekmenin verisiyle sınırlıdır.

**Örnek çalışma ortamı:** İki örnek hasta, iki örnek doktor, 12–13 Kasım 2030 tarihleri ve sabit saatler kullanılır. Tarayıcı izin verirse randevu kayıtları yerel olarak saklanır; saklama kullanılamazsa yalnız açık oturumun belleğinde tutulur. Sayfa yenilendiğinde rol, hasta, doktor ve tarih seçimleri başlangıç değerlerine döner.

## Kapsam dışında

Aşağıdaki sınırlar bu başlangıç sürümüne aittir. Sonraki haftaların kapsamı, ders planındaki ayrı çalışmalarla genişletilecektir.

- Gerçek kullanıcı hesabı, parola ile giriş ve sunucu tarafında yetkilendirme. Ekrandaki rol seçimi eğitim amaçlı bir canlandırmadır.
- Merkezi veritabanı, farklı cihazlarda ortak veri, sekmeler arasında eşzamanlama ve eşzamanlı randevu çakışmalarının güvenilir biçimde önlenmesi.
- SMS/e-posta bildirimi, ödeme, gerçek hasta veya sağlık kaydı, kurum sistemleriyle entegrasyon.
- Serbest takvim, tatil ve çalışma saatleri yönetimi, geçmiş tarih/saat engeli, farklı randevu süreleri, randevu taşıma ve arama.
- Resepsiyonun iptal veya tamamlama yapması; doktorun randevu oluşturması. Bu prototipte bu işlemler ilgili rollerin kapsamına alınmamıştır.
- Tamamlanmış kaydı iptal etme veya iptal edilmiş kaydı yeniden Bekliyor durumuna döndürme.
- Bütün kliniği veya birden fazla günü kapsayan raporlar. Günlük toplamlar yalnız seçili doktor ve tarih içindir.
- Bu başlangıç paketinin parçası olarak C#/Java MVC uygulaması, otomatik test altyapısı ve CI/CD servisi kurma.

## Başarıyı nasıl gözleyeceğiz?

Aşağıdaki kanıtlar `08-prototip-gozlemleri.md` dosyasındaki öğretmen denemesine dayanır. “Henüz uygulanmadı” yazan ölçüt, bu denemede başarılı yapılmış gibi değerlendirilmez.

| Kullanıcı amacı | Gözlenebilir başarı kanıtı | Kim kontrol edecek? |
|---|---|---|
| Hasta uygun saate randevu alır. | G-01: 09:30 için R008 Bekliyor olarak oluştu; 09:30 Dolu oldu. Yeni kaydın hasta, doktor, tarih ve saati yapılan seçimle uyuştu. | Denemeyi yapan üye ve kontrol eden ikinci ekip üyesi; öğretmen örneğinde eğitmen. |
| Hasta iptal eder veya iptal etmekten vazgeçer. | G-02: R008 İptal edildi oldu ve 09:30 yeniden Uygun göründü. G-03-T3: onay penceresinde İptal seçilince R011 Bekliyor, 09:00 Dolu kaldı. | İş kuralını yazan üye ve kontrol eden ikinci ekip üyesi. |
| Hasta kendi kayıtlarını izler. | G-04: Kaan seçildiğinde Randevularım alanında Kaan'ın R002 ve R004 kayıtları göründü; Ece'nin kayıtları bu listede gösterilmedi. Bu, arayüzde filtreleme gözlemidir. | Gereksinimi yazan üye ve kontrol eden ikinci ekip üyesi. |
| Doktor bir muayeneyi tamamlar. | G-05-B: R002 Bekliyor durumundan Tamamlandı durumuna geçti; 10:00 Kapalı oldu. Bekleyen sayısı 2'den 1'e, tamamlanan sayısı 1'den 2'ye geçti; toplam 8 kaldı. | Denemeyi yapan üye ve kontrol eden ikinci ekip üyesi. |
| Resepsiyon günlük akışı izler. | G-06: R011 Bekliyor durumunda, iptal veya tamamlama düğmesi olmadan göründü. Günlük toplamlar 1 bekleyen + 2 tamamlanan + 5 iptal edilen = 8 kayıt olarak doktor görünümüyle eşleşti. | Denemeyi yapan üye ve kontrol eden ikinci ekip üyesi. |
| Aynı dosya ve tarayıcıda sayfayı yenileyince randevu durumlarını yeniden görür. | Kaydetme denemesi: yenileme sonrası R011 Bekliyor, R002 Tamamlandı olarak kaldı; toplamlar yine 1 / 2 / 5 / 8 idi. Rol seçimi Hasta'ya döndü. Bu sonuç incelenen dosya ve tarayıcı içindir. | Denemeyi yapan üye ve kontrol eden ikinci ekip üyesi. |
| Resepsiyon seçilen hasta adına yeni randevu oluşturur. | Paket açıklamasındaki FR-02 kapsamında; öğretmen denemesinde henüz uygulanmadı. Beklenen kontrol: uygun saatten oluşturulan yeni kaydın seçili hastaya ait olması, Bekliyor görünmesi ve saatin Dolu olması. | Öğrenci grubunda denemeyi yapan üye ve kontrol eden ikinci ekip üyesi. |

Kayıt kimlikleri ve toplam sayılar bu öğretmen denemesine aittir. Öğrenci gruplarında önceki işlemlere göre farklı kimlik ve sayılar oluşabilir; başarı ölçütü, seçilen kaydın beklenen duruma geçmesi ve toplamların o grubun kayıtlarıyla tutarlı olmasıdır.

## Varsayımlar ve açık sorular

- **Varsayım:** Problem tanımı eğitim için oluşturulmuş örnek klinik senaryosudur; gerçek bir klinikten doğrulanmış ihtiyaç olarak sunulmaz.
- **Çalışma koşulu:** Başlangıç incelemesinde her grup kendi proje kopyasında, tek sekmede ve yalnız örnek verilerle çalışır.
- **Varsayım:** Mevcut prototipteki rol ve işlem kuralları, paydaş görüşmesinde tartışılacak başlangıç noktasıdır. Gerçek ürün kapsamı henüz paydaşlarca onaylanmamıştır.
- **Kanıtın sınırı:** Aynı tarayıcıda başarılı olan yenileme deneyi, başka tarayıcı veya cihazlarda ortak kayıt bulunduğunu göstermez.
- **Paydaşa sorulacak soru 1:** İptal onayındaki düğmeler “Randevuyu iptal et” ve “Vazgeç” biçiminde adlandırılmalı mı? Dayanak: iptal ile vazgeçme akışının öğrenilmesi sırasında düğmelerin anlamları karıştı.
- **Paydaşa sorulacak soru 2:** Resepsiyon hastanın talebi üzerine bekleyen randevuyu iptal edebilmeli mi; bu yetki hangi kurallara bağlanmalı? Dayanak: mevcut resepsiyon görünümünde bu işlem bulunmuyor.
- **Paydaşa sorulacak soru 3:** Hasta, doktor ve resepsiyonun farklı cihazlardan aynı kayıtları görmesi gerekiyor mu; değişiklikler diğer kullanıcılara ne kadar sürede yansımalı? Dayanak: mevcut kayıtlar yalnız aynı tarayıcıda tutuluyor.

Bu soruların yanıtları henüz alınmadı. Alınan kararlar daha sonra `07-toplanti-notu.md` dosyasına, gerekli kapsam değişiklikleri ise bu belgenin yeni sürümüne işlenecek.

Dayanak dosyalar: `README.md`, `BILINEN_KISITLAR.md` ve `docs/08-prototip-gozlemleri.md`.
