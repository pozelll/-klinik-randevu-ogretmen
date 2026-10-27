# Bağlam diyagramı — adım adım çalışma

Tarih: 27.10.2026  
Proje: Klinik Randevu eğitim prototipi  
Sürüm: Diyagram 1.1 — ok açıklamalarının yerleşimi düzeltildi.  
Durum: Kullanıcının ilk çizimi editörde açtığı görüntüyle görüldü. Bu görüntüdeki dar ve üst üste binen ok açıklamaları düzeltildi; yeni çizim içeriği gerçek editörde görsel olarak kontrol edildi. Düzeltilmiş sürümün kullanıcı bilgisayarında yeniden açılması/kaydedilmesi ve öğrenci incelemesi henüz doğrulanmadı.

**Bu dosya nereden geldi?** Bu rehber başlangıç paketinde yoktu; diyagramın amacını, açma/kaydetme adımlarını ve sınıf uygulamasını açıklamak için 27.10.2026'da sonradan eklendi. Ek bir gereksinim veya değerlendirme belgesi değildir; uygulamanın çalışması için gerekli değildir. Rehberi **diagrams/01-baglam-adim-adim.md** konumunda saklayın. **docs** klasöründeki 01–09 proje belgeleri mevcut düzenini korur.

## 1. Neyi öğreniyoruz?

Bağlam diyagramı, sistemi tek kutu olarak ele alır: Kim kullanıyor, sisteme ne iletiyor ve karşılığında ne görüyor? Bu çizimde üç rol ve her rol için iki yönlü etkileşim vardır. İşlemlerin sırası gösterilmez; okları yukarıdan aşağıya bir işlem akışı gibi okumayın.

| Rol | Sisteme iletilen seçim / istek | Sistemin gösterdiği bilgi / sonuç | Gereksinim bağlantısı |
|---|---|---|---|
| Hasta | Doktor/tarih seçimi, randevu oluşturma ve kendi kaydını iptal isteği | Seçili doktor/tarihin saatleri, kendi randevuları ve işlem sonucu | FR-01, FR-02, FR-03 |
| Resepsiyon | Doktor/tarih ve adına kayıt açılacak hasta seçimi, randevu isteği | Seçili doktor/tarihin günlük listesi, saatler, toplamlar ve işlem sonucu | FR-01, FR-02, FR-04, FR-06 |
| Doktor | Görevli doktor/tarih seçimi, randevuyu tamamlama isteği | Seçili doktor/tarihin günlük listesi, saatler, toplamlar ve işlem sonucu | FR-01, FR-04, FR-05, FR-06 |

Hasta yalnız kendi Bekliyor kaydını iptal eder. Resepsiyon bu sürümde iptal veya tamamlama yapmaz. Doktor yeni randevu oluşturmaz; görevli seçilen doktorun o tarihteki Bekliyor kaydını tamamlar. Günlük liste ve toplamlar bütün klinik/tarihler için ortak rapor değildir.

Bu model 01-vizyon-kapsam.md, 02-paydaslar.md, 03-gereksinimler.md ve başlangıç prototipinin davranış tanımına dayanır. Diyagramın varlığı, bütün işlevlerin test edildiği anlamına gelmez. Özellikle resepsiyonun randevu oluşturması önceki bireysel uygulamada ayrıca denenmedi.

## 2. Dosyayı açalım

diagrams.net/draw.io kullanmak için ayrı bir üyelik gerekmez. Bu etkinlikte bilgisayardaki dosyayla çalışılır; bulut hesabı bağlamak gerekmez.

1. Hazırlanan **01-baglam.drawio** dosyasını indirin.
2. Projede index.html ile aynı düzeyde bulunan **diagrams** klasörüne koyun. Önceki dosya yalnız boş başlangıç şablonuysa güncel örneği onun yerine kullanın. Kendi çiziminiz varsa önce ayrı bir kopyasını koruyun.
3. Tarayıcıda **https://app.diagrams.net/** adresini açın.
4. Saklama yeri sorulursa **Device / Cihaz** seçeneğini kullanın. Mevcut bir diyagram açıksa önce kaydedin.
5. Türkçe arayüzde **Dosya → Şuradan aç → Cihaz** yoluyla indirdiğiniz dosyayı seçin. İngilizce karşılığı **File → Open From → Device**. Başlangıç ekranında dosya açma seçeneği görünürse oradan da seçebilirsiniz.
6. Ekranda Hasta, Resepsiyon, Doktor ve Klinik Randevu kutularını; toplam altı yönlü oku kontrol edin.

