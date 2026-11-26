# 9. hafta / 5. adım - Hotfix'i iki dala taşı

Öğrenci çalışma yönergesi · Güncelleme: 26 Kasım 2026.

## Amaç

Düzeltmeyi teslim dalına ve sonraki sürümün geliştirme dalına taşıyın. Hem commit geçmişini hem hedeflerdeki son içeriği kontrol edin.

## Grup çalışması

1. [Hotfix kaydındaki](42-hotfix-ve-senkronizasyon.md) kontrollü iptal açıklaması kusurunu inceleyin. Depo kökünden aşağıdaki üç kontrolü ayrı ayrı çalıştırıp gerçek sonuçlarını kaydedin.

```bash
python hafta09/tools/surum_kontrol.py hafta09/senaryolar/04-release.json
python hafta09/tools/surum_kontrol.py hafta09/senaryolar/04-release.json --anlam
python hafta09/tools/surum_kontrol.py hafta09/senaryolar/05-hotfix.json --anlam
```

2. Örnekte ilk kontrol 5/5; anlam denetimi eklenen ikinci kontrol 5/6 FAIL; düzeltilmiş girdi 6/6 sonucunu verir. İkinci komutun `1` çıkışı, kontrollü kusurun reddedilmesidir. P01–P05 yapısal kontrollerini ve A01'in denetlediği belirli gereksinimi rapora yazın.
3. Deney deposunda düzeltmenin her iki hedefin geçmişinde bulunduğunu ve son panel içeriklerinin eşit olduğunu kontrol edin.

```bash
git -C h9-deneyim/lab-deposu merge-base --is-ancestor hotfix/0.9.1 main
git -C h9-deneyim/lab-deposu merge-base --is-ancestor hotfix/0.9.1 develop
git -C h9-deneyim/lab-deposu diff --exit-code main develop -- panel/surum.json
```

4. Her iki hedefte `panel/surum.json` dosyasını ayrıca inceleyin. H9-G09 sonucundaki çıkış kodlarını ve içerik denetimini kaydedin.
5. H9-G10 kaydında yeni `egitim-hafta09-v0.9.1` etiketinin hedefini ve eski `egitim-hafta09-v0.9.0` etiketinin korunmasını doğrulayın. Kendi düzeltmenizin gerekçesini, iki hedefini ve kontrol sonuçlarını yazın.

## Teslim edilecek çıktı

Hotfix gerekçesi, düzeltme commit'i, iki hedef için atalık ve içerik kontrolü, yeni etiket hedefi ve eski etiketin değişmediğini gösteren kayıt.

## Çıktı kontrolü

- İki atalık komutu ve içerik karşılaştırması `0` çıkışı verir.
- Son içerikte düzeltme korunur.
- Eski etiketin hedefi değişmemiştir.

[Önceki adım](04-release.md) · [Sonraki adım: Kanıtı yeniden üretme](06-kanit.md)
