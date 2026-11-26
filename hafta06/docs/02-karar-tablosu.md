# 6. hafta / 2. basamak - Karar tablosu

## Amaç

İşlem koşulları ile beklenen sonuçları aynı tabloda tanımlayın. Aşağıdaki yedi satır örnek iptal kuralını temsil eder; bütün olası koşul birleşimlerini kapsadığı varsayılmaz.

## Örnek karar tablosu

| Satır | Kayıt | Rol | Sahiplik | Durum | Beklenen | İstek sırasında update / kalıcı yazma |
|---|---|---|---|---|---|---|
| DK-K01 | Yok (R999) | Hasta | Uygulanmaz | Uygulanmaz | NOT_FOUND | 0 / 0 |
| DK-K02 | R001 | Resepsiyon | Ece'nin | Bekliyor | ROLE | 0 / 0 |
| DK-K03 | R001 | Doktor | Ece'nin | Bekliyor | ROLE | 0 / 0 |
| DK-K04 | R001 | Hasta: Kaan | Başkasının | Bekliyor | OWNER | 0 / 0 |
| DK-K05 | R001 | Hasta: Ece | Kendi | Tamamlandı | STATUS | 0 / 0 |
| DK-K06 | R001 | Hasta: Ece | Kendi | İptal edildi | STATUS | 0 / 0 |
| DK-K07 | R001 | Hasta: Ece | Kendi | Bekliyor | OK; İptal edildi | 1 / 1 |

Her satır yeni `seedData`, yeni depo ve yeni servis ile çalışır. Başlangıçtaki hazırlık yazımları istek sırasındaki yazma sayısına dahil edilmez. K07'de depolama kullanılabilir olduğu için 1 kalıcı yazma vardır; saklama hatası ayrı testtir.

## Çalışma

1. [Karar testlerindeki](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/test/h6-karar-tablosu/tests/h6-decision.test.cjs) her test kimliğini ilgili tablo satırıyla eşleştirin.
2. Kendi grubunuzun kuralı için koşulları ve beklenen veri değişimini yazın. Her senaryo bağımsız başlangıç verisi kullanmalıdır.
3. Her satırın gerçek sonucunu ayrı kaydedin. Tek ekran görüntüsünü bütün satırların yürütüm kaydı olarak kullanmayın.

## Teslim edilecek çıktı

Karar tablosu, her satıra ait test kimliği, başlangıç durumu, gerçek sonuç ve ilgili kanıt bağlantısı.

Örnek tablo 22 Kasım 2026 tarihli H6 çalışmasına aittir. [Görev #14](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/14) · [PR #16 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/16)
