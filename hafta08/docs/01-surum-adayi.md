# 8. hafta / 1. basamak — Aday sürümü sabitledik

Öğretmen örneği · 22 Kasım 2026

## Derste anlat

“En son dosya” teslim kimliği değildir; dalın içeriği değişebilir. Tam commit ve dosya özetleri hangi uygulamadan paket ürettiğimizi belirtir. 0.3.0-rc.1 etiketi bu çalışmada seçtiğimiz aday sürüm adıdır. GitHub Release yayımlanmış veya üretime alınmış değildir.

## Ekranda göster ve uygula

Aday tanımındaki sourceCommit ve sourceFiles alanlarını açın. H7 kod commit’ini GitHub’da gösterin. Sonradan eklenen ders belgelerinin uygulama dosyalarını değiştirmediğini özetlerle karşılaştırın. Paket üretim aracı kaynak dosya değişirse neden duruyor, açıklayın.

- [01-surum-adayi.md](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/01-surum-adayi.md)
- [Aday tanımı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/config/surum-adayi.json)

## Öğrenciye soru

**Dosya adını v1-final-son.zip yapmak sürümü doğrular mı?**

Beklenen açıklama: Hayır. Ad tek başına içerik kanıtı değildir. Commit, manifest ve gerçek paket özeti birlikte incelenir.

## Grubun yapacağı iş

Kendi aday sürümünü adlandır. Tam kaynak commit’ini, kapsamı ve dosya listesini kaydet.

Kontrol: Adayın kaynağı hareketli dal adı yerine tam commit ve dosya özetiyle tanımlı mı?

## Hazırlığın gerçek durumu

Sabit kaynak, açık aday kimliği. rc.1 ders adayıdır; yayın onayı değildir.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)

## Kimlik kartı

| Alan | Değer |
|---|---|
| Aday | 0.3.0-rc.1 |
| Uygulama kaynağı | `bd5fa3fb2c35d1c11864eed982fdbc20d539d58a` |
| H8 üretim/test kaynağı | `6eb6088bdd8cdc9b8c3fe5b7ff1b703e2bd87fa2` |
| Başlangıç H6 | `f100249a9ece6cb18ff905fe6a3bee8a6cb6f9f8` |
| Dağıtım dosyası | `Klinik_Randevu_0.3.0-rc.1.zip` |
| Paket boyutu | 47.825 bayt |
| SHA-256 | `36822b44675d5df7d1613f9605f907e18fe3656cc74b64e614d19c277bde2dc5` |

H7'nin son belge commit'i uygulamanın kaynağıyla aynı kavram değildir. Paket tanımı ürün dosyalarının geldiği tam commit'i gösterir; H8 CI kaydı üretim/test araçlarının sürümünü ayrıca taşır. `sourceCommit` alanının yazılması tek başına uzak sunucuyu doğrulamaz: beş uygulama dosyasının CI raporundaki özetleri tanımla karşılaştırıldı. Lisans da sabit kaynak dosya listesine dahildir.
