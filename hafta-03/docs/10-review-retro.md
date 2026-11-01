# 3. hafta — Ürün değerlendirmesi ve retrospektif

Tarih: 28.10.2026  
Sürüm: 0.1 — öğretmen uygulaması; değerlendirme taslağı  
Konum: hafta-03/docs/10-review-retro.md

Bu belge öğretmenle yapılan uygulamanın kaydıdır. Gerçek öğrenci toplantısı, paydaş onayı veya bağımsız kod incelemesi yapılmış gibi sunulmaz.

## 1. Review: Ortaya çıkan ürün ne sağladı?

Amaç: Hastanın randevu iptal koşullarını ve onay penceresindeki seçeneklerin sonuçlarını işlemden önce anlamasına yardımcı olmak.

İncelenen çalışma: Ana iptal açıklaması, Tamamlandı sınırı ve ayrıntılı onay metni bulunan B sürümü. Son doğrulanan kod değişikliği commit'i b44550b; test/pano paketi c0bff15. PR: https://github.com/pozelll/-klinik-randevu-ogretmen/pull/11

07/08/09 dosyalarının sonraki yüklemesi kullanıcı tarafından bildirildi; yeni commit kimliği ve uzak dosya içerikleri henüz doğrulanmadı.

| Başlık | Gerçek durum |
|---|---|
| Üründe yapılan değişiklik | Ana yardım ve onay metni güncellendi. |
| Kontrol edilen sonuç | 08-test-kaydi.md içindeki altı kontrol, belirtilen kapsamlarıyla geçti. |
| Sayım kanıtı | R013 oluşturma/vazgeçme/iptal boyunca toplam 9 → 10 → 10 → 10. |
| Ertelenen iş | H3-03 / #10 saat seçimi yardımı uygulanmadı; Todo. |
| Kalan koşullar | Bağımsız inceleme, #7 bağımlılığının çözülmesi, birleştirme ve son teslim kontrolü. |
| Ölçülmeyenler | Kullanılabilirlik, performans ve klavye NFR ölçümleri. |

Paydaş rolünü canlandıran kişi: Henüz belirlenmedi.  
Sınıf demosu ve gerçek paydaş yanıtı: Henüz yapılmadı/kaydedilmedi.  
Demoda sorulacak soru: “Tamam ve İptal seçeneklerinden hangisi randevuyu iptal ediyor; hangisi kaydı değiştirmeden pencereyi kapatıyor?”

Bu sorunun yanıtı şimdiden başarılı kabul edilmez. Sınıf provası gerçek hasta araştırması değildir.

Mevcut kapsam kararı: #8 ve #9 inceleme/teslim beklerken In Progress ve Open kalır. #10, kapsam artışından sonra ertelenmiş olarak korunur; bu değerlendirme onu tekrar plana almaz.

Açık metin tutarlılığı gözlemi: Eski başarı bildirimi “İlgili saat yeniden uygun.” derken yeni açıklama başka iptal edilmemiş kayıt bulunmaması koşulunu belirtir. Bu gözlem 09-pr-inceleme.md içinde kayıtlıdır; henüz düzeltildi veya başarısız test bulundu denmez.

## 2. Retrospektif: Çalışma biçiminde ne öğrendik?

Aşağıdakiler oturumda gözlenen süreçten hazırlanmıştır; öğretmenin kişisel değerlendirmesi veya ekip kararı olarak uydurulmamıştır.

| Başlık | Gözlem |
|---|---|
| İşe yarayan uygulama | Küçük adımlar, ayrı test kaydı ve ekran kanıtı/kullanıcı bildirimi ayrımı sonuçları izlemeyi sağladı. |
| İşlemde yaşanan güçlük | İptal et düğmesiyle onay penceresindeki İptal seçeneğinin anlamı karıştı; R011 denemesinde yanlışlıkla Tamam seçildi. Gerçek sonuç kayıtta korundu. |
| Belgelerde yaşanan güçlük | Yükleme ve PR açılışı tamamlandıktan sonra bazı belgelerde eski “bekliyor” ifadeleri kaldı; birlikte okumada bulunup 07/08 güncellemelerinde düzeltildi. |
| Planlama dersi | H3-01 tahmini 2'den 3'e çıkınca toplam 9 oldu; kapasite 8 iken H3-03 ertelendi. Kalan iki işin toplamı 6. |

## 3. Sonraki uygulama için tek iyileştirme önerisi

Öneri: Her yükleme/PR adımının sonunda kısa bir durum kontrolü yap: “İşlem gerçekleşti mi; ilgili belgede hâlâ bekliyor mu yazıyor?” Güncel bağlantıyı ve doğrulanabilen commit bilgisini aynı anda kaydet.

Karar durumu: Öneri; öğretmenin veya öğrenci ekibinin kabul kararı henüz alınmadı.  
Önerilen sorumlu: Öğretmen uygulamasında Pınar Kızıloğlu; sınıfta her grubun kendi belirlediği belge sorumlusu. Öğrenci isimleri henüz atanmadı.  
Önerilen zaman: Bir sonraki belge yüklemesi/PR durum değişikliğinin hemen ardından.  
Başarı kontrolü: İlgili belgelerde gerçekleşmiş işlem için güncelliğini yitirmiş “henüz yapılmadı” ifadesi kalmaması; doğrulanmamış commit bilgisinin yazılmaması.

## 4. Sınıfta uygulama ve konuşma notu

Üç beş kişilik ve bir dört kişilik grup kendi ürününü gösterir. Her grup bir kişiye demoyu, farklı bir kişiye geri bildirim kaydını yaptırır; ardından herkes bir süreç gözlemi paylaşır. İsimler ve gerçek yanıtlar uygulama sırasında yazılır. Öğretmen örneğindeki sonuçlar öğrenci grubunun sonucu gibi kopyalanmaz.

Öğretmen anlatımı: “Review sırasında ürüne bakıyoruz: Ne değişti, hangi ihtiyacı karşıladı, ne eksik? Retrospektifte çalışma biçimimize bakıyoruz: Nerede zorlandık ve bir sonraki çalışmada hangi tek davranışı değiştireceğiz? Ürünü göstermek, PR'a bağımsız onay verilmesiyle aynı şey değildir.”

## Kaydetme

Dosyayı hafta-03/docs içine kaydedin. Bu belge henüz GitHub'a yüklenmedi. 11-teslim.md, 12-metrikler.md ve 13-cikis-bileti.md gerçek durumla hazırlanacak; üçüncü hafta henüz tamamen kapatılmış değildir.
