# 7. hafta / 5. basamak — Yardımı uyguladık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Yardım metni, uygulamanın mevcut durumunu anlatmalıdır. Metni ayrı bir değişkende tutup eskimesine izin vermek yerine saatler yeniden çizilirken güncelliyoruz. aria-describedby yardım ile ilgili alanı bağlar; aria-live değişen açıklama için bir ipucu verir. Bunlar tek başına erişilebilirlik onayı değildir.

## Ekranda göster ve uygula

Uygulamayı ayıklanmış klasörden açın. 09:30’u seçin; “henüz randevu oluşturulmadı” metnini gösterin. Onaydan önce tarih değiştirin ve seçimin temizlendiğini izleyin. Sonra yeniden saat seçip onaylayın. Doktor rolüne geçerek rol açıklamasını gösterin.

- [05-uygulama.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/hafta07/docs/05-uygulama.md)
- [src/ui.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/src/ui.js)
- [index.html](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/index.html)

## Öğrenciye soru

**Aynı açıklamayı her role göstermek neden yanlış olabilir?**

Beklenen açıklama: Doktor rolü kayıt oluşturamaz. Yardım, izin verilen eylemle uyumlu olmalı ve yapılamayan bir işlem önermemelidir.

## Grubun yapacağı iş

Kendi değişikliğini uygula. En az bir durum geçişini göster ve ilgili commit’i kaydet.

Kontrol: Yardım görünümü gerçek seçimle tutarlı mı? Seçim ile kayıt oluşturma ayrı eylemler mi?

## Hazırlığın gerçek durumu

Seçim ve onay adımı ayrılıyor. Saat seçmek tek başına kayıt oluşturmuyor.

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)

## Uygulama kaydı

[Kod farkı](https://github.com/pozelll/-klinik-randevu-ogretmen/commit/bd5fa3fb2c35d1c11864eed982fdbc20d539d58a). Yardımın tek güncelleme noktası renderSlots'tur. Başlangıç verisi 7 kayıttır; yeniden denemeden önce yalnız sentetik örnek veriyi sıfırlayın veya yeni yalıtılmış tarayıcı oturumu kullanın. Öğrencinin mevcut çalışmasını habersiz sıfırlamayın.

Oluşturma, iptal ve tamamlama iş kuralları src/rules.js üzerinden çalışmaya devam eder. Saat yardımı kayıt oluşturmaz. aria özelliklerinin bulunması tek başına klavye/ekran okuyucu uygunluk belgesi değildir.
