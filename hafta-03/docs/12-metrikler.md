# 3. hafta — Plan ve gerçekleşen metrikleri

Tarih: 28.10.2026  
Sürüm: 0.1 — inceleme ve teslim öncesi durum  
Konum: hafta-03/docs/12-metrikler.md

## Amaç

Plan tahminlerini, uygulanan işi ve tamamlanma koşullarını birbirine karıştırmadan karşılaştırmak. Bu kayıt öğretmen uygulamasına aittir; öğrenci takımlarının performansı değildir.

## Plan ve sonuç tablosu

| Ölçüm | Değer | Tür / açıklama |
|---|---|---|
| Öğretim uygulamasında belirlenen kapasite | 8 puan | Planlama varsayımı; ölçülmüş takım hızı değil. |
| İlk seçimin ilk tahmini | 2 + 3 + 3 = 8 puan | H3-01, H3-02, H3-03. |
| Yeni bilgi sonrası aynı kapsam | 3 + 3 + 3 = 9 puan | H3-01'e Tamamlandı koşulunu açıkça belirtme işi eklendi; tahmini 2'den 3'e çıktı. |
| Kapasite aşımı | 9 − 8 = 1 puan | Aynı kapsamı korursak plan kapasiteyi aşıyor. |
| Güncel seçimin tahmini | 3 + 3 = 6 puan | H3-01 ve H3-02 seçili. |
| Ertelenen kapsam | H3-03 / #10, 3 puan | Todo; uygulanmadı. |
| Güncel plandaki kullanılmayan kapasite | 8 − 6 = 2 puan | Bu boşluk tek başına 3 puanlık ertelenmiş işin sığdığını göstermez. |
| Kodu uygulanan işler | H3-01 / #8 ve H3-02 / #9 | Kod farkı ve test kaydı var; tam DoD sonucu değil. |
| Tüm DoD koşullarını geçtiği doğrulanan işler | Henüz yok | Bağımsız inceleme ve son teslim koşulları bekliyor. |
| DoD ile bitmiş işlerin güncel puan toplamı | 0 puan | Bu kapanış öncesi ölçümde; “hiç çalışma yapılmadı” anlamına gelmez. |
| Çalıştırılan kontrol | 6: T01–T06 | 08-test-kaydi.md içindeki tanımlı kapsamlarla. |
| Geçen kontrol | 6 | Ekran ve kullanıcı bildirimi ayrımı test belgesinde. |
| Başarısız kayıtlı kontrol | 0 | Yalnız bu altı kontrolün kayıtlı sonuçları için. |
| Bu altı kontrol içinde çalıştırılmayan | 0 | Bütün olası testlerin yapıldığı anlamına gelmez. |
| NFR ölçümleri | Ölçülmedi | Kullanılabilirlik, performans ve klavye ölçümleri. |
| Bağımsız inceleme | Bekliyor | Ortak kod okuması bağımsız onay sayılmaz. |

## Hesapların yorumu

İlk plan 8 puandı. Yeni bilgiyle aynı üç işi yapmak 9 puan olarak yeniden tahmin edildi. Kapasite 8 olarak korunduğu için H3-03 ertelendi; kalan iki işin toplamı 6 oldu. Tahmin değişikliği, harcanmış süre ölçümü değildir. Puanlar saat değildir; 3 puan doğrudan 3 saat anlamına gelmez.

Seçili altı kontrolün geçme oranı 6/6 = %100'dür. Bu yalnız tanımlı kontrol kümesinin sonucudur; ürünün yüzde yüz hatasız, güvenli veya bütün kullanıcılar için anlaşılır olduğunu göstermez. Başarı bildiriminin koşullu saat ifadesiyle tutarlılığına ilişkin açık gözlem 09-pr-inceleme.md içindedir; henüz başarısız test olarak sınıflandırılmadı.

Kod uygulaması bitmiş olan iki işin tahmini toplamı 6 puandır. Fakat DoD kapsamında bağımsız inceleme ve teslim koşulları beklediği için bu aşamada bitmiş iş toplamına 6 yazılmaz. İnceleme ve kapanış kanıtı geldiğinde bu tablo yeniden güncellenir; geçmiş ölçüm anı korunur.

## Test verisinin sayımı

| Aşama | Bekleyen | Tamamlanan | İptal edilen | Toplam |
|---|---:|---:|---:|---:|
| R013 öncesi | 1 | 2 | 6 | 9 |
| R013 oluşturuldu | 2 | 2 | 6 | 10 |
| R013 iptalinden vazgeçildi | 2 | 2 | 6 | 10 |
| R013 iptali onaylandı | 1 | 2 | 7 | 10 |

Kaynak: [08-test-kaydi.md](08-test-kaydi.md). Vazgeçme satırı kullanıcı bildirimiyle, diğer sayım satırları ekran görüntüleriyle doğrulandı. Oluşturma toplamı bir artırdı; vazgeçme ve onaylı iptal toplamı değiştirmedi. Bunlar uygulamanın kayıt sayılarıdır; takımın iş puanı değildir.

## Bu kayıttan çıkarılamayacak sonuçlar

Tek öğretmen uygulamasından takım hızı veya bireysel verimlilik sonucu çıkarılmaz. Tekrar eden, karşılaştırılabilir tamamlanmış çalışma dönemleri yoktur. İşlerin başlangıç/bitiş zamanları düzenli kaydedilmediğinden çevrim süresi veya ortalama iş tamamlama süresi hesaplanmadı. Görev puanı, commit sayısı veya dosya sayısı öğrencileri sıralamak için kullanılmaz.

## Sınıfta kullanım ve konuşma notu

Üç beş kişilik ve bir dört kişilik grup kendi ilk/güncel planını ve gerçek sonuçlarını bu yapıda kaydeder. Gruplar öğretmen örneğinin 6/6 sonucunu kendi sonuçları gibi kopyalamaz; çalıştırılmayan kontrolü açıkça belirtir.

Öğretmen anlatımı: “Önce 8 puanlık iş seçtik. Yeni bilgi geldiğinde aynı işler 9 puan oldu. Kapasitemizi artırmış gibi yapmadık; bir işi erteledik ve 6 puanlık kapsamı koruduk. İki işin kodunu yaptık ama inceleme ve teslim koşulları bitmediği için henüz Done puanı yazmıyoruz. Metrik, yaptığımız işi görünür kılar; eksikleri saklamak için kullanılmaz.”

## Kaydetme

Dosyayı hafta-03/docs içine kaydedin. Bu sürüm henüz GitHub'a yüklenmedi. Sonraki belge 13-cikis-bileti.md; bireysel yanıtlar gerçek öğrenci/öğretmen yanıtı alınmadan doldurulmayacak.
