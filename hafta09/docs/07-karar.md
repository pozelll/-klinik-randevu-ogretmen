# 9. hafta / 7. adım - Kaliteyle sürüm kararı

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Kendi sürümünüz için kalite kararını mevcut kanıtlara dayandırın. Eksik ölçümü, açık işi ve kararın sınırını görünür kılın.

## Grup çalışması

1. [Tarihsel rc.1 kalite kararını](44-surum-kalite-karari.md) ve [plan–gerçekleşen tablosunu](45-plan-gerceklesen.md) inceleyin. Bunların hangi hazırlık anını anlattığını kaydedin.
2. [Güncel rc.2 kapanış kaydıyla](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md) karşılaştırın. Sonradan eklenen klavye ve otomatik performans kanıtlarını, hâlâ tamamlanmamış insan kabulünden ayırın.
3. Kendi adayınız için işlevsel test, paket bütünlüğü, NFR, bağımsız inceleme ve alıcı kabulünü ayrı satırlara yazın. Her satıra aynı adaya ait kaynak commit'i ve kanıt bağlantısını ekleyin.
4. Eksik satırlar için yapılacak işi, gerçekten atanmış sorumluyu ve tamamlanma ölçütünü belirleyin. Ölçülmemiş sonuç veya atanmamış kişi için başarı/isim üretmeyin.
5. Yayın kararınızı gerekçelendirin. Tahmini emek, gerçek insan emeği, otomasyon süresi ve takvim süresini ayrı alanlarda kaydedin.

## Teslim edilecek çıktı

Kalite kapıları tablosu, her kapıya bağlı kanıt, gerekçeli yayın kararı ve sorumlusu/ölçütü belirtilmiş açık iş listesi.

## Çıktı kontrolü

- Karar verilen adayın tam kaynak kimliği bellidir.
- Kanıtın yöntemi ve kapsamı açıktır; farklı adayın sonucu doğrudan aktarılmamıştır.
- Eksik kapılar ve sonraki işler kayıtlıdır.

Klinik örnekte rc.2 için teknik klavye ve otomatik performans sonuçları vardır. NFR-01 insan kullanılabilirliği, NFR-02'nin özgün ekran kaydı yöntemi, bağımsız insan incelemesi ve alıcı kabulü [50 numaralı protokolde](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/50-insan-kabul-oturumu.md) tamamlanacak işlerdir. Bu kayıtlar tamamlanmadığı için nihai klinik yayın kararı **BEKLET** olarak kalır.

[Önceki adım](06-kanit.md) · [Sonraki adım: Devir](08-devir.md)
