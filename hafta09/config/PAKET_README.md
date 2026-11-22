# Klinik Randevu - 0.3.0-rc.2 ders sürüm adayı

YAZ325 Yazılım Geliştirme Süreçleri öğretmen uygulaması. Bu paket klinik uygulamayı içerir; H9 Gitflow panelinin 0.9.x eğitim sürümü ayrı bir örnektir.

## Açma

1. ZIP'in tamamını yeni bir klasöre ayıklayın; ZIP içinden çalıştırmayın.
2. index.html ile src/ klasörünü birlikte tutun.
3. index.html dosyasını JavaScript açık bir tarayıcıda açın.
4. Başlangıçta Hasta / Ece / Deniz / 12 Kasım 2030 seçilidir; 09:30 uygundur.
5. Saati seçmek kayıt oluşturmaz. Randevuyu onayla düğmesi yeni kayıt oluşturur.

Uygulamayı açmak için internet, Node.js veya Python gerekmez. Kaynak test araçları, NFR ölçüm kayıtları ve ders PDF'leri bu küçük uygulama ZIP'ine dahil değildir; ders deposundan erişilir.

## Bu adayda değişen

Saat seçimi ve kayıt işlemlerinden sonraki ekran çiziminde klavye odağının kaybolmasını önleyen düzenleme yapıldı. Görünür odak stili eklendi. H7'nin saat seçimi yardımı korunur. İş kuralları, sentetik veri biçimi ve mevcut localStorage anahtarı değişmedi. H8'in 0.3.0-rc.1 paketi tarihsel kaynak olarak ayrıca korunur.

## Veri ve kapsam

Bütün kişiler ve randevular sentetiktir. Rol seçimi gerçek kimlik doğrulama değildir. Tek tarayıcıda kullanılan eğitim örneğidir; gerçek klinik hizmeti için üretilmemiştir. localStorage kullanılabiliyorsa bu tarayıcıya kaydeder; kullanılamazsa yalnız oturum belleğinde çalışır. Farklı dosya yolu, tarayıcı veya profil mevcut kayıtlara erişimi değiştirebilir. Çoklu sekme veya cihaz eşzamanlama garantisi yoktur. Bu kaynak paketi öğrencinin tarayıcı verilerinin yedeği değildir.

SURUM.json tam kaynak commit'ini ve dosya özetlerini, SHA256SUMS.txt paket içeriğinin özetlerini taşır. Hash doğrulaması dijital imza veya insan onayı değildir.

**İnsan kabulü bekliyor.** Dört gerçek katılımcıyla NFR-01 kullanılabilirlik deneyi, yazar dışında bir kişinin incelemesi ve alıcının erişim/çalıştırma kabulü tamamlanmış olarak gösterilmez. Otomatik teknik kontroller bu koşulların yerine geçmez. Bu dosya nihai üretim yayını onayı değildir; güncel ölçüm sonuçları ve açık işler ders deposunda ayrıca izlenir.

Ders deposu: https://github.com/pozelll/-klinik-randevu-ogretmen

Lisans: LICENSE içindeki MIT metni geçerlidir.
