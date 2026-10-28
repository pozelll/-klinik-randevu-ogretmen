# 3. hafta — Pano ve günlük plan kontrolü

Tarih: 28.10.2026  
Sürüm: 0.2 — test sonuçları ve #9 kontrol kutusu güncellendi  
Konum: hafta-03/docs/07-pano-ve-gunluk.md

## Amaç

İş listesinde ne yapabileceğimizi, Sprint planında neyi seçtiğimizi yazdık. Bu belge ise gerçek görevlerin şimdi hangi aşamada olduğunu, kalan engelleri ve sonraki adımı kaydeder. Gerçek öğrenci toplantısı veya yapılmış bir Daily Scrum tutanağı değildir; öğretmenin günlük plan kontrolü örneğidir.

Pano: https://github.com/users/pozelll/projects/1/views/1  
Depo: https://github.com/pozelll/-klinik-randevu-ogretmen  
Çalışma dalı: feat/h3-iptal-acikligi  
Son doğrulanan commit: b44550b.

## Doğrulanan görevler

| İş | Gerçek görev | Sorumlu | İlk görülen pano durumu | Son doğrulanan pano durumu | Güncel plan | Güncel puan |
|---|---|---|---|---|---|---:|
| H3-01 | [#8](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/8) | pozelll | Todo | In Progress | H3-S1 içinde | 3 |
| H3-02 | [#9](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/9) | pozelll | In Progress | In Progress | H3-S1 içinde | 3 |
| H3-03 | [#10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) | pozelll | Todo | Todo | H3-S1'den ertelendi | 3 |

Üç görev de Open. Tabloda ilk görülen durum kullanıldı. Son #9 ekranının olay geçmişi ayrıca otomasyonun kartı Todo durumuna eklediğini, kullanıcının sonra In Progress yaptığını gösteriyor. Pano durumları ayrı görev ekranlarından doğrulandı; bütün panonun yeni toplam sayıları bu aşamada yeniden sayılmadı.

H3-04, H3-05 ve H3-06 ürün iş listesinde geleceğe yönelik aday olarak duruyor. Gerçek Issue ve pano kartları henüz yok; varmış gibi URL veya Status yazılmadı.

## Alanların anlamı

- **Assignees:** Gerçek sorumlu kişi. Atama, işin tamamlandığı anlamına gelmez.
- **Status:** Panodaki ilerleme; burada Todo, In Progress ve Done seçenekleri kullanılıyor.
- **Open / Closed:** GitHub görevinin açık veya kapalı olması; pano Status alanından ayrıdır.
- **H3-S1:** Belgelerdeki çalışma etiketi. GitHub panosunda ayrı Sprint alanı oluşturulduğu henüz doğrulanmadı; tablodaki güncel plan sütunu belge kaydıdır.

Bu öğretim uygulamasında aynı anda en fazla iki H3 kartını In Progress tutma çalışma kuralı kullanılıyor. Son doğrulanan H3 durumları bu kuralla uyumlu. Önceki haftaların görevleri aynı panoda bulunduğundan bu sınır panonun tüm kart sayısına uygulanmaz.

## Bugünkü plan kontrolü

**Gerçekleşenler:** Ana iptal açıklaması ve onay metni uygulandı; ardından Tamamlandı sınırı açıkça eklendi. Kod ve ilgili plan belgeleri GitHub'a kaydedildi. Yeni görevler uygulamadan sonra oluşturuldu; tarihleri geçmişe çekilmedi.

**Gözlenen kontroller:** R011'de Tamam ile iptal sonucu; R012'de İptal ile vazgeçme sonucu; R003 için Tamamlandı, iptal düğmesi yok ve 11:00 Kapalı görünümü. Bu kayıtlar 08-test-kaydi.md v1.0 içinde sürümleriyle kaydedildi. T05 hasta görünümü ve T06 R013 oluşturma–vazgeçme–iptal döngüsü de tamamlandı. Sayımlar 1/2/6/9 → 2/2/6/10 → 2/2/6/10 → 1/2/7/10; kanıt türleri test belgesinde ayrıldı.

**Açık işler / engeller:** Altı kontrol, test belgesinde belirtilen kapsamlarıyla geçti. #9 kartında toplam kayıt sayısı kutusu işaretlendiği ekranla doğrulandı. İnceleme ve son teslim kutuları boş; Open ve In Progress korunuyor. NFR ölçümleri yapılmadı. Yazardan/ortak yazardan farklı gerçek inceleyen kişi henüz belirlenmedi. H3 PR ve son teslim kontrolleri bekliyor.

**Sonraki küçük adım:** Güncel 03/07/08 belgeleri ile üç sayım kanıtını çalışma dalına kaydetmek ve H3 PR/inceleme hazırlığı yapmak.

**Gereken destek:** Bağımsız inceleme için katkıyı yazmayan gerçek bir kişi. Öğretmenin kendi kontrolü bu inceleme yerine sayılmaz.

**Karar:** #8 ve #9 In Progress ve Open kalır; #10 Todo ve Open olarak bekler. H3-03 sırf kartı açıldı diye güncel plana geri alınmaz. İlk plan ve erteleme gerekçesi 05/06 belgelerinde korunur.

## Sınıfta nasıl kullanılacak?

Üç beş kişilik ve bir dört kişilik grup kendi görevlerine bakarak hedefe yaklaşma durumunu, engeli ve sonraki küçük adımı kısaca konuşur. Gerçek sorumlular ve kararlar kaydedilir. Bir kartın yerini değiştirmek tek başına ilerleme kanıtı değildir; dosya, commit, test ve inceleme kayıtlarıyla birlikte değerlendirilir.

Bu öğretmen kaydındaki pozelll hesabı veya sonuçlar öğrenci gruplarının gerçek katkıları gibi kopyalanmaz.

## Kaydetme

Bu dosyayı hafta-03/docs içine 07-pano-ve-gunluk.md adıyla kaydedin. Gerçek görev bağlantıları eklenen güncel 03-product-backlog.md dosyasını da aynı klasördeki eski kopyasının yerine koyun. Bu dosyaların GitHub'a yüklenmesi henüz gerçekleşmedi.
