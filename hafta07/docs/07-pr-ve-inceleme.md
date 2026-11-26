# 7. hafta / 7. adım - PR ve inceleme

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Değişikliğin amacı, dosya farkları ve test kanıtlarını bir PR içinde birleştirmek; gerçek inceleme sonucunu kaydetmek.

Otomatik kontrollerin sonucu, başka bir kişinin incelemesi ve değişikliğin hedef dala birleştirilmesi ayrı durumlardır. İncelemeyi ilgili içeriğin yazımına katılmamış bir kişi yapar.

## Grup çalışması

1. Kendi PR açıklamanıza sorunu, değişen davranışı ve test kanıtlarını yazın.
2. Kaynak dalı, hedef dalı ve **Files changed** bölümündeki farkı kontrol edin.
3. Başka bir üyeye belirli bir inceleme kapsamı verin; ortak yazılan kapsam için gerekirse grup dışından inceleyen belirleyin.
4. Gerçek inceleme sonucunu, incelenen tam commit'i ve varsa bulguları kaydedin.
5. Düzeltme yapıldıysa düzeltme commit'ini ve yeniden kontrol sonucunu ekleyin.

## İnceleme kayıt formu

| Alan | Grubun kaydı |
|---|---|
| İnceleyen adı / hesabı | |
| İncelenen içeriğin yazımına katılma durumu | |
| İncelenen tam commit / tarih | |
| Kapsam ve bulgular | |
| Düzeltme commit'i ve yeniden kontrol | |
| Hedef dal | |
| Gerçek GitHub review bağlantısı | |
| Birleştirme durumu ve kaydı | |

Henüz yapılmayan incelemeyi onay olarak doldurmayın. Bağımlı PR'larda hedef dal değiştiğinde farkı, çakışmaları ve kontrol edilen commit'i yeniden doğrulayın.

## Örnek PR kaydı

[PR #18](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/18), **22 Kasım 2026 tarihinde `main` dalına birleştirilmiştir**. İlk hazırlıkta kaynak dal `feat/h7-saat-secimi-yardimi`, hedef dal `test/h6-karar-tablosu` idi; tarihsel bağımlılık sırası #7 → #11 → #12 → #15 → #16 → #18 olarak kaydedilmişti.

Bu tarihsel hedef bilgisi güncel birleştirme durumuyla karıştırılmamalıdır. PR sayfası gerçek inceleme ve birleştirme kayıtları için kaynaktır; birleştirilmiş olması bağımsız insan incelemesi yapıldığını tek başına göstermez.

[Görev #10](https://github.com/pozelll/-klinik-randevu-ogretmen/issues/10) · [Grup kayıt formu](../sablonlar/grup-kaydi.md)
