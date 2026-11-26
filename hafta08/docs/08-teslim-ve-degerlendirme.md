# 8. hafta / 8. adım - Teslim ve değerlendirme

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Alıcının açacağı paketi, değerlendireceği sürümü ve henüz tamamlanmayan işleri tek teslim kaydında birleştirin.

## Grup çalışması

1. Kendi ZIP dosyanızın adını, boyutunu ve SHA-256 özetini kaydedin.
2. Kaynak commit'i, sürüm notları, test kanıtları ve PR bağlantısını tesliminize ekleyin.
3. [Grup formuna](../sablonlar/grup-kaydi.md) her üyenin gerçek katkısını ve çalışma süresini yazın.
4. Gerçek alıcı değerlendirmesinde erişim, cihaz, tarayıcı, yapılan akış ve sonucu [kabul kaydına](09-kabul-ve-teslim.md) işleyin. Değerlendirme gerçekleşmediyse bekleyen iş olarak belirtin.
5. Test, kişi incelemesi, birleştirme ve kullanıcı kabulü durumlarını ayrı gösterin. Açık bulguları bir sonraki iş listesine aktarın.

## Teslim edilecek çıktı

- Dağıtım paketi ve sürüm kimliği.
- Dosya özetleri ve gerçek test kayıtları.
- Sürüm notu, açılış yönergesi ve geri dönüş planı.
- Grup katkıları, inceleme ve varsa düzeltme kayıtları.
- Alıcı değerlendirmesi veya değerlendirme için bekleyen işler.
- Gerçek bulgudan türetilmiş bir sonraki iyileştirme önerisi.

## Tarihli örnek teslim paketi

22 Kasım 2026 tarihli H8 hazırlığının dosyaları:

- [0.3.0-rc.1 dağıtım ZIP'i](../dagitim/Klinik_Randevu_0.3.0-rc.1.zip): 47.825 bayt; SHA-256 `36822b44675d5df7d1613f9605f907e18fe3656cc74b64e614d19c277bde2dc5`.
- [H8 süreç PDF'i](../dagitim/YAZ325_Hafta_08_Surec_Infografik_Aktif_Linkli.pdf).
- [Kabul ve teslim tablosu](09-kabul-ve-teslim.md).
- [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19): 22 Kasım 2026 tarihinde `main` dalına birleştirilmiştir. Güncel inceleme ve birleştirme ayrıntıları PR kaydındadır.

Hazırlıktaki bağımlılık sırası #7 → #11 → #12 → #15 → #16 → #18 → #19 olarak kaydedilmiştir. Alıcının cihazında açılış ve gerçek kabul kontrolü, o hazırlık kaydında yapılmamış iş olarak belirtilmiştir. Birleştirme kaydı tek başına kullanıcı kabulünü göstermez.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
