# 7. hafta / 3. adım - Etki ve risk planı

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Değişikliğin dosyalar, durum geçişleri ve mevcut davranışlar üzerindeki etkisini belirlemek; riskleri kontrol adımlarıyla eşleştirmek.

Duruma bağlı bir açıklama, hasta veya tarih değiştiğinde yenilenmezse eski bilgiyi gösterebilir. Etki analizi, değişen dosyalarla birlikte bu olayları da kapsar. Değişmeyen bileşenlerin birlikte çalışma davranışı regresyon testleriyle yeniden sınanır.

## Grup çalışması

1. Değişecek dosyaları ve her dosyanın sorumluluğunu yazın.
2. En az iki etki ve bir risk tanımlayın. Durumu değiştiren kullanıcı işlemlerini belirtin.
3. Her riski bir test veya gözlenebilir kontrolle eşleştirin.
4. Uygulama, test, belge ve inceleme işlerini planlayın. Tahmini süre ile çalışmadan sonra ölçülen gerçek süreyi ayrı kaydedin.

## Teslim edilecek çıktı

Etki tablosu, risk-kontrol eşleştirmesi, iş sırası ve grup üyelerinin sorumlulukları.

## Tarihli örnek etki ve kontrol

Aşağıdaki tablolar 22 Kasım 2026 tarihli H7 hazırlığına aittir.

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

Örnek plan sırası: kabul koşulları → iki ürün dosyası → yeni senaryolar → regresyon → kanıt ve belge → bağımsız inceleme. Hazırlık kaydında ilk beş iş tamamlanmış, bağımsız inceleme bekliyor olarak belirtilmiştir. Gerçekleşmiş insan emeği bu kayıtta ölçülmemiştir. H6 commit'i kod için geri dönüş kaynağıdır; kullanıcı verisinin yedeği değildir.

[src/ui.js](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/feat/h7-saat-secimi-yardimi/src/ui.js)

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [PR #18 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18)
