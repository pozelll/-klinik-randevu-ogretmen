# 06 — Riskler

Ekip: Öğretmen çalışma örneği; öğrenci grubu henüz atanmadı.  
Tarih: 27.10.2026  
Sürüm: 0.1 — Birlikte incelenecek taslak.  
Kapsam: Klinik Randevu başlangıç prototipi ve ilk üç dersin proje çalışması.

## Amaç ve kullanım

Bu dosyada, proje hedefini veya ders çalışmasını ileride olumsuz etkileyebilecek durumları, bunların erken işaretlerini ve alınacak önlemleri kaydederiz. Gerçekleşmiş olayı 08-prototip-gozlemleri.md içinde kanıtıyla tutarız; ele alınacak mevcut sorunu ayrıca bir görev/issue ile izleriz. Henüz açılmamış bir GitHub kaydı için bağlantı üretmeyiz.

RSK-01 gibi kimlikler risk kaydını belirtir. Uygulamadaki R011 gibi randevu numaralarıyla aynı şey değildir.

Olasılık değerleri düşük/orta/yüksek biçimindeki ilk nitel değerlendirmelerdir; ölçülmüş oran veya yüzde değildir. Etki de aynı üç düzeyle ve gerekçesiyle yazılır. Bu taslakta puan hesabı yapılmaz. Sorumlular önerilen ekip görevleridir; 09 numaralı ekip belgesinde gerçek öğrenci adlarıyla eşleştirilecektir.

## Risk listesi

| Kimlik | Risk ve nedeni | Olasılık: düşük/orta/yüksek | Etki | Erken işaret | Önlem | Sorumlu |
|---|---|---|---|---|---|---|
| RSK-01 | İptal onayındaki ifadelerin karıştırılması nedeniyle, işlemden vazgeçmek isteyen kullanıcının randevuyu istemeden iptal etmesi. Karttaki İptal et ile onay kutusundaki İptal farklı sonuçlara karşılık gelir. | Orta — öğretmen denemelerinde karışıklık görüldü; diğer kullanıcılar için sıklık ölçülmedi. | Yüksek — korunmak istenen randevu iptal olabilir ve saati yeniden uygun görünebilir. | Kullanıcının hangi düğmeyi seçmesi gerektiğini sorması; vazgeçme görevinde Tamam seçmesi. | Üçüncü derste görünür iptal açıklamasını ve onay metnini netleştirmek; AC-03 ile ALT-01 akışlarını yeniden kontrol etmek; NFR-01'i dört farklı katılımcıyla ölçmek. | Kullanılabilirlik kontrolünü üstlenen üye — adı atanacak. |
| RSK-02 | Tarayıcıya bağlı yerel saklamanın kullanılamaması veya temizlenmesi nedeniyle çalışma kayıtlarının yenileme/kapatma sonrasında kaybolması; dersin aynı kayıtlarla sürdürülememesi. | Orta — ortam koşullarına bağlı nitel varsayım; veri kaybı deneyi yapılmadı. | Yüksek — gözlem yeniden kurulabilir, ancak ders zamanı ve önceki kayıtlarla karşılaştırma kaybedilebilir. | Kalıcı saklamanın kullanılamadığına ilişkin uyarı; aynı koşullardaki yenileme öncesi ve sonrası referans kayıtların farklı görünmesi. | Aynı dosya, tarayıcı ve tek sekmeyle çalışmak; rol ve seçimleri eşitleyerek referans kayıtları karşılaştırmak; gözlem ve ekran kanıtlarını proje dosyalarında saklamak. Saklama sınırlarını ayrıca denemek gerekirse mevcut öğretmen kayıtları yerine ayrı test ortamı kullanmak. | Çalışma ortamı ve kanıt kaydını üstlenen üye — adı atanacak. |
| RSK-03 | Gereksinim, kabul kriteri ve diyagramın ayrı ayrı güncellenmesi nedeniyle aynı role farklı belgelerde farklı görevler verilmesi; yanlış işin geliştirilmesi veya değerlendirilmesi. | Orta — birden çok belge birlikte tutuluyor; şu anda yeni bir çelişki saptandığı iddia edilmiyor. | Orta — düzeltme ve yeniden inceleme gerekir; kapsam veya test beklentisi karışabilir. | Örneğin bir belgede Resepsiyona iptal/tamamlama görevi eklenirken FR-03 ve FR-05'in değişmemesi; seçili doktor/tarih sınırının bir çizimde unutulması. | FR kimlikleriyle 03, 04 ve iki diyagramı karşılaştırmak; değişiklikte ilgili belgeleri birlikte güncellemek; çizen/yazan dışındaki üyeye inceletmek. | Belge tutarlılığı kontrolünü üstlenen üye — adı atanacak. |

