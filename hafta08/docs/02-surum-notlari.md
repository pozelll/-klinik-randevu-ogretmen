# 8. hafta / 2. basamak — Değişiklik notunu yazdık

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Sürüm notu bütün commit mesajlarının kopyası değildir. Alıcıya görünen davranışı ve kullanma koşullarını anlatır. Bu sürümde yardım, seçilen saate ve role göre değişir. İş kuralları aynı kalır. Kullanılabilirlik artışı ve bağımsız kabul henüz ölçülmediği için başarı iddiası olarak yazılmaz.

## Ekranda göster ve uygula

Sürüm notunun Yenilik, Açma ve Açık işler bölümlerini gösterin. ZIP’in tamamen ayıklanması ve index.html ile src klasörünün birlikte bulunması gerektiğini okuyun. Kabul tablosunda teknik kontroller ile bağımsız inceleme ve kullanıcı kabulünü farklı satırlarda gösterin.

- [02-surum-notlari.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/02-surum-notlari.md)
- [Kabul kapıları](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/09-kabul-ve-teslim.md)

## Öğrenciye soru

**Testler geçtiyse kullanıcı kabulünü de tamamlandı yazabilir miyiz?**

Beklenen açıklama: Hayır. Test belirli beklenen davranışları doğrular; gerçek kabul kararı yetkili kişi tarafından ayrıca kaydedilir.

## Grubun yapacağı iş

Kendi paketin için kısa sürüm notu yaz. Açık koşulları ve bilinen sınırları açık bırak.

Kontrol: Alıcı değişikliği ve açılış adımlarını kod okumadan anlayabiliyor mu?

## Hazırlığın gerçek durumu

Ne değişti, nasıl açılır, ne bekliyor? Teknik kontrol ile kullanıcı kabulü ayrıdır.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## 0.3.0-rc.1 — Alıcıya sürüm notu

**Yeni:** Saat alanında seçim adımları açıklanır. Saat seçilince henüz kayıt oluşturulmadığı belirtilir. Doktor rolüne uygun açıklama gösterilir. Hasta, doktor, tarih veya rol değiştiğinde eski seçim metni temizlenir.

**Korunan:** FR-01–FR-06 davranışları, iptal/tamamlama kuralları, tek ortak depo ve saklama biçimi. Veri şeması göçü yoktur.

**Açma:** ZIP'in tamamını yeni bir klasöre çıkarın. index.html ile src/ birlikte kalsın. index.html dosyasını tarayıcıda açın. İnternet ve sunucu gerekmez. Kaydetme durumunu ekranın altından okuyun.

**Bilinen sınırlar:** Tek tarayıcı ve sentetik veri. Gerçek giriş, merkezi veritabanı ve cihazlar arası eşzamanlama yok. Yerel dosya saklaması tarayıcıya bağlı. Kullanılabilirlik, yanıt süresi ve klavye NFR ölçümleri yapılmadı. Bağımsız inceleme ve gerçek kullanıcı kabulü bekliyor.

Bu, inceleme için hazırlanmış ders adayıdır. GitHub etiketi veya yayımlanmış Release oluşturulmadı.
