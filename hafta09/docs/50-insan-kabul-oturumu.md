# 50 - RC2 insan kabul oturumu

Bu belge uygulanacak protokoldür; tamamlanmış katılımcı deneyi, bağımsız insan incelemesi veya alıcı kabulü kaydı değildir. CSV sonuç hücreleri bilerek boştur. Kaynak [NFR hedefleri](../../docs/03-gereksinimler.md) korunur.

## Oturumda kullanılacak sabit aday

| Alan | Değer |
|---|---|
| Klinik uygulama | `0.3.0-rc.2` |
| Uygulama kaynak commit'i | `5c796623a18d4ba187d2a9fe9beba4708915360b` |
| Paket | [Klinik_Randevu_0.3.0-rc.2.zip](../dagitim/Klinik_Randevu_0.3.0-rc.2.zip) |
| Paket SHA-256 | `85371dd961cee6e197158d95b68906dbaf21bf96e540fc2ef8a7b1f300feb84a` |
| Aday tanımı | [surum-adayi.json](../config/surum-adayi.json) |
| Oturum kayıtları | [NFR-01 katılımcı CSV](../sablonlar/nfr01-katilimci-kaydi.csv), [NFR-02 ekran kaydı CSV](../sablonlar/nfr02-ekran-kaydi.csv) |

Her oturumda paket adı ve hash'i doğrulanır. Kaynak commit, uygulamanın kimliğidir; sonradan eklenen form/belge commit'leriyle karıştırılmaz. Farklı uygulama kodu veya paket kullanılırsa eski sonuçlar yeni adaya doğrudan taşınmaz.

## NFR-01 - Dört kişiyle kullanılabilirlik

**Değişmeyen eşik:** dört farklı katılımcının en az üçü iki görevin ikisini de doğru, yardım almadan ve **her görev için en fazla 60 saniyede** tamamlamalıdır. Bir kişinin dört tekrarı dört katılımcı sayılmaz. Bu küçük ders örneği bütün kullanıcıları temsil eden bir araştırma sonucu olarak sunulmaz.

1. Dört ayrı kişi P01–P04 olarak kaydedilir. Gerçek oturum tarihi, cihaz/işletim sistemi, tarayıcı sürümü, gözlemci ve önceki prototip deneyimi yazılır. Katılımcıların birbirinin denemesini görmesi önlenir; görevden önce hangi düğmeye basılacağı öğretilmez.
2. Gözlemci her katılımcı için ayrı, yalnız bu deneye ait temiz tarayıcı profili/oturumu açar. Katılımcının mevcut çalışma verisi sıfırlanmaz. Aynı RC2 paketi kullanılır; Hasta, Ece Yılmaz, Deniz Arı, 12 Kasım 2030 seçilidir.
3. Başlangıçtaki R001 / 09:00 Bekliyor kaydı görev 1 içindir. Gözlemci, katılımcı başlamadan 09:30 için ikinci bir randevu oluşturur; temiz örnekte bu R008 olur. Bu ikinci Bekliyor kaydı görev 2 içindir. İki kimlik ve başlangıç durumları kontrol edilir; farklı kimlik oluşursa gerçek kimlik yazılır. Hazırlık süresi katılımcı süresine dahil edilmez.
4. Görev sırası oturumdan önce belirlenir ve CSV'ye yazılır. Tüm katılımcılara aynı görev metinleri okunur. Hedef kayıt kimliği/saatinin söylenmesi, hangi düğmenin kullanılacağını tarif etmek değildir.

| Görev | Katılımcıya okunacak metin | Hedef kayıt | Beklenen son durum |
|---|---|---|---|
| T1 - İptal | “Bekleyen randevunuzu iptal edin.” | R001 / 09:00 | Kayıt İptal edildi ve listede; 09:00 Uygun |
| T2 - Vazgeçme | “İptal sürecini başlatın, sonra randevunuzu koruyarak işlemden vazgeçin.” | Ayrı R008 / 09:30 | Kayıt Bekliyor; 09:30 Dolu |

5. Görev okunup başlama işareti verildiğinde süre başlatılır; katılımcı bitirdiğini söylediğinde durdurulur. Gerçek sonuç kayıt ve saat üzerinden kontrol edilir. Süre, doğruluk, yardım isteme, yardım verilmesi ve yanlışlıklar ayrı yazılır. 60 saniyeyi aşan gerçek süre veya tamamlanamayan görev gizlenmez; öğretmen yardımından sonra başarıya ulaşması yardımsız başarı sayılmaz.
6. CSV'de `gorev1_*` T1'i, `gorev2_*` T2'yi ifade eder; gerçek uygulama sırası `gorev_sirasi` alanındadır. Doğruluk/yardım alanları gerçek gözleme göre `evet` veya `hayir` olarak doldurulur. Ölçülmeyen süreye `0` yazılmaz; alan boş bırakılıp notta açıklanır.
7. Bir katılımcı yalnız iki görev de doğru, yardımsız ve ayrı ayrı ≤60 saniye ise başarılıdır. Yardım isteği ayrıca raporlanır; değerlendirme gerçek yardım ve sonuç kaydıyla gerekçelendirilir. Katılımcı başarısını yalnız bir görevin ortalamasına göre hesaplamayın.

