# 5. hafta / 2. basamak - Sözleşmeyi netleştirdik

Hazırlık tarihi: 22 Kasım 2026. Öğretmen örneği; öğrenci katkısı veya bağımsız kişi incelemesi değildir.

## Derste ne söyleyeceğim?

Sözleşme, bir bileşenden ne istediğimizi ve nasıl bir sonuç beklediğimizi tanımlar. Randevu Deposu, GitHub deposu değildir; uygulama verisini okuyan ve güncelleyen küçük bir bileşendir. findById ve list bağımsız kopya döndürür.

## Ekranda ne açacağım, ne yapacağım?

repository.js içinde findById, list ve update işlemlerini bulun. H5-S02 testinde dönen kopyanın durumunu değiştirdiğimiz hâlde kayıtlı R001’in Bekliyor kaldığını gösterin. update, yeni randevu oluşturmaz; bulunmayan kimlikte applied:false döner. Oluşturma için add, sıfırlama için reset aynı veri kaynağını kullanır.

- [02-sozlesme.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/hafta05/docs/02-sozlesme.md)
- [src/repository.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h5-moduler-uygulama/src/repository.js)

## Kontrol sorusu

Kopyayı değiştirmek ile update çağırmak arasındaki fark açıklanıyor mu? applied ve persistent birbirine karıştırılıyor mu?

**Öğrenciye soru:** applied:true ve persistent:false birlikte mümkün mü?

**Beklenen açıklama:** Evet. İşlem oturum belleğine uygulanmış olabilir; tarayıcıya kalıcı yazma başarısız olabilir. Yenilemede bu değişiklik korunmayabilir.

## Öğrencinin yapacağı iş

Bir başarılı güncelleme, bir ret ve bir saklama hatası için beklediğin sonuç alanlarını yaz.

## Öğretmen örneğinin gerçek durumu

findById · list · update sınırı kuruldu. applied: oturum değişti / persistent: kalıcı yazıldı.

Görev: [#13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13) · İnceleme paketi: [PR #15](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15).
Bağımsız inceleme ve birleştirme bekliyor. Gerçek isim, öğrenci çalışması veya inceleme sonucu uydurulmadı.
