# YAZ325 - 5. hafta: Mimariyi Koda Aktarma

Bu haftanın öğrenci çalışma yönergeleri, 4. haftada belirlenen mimariyi uygulama koduna taşımayı kapsar. Arayüz, iş kuralları ve veri erişimi ayrı sorumluluklar olarak düzenlenir; kritik davranışlar testlerle kaydedilir.

Örnek çalışmanın dalı: `feat/h5-moduler-uygulama` · [PR #15](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/15) · [Görev #13](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/13)

Bu sayfalardaki örnek test sonuçları **22 Kasım 2026 tarihli kayıtlara** aittir. Her grup kendi sürümünü çalıştırır ve kendi sonuçlarını kaydeder. Yönergelerin güncelleme tarihi: 26 Kasım 2026.

## Çalışma adımları

| Adım | Çalışma yönergesi | Grubun üreteceği çıktı |
|---|---|---|
| 1 | [Başlangıç sürümü ve çalışma dalı](docs/01-baslangic.md) | Başlangıç commit'i, dal ve görev sorumlusu. |
| 2 | [Bileşen sözleşmesi](docs/02-sozlesme.md) | Okuma, güncelleme ve saklama sonuçlarının tanımı. |
| 3 | [Veri erişimi](docs/03-veri-erisimi.md) | Ortak veri kaynağı ve saklama sonucunu bildiren bileşen. |
| 4 | [İş kuralları](docs/04-is-kurallari.md) | Arayüzden ayrılan kural ve ret senaryosunun sonucu. |
| 5 | [Arayüz bağlantısı](docs/05-arayuz.md) | Çalışan uygulama; vazgeçme ve onay kayıtları. |
| 6 | [İlk davranış testleri](docs/06-kontrol.md) | Test komutu, uygulama sürümü ve gerçek sonuçlar. |
| 7 | [Commit ve PR kaydı](docs/07-commit-pr.md) | Commit, PR ve gerçekleştirilen incelemenin kaydı. |
| 8 | [Teslim paketi](docs/08-teslim.md) | Dosya, test, katkı ve açık iş bağlantıları. |

## Grubun iş bölümü

Veri erişimi, iş kuralları, arayüz ve davranış kontrollerini [grup büyüklüğüne göre](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşın. Her üyenin sorumluluğunu, dosyalarını ve katkısını [grup kaydına](sablonlar/grup-kaydi.md) yazın. İncelemeyi ilgili bölümün yazımına katılmamış bir üye yapar; ortak yazılan bölüm için gerekirse grup dışından inceleme planlanır.

## Örnek uygulamanın kayıtları

22 Kasım 2026 tarihli [kaynak sürüm kaydında](kanitlar/kaynak-surum.json), H5-S01–H5-S08 için **8 başarılı, 0 başarısız Node testi** bulunur. Bu sonuç belirli sürüme ve test kapsamına aittir. Tarayıcı regresyonları 6. haftada ayrı ele alınır. PR #15, 22 Kasım 2026 tarihinde `main` dalına birleştirilmiştir; ayrıntılar PR sayfasındadır.

## Çalışma materyali ve teslim

[Tek sayfalık süreç infografiği](dagitim/YAZ325_Hafta_05_Surec_Infografik_Aktif_Linkli.pdf) adımları özetler. Tesliminizi [8. adımın listesine](docs/08-teslim.md) göre düzenleyin; henüz yapılmayan kontrolleri ve ölçümleri açık iş olarak yazın.

NFR-01 kullanılabilirlik, NFR-02 yanıt süresi ve NFR-03 klavye ölçümleri bu haftanın sekiz Node testiyle doğrulanmış sayılmaz. 4. haftadaki 9 saat / 19 kişi-saat değerleri planlama tahminidir; grubunuzun gerçek çalışma süresini ayrıca kaydedin.