Bir menünün ekranını henüz görmediysek açıldığını veya aynı yerde bulunduğunu varsaymayız. Buradaki yol resmî kullanım dokümanına dayanır; kendi ekranınızda açılan kutuyu okuyarak ilerleyin. Kaydedilmemiş çalışmanız varsa değişiklikleri atma seçeneğini kullanmadan önce saklayın.

## 3. Diyagramı nasıl okuyacağız?

Önce Hasta satırındaki sisteme giden oku okuyun: hasta bir seçim veya işlem isteği iletiyor. Ters yöndeki ok, sistemin hastaya hangi bilgiyi gösterdiğini anlatıyor. Ardından aynı okumayı Resepsiyon ve Doktor için yapın.

- Yeşil oklar sisteme iletilen seçimleri ve istekleri, mavi oklar kullanıcıya gösterilen bilgileri ve sonuçları temsil eder. Anlamı yalnız renkten değil, ok yönü ve metninden de okuyun.
- Hasta, Resepsiyon ve Doktor yazılımın dışındaki kullanıcı rolleridir. Klinik çalışanı olmak, yazılımın iç bileşeni olmak demek değildir.
- Klinik yönetimi bir paydaştır; prototipte ona ait kullanıcı ekranı olmadığı için bu çizimde ayrı bir rol kutusu yoktur.
- Veritabanı, localStorage, B1/B2/B3 ekran alanları ve kod parçaları bu bağlam çiziminde ayrı kutulara bölünmez.
- GitHub ve diagrams.net proje geliştirme araçlarıdır. Klinik Randevu'nun bu sürümünde çalışma zamanı dış servisleri olarak bağlanmazlar. SMS ve ödeme bağlantıları da bulunmaz.
- Rol seçimi eğitim simülasyonudur. Oklar gerçek kullanıcı hesabı, güvenli oturum veya ortak sunucu bağlantısı kurulduğu anlamına gelmez.

## 4. Düzenleme ve kaydetme

Bir kutuyu seçtiğinizde o kutuyu, bir okun yazısını seçtiğinizde etkileşim açıklamasını düzenlersiniz. Öğretmen örneğinin anlamını değiştirmeden önce ilgili gereksinime bakın. Öğrenci çalışmasında etiketler ekibin kendi açıklamasıyla yazılabilir; rol sınırları korunmalıdır.

### İlk alıştırma — Hasta kutusunun yazısını değiştirme

Amaç, bir şeklin etiketini düzenlemek ve değişikliği geri almak. Kullanıcı metni düzenlemeyi denedi; Enter'a bastıkça yazının yukarı kaydığını bildirdi. Düzenleme, geri alma ve kaydetme adımlarının tamamı henüz doğrulanmadı.

1. Düzeltilmiş diyagramda **Hasta** yazısına çift tıklayın.
2. Metin düzenleme açıkken yazıyı **Hasta (randevu alan kişi)** olarak değiştirin. Yalnız metni seçmek gerekiyorsa yazı imleci etiketin içindeyken Ctrl + A kullanın.
3. Kutunun dışındaki boş çizim alanına **bir kez tıklayarak** metin düzenlemesini bitirin. Bu ayarda Enter yeni satır ekler. Kutuda yeni açıklamayı görmelisiniz; uzun yazı kutu içinde birkaç satıra ayrılabilir.
4. Metin düzenleme bittikten sonra **Düzenle → Geri al** veya **Ctrl + Z** kullanın. Etiket yeniden **Hasta** olmalı. Arada başka değişiklik yapmayın; geri alma son işlemi hedefler.
5. **Dosya → Kaydet** ile çizimi kaydedin; dosya yeri sorulursa projenin **diagrams/01-baglam.drawio** konumunu kullanın.

Beklenen son durum: Hasta, Resepsiyon ve Doktor kutuları; bir Klinik Randevu kutusu ve altı ok korunur. Kaydedilecek etiket yeniden Hasta'dır. Bu yalnız diyagram düzenleme alıştırmasıdır; uygulamanın rol kodunu veya izinlerini değiştirmez. Yeni bir Markdown dosyası veya yeni görev kartı oluşturulmaz.

Bir sonraki alıştırmada mevcut ok açıklamasının yazısına çift tıklayarak etkileşim metnini düzenleyeceğiz. Kutudaki ad kullanıcı rolünü, ok üzerindeki metin ise iletilen isteği veya gösterilen bilgiyi anlatır.

**Enter'a birkaç kez basıldıysa toparlama:** Kutunun yazısını çift tıklayın. Yazı imleci metnin içindeyken Ctrl + A ile metni ve eklenen boş satırları seçip yalnız **Hasta** yazın. Ardından boş çizim alanına bir kez tıklayın ve **Dosya → Kaydet** kullanın. Metin düzenlemesinden çıkmak ile dosyayı kaydetmek ayrı işlemlerdir. Bu toparlamada birden çok düzenleme oluşabileceğinden, tek bir Geri al komutunun mutlaka Hasta etiketine döndüreceği varsayılmaz. Önceki Enter ile bitirme yönergesi 27.10.2026 tarihinde kullanıcı bildirimi ve güncel editör yapılandırma açıklaması üzerine düzeltildi; toparlama sonucu henüz kullanıcıdan gelmedi.