| Oturum sonunda doldurulacak özet | Gerçek sonuç |
|---|---|
| Başarılı katılımcı / 4 | |
| NFR-01: sağlandı / sağlanmadı / eksik veri | |
| Gözlenen yanlış işlem ve yardım ihtiyacı | |
| Değerlendiren kişi ve tarih | |
| Düzeltme veya yeniden deneme kararı | |

## NFR-02 - Özgün ekran kaydı yöntemi

**Değişmeyen eşik:** aynı cihaz/tarayıcıda, tek sekme ve en fazla 20 kayıtla yapılan **10 doktor seçimi değişikliğinin tamamında**, B1 saatler, B2 günlük liste ve B3 günlük toplamlar yeni seçime uygun olarak **en fazla 1 saniyede** görünmelidir. Yanlış içeriğin hızlı görünmesi başarı değildir.

1. Ayrı temiz RC2 oturumu açın. Başlangıçtaki 7 sentetik kayıt yeterlidir; gerçek kayıt sayısını CSV'ye yazın. Resepsiyon rolünü ve 12 Kasım 2030 tarihini seçin. Başlangıç doktoru Deniz Arı olsun. Açık onay penceresi veya geliştirici araçlarında CPU/ağ yavaşlatması bulunmasın.
2. Kullanılan cihazı, işletim sistemini, tarayıcı sürümünü, kayıt yazılımını, gerçek kayıt kare hızını (FPS) ve video dosyası adını kaydedin. B1, B2 ve B3 alanlarının üçünü de kayıtta aynı anda görünür tutun. Başlangıç olayının (tıklama/Enter onayı) videodan belirlenebilir olmasını sağlayın; mümkünse kayda görünür giriş işareti ekleyin.
3. Deniz Arı → Selin Kaya ve Selin Kaya → Deniz Arı yönlerinde dönüşümlü 10 seçim yapın. CSV'nin `planlanan_*` sütunları yalnız deney planıdır; `gercek_*` sütunlarına gerçekten yapılan seçimi yazın. Kullanıcının seçimi düşünme veya menüde gezinme süresi yanıt süresine dahil edilmez.
4. Başlangıç karesi seçimin tıklama veya Enter ile onaylandığı andır. Bitiş karesi yeni doktorun B1, B2 ve B3 içeriğinin **tamamının doğru** göründüğü ilk karedir. Menüde bir seçenek üzerinde gezinmek seçim onayı sayılmaz. Olay görünmüyorsa başlangıç zamanını tahmin etmeyin.
5. Başlangıç/bitiş karelerini ve zaman damgalarını, üç alanın doğruluğunu ve ölçüm belirsizliğini kaydedin. Sabit FPS kayıtta gözlenen süre `(bitis_kare - baslangic_kare) / FPS` ile hesaplanabilir. Değişken kare hızlı veya atlanan kareli kayıtta gerçek kare zaman damgaları kullanılır; sabit FPS varsayılmaz.
6. Aynı kare içinde görünen değişime sıfır saniye yazmayın: süre hücresine `<1/FPS` açıklamasını ve notlara gerçek kare aralığını yazın. Kare aralığı ve olayın hangi karede başladığına bağlı belirsizliği belirtin. Belirsizlik nedeniyle 1 saniye sınırı ayırt edilemiyorsa o denemeyi başarılı saymayın; orijinal kaydı koruyarak uygun kayıtla yeniden ölçün.

Temiz başlangıç verisindeki beklenen içerik:

| Yeni doktor | B1 dolu/kapalı saatler | B2 günlük kayıtlar | B3 Bekliyor / Tamamlandı / İptal / Toplam |
|---|---|---|---|
| Deniz Arı | 09:00 Dolu, 10:00 Dolu, 11:00 Kapalı; 13:00 Uygun | R001, R002, R003, R004 | 2 / 1 / 1 / 4 |
| Selin Kaya | 09:30 Dolu, 11:00 Kapalı | R005, R006 | 1 / 1 / 0 / 2 |

Diğer saatler uygun olmalıdır. Tablo yalnız belirtilen temiz başlangıç içindir; veri değiştirilmişse sonucu bu sayılara zorlamayın, oturumu uygun başlangıçla yeniden hazırlayın.

