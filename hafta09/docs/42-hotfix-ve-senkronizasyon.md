# 42 - Hotfix ve senkronizasyon

> 22 Kasım 2026 tarihli teknik hazırlık kaydı: Bu belge Gitflow eğitim deneyini ve klinik 0.3.0-rc.1 başlangıcını anlatır. Dal, hedef ve açık/taslak PR bilgileri birleştirme öncesindeki duruma aittir. [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21) aynı gün main'e birleştirilmiştir; bu işlem bağımsız insan incelemesi veya kabulü yerine geçmez. Güncel 0.3.0-rc.2 sonuçları [kapanış raporunda](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md), açık insan kabul işleri [kabul oturumu ve formlarında](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/50-insan-kabul-oturumu.md) bulunur.

## Kontrollü bulgu

Eski laboratuvardan alınan kasıtlı yanlış girdi: “İptal edilen randevu listeden silinir.” Klinik gereksiniminde iptal edilen kayıt geçmişte kalır ve saat serbestleşir. H9 klinik iş kuralını değiştirmez; yalnız panel metnini düzeltir.

```bash
python hafta09/tools/surum_kontrol.py hafta09/senaryolar/04-release.json
python hafta09/tools/surum_kontrol.py hafta09/senaryolar/04-release.json --anlam
python hafta09/tools/surum_kontrol.py hafta09/senaryolar/05-hotfix.json --anlam
```

Beklenen gerçek sonuçlar: **5/5 PASS → 5/6 FAIL (çıkış 1) → 6/6 PASS**. P01–P05: JSON, alanlar, metin sınırı, sürüm/kanal ve çakışma işareti. A01: bu örnekte kararlaştırılmış iptal açıklamasına tam eşitlik. A01 doğal dili genel olarak anlayan bir doğrulayıcı değildir; bilinen gereksinime bağlı bir regresyon kapısıdır. Geçerli başka bir ifadeyi kullanmak istiyorsanız gereksinim ve testi birlikte inceleyin.

Hotfix `main` üzerinden ayrıldı. `hotfix/0.9.1` commit'i `c9ca0bd6a0b8405707cd104440aff39137f5021c`. Main birleşimi `0bb56efd7b1598632e5347b4277d8ad14a339c73`, develop birleşimi `2c31d9f90d55186b5aed3aa7c672c59c51f9b3f2`.

```bash
git -C h9-deneyim/lab-deposu merge-base --is-ancestor hotfix/0.9.1 main
git -C h9-deneyim/lab-deposu merge-base --is-ancestor hotfix/0.9.1 develop
git -C h9-deneyim/lab-deposu diff --exit-code main develop -- panel/surum.json
git -C h9-deneyim/lab-deposu show main:panel/surum.json
git -C h9-deneyim/lab-deposu show develop:panel/surum.json
```

İlk üç komutun çıkışı 0'dır; başarılı durumda metin basmayabilir. Otomatik rapor çıkış kodlarını kaydeder. Atalık düzeltmenin geçmişte bulunduğunu gösterir; sonraki bir commit düzeltmeyi geri alabileceği için son içerik de kontrol edilir. Panelin iki hedefte eşit ve doğru olduğu doğrulandı.

Yeni açıklamalı etiket `egitim-hafta09-v0.9.1`; önceki 0.9.0 etiketinin hedefi korunur. Geri dönüş eski etiketi taşımak değil, ayrı karar ve doğrulama gerektiren bir işlemdir. Klinik uygulamanın [H8 geri dönüş planı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta08/docs/07-geri-donus.md) ayrı kapsamdır.
