# 5. hafta / 4. basamak - İş kurallarını ayırdık

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

İş kuralı, işlemin hangi koşullarda yapılabileceğini belirler. Düğmenin ekranda gizlenmesi tek başına yeterli değildir. cancelEligibility kaydı, rolü, sahipliği ve Bekliyor durumunu denetler. cancel, onaydan sonra bu denetimi güncel kayıt üzerinde yeniden yapar.

## Ekranda ne açacağım, ne yapacağım?

rules.js içindeki cancelEligibility ve cancel işlemlerini yan yana açın. NOT_FOUND, ROLE, OWNER ve STATUS ret kodlarını bulun. Uygunluk sorgusuyla işlem arasında durum değişirse H5-S08’in iptali nasıl reddettiğini gösterin. occupiedAt, BR-01’e göre başka iptal edilmemiş kayıt bulunup bulunmadığını hesaplar.

- [src/rules.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/rules.js)
- [04-is-kurallari.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/04-is-kurallari.md)

## Kontrol sorusu

rules.js DOM veya localStorage biliyor mu? Ret halinde repository.update çağrısı var mı? İptal, nextId veya toplam kayıt sayısını artırıyor mu?

**Öğrenciye soru:** İlk uygunluk kontrolünden sonra neden yeniden kontrol ediyoruz?

**Beklenen açıklama:** İşlem gerçekleşirken koşulların hâlâ geçerli olmasını sağlamak için. Bu yeniden kontrol, çoklu cihaz eşzamanlama garantisi değildir.

## Öğrencinin yapacağı iş

Kendi uygulamanda bir kuralı ekran kodundan ayır ve reddedilen isteğin veriyi değiştirmediğini göster.

## Öğretmen örneğinin gerçek durumu

Ret → yazma yok; uygun istek → güncelleme. BR-01 saat sonucu da iş kurallarından gelir.

Görev: [#13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13) · İnceleme paketi: [PR #15](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.
