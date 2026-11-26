# 9. hafta / 6. adım - Kanıtı yeniden üret

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Sonuçları kaynak commit, komut, ortam ve koşu tarihiyle ilişkilendirin. Git geçmişinin teslim dosyasından yeniden açılabildiğini doğrulayın.

## Grup çalışması

1. Kendi `h9-deneyim/gitflow-sonuclari.json`, `komut-kaydi.json` ve `git-gecmisi.txt` dosyalarınızı birlikte inceleyin. Kaynak deponun commit'ini, deneyin ürettiği commit'leri ve koşu tarihini ayrı kaydedin.
2. H9-G01–G12 süreç kontrollerini ve son panelin altı kontrolünü kendi koşunuzdan okuyun. Başarısız veya eksik bir sonucu örneğin başarılı sonucuyla değiştirmeyin.
3. Kendi deneyinizin bundle dosyasını, henüz var olmayan yeni bir klasöre açın:

```bash
git clone -b develop h9-deneyim/YAZ325_Hafta09_Gitflow_Deneyi.bundle h9-gecmis
git -C h9-gecmis log --graph --decorate --oneline --all
git -C h9-gecmis rev-parse HEAD
git -C h9-gecmis show HEAD:panel/surum.json
```

4. Açılan `HEAD` kimliğini kendi raporunuzun `commits.develop` değeriyle karşılaştırın. Panelin son içeriğini ve bundle dosyasının SHA-256 değerini aynı koşunun kaydıyla doğrulayın.
5. [Yerel örnek ile CI kanıtını](43-git-kanit-ve-izlenebilirlik.md) karşılaştırın. Yeniden üretilen geçmişlerin commit kimlikleri farklı olabilir; her dosyayı ait olduğu koşuyla eşleştirin.

## Teslim edilecek çıktı

Tarih, ortam, kaynak commit, çalıştırılan komutlar, sonuç dosyaları, bundle ve yeni klasörden yapılan kimlik/içerik doğrulaması.

## Çıktı kontrolü

- Bundle'dan açılan geçmiş kendi koşunuzun son commit'iyle eşleşir.
- Gitflow, panel ve klinik uygulama sonuçları ayrı kapsamda raporlanır.
- Otomatik kontroller insan incelemesi veya kullanıcı kabulü olarak yazılmaz.

22 Kasım 2026 örneğinde [Gitflow CI](https://github.com/pozelll/-klinik-randevu-ogretmen/actions/runs/45023202073) 12/12, son panel 6/6'dır. Tarihsel klinik koşu 30 Node, 14 kaynak tarayıcı, 8 paket ve pakette aynı 14 senaryoyu içerir. Klinik rc.2'nin sonraki ölçümleri [49 numaralı kayıtta](https://github.com/pozelll/-klinik-randevu-ogretmen/blob/main/hafta09/docs/49-kapanis-raporu.md) bulunur.

[Önceki adım](05-hotfix.md) · [Sonraki adım: Kalite kararı](07-karar.md)
