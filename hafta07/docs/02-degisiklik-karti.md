# 7. hafta / 2. basamak — Değişikliği sınırladık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Değişiklik isteği, hangi sorunu ele aldığımızı ve hangi sınır içinde kalacağımızı anlatmalıdır. Saat seçildiğinde henüz randevu oluşmaz. Yardım, bu ayrımı ekranda açıklar. Bunun kullanıcı hatasını azalttığı henüz ölçülmedi; şu anda yalnız gözlenebilir davranışını tanımlıyoruz.

## Ekranda göster ve uygula

H7-DK-01 kartını açın. Başlangıç, seçili saat ve doktor rolü için üç metin durumunu okuyun. FR-01 uygun saatler ve FR-02 oluşturma bağlantısını gösterin. Kapsam dışındaki hatırlatma, yeni takvim ve kullanıcı araştırması işlerinin bu küçük göreve eklenmediğini belirtin.

- [02-degisiklik-karti.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/hafta07/docs/02-degisiklik-karti.md)
- [FR-01 / FR-02](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/docs/03-gereksinimler.md)

## Öğrenciye soru

**“Kullanımı kolaylaştırdık” cümlesi tek başına kabul koşulu olur mu?**

Beklenen açıklama: Hayır. Gözlenebilir sonuç gerekir: seçimde açıklama değişmeli, onaydan önce veri değişmemelidir.

## Grubun yapacağı iş

Bir değişiklik kartı yaz. Varsayımını ölçülmüş sonuç gibi sunma; en az bir kapsam dışı işi belirt.

Kontrol: Kartta sorun, kapsam, kapsam dışı işler ve kabul koşullarına bağlantı bulunuyor mu?

## Hazırlığın gerçek durumu

H7-DK-01: yardım metni ve durumu. Yeni iş kuralı veya veri alanı yok.

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)

## H7-DK-01 — Değişiklik kartı

| Alan | Karar |
|---|---|
| Kaynak | H3-03 / GitHub Issue #10, öğretmen planlama kararı |
| Ele alınan açıklık | Saat seçmenin onay vermek ve kayıt oluşturmakla karıştırılabilmesi |
| Kapsam | Başlangıç yönlendirmesi, seçili saat açıklaması, doktor rolü açıklaması, bağlam değişiminde metin yenileme |
| Ürün dosyaları | index.html ve src/ui.js |
| İlgili gereksinim | FR-01 uygun saatler, FR-02 oluşturma; BR-01 korunur |
| Kapsam dışı | Yeni takvim, hatırlatma, gerçek kimlik doğrulama, yeni saklama şeması |
| Kabul | H7-B01–B05; beş gözlenebilir senaryo |
| Fayda varsayımı | Seçim/onay ayrımının anlaşılmasına yardımcı olabilir; kullanıcı araştırmasıyla ölçülmedi |
| Karar durumu | Öğretmen örneğinde uygulandı; bağımsız kabul bekliyor |
