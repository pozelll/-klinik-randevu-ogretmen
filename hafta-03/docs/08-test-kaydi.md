# 3. hafta — Gerçek test kaydı

Tarih: 28.10.2026; denemelerin ayrı saatleri kaydedilmedi.  
Sürüm: 1.1 — test sonuçları değişmeden PR/yükleme durumu güncellendi.  
Konum: hafta-03/docs/08-test-kaydi.md  
Test eden: Pınar Kızıloğlu — yönlendirilmiş öğretmen uygulaması.  
Ortam: Windows, Google Chrome; sürüm numaraları kaydedilmedi.  
Veriler: Mevcut örnek randevular korundu; bu kayıt için sıfırlama yapılmadı.

## Sürümleri ayırma

- A: Ana açıklama ve yeni onay metni bulunan yerel sürüm; daha sonra f857deb mesajıyla GitHub'a yüklenen çalışma. R011 iptal ve R012 vazgeçme denemeleri bu aşamada yapıldı.
- B: Ana açıklamaya Tamamlandı cümlesi eklenmiş yerel sürüm; daha sonra b44550b mesajıyla GitHub'a yüklenen çalışma. T01/T04 görünüm kontrolü bu aşamada yapıldı. JavaScript bloğunun A ile aynı olduğu dosya karşılaştırmasıyla kontrol edildi.
- GitHub commit bilgileri ekranlarda doğrulandı; uzak dosya byte içeriği indirilip yerel dosyayla ayrıca karşılaştırılmadı. Testler kullanıcı bilgisayarındaki yerel uygulamada yapıldı.

Hazırlanan B çalışma kopyasının SHA256 değeri: `a8efb6ed40b5fb10cd09aded207e13f6a92ea2b1263a3fafcf2a1585518721f5`.

## Altı kontrolün durumu

| Test | Amaç ve başlangıç | Gerçek işlem | Beklenen | Gözlenen | Durum / kanıt |
|---|---|---|---|---|---|
| T01 | B sürümü, Hasta/Ece/Deniz/12.11.2030; ana açıklama. | Kullanıcı yeni dosyayı açtı, iki ekran gönderdi; metin incelendi. | Bekliyor koşulu, Tamamlandı yasağı, kaydın kalması ve koşullu saat açılması görünür. | Dört açıklama ana ekranda okunuyor. | Geçti — ekran incelemesi. Kullanılabilirlik ölçümü değil. |
| T02 | A sürümü; R012 / 09:00 Bekliyor, saat Dolu. | Kullanıcı karttaki İptal et ardından penceredeki İptal düğmesine bastığını bildirdi. | Vazgeçme sonrası R012 Bekliyor ve 09:00 Dolu kalır. | Son görüntüde pencere kapalı; R012 Bekliyor, 09:00 Dolu. | Geçti — kayıt/saat kontrolü; kullanıcı bildirimi + son ekran. Toplam sayısı ayrıca ölçülmedi. |
| T03 | A sürümü; R011 / 09:00 Bekliyor. | Kullanıcı yanlışlıkla penceredeki Tamam'a bastığını bildirdi. | Tamam seçilince kayıt İptal edildi olarak listede kalır; saat Uygun olur. | R011 İptal edildi olarak listede kaldı; 09:00 Uygun oldu; bildirim iptali gösterdi. | Geçti — onaylı iptalin görünen sonucu. Planlanan vazgeçme bu denemede uygulanmadı. Toplam sayısı ölçülmedi. |
| T04 | B sürümü; Hasta/Ece/Deniz/12.11.2030; R003 / 11:00 Tamamlandı. | Yeni cümle, R003 işlem alanı ve 11:00 saati görüntülerden incelendi. | R003 için İptal et düğmesi yok; 11:00 Kapalı. | R003 Tamamlandı, iptal düğmesi yok; 11:00 Kapalı. | Geçti — H3-AC05 görünüm kontrolü. Doğrudan işlev çağrısı/güvenlik testi değil. |
| T05 | B sürümü; Hasta/Kaan/Deniz/12.11.2030. | Kullanıcı Kaan seçip üç beklenen sonucun doğru olduğunu bildirdi; ekran gönderdi. | Kaan'ın R002 ve R004 kayıtları görünmeli; Ece'nin R012 kaydı görünmemeli. 09:00 Dolu kalmalı. | Listede Kaan R002 / 10:00 Tamamlandı ve R004 / 13:00 İptal edildi var; Ece R012 yok. 09:00 Dolu. | Geçti — kullanıcı bildirimi ve ekran. Arayüz süzme kontrolü; gerçek kimlik doğrulaması testi değil. |
| T06 | B sürümü; Ece/Deniz/12.11.2030; ayrı 09:30 deneme kaydı. | R013 oluşturuldu, önce vazgeçildi, sonra aynı kaydın iptali onaylandı. | Oluşturmada Bekliyor/Dolu; vazgeçmede korunma; iptalde kayıt listede İptal edildi ve saat Uygun. | R013 oluşturma ekranla; Bekliyor/09:30 Dolu vazgeçme sonrası kullanıcı bildirimiyle; R013 İptal edildi/listede ve 09:30 Uygun son kullanıcı bildirimiyle doğrulandı. Sayım 9 → 10 → 10 → 10. | Geçti — ekranlar ve kullanıcı bildirimleri; aşağıdaki sayım tablosuna bakınız. |