## RSK-01 — Birlikte okuyacağımız ilk kayıt

- **Dayanak:** 08 numaralı belgede G-03-T1 ve G-03-T2 sırasında vazgeçme görevi planlanmışken onay kutusunda Tamam seçildi ve ilgili randevular iptal edildi. G-03-T3'te İptal seçilince R011 Bekliyor kaldı; 09:00 Dolu olarak korundu.
- **Geçmiş olay ile riskin ayrımı:** Önceki karışıklıklar gözlem kaydıdır. Buradaki risk, benzer karışıklığın sonraki kullanımda yeniden yaşanmasıdır. Tamam seçiminin iptali gerçekleştirmesi tek başına yazılımın işlevsel olarak bozuk olduğunu göstermez; ifadelerin anlaşılabilirliği ayrıca değerlendirilir.
- **Bugünkü durum:** Açık — önlem planlandı; üçüncü dersin metin değişiklikleri ve NFR-01 ölçümü henüz yapılmadı.
- **Önemli sınır:** Bu prototip yerel onay penceresini kullanır. Üçüncü ders planı açıklama ve onay metnini iyileştirir; tarayıcının Tamam/İptal düğmelerini özel düğmelerle değiştirme işi bu değişikliğin kapsamında değildir.
- **Risk ne zaman yeniden değerlendirilecek?** Metin iyileştirmesi uygulanıp işlev kontrolleri ve NFR-01 ölçümü yapıldıktan sonra. Tek bir doğru öğretmen denemesi riski kapatmak için yeterli sayılmaz.

## Diğer kayıtların dayanakları ve sınırları

**RSK-02:** Başlangıç paketindeki BILINEN_KISITLAR.md, saklamanın tarayıcı koşullarına bağlı olduğunu ve kalıcı saklama başarısızsa bellekte devam edildiğini açıklar. Önceki öğretmen yenileme denemesinde kontrol edilen randevu durumları ve toplamlar korundu. Bu nedenle veri kaybı yaşandığını yazmıyoruz. Sayfa açılınca rolün Hasta'ya dönmesi tek başına veri kaybı değildir. Gözlem belgesini veya kaynak kodunu kaydetmek, uygulamadaki randevuların otomatik yedeğini almak anlamına gelmez; prototipte veri dışa aktarma işlevi yoktur.

**RSK-03:** Öğretmen kullanım durumu örneğinde Hasta'nın üç, Resepsiyonun dört, Doktorun dört bağlantısı 03 numaralı gereksinimlerle karşılaştırıldı. Bu çalışma öğrencilerin arkadaş incelemesi yerine geçmez. Risk satırındaki örnek çelişkiler olası erken işaretlerdir; kullanıcı dosyalarında gözlenmiş yeni hatalar olarak kaydedilmemiştir.

## Bir riski gözden geçirme — sonraki uygulamada doldurulacak

- İncelenecek risk: RSK-01.
- Önceki değerlendirme: İlk taslakta olasılık Orta, etki Yüksek; nitel öğretmen değerlendirmesi.
- Yeni kanıt: Henüz yok. Metin iyileştirmesi sonrası gerçek kontrol ve ölçüm sonuçları buraya eklenecek.
- Güncel karar: Açık; planlanan önlemler uygulanıp ölçülene kadar ilk değerlendirme korunuyor.
- Bir sonraki kontrol zamanı: Üçüncü dersin iyileştirme ve doğrulama adımları sonrası. NFR ölçümü o aşamada tamamlanmamışsa risk açık tutulur ve ekip yeni kontrol zamanını yazar.
- Kontrol eden kişi ve gerçek tarih: Henüz atanmadı / uygulanmadı.

## Kaydetme ve çalışma durumu

Bu dosya projenin docs/06-riskler.md yoluna kaydedilir. Başlangıçtaki boş risk şablonunun doldurulmuş öğretmen taslağıdır; yeni bir belge türü değildir. Bu adımda dosyanın amacı ve RSK-01 açıklanır. RSK-02, RSK-03 ve gözden geçirme bölümü sonraki adımlarda birlikte incelenecektir. Kullanıcının kendi bilgisayarında kaydettiği ayrıca doğrulanmamıştır.

Gerçek GitHub issue, kod değişikliği, yeni prototip testi, NFR ölçümü veya öğrenci incelemesi bu dosya hazırlanırken yapılmış sayılmaz.