| Ekran kaydı sonunda doldurulacak özet | Gerçek sonuç |
|---|---|
| Doğru içerik + yeterli ölçüm + ≤1 saniye sağlanan deneme / 10 | |
| En büyük gözlenen süre ve ölçüm belirsizliği | |
| NFR-02: sağlandı / sağlanmadı / ölçüm yetersiz | |
| Video dosyası, değerlendirici ve tarih | |

[Otomatik performans ölçümleri](../kanitlar/kapanis/performans-sonuclari.json) tarayıcı içi instrumentasyonun ayrı teknik kanıtıdır. Bu dosya tek başına özgün ekran kaydı oturumunun yapılmış olduğu anlamına gelmez. Otomatik ölçüm ve ekran kaydı sonuçları ayrı yöntem başlıklarıyla raporlanır. Bu NFR-02 oturumu sunucu yükü veya çok kullanıcılı ölçek testi değildir.

## Bağımsız insan incelemesi

İncelemeyi fiilen yapan, değişikliğin yazarı olmayan kişi aşağıdaki alanları doldurur. AI teknik incelemesi veya otomatik test koşusu insan incelemesi olarak kaydedilmez. Kullanıcının merge talimatı, yapılmamış bağımsız inceleme sonucunun yerine yazılmaz.

| Alan | Gerçek kayıt |
|---|---|
| İnceleyen kişi; yazarla ilişkisi/bağımsızlık açıklaması | |
| Tarih; incelenen tam commit ve RC2 paket hash'i | |
| İncelenen PR / dosya / kabul koşulları | |
| İşlevsel test, klavye, performans ve NFR kanıtlarına ilişkin bulgular | |
| Bulgu önem düzeyi; düzeltme gereksinimi | |
| Düzeltme commit'i; yeniden kontrol sonucu | |
| Kabul / değişiklik gerekli / eksik kanıt kararı ve gerekçesi | |

## Alıcının ZIP doğrulaması ve kabul kaydı

1. Alıcı RC2 ZIP'ini kendi erişimiyle indirir. İndirme bağlantısı, gerçek tarih, dosya adı ve alıcı kimliği kaydedilir. “Dosya yüklendi” bilgisi, alıcının eriştiği ve çalıştırdığı anlamına gelmez.
2. İndirilen **ZIP'in** SHA-256 değerini yukarıdaki sabit değerle karşılaştırır. Ubuntu/Linux: `sha256sum Klinik_Randevu_0.3.0-rc.2.zip`; macOS: `shasum -a 256 Klinik_Randevu_0.3.0-rc.2.zip`; Windows PowerShell: `Get-FileHash .\Klinik_Randevu_0.3.0-rc.2.zip -Algorithm SHA256`. Eşleşmeyen dosya çalıştırma kabulüne alınmaz.
3. ZIP tamamen yeni bir klasöre ayıklanır; ZIP'in içinden doğrudan açılmaz. `SURUM.json` içinde `version=0.3.0-rc.2` ve yukarıdaki kaynak commit kontrol edilir. `index.html` ve `src/` aynı kökte tutulur. Paketteki `README.md` ve `SHA256SUMS.txt` incelenir.
4. Alıcı `index.html` dosyasını kendi tarayıcısında açar. Yalnız sentetik eğitim verisi kullanır. Bu işe ayrılmış temiz tarayıcı oturumunda başlangıç, bir randevu oluşturma, iptalden vazgeçme, iptal ve doktor rolünde tamamlama işlemlerini gözler. Mevcut öğrenci çalışması habersiz sıfırlanmaz. Kaydetme durumunun yerel kayıt mı yalnız oturum belleği mi olduğu kaydedilir.
5. Tam depo ve Python bulunan teknik kontrol ortamında ayrıca şu komut çalıştırılabilir: `python scripts/build_candidate.py --profile h9 verify hafta09/dagitim/Klinik_Randevu_0.3.0-rc.2.zip`. Bu teknik doğrulama alıcının kendi kullanım/kabul kaydını tamamlamaz.

| Alan | Gerçek kayıt |
|---|---|
| Alıcı, tarih, indirme bağlantısı ve erişim sonucu | |
| İndirilen ZIP SHA-256; eşleşti mi? | |
| SURUM.json sürümü ve kaynak commit | |
| Cihaz, işletim sistemi ve tarayıcı | |
| Başlangıç ve dört temel işlemde gözlenen gerçek sonuçlar | |
| Kaydetme durumu; yeniden açma gözlemi | |
| Sorun, hata mesajı veya eksik dosya | |
| Kabul / değişiklik gerekli / tamamlanmadı ve gerekçesi | |

Nihai kabul ancak bu oturumların gerçek kayıtları değerlendirilerek güncellenir. Boş alanlar, AI çıktıları veya ölçülmemiş hedefler başarılı sonuç olarak işaretlenmez.
