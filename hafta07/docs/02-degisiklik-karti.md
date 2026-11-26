# 7. hafta / 2. adım - Değişiklik kartı

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Değişikliğin ele aldığı sorunu, sınırlarını ve kabul koşullarını tanımlamak.

Saat seçimi ile randevunun onaylanarak oluşturulması ayrı işlemlerdir. Örnek değişiklik, uygulamanın bu durumlarını yardım metniyle açıklar. Kullanıcı hatasını azalttığına ilişkin fayda varsayımı, ölçülmüş sonuç olarak sunulmaz.

## Grup çalışması

1. Kendi değişikliğinizin ele aldığı sorunu somut bir davranış üzerinden yazın.
2. Başlangıç durumu, kullanıcı işlemi ve beklenen yeni davranışı tanımlayın.
3. Değişen dosyaları, ilgili gereksinimi ve en az bir kapsam dışı işi belirtin.
4. Kabul koşullarına bağlantı ekleyin. Henüz ölçülmemiş faydayı varsayım olarak işaretleyin.

## Teslim edilecek çıktı

Sorun, kapsam, kapsam dışı işler, ilgili gereksinim, değişen dosyalar ve kabul koşulları bulunan bir değişiklik kartı.

## H7-DK-01 - Tarihli örnek değişiklik kartı

Aşağıdaki kart 22 Kasım 2026 tarihli hazırlık kaydıdır. Karar ve kabul durumu o hazırlık anını gösterir; güncel PR durumu bağlantıdan izlenir.

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

[FR-01 ve FR-02 gereksinimleri](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/docs/03-gereksinimler.md)

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)
