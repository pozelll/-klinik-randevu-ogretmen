# 9. hafta / 1. adım - Başlangıç ve dal planı

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Hangi ürün ve kaynak üzerinde çalıştığınızı belirleyin. Bu laboratuvarın `0.9.x` paneli, H8'in `0.3.0-rc.1` klinik başlangıç paketinden ayrıdır. Daha sonraki klinik `0.3.0-rc.2` adayı [güncel kapanış kaydında](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md) izlenir.

## Grup çalışması

1. [Dal planını](39-gitflow-ve-dal-plani.md) ve [H8 başlangıç kaydını](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/release/h8-surum-adayi/hafta08/docs/01-surum-adayi.md) inceleyin. Kendi başlangıç commit'inizi, ürün kapsamınızı ve kapsam dışında bırakacağınız işleri yazın.
2. Git ve Python 3 kurulu bir ortamda depo kökünü açın. Aşağıdaki komutları çalıştırın. Windows'ta Python komutunuz `py -3` olabilir.

```bash
git --version
python --version
python hafta09/tools/gitflow_lab.py --output h9-deneyim
```

3. `h9-deneyim` yeni veya boş bir klasör olmalıdır. Komut bütün eğitim senaryosunu otomatik olarak kurar; sonraki adımlarda oluşan geçmişi inceleyin. Kendi insan katkılarınızı ayrıca kaydedin.
4. Ayrı terminalde depo kökünden `python -m http.server 8000` çalıştırın. Tarayıcıda `http://localhost:8000/hafta09/panel/` adresini açın. Kendi deneyinizin paneli `http://localhost:8000/h9-deneyim/lab-deposu/panel/` adresindedir.
5. Kendi dal planınızda `main`, `develop`, `feature`, `release` ve `hotfix` dallarının çıkış ve hedeflerini yazın. Bu akışı seçme gerekçenizi belirtin.

## Teslim edilecek çıktı

Başlangıç commit'i, ürün/sürüm kapsamı, dal planı, kullanılan Git/Python sürümleri ve deney klasörünün yolunu içeren çalışma kaydı. Panelin sürüm numarasıyla klinik paketin kimliğini ayrı alanlarda tutun.

## Çıktı kontrolü

- Başlangıç kimliği tam commit ile kayıtlıdır.
- Deney çıktıları kendi klasöründedir; `gitflow-sonuclari.json` ve `komut-kaydi.json` oluşmuştur.
- Her dalın amacı ve dönüş hedefi bellidir.

[Sonraki adım: İki feature, ortak taban](02-feature.md) · [Hafta ana sayfası](../README.md)
