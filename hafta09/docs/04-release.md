# 9. hafta / 4. adım - Release ve etiket

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Seçilen sürümün kapsamını, tam commit'ini ve etiketini kayıt altına alın. Etiket kaydıyla test, inceleme ve kabul sonuçlarını ayrı alanlarda izleyin.

## Grup çalışması

1. [Örnek sürüm kaydındaki](41-release-ve-surum-kaydi.md) `release/0.9.0` dalını, `main` birleşimini ve `develop` dalına geri taşıma adımını inceleyin.
2. Kendi deneyinizin açıklamalı etiketini aşağıdaki komutlarla kontrol edin. Etiket mesajını, türünü ve tam hedef commit'ini çalışma kaydınıza ekleyin.

```bash
git -C h9-deneyim/lab-deposu show egitim-hafta09-v0.9.0
git -C h9-deneyim/lab-deposu cat-file -t egitim-hafta09-v0.9.0
git -C h9-deneyim/lab-deposu rev-parse 'egitim-hafta09-v0.9.0^{}'
```

3. Tür çıktısını `tag` olarak ve hedefi aynı koşunun `commits.releaseMain` değeriyle doğrulayın. H9-G06 kaydını ekleyin.
4. Grubunuzun sürüm kaydına kapsamı, tam commit'i, etiket mesajını, açık bulguları ve ilgili test kayıtlarını yazın.
5. GitHub'daki [PR #21'in güncel durumunu](https://github.com/pozelll/-klinik-randevu-ogretmen/pull/21) kendi kaynağından okuyun. Yerel eğitim deposunun merge/tag kayıtlarını gerçek GitHub PR ve ürün yayın kayıtlarından ayrı tutun.

## Teslim edilecek çıktı

Sürüm adı, kapsam, açıklamalı etiket mesajı, hedef commit, doğrulama çıktıları ve açık riskleri içeren sürüm kaydı.

## Çıktı kontrolü

- Etiket türü ve hedefi komut çıktısıyla doğrulanmıştır.
- Yerel `0.9.0` eğitim senaryosu klinik uygulamanın yayın kararı olarak kullanılmamıştır.
- Sürüm kararı için gerekli kalite kanıtları ayrıca bağlantılanmıştır.

Örneğin `0.9.0` sürümündeki kontrollü anlam kusuru bir sonraki hotfix adımının girdisidir. Gerçek klinik uygulamada aynı kusurun bulunduğu sonucu çıkarılmaz.

[Önceki adım](03-cakisma.md) · [Sonraki adım: Hotfix](05-hotfix.md)
