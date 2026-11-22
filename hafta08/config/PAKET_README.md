# Klinik Randevu — 0.3.0-rc.1 ders sürüm adayı

YAZ325 Yazılım Geliştirme Süreçleri, 7–8. hafta öğretmen uygulaması.

## Açma

1. ZIP'in tamamını yeni bir klasöre ayıklayın.
2. index.html ile src/ klasörünü birlikte tutun.
3. index.html dosyasını JavaScript açık bir tarayıcıda açın.
4. İlk durum Hasta / Ece / Deniz / 12 Kasım 2030'dur. Saat 09:30 başlangıçta uygundur.
5. Saati seçince yeni yardım metnini okuyun. Seçim kayıt oluşturmaz; Randevuyu onayla düğmesi kayıt oluşturur.

Uygulamayı açmak için internet, Node.js veya Python gerekmez. Bu paket kaynak test araçlarını ve ders PDF'lerini içermez; onlar ders deposundadır.

## Bu adayda değişen

Saat seçimi yardımı mevcut seçime ve role göre değişir. Hasta, doktor, tarih veya rol değişince eski seçimin açıklaması temizlenir. İş kuralları ve veri şeması H6 ile aynıdır.

## Veri ve kapsam

Bütün kişiler ve randevular sentetiktir. Rol seçimi gerçek kimlik doğrulama değildir. Tek tarayıcılı eğitim örneğidir; gerçek klinik için değildir. localStorage kullanılabiliyorsa bu tarayıcıya kaydeder; kullanılamazsa yalnız oturum belleğinde çalışır. Dosya adresini değiştirmek veya farklı tarayıcı kullanmak kayıt erişimini etkileyebilir. Çoklu sekme/cihaz eşzamanlama garantisi yoktur. Kaynak paketi öğrenci tarayıcısındaki kayıtların yedeği değildir.

SURUM.json kaynak commit'ini ve dosya özetlerini, SHA256SUMS.txt paket içeriğinin özetlerini taşır. Özet listesi dijital imza veya insan onayı değildir. Bağımsız inceleme, NFR ölçümü ve kullanıcı kabulü bekliyor; nihai GitHub Release yayımlanmadı.

Ders deposu: https://github.com/pozelll/-klinik-randevu-ogretmen/tree/release/h8-surum-adayi/hafta08

Lisans: LICENSE içindeki MIT metni geçerlidir.
