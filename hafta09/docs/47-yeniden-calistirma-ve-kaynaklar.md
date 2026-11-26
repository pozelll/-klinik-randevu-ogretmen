# 47 - Yeniden çalıştırma ve kaynaklar

## Öğrenci kurulumu ve yeniden çalıştırma

1. Çalışma ZIP'ini tamamen ayıklayın. Git ve Python 3'ün kurulu olduğunu `git --version` ve `python --version` komutlarıyla kontrol edin. Windows'ta Python komutu `py -3` olabilir.
2. Paket kökünde `python hafta09/tools/gitflow_lab.py --output kendi-deneyim` çalıştırın. `kendi-deneyim` klasörü yeni veya boş olmalıdır. Araç gerçek bir Git deneyi kurar; çakışmayı oluşturur, çözer ve sonucu doğrular. Beklenen süreç sonucu 12/12'dir. Kendi yürütümünüzün raporunu ve çıkış durumunu kaydedin.
3. `python hafta09/tools/surum_kontrol.py --anlam` çalıştırın. Beklenen sonuç 6/6'dır; bu sonuç eğitim panelinin kontrolüdür.
4. `python -m http.server 8000` ile `http://localhost:8000/hafta09/panel/` açın. Bu panel için HTTP gerekir. Yeni bir deneyin içindeki paneli görmek isterseniz `/kendi-deneyim/lab-deposu/panel/` yolunu açın.
5. H8 başlangıcı için `baslangic/Klinik_Randevu_0.3.0-rc.1.zip` dosyasını ayrı klasöre ayıklayın; içindeki index.html'i açın. Paneldeki 0.9.x bu uygulamanın sürüm numarası değildir.
6. Aktif bağlantılı süreç infografiğinde kartlara tıklayarak sekiz öğrenci yönergesini açın. PDF'deki GitHub bağlantıları internet ister. ZIP içindeki Markdown dosyaları, yerel HTTP sunucusuyla çalışan panel ve Git bundle çevrimdışı kullanılabilir.
7. [Bundle'ı açma adımlarını](43-git-kanit-ve-izlenebilirlik.md) izleyerek geçmişi yeni bir klasörde inceleyin. Kendi deneyinizin başlangıç ve çıktı kimliklerini, kullandığınız komutları ve elde ettiğiniz sonuçları grup kaydına yazın. Otomatik örnek commit'lerini kişisel katkı olarak kaydetmeyin.

Çalışma ZIP'i öğrenci README'sini, sekiz çalışma yönergesini, teknik destek belgelerini, H9 araçlarını, paneli, senaryoları, kanıtları, bir aktif bağlantılı süreç infografiği PDF'sini ve iç ZIP olarak H8 başlangıç uygulamasını içerir. Dosyalar 26 Kasım 2026 öğrenci yönergeleri düzenlemesini yansıtır; deney kodu ve tarihsel kanıtlar korunur. Klinik başlangıç ZIP'i 0.3.0-rc.1 sürümüne aittir; 0.9.x eğitim panelinden ayrıdır.

H1–H8 belgeleri ve diğer öğrenci kaynakları için [GitHub ders dosyaları dizinini](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/48-drive-teslim-dizini.md) kullanın. Bu çalışma ZIP'i tüm tarihsel ders deposunu içermez. Klinik testlerinin kaynakları GitHub deposundadır; H9 panel kontrolleri onların yerine geçmez. Güncel 0.3.0-rc.2 ve açık insan kabul işleri için [kapanış raporuna](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md) ve [kabul oturumu formlarına](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/50-insan-kabul-oturumu.md) bakın.

## Birincil teknik kaynaklar

- [Pro Git - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging): dal, merge ve çakışma.
- [Git bundle belgesi](https://git-scm.com/docs/git-bundle): geçmişin dosya olarak aktarılması ve doğrulanması.
- [Özgün Gitflow yazısı ve 2020 değerlendirmesi](https://nvie.com/posts/a-successful-git-branching-model/): release/hotfix modeli ve her ekibe zorunlu olmadığı bağlamı.
- [GitHub Actions kavramları](https://docs.github.com/en/actions/get-started/understand-github-actions): workflow/run/job ilişkisi.

Kaynak bağlamı: 26 Ekim 2026 ders planı ve önceki H9 panel örneği temel alınmıştır. Bu laboratuvar düz HTML/JavaScript uygulamasına uyarlanmıştır; .NET kurulumu gerekmez.