**File → Save As** ile **01-baglam.drawio** adı ve cihaz konumu seçilir. Windows'ta uygulamanın Farklı Kaydet kısayolu Ctrl + Shift + S'dir. Tarayıcı dosyayı doğrudan İndirilenler'e bırakırsa güncel kopyayı projenin diagrams klasörüne taşıyın. Dosyayı editörde yeniden açıp üç rol, bir sistem ve altı okun korunduğunu kontrol edin.

| Dosya | Ne için saklanır? | Projede önerilen yer |
|---|---|---|
| 01-baglam.drawio | Şekilleri, okları ve yazıları sonradan düzenlemek | diagrams/01-baglam.drawio |
| 01-baglam.png | Sunumda veya raporda görsel olarak göstermek | diagrams/01-baglam.png |
| 01-baglam-adim-adim.md | Bu etkinliğin yönergesi ve açıklaması | diagrams/01-baglam-adim-adim.md |

Güncel PNG, düzeltilen çizim gerçek diagrams.net editöründe görüntülendikten sonra editörden dışa aktarıldı; arayüzün ekran görüntüsü değildir. PNG tek başına düzenlenebilir çizim dosyasının yerine geçmez. DRAWIO değişirse sunumda kullanılacak görsel de son sürümle eşleştirilmelidir. Ayrı **01-baglam-editor-kontrol-20261027.jpg** dosyası, düzeltmenin gerçek editördeki kontrol görüntüsüdür; kullanıcının kendi bilgisayarında yeni sürümü kaydettiğinin kanıtı değildir.

## 5. Sınıfta görev paylaşımı

Bu etkinlik için önerilen dağılım; yapılmış öğrenci çalışması olarak kaydedilmemiştir. Sınıf 19 kişi: ilk üç grup beşer, dördüncü grup dört kişidir.

| Görev | Beş kişilik gruplar | Dört kişilik grup |
|---|---|---|
| Sistem sınırını 01 belgesinden açıklamak | Üye 1 | Üye 1 |
| Rol ve izinleri 02 belgesinden kontrol etmek | Üye 2 | Üye 2 |
| Diyagramı oluşturmak / düzenlemek | Üye 3 | Üye 3 |
| Okları 03 gereksinimleriyle karşılaştırmak | Üye 4 | Üye 4 |
| Dosya adını, kaydı ve açıklama notunu kontrol etmek | Üye 5 | Üye 4 |

Her üye en az bir ilişkiyi sözlü olarak açıklar. Çizen kişinin dışındaki bir üye rol ve ok kontrolünü yapar. Bir sonraki etkinlikte görevler döndürülür; kalıcı ekip sorumlulukları 09 numaralı belgede ayrıca düzenlenecek.

## 6. Tamamlanma kontrolü

- [ ] Üç rol ve bir sistem kutusu doğru adlandırıldı.
- [ ] Her rolün sisteme gönderdiği istek ve sistemden aldığı bilgi açıkça ayrıldı.
- [ ] Altı okun yönü doğru; rol izinleri gereksinimlerle tutarlı.
- [ ] Çizim proje içindeki diagrams klasörüne doğru adla kaydedildi ve yeniden açıldı.
- [ ] Öğrenci çalışmasında çizen dışındaki üye kontrolü gerçekten yaptı; adı ve varsa düzeltme notu kaydedildi.

Kutular kullanıcı/öğrenci tarafından uygulanınca işaretlenir. Hazır öğretmen örneği bu adımların yapıldığının kanıtı değildir. 04 belgesindeki kalite ölçümleri ve 08 belgesindeki gözlemler bu çizim nedeniyle değişmez.

## Araç adımları için resmî kaynaklar

27.10.2026 tarihinde kontrol edildi:

- Üyelik gerekmemesi ve çevrimiçi editör: https://www.drawio.com/
- Mevcut dosyayı açma: https://www.drawio.com/docs/manual/open-diagram-file/
- DRAWIO biçimi ve Farklı Kaydet: https://www.drawio.com/docs/manual/editor/save-file-formats/
- Şekil metnini düzenleme: https://www.drawio.com/docs/manual/text/labels-add/
- Enter ve düzenlemeyi bitirme davranışı: https://www.drawio.com/docs/reference/configure-diagram-editor/ — stopEditingOnEnter açıklaması.
