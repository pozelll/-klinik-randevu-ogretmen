# 5. hafta / 5. adım - Arayüz bağlantısı

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Kullanıcı seçimlerini ve onayını iş kuralları bileşenine bağlamak; işlem ve saklama sonuçlarını arayüzde göstermek.

Arayüz kullanıcı seçimini alır, onay ister ve sonucu gösterir. Kullanıcı vazgeçtiğinde iptal isteği gönderilmez. Onay verdiğinde işlem sonucu iş kuralları bileşeninden alınır. Saat uygunluğu mesajı BR-01'in sonucuna dayanır.

## Uygulamayı çalıştırma

1. Çalışacağınız dalın tamamını indirin ve arşivi ayıklayın.
2. `index.html` dosyasını `src/` klasörüyle aynı proje dizininde tutun.
3. `index.html` dosyasını tarayıcıda açın.

Uygulama dört yerel JavaScript dosyasını `demo-data`, `repository`, `rules`, `ui` sırasında yükler. Dosyaları paylaşırken proje klasörünü birlikte aktarın.

## Grup çalışması

Kendi uygulamanızda iptal işlemini iki ayrı senaryoyla çalıştırın:

- Onay penceresinde **İptal** seçeneğiyle vazgeçme.
- Onay penceresinde **Tamam** seçeneğiyle iptali onaylama.

Her senaryonun başlangıç kaydını, gerçek sonucunu, kullanılan sürümü ve tarihini ayrı kaydedin. Önceki haftanın kanıtı yerine bu sürümdeki çalıştırmanızın sonucunu ekleyin. Arayüzdeki saklama bildiriminin veri erişimi bileşeninden dönen sonuçla uyumlu olmasını sağlayın.

## Örnek uygulama kaydı

22 Kasım 2026 tarihli H5 çalışmasında arayüz, iş kuralları ve veri erişimi aynı uygulama akışında bağlanmıştır. Örnek uygulama `index.html` ile `src/` klasörü birlikte kullanılarak çalışır.

## Kaynaklar

- [index.html](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/index.html)
- [src/ui.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/ui.js)
- [H5 dalındaki arayüz yönergesi](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/05-arayuz.md)
- [Görev #13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13)
- [PR #15 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15)
