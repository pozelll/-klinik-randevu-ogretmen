# 9. hafta / 1. basamak - Başlangıç ve dal planı

## Derste anlat
Önce hangi sürüm üzerinde çalıştığımızı belirleriz. Klinik uygulamanın H8 adayı 0.3.0-rc.1 olarak kalır. Gitflow kavramlarını, bilgilendirme paneli içeren ayrı bir eğitim deposunda 0.9.x sürümüyle uygularız. main teslim geçmişini, develop gelecek sürümün birleşik çalışmasını temsil eder. Gitflow her proje için zorunlu değildir; burada release ve hotfix ayrımını görünür kılmak için seçildi.

## Ekranda göster ve uygula
GitHub H9 dalını ve 39 numaralı belgeyi açın. Önce H8 paketini gösterin. Terminalde python hafta09/tools/gitflow_lab.py --output h9-deneyim komutu bütün deneyi yeni klasörde kurar. Komut mevcut dolu klasörü kabul etmez. Sonraki basamaklarda bu deneyin gerçek commit, çakışma ve etiket kayıtlarını inceleyeceğiz. Ayrı terminalde python -m http.server 8000 çalıştırıp /hafta09/panel/ yolunu açın.

- [39 · Dal planı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta09/docs/39-gitflow-ve-dal-plani.md)
- [H8 başlangıç kaydı](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/docs/h9-gitflow-teslim/hafta08/docs/01-surum-adayi.md)

## Öğrenciye soru
**Panelde 0.9.1 yazması klinik uygulamanın da 0.9.1 olduğu anlamına gelir mi?**

Beklenen açıklama: Hayır. Panel ve klinik aday farklı kapsamdır. Sürüm metnini ürün, commit ve paket kaydıyla birlikte yorumlarız.

## Grubun yapacağı iş
Kendi başlangıç commit’inizi, dal politikanızı ve kapsam dışı işleri 39 belgesine kaydedin. Sürüm alanlarını adlandırın.

Kontrol: Başlangıç SHA’sı ve iki ürün kapsamı açık; deney kendi klasöründe.

## Hazırlığın durumu
Klinik: 0.3.0-rc.1 · Lab: 0.9.x İki sürüm alanı ayrı tutulur.

[Görev #20](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/20) · [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21). Öğretmen örneği; gerçek öğrenci katkısı veya bağımsız inceleme iddiası değildir.