T02'de kullanılan yeni onay metni daha önce R011 penceresinde görüldü. R012 penceresinin tam metni ayrıca ekran görüntüsüyle kaydedilmedi; T02'nin Geçti kararı kayıt/saat korunmasıyla sınırlıdır.

## B sürümünde ek vazgeçme ve kayıt sayısı kontrolü

R013 / 09:30 üzerinde oluşturma, vazgeçme ve onaylı iptal sırasıyla uygulandı. R012 üzerinde yeni iptal yapılmadı.

| Aşama | Bekleyen | Tamamlanan | İptal edilen | Toplam | Kanıt |
|---|---:|---:|---:|---:|---|
| Yeni kayıt öncesi | 1 | 2 | 6 | 9 | Resepsiyon B3 ekran görüntüsü. |
| R013 oluşturma sonrası | 2 | 2 | 6 | 10 | R013 Bekliyor görüntüsü ve ayrı B3 sayım görüntüsü. |
| R013'te vazgeçme sonrası | 2 | 2 | 6 | 10 | Açık doğrulama sorusuna kullanıcının evet yanıtı. |
| R013 iptali onaylandıktan sonra | 1 | 2 | 7 | 10 | B3 ekran görüntüsü. |

**Vazgeçme:** Kullanıcı R013 Bekliyor, 09:30 Dolu ve toplamlar 2/2/6/10 kaldığını açık soruya evet diyerek doğruladı. Bu aşamanın yeni ekran görüntüsü yok. İlk kopyalanmış yönerge tek başına sonuç kabul edilmedi. R013 penceresinin kimlik/tarih/saat metni bu yanıttan ayrıca doğrulanmış sayılmadı; yeni onay metni önceki R011 görüntüsünde görülmüştü.

**Onaylı iptal:** B3 görüntüsünde 1/2/7/10 görüldü. R013 satırı ve 09:30 kutusu görüntüde olmadığı için ayrıca soruldu. Kullanıcı “ikisi de doğru” diyerek R013'ün İptal edildi olarak listede kaldığını ve 09:30'ın Uygun olduğunu doğruladı.

**Sonuç:** R013 üzerindeki vazgeçme ve onaylı iptal toplam kaydı değiştirmedi. Yeni kayıt oluşturma ise toplamı bir artırdı. H3-AC04'ün bu sayı koşulu geçti; #9 kartındaki ilgili kutu artık kullanıcı tarafından işaretlenebilir. Sonraki kullanıcı ekranında #9 kartındaki bu kutunun işaretlendiği doğrulandı; inceleme ve teslim kutuları boş, kart Open ve In Progress.

## Kanıt dosyaları ve kapsam

Sunum hazırlık kanıtlarında saklanan sayım görüntüleri:

- [h3-t06-baslangic-toplamlar-20261028.png](../kanitlar/h3-t06-baslangic-toplamlar-20261028.png) — 1/2/6/9.
- [h3-t06-olusturma-toplamlar-20261028.png](../kanitlar/h3-t06-olusturma-toplamlar-20261028.png) — 2/2/6/10.
- [h3-t06-iptal-toplamlar-20261028.png](../kanitlar/h3-t06-iptal-toplamlar-20261028.png) — 1/2/7/10.

Diğer sonuçlar kullanıcının bu oturumdaki mesajları ve incelenen ekranlarla kaydedildi. Kişisel yerel dosya yolu içeren ekranlar belgeye gömülmedi. Ayrıntılı sıra sunum hazırlık notlarında korunuyor. Belgeye ekranla doğrulanmayan bir sonuç ekran kanıtı diye yazılmadı.

## Açık kalanlar

- Altı işlev/görünüm kontrolü tabloda belirtilen kapsamlarıyla geçti. Bu, bağımsız inceleme veya bütün kalite ölçümleri tamamlandı anlamına gelmez.
- Kullanılabilirlik, performans ve klavye ölçümleri yapılmadı. Öğretmenle yönlendirilmiş denemeler bağımsız kullanıcı ölçümü yerine sayılmaz.
- Yanlış Tamam seçimi geçmiş kayıtta korunuyor. R011 iptali başarılı vazgeçme gibi sunulmuyor.
- Son doğrulanan durum: R012 / 09:00 Bekliyor; R013 / 09:30 İptal edildi, 09:30 Uygun. Son sayım 1/2/7/10.
- H3 PR #11 açıldı. Yazardan/ortak yazardan farklı kişinin incelemesi ve son teslim bekliyor. #8 ve #9 bu test kaydıyla Done/Closed yapılmaz.
- Main'e birleştirme ve birleştirme sonrası kısa kontrol henüz yapılmadı.

## Kaydetme ve sonraki adım

Bu güncel dosyayı hafta-03/docs içindeki önceki 08-test-kaydi.md dosyasının yerine kaydedin. GitHub #9 kartındaki toplam kayıt sayısı kutusu işaretlendi. İnceleme ve son teslim kutuları boş kalıyor. Önceki test kaydı ve üç sayım kanıtı c0bff15 ile çalışma dalına yüklendi; PR #11 açık. Bu v1.1 idari güncellemesi henüz GitHub'a yüklenmedi. Sonraki aşama belge düzeltmelerini kaydetmek ve bağımsız inceleme/teslim adımlarını tamamlamaktır.
