# 8. hafta / 8. basamak — Teslim ve açık işleri kaydettik

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Teslim, bir dosyayı göndermekten fazlasıdır: alıcının neyi açacağı, hangi sürümü değerlendireceği ve neyin tamamlanmadığı anlaşılmalıdır. Teknik kontroller tamamlandı; bağımsız kişi incelemesi ve kullanıcı kabulü tamamlanmadı. Bu nedenle çalışma, incelenebilir ders sürüm adayı olarak sunulur.

## Ekranda göster ve uygula

H8 PR’ını, dağıtım klasörünü ve kabul tablosunu açın. ZIP’in SHA-256 özetini kanıt kaydıyla eşleştirin. Öğrenci formunda gerçek katkı, alıcı erişimi ve değerlendirme alanlarını gösterin. Son soruda hangi riskin kapandığını ve hangisinin açık kaldığını tartıştırın.

- [08-teslim-ve-degerlendirme.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/08-teslim-ve-degerlendirme.md)
- [Kabul ve teslim](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/09-kabul-ve-teslim.md)
- [Grup formu](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/sablonlar/grup-kaydi.md)

## Öğrenciye soru

**Sürüm adayı hazır olduğunda tüm Issue’ları kapatmalı mıyız?**

Beklenen açıklama: Hayır. İnceleme ve birleştirme gibi kabul koşulları açıksa görev açık kalır; teknik hazırlık durumu ayrıca yazılır.

## Grubun yapacağı iş

Teslim kaydını gerçek alıcı ve gerçek sürümle doldur. Bir iyileştirme önerisini sonraki iş listesine ekle.

Kontrol: Paket, sürüm, kanıt, sorumlu ve açık koşullar birbirine bağlı mı?

## Hazırlığın gerçek durumu

İncelenebilir sürüm adayı hazır. Nihai kabul, bağımsız inceleme ve merge açık.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## İnceleme paketi

- [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19), hedef `feat/h7-saat-secimi-yardimi`.
- [Dağıtım ZIP'i](../dagitim/Klinik_Randevu_0.3.0-rc.1.zip), 47.825 bayt, SHA-256 `36822b44675d5df7d1613f9605f907e18fe3656cc74b64e614d19c277bde2dc5`.
- [H8 süreç PDF'i](../dagitim/YAZ325_Hafta_08_Surec_Infografik_Aktif_Linkli.pdf).
- [H7–H8 öğretmen anlatım rehberi](../dagitim/YAZ325_Hafta_07_08_Ders_Anlatim_Rehberi.pdf).
- [Kabul ve teslim tablosu](09-kabul-ve-teslim.md).

Bağımlılık: #7 → #11 → #12 → #15 → #16 → #18 → #19. main'e birleştirme yapılmadı. Alıcının cihazında açılış ve kabul kontrolü bu hazırlıkta yapılmadı.

Ders sonu değerlendirme: (1) Hangi risk testle azaltıldı? (2) Hangi varsayım hâlâ ölçülmedi? (3) Bir sonraki işi hangi gerçek bulguya göre seçeceğiz? Yanıtlar grubun gerçek gözleminden üretilir; yapılmamış toplantı tutanağı yazılmaz.
