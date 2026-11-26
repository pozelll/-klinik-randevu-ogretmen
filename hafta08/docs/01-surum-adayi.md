# 8. hafta / 1. adım - Aday sürüm kimliği

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Teslim paketinin hangi kaynaklardan üretileceğini açıkça belirleyin. Dalın içeriği zamanla değişebileceği için tam commit ve dosya özetleri, adayın kaynak kimliğini birlikte tanımlar.

## Grup çalışması

1. Kendi aday sürümünüzü adlandırın ve kapsamını yazın.
2. Tam kaynak commit'ini ve pakete girecek dosyaları kaydedin.
3. [Örnek aday tanımındaki](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/config/surum-adayi.json) `sourceCommit` ve `sourceFiles` alanlarını inceleyin. Kendi dosya listenizi sürüm kaydınızla eşleştirin.
4. Kaynak dosyaların özetlerini üretin ve aday tanımına bağlayın. Dosya değişirse yeni sürümü inceleyerek tanımı güncelleyin.

## Teslim edilecek çıktı

Aday adı, kapsam, tam kaynak commit'i, dosya listesi ve dosya özetlerini içeren sürüm kaydı. Paketin adı, içerik doğrulamasının yerine geçmez.

## 22 Kasım 2026 tarihli örnek kimlik kartı

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

`0.3.0-rc.1`, bu hazırlıkta kullanılan ders adayı adıdır. Hazırlık kaydında GitHub Release veya üretim yayını bulunmaz.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
