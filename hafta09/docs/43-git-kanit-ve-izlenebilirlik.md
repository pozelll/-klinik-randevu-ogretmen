# 43 - Git kanıtı ve izlenebilirlik

> 22 Kasım 2026 tarihli teknik hazırlık kaydı: Bu belge Gitflow eğitim deneyini ve klinik 0.3.0-rc.1 başlangıcını anlatır. Dal, hedef ve açık/taslak PR bilgileri birleştirme öncesindeki duruma aittir. [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21) aynı gün main'e birleştirilmiştir; bu işlem bağımsız insan incelemesi veya kabulü yerine geçmez. Güncel 0.3.0-rc.2 sonuçları [kapanış raporunda](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md), açık insan kabul işleri [kabul oturumu ve formlarında](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/50-insan-kabul-oturumu.md) bulunur.

## Kanıt katmanları

| Kanıt | Kapsam | Sonuç / kaynak |
|---|---|---|
| [Yerel rapor](../kanitlar/gitflow-sonuclari.json) | Gerçek yerel Gitflow deneyi | 12/12; 22 Kasım 2026, Git 2.56.1 |
| [CI Gitflow raporu](../kanitlar/ci-gitflow-sonuclari.json) | Aynı araçların GitHub Actions yürütümü | [45023202073](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202073), 12/12 |
| Son panel kontrolü | 5 yapı + 1 tanımlı anlam kontrolü | CI'da 6/6 |
| [Klinik CI](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202040) | Mevcut uygulama ve dağıtım paketi | 30 Node; 14 kaynak tarayıcı; 8 paket; 14 paket tarayıcı |
| [Komut kaydı](../kanitlar/komut-kaydi.json) | Git komutları, çıkış kodları, stdout/stderr | Gerçek yürütüm |
| [Git bundle](../kanitlar/YAZ325_Hafta09_Gitflow_Deneyi.bundle) | Yerel deneyin dalları, commit'leri, etiketleri | 6.786 bayt; yeni klasörde açılarak doğrulandı |
| [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21) | GitHub değişiklik paketi | Taslak, açık; bağımsız inceleme bekliyor |

CI'nın denetlediği H9 kaynak commit: `901f8144b83947ec4bfc0aabad5a7f7998a24ce8`. Kaynak SHA PR başıdır; pull_request koşusu GitHub'ın geçici birleşim çalışma kopyasını kullanır. Yerel ve CI deneylerinin commit kimlikleri farklıdır; her raporun kendi kimliği esas alınır. Bundle yalnız yerel raporla eşleştirilir.

Panel kontrolleri klinik testlerinin yerine sayılamaz. Kaynak tarayıcı ve paket tarayıcı aynı 14 senaryonun iki farklı sunumda yürütümüdür; 28 ayrı davranış kapsamı iddiası değildir. Otomasyon bağımsız insan incelemesi veya gerçek kullanıcı kabulü değildir.

## Bundle'ı açma

Depo kökünden, henüz var olmayan hedef klasöre:

```bash
git clone -b develop hafta09/kanitlar/YAZ325_Hafta09_Gitflow_Deneyi.bundle h9-gecmis
git -C h9-gecmis log --graph --decorate --oneline --all
git -C h9-gecmis rev-parse HEAD
git -C h9-gecmis show HEAD:panel/surum.json
git -C h9-gecmis bundle verify ../hafta09/kanitlar/YAZ325_Hafta09_Gitflow_Deneyi.bundle
```

Beklenen HEAD: `2c31d9f90d55186b5aed3aa7c672c59c51f9b3f2`. Bundle SHA-256: `d8fd9933df4a095305323b6767487d2ed2db7b9cbf0c2c7f694fc82e858d3b65`.

Klonlama diğer dalları `origin/main`, `origin/hotfix/0.9.1` gibi uzak izleme referansları olarak açar. Bunlar GitHub'a bağlı değildir; origin yerel bundle dosyasıdır. Atalık incelemesinde bu referansları kullanın. Kendi denemenizi çalıştırırsanız `lab-deposu` içindeki dallar yerel isimlerle bulunur.

## 12 süreç kontrolü

| Kimlik | Denetlenen sonuç |
|---|---|
| G01 | Başlangıçta 5 yapısal kapı |
| G02 | Feature'ların ortak tabanı |
| G03 | Gerçek merge çakışması |
| G04 | Çözülmemiş panelin reddi |
| G05 | İki ebeveyn ve iki katkının korunması |
| G06 | Release etiket türü ve hedefi |
| G07 | Yanlış anlamın 5/6 ile reddi |
| G08 | Hotfix sonrasında 6/6 |
| G09 | İki hedefe atalık ve aynı son içerik |
| G10 | Yeni etiket doğru, eski etiket değişmedi |
| G11 | Bundle'dan açılan geçmiş ve içerik doğru |
| G12 | Temiz deney; harici remote/push yok |
