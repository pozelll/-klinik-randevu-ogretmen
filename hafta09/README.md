# YAZ325 - 9. hafta: Gitflow, Sürüm ve Hotfix

> 22 Kasım 2026 kapanış güncellemesi: PR zinciri main’e birleştirildi; rc.2, gerçek klavye ve performans sonuçları [49 numaralı raporda](docs/49-kapanis-raporu.md). Aşağıdaki rc.1 hazırlık kayıtları tarihseldir; insan kabulü hâlâ açıktır.

22 Kasım 2026 öğretmen hazırlığı. Mevcut Drive planına uygun, sekiz basamaklı anlatım ve gerçek Gitflow laboratuvarı.


## Grubun iş bölümü

İki, üç ve dört kişilik gruplar dal katkıları, çakışma çözümü, sürüm ve hotfix kontrollerini [grup büyüklüğüne göre](../docs/11-grup-buyuklugune-gore-yonlendirme.md) paylaşır. Her üye anlamlı bir çıktı ve gerçek katkı kaydı üretir; yazmadığı kapsamı inceler. Ortak yazılan bölüm için gerekirse grup dışından inceleyen belirlenir. Kendi sorumlularınızı ve sonuçlarınızı [grup kaydına](sablonlar/grup-kaydi.md) yazın; öğretmen örneğinin kişi ve süre varsayımlarını doğrudan kendi planınız saymayın.

| Basamak | Derste açılacak belge | Sonuç |
|---|---|---|
| 1 | [Başlangıç ve dal planı](docs/01-baslangic.md) | Klinik: 0.3.0-rc.1 · Lab: 0.9.x |
| 2 | [İki feature, ortak taban](docs/02-feature.md) | Ortak taban doğrulandı. |
| 3 | [Çakışmayı anlamıyla çöz](docs/03-cakisma.md) | Çözüm: iki ebeveyn, iki katkı. |
| 4 | [Release ve etiket](docs/04-release.md) | Yerel etiket: v0.9.0 senaryosu. |
| 5 | [Hotfix’i iki dala taşı](docs/05-hotfix.md) | İki atalık kontrolü geçti. |
| 6 | [Kanıtı yeniden üret](docs/06-kanit.md) | 12/12 Gitflow · 6/6 panel. |
| 7 | [Kaliteyle sürüm kararı](docs/07-karar.md) | Klinik nihai yayın: BEKLET. |
| 8 | [Kapsamı kapat, devret](docs/08-devir.md) | Ders paketi hazır; açık işler kayıtlı. |

## Derste kullan

- [Tek sayfalık tıklanabilir süreç PDF'i](dagitim/YAZ325_Hafta_09_Surec_Infografik_Aktif_Linkli.pdf)
- [9 sayfalık anlatım rehberi](dagitim/YAZ325_Hafta_09_Ders_Anlatim_Rehberi.pdf)
- [Uygulama ZIP'i](dagitim/YAZ325_Hafta09_Gitflow_Calisma_Paketi.zip): H9 araçları, kaynak metinler, bundle, PDF'ler ve H8 başlangıç paketi.
- [Kurulum, prova ve teknik kaynaklar](docs/47-yeniden-calistirma-ve-kaynaklar.md)
- [Grubun kendi çalışma formu](sablonlar/grup-kaydi.md)

## Gerçek durum

12/12 Gitflow kontrolü yerelde ve [CI'da](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202073) geçti. Son panel 6/6. [Klinik CI](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202040) 30 Node, 14 kaynak tarayıcı, 8 paket ve 14 paketten tarayıcı kontrolünü geçti. Yeni 0.9.x paneli klinik 0.3.0-rc.1 adayından ayrıdır. Yerel eğitim merge/tag'leri GitHub ana dalında yayın değildir.

**Nihai klinik yayın kararı BEKLET:** bağımsız inceleme, NFR ve performans kanıtı açık. [Kalite kararı](docs/44-surum-kalite-karari.md), [plan-gerçekleşen](docs/45-plan-gerceklesen.md), [14 konu kapsamı](docs/46-konu-kapsam-tablosu.md). Otomatik deneydeki Git yazarı “YAZ325 Otomatik Ders Deneyi”dir; öğrenci/öğretmen tarafından yapılmış insan katkısı taklit edilmez.
