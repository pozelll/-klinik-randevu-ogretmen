# 8. hafta / 2. adım - Sürüm notları

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Alıcının değişen davranışı, paketi nasıl açacağını ve kullanım sınırlarını anlayabileceği kısa bir sürüm notu hazırlayın. Yalnızca kanıtlanan sonuçları belirtin.

## Grup çalışması

1. Kendi sürümünüzde kullanıcıya görünen değişikliği yazın.
2. Korunan davranışları ve varsa veri biçimi değişikliğini belirtin.
3. Paketi indirme, ayıklama ve açma adımlarını sıralayın.
4. Bilinen sınırları, tamamlanan teknik kontrolleri ve bekleyen değerlendirmeleri ayrı kaydedin.
5. Sürüm notunu [kabul ve teslim kaydına](09-kabul-ve-teslim.md) bağlayın.

## Teslim edilecek çıktı

**Yenilik, korunan davranışlar, açılış adımları, bilinen sınırlar ve kabul durumu** başlıklarını içeren sürüm notu. Alıcı bu bilgileri uygulama kodunu okumadan kullanabilmelidir.

## 0.3.0-rc.1 için tarihli örnek sürüm notu

Aşağıdaki not, 22 Kasım 2026 tarihli H8 hazırlığının kapsamını ve o andaki ölçüm durumunu gösterir.

**Yeni:** Saat alanında seçim adımları açıklanır. Saat seçilince henüz kayıt oluşturulmadığı belirtilir. Doktor rolüne uygun açıklama gösterilir. Hasta, doktor, tarih veya rol değiştiğinde eski seçim metni temizlenir.

**Korunan:** FR-01–FR-06 davranışları, iptal/tamamlama kuralları, tek ortak depo ve saklama biçimi. Veri şeması göçü yoktur.

**Açma:** ZIP'in tamamını yeni bir klasöre çıkarın. index.html ile src/ birlikte kalsın. index.html dosyasını tarayıcıda açın. İnternet ve sunucu gerekmez. Kaydetme durumunu ekranın altından okuyun.

**Bilinen sınırlar:** Tek tarayıcı ve sentetik veri. Gerçek giriş, merkezi veritabanı ve cihazlar arası eşzamanlama yok. Yerel dosya saklaması tarayıcıya bağlı. Kullanılabilirlik, yanıt süresi ve klavye NFR ölçümleri yapılmadı. Bağımsız inceleme ve gerçek kullanıcı kabulü bekliyor.

Bu, inceleme için hazırlanmış ders adayıdır. GitHub etiketi veya yayımlanmış Release oluşturulmadı.

Teknik test sonucu, alıcının gerçek kabul kararından ayrı tutulur. Grubunuzun güncel kabul durumunu kendi kayıtlarında belirtin.

[Görev #17](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/17) · [PR #19 ve güncel durumu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/19)
