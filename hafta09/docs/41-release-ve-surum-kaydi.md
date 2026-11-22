# 41 - Release ve sürüm kaydı

| Alan | Gerçek yerel eğitim kaydı |
|---|---|
| Release dalı | release/0.9.0 |
| Kapsam | Birleşik hasta/personel duyurusu; eğitim sürüm ve kanal alanları |
| Release commit | 077d5fb6898dd3c00e575361e5c89ccc2182b252 |
| main birleşimi | 4c7cb9852875a97fefdc661f2fa8a941b83d09f8 |
| Açıklamalı etiket | egitim-hafta09-v0.9.0 |
| Etiket hedefi | 4c7cb9852875a97fefdc661f2fa8a941b83d09f8 |
| develop'a geri taşıma | Gerçek merge; komut kaydında mevcut |
| Geç fark edilen bulgu | Kasıtlı yanlış iptal metni; hotfix basamağının girdisi |
| GitHub ürün Release'i | Oluşturulmadı |

Bu kimlikler paylaşılan bundle'a aittir; yeniden yürütüm yeni kimlik üretir. Ders, yalnız yapısal testle etiketlenen sürümde anlam kusurunun sonradan bulunmasını canlandırır. Gerçek klinik uygulamada bu hata oluşturulmadı ve bir nihai yayın yapılmadı.

```bash
git -C h9-deneyim/lab-deposu show egitim-hafta09-v0.9.0
git -C h9-deneyim/lab-deposu cat-file -t egitim-hafta09-v0.9.0
git -C h9-deneyim/lab-deposu rev-parse 'egitim-hafta09-v0.9.0^{}'
```

| Kavram | Anlam | Tek başına kanıtlamadığı şey |
|---|---|---|
| Commit | İçerik ve geçmişte bir nokta | Bağımsız inceleme |
| Dal | İlerleyebilen commit referansı | Yayına uygunluk |
| Etiket | Seçili sürüm noktasının adı; burada açıklamalı | Test/kabul başarısı |
| Pull request | Değişikliği tartışma ve inceleme isteği | Birleştirilmiş olmak |
| Yayın kararı | Kanıta göre belirlenen uygunluk | Yalnız sürüm numarasıyla oluşmaz |

İsimler değiştirilebilir referanslardır; bu deney eski etiketi taşımadığını G10 ile ayrıca doğrular. Ders deposundaki [PR #21](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21) bağımsız insan incelemesini bekler; yerel eğitim merge'leri bu koşulu kapatmaz.
