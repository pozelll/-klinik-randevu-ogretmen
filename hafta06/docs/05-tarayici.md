# 6. hafta / 5. basamak - Ekran akışını kontrol ettik

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

Tarayıcı kontrolü, kullanıcının düğme, liste, onay ve toplamlarla izlediği akışı sınar. Onay penceresindeki Tamam iptali uygular; İptal vazgeçirir. Eski H3 kanıtı bu hafta yeniden test edilmiş sayılmaz; burada aynı davranışlar yeni sürümde tekrar çalıştırılır.

## Ekranda ne açacağım, ne yapacağım?

Tarayıcı kanıtında H3-T02 ile H3-T03’ü karşılaştırın. T06 için yeni sentetik başlangıçta seçili doktor/gün toplamı 4 → 5 → 5 → 5 olur; bütün verideki kayıt sayısı 7 → 8’dir. Eski H3 çalışma oturumundaki 9 → 10 sayıları bu yeni başlangıca taşınmaz.

- [tests/browser_smoke.py](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/browser_smoke.py)
- [Tarayıcı sonuçları](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/kanitlar/tarayici-sonuclari.json)
- [05-tarayici.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/hafta06/docs/05-tarayici.md)

## Kontrol sorusu

Test edilen tarayıcı sürümü ve uygulama dosyalarının özetleri kayıtlı mı? Dar ekran kontrolü klavye erişilebilirliği testi gibi anlatılıyor mu?

**Öğrenciye soru:** Kayıt iptal edilince toplam neden azalmıyor?

**Beklenen açıklama:** İptal edilen kayıt silinmiyor. Bekleyen azalıyor, iptal edilen artıyor; toplam kayıt sayısı korunuyor.

## Öğrencinin yapacağı iş

Kendi grubunda vazgeçme ve onaylı iptali yeniden çalıştır. Tarayıcı, tarih, başlangıç verisi ve gerçek sonuçla kaydet.

## Öğretmen örneğinin gerçek durumu

9/9 Chromium senaryosu geçti. Bu sonuç NFR kullanılabilirlik ölçümü değildir.

Görev: [#14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · İnceleme paketi: [PR #16](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.
