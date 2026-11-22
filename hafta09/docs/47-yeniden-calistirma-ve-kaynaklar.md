# 47 - Yeniden çalıştırma ve kaynaklar

## Dersten önce kısa prova

1. Çalışma ZIP'ini tamamen ayıklayın. Git ve Python 3 kurulu olmalı.
2. Paket kökünde `python hafta09/tools/gitflow_lab.py --output kendi-deneyim` çalıştırın. Sonuç 12/12 olmalı; bu sırada beklenen çakışma oluşturulup çözülür.
3. `python hafta09/tools/surum_kontrol.py --anlam` çalıştırın: 6/6.
4. `python -m http.server 8000` ile `http://localhost:8000/hafta09/panel/` açın. Bu panel için HTTP gerekir. Yeni bir deneyin içindeki paneli görmek isterseniz `/kendi-deneyim/lab-deposu/panel/` yolunu açın.
5. H8 başlangıcı için `baslangic/Klinik_Randevu_0.3.0-rc.1.zip` dosyasını ayrı klasöre ayıklayın; içindeki index.html'i açın. Paneldeki 0.9.x bu uygulamanın sürüm numarası değildir.
6. PDF'de kartlara tıklayın; belgeler GitHub bağlantılarıdır ve internet ister. ZIP içindeki Markdown, panel ve Git bundle çevrimdışı kullanılabilir.
7. Bundle'ı yeni klasörde açıp geçmişi gösterin. Öğrenci grubu kendi başlangıç/çıktı kimliğini kaydetsin.

Çalışma ZIP'i bütün tarihsel ders deposunun kopyası değildir: H9 araç/panel/senaryo/kanıtları, düzenlenebilir ders metinleri, iki PDF ve H8 başlangıç uygulaması içerir. Geçmiş H1–H8 belge bağlantıları için GitHub veya Drive dizinini kullanın. Klinik testlerinin kaynakları GitHub deposundadır; H9 panel kontrolleri onların yerine geçmez.

## Birincil teknik kaynaklar

- [Pro Git - Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging): dal, merge ve çakışma.
- [Git bundle belgesi](https://git-scm.com/docs/git-bundle): geçmişin dosya olarak aktarılması ve doğrulanması.
- [Özgün Gitflow yazısı ve 2020 değerlendirmesi](https://nvie.com/posts/a-successful-git-branching-model/): release/hotfix modeli ve her ekibe zorunlu olmadığı bağlamı.
- [GitHub Actions kavramları](https://docs.github.com/en/actions/get-started/understand-github-actions): workflow/run/job ilişkisi.

Ders planı ve eski H9 panel örneği Drive'daki mevcut kullanıcı materyalinden alınmıştır. Eski .NET odaklı rehber ve ZIP'ler yerinde bırakıldı; bu paket güncel düz HTML/JavaScript uygulamasıyla kullanılan ayrı uyarlamadır.
