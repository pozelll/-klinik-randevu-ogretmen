# 7. hafta / 3. basamak — Etkiyi ve riski gördük

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

Küçük bir metin değişikliği de duruma bağlıysa hata üretebilir. Hasta veya tarih değiştiğinde eski saat yardımda kalırsa ekran yanıltır. Bu yüzden etki analizi yalnız dosya sayısı değildir; hangi olayın hangi durumu yenilediğini de inceler. Tahmin ile gerçek emek ayrı kaydedilir.

## Ekranda göster ve uygula

Etki tablosunu açın: index.html yardım alanını, ui.js güncel metni üretir. rules.js, repository.js ve demo-data.js değişmez. Hasta, doktor, tarih ve rol değişimlerini risk tablosunda bulun. Planlanan işleri uygulama, tarayıcı kontrolü, belge ve inceleme olarak gösterin.

- [03-etki-ve-plan.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/hafta07/docs/03-etki-ve-plan.md)
- [src/ui.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/src/ui.js)

## Öğrenciye soru

**Kurallar değişmediyse eski testleri neden yeniden çalıştırıyoruz?**

Beklenen açıklama: Arayüz yanlış çağrı yapabilir veya eski akışı bozabilir. Regresyon kontrolü önceki davranışın korunmasına kanıt sağlar.

## Grubun yapacağı iş

En az iki etki ve bir risk yaz. Her riski bir kontrolle eşleştir; gerçek süreyi çalıştıktan sonra kaydet.

Kontrol: Öğrenci değişen dosyalarla yeniden kontrol edilen fakat değişmeyen dosyaları ayırabiliyor mu?

## Hazırlığın gerçek durumu

Ürün değişikliği iki dosyada. Kurallar, depo ve şema korunuyor.

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)

## Etki ve kontrol

| Varlık | Değişiklik / kontrol |
|---|---|
| index.html | slot-help alanı, aria-describedby bağlantıları, 7–8 hafta ve aday sürüm etiketi |
| src/ui.js | renderSlots içinde role ve selectedTime'a göre yardım üretimi |
| src/rules.js, repository.js, demo-data.js | Bayt düzeyinde H6 ile aynı; 30 Node testi tekrar çalıştı |
| tests/browser_smoke.py | 5 yeni senaryo ve H8 paket kökü için --app-dir |
| CI | H7/H8 dallarını ve 14 tarayıcı senaryosunu kapsar |

| Risk | Kontrol |
|---|---|
| Seçili saat metninin eskimesi | H7-B03 hasta/doktor/tarih değişimleri |
| Yanlış role işlem önerilmesi | H7-B04 doktor ve resepsiyon |
| Onaydan önce kayıt oluşması | H7-B02 önce/sonra veri karşılaştırması |
| Dar ekranda taşma | H7-B05, 390 × 844 px |

Plan sırası: kabul → iki ürün dosyası → yeni senaryolar → regresyon → kanıt/belge → bağımsız inceleme. İlk beş iş hazırlıkta tamamlandı; bağımsız inceleme bekliyor. Kişi ataması veya gerçekleşmiş emek uydurulmadı. Geri dönüş kaynağı H6 commit'idir; veri geri yüklemesi değildir.
