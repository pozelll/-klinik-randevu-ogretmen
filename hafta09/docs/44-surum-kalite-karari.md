# 44 - Sürüm kalite kararı

**Karar: Klinik 0.3.0-rc.1 için nihai yayını BEKLET.** H9 eğitim materyali hazırlanmıştır; bu karar dersin yapılamayacağı anlamına gelmez. Karar sahibi ve bağımsız kabul edecek kişi henüz kaydedilmemiştir.

| Kalite kapısı | Kanıt / aynı sürümle ilişki | Durum |
|---|---|---|
| İşlevsel regresyon | H9 PR kaynağında 30 Node ve 14 tarayıcı; uygulama H8 ile aynı | Başarılı |
| Paket bütünlüğü ve davranış | Mevcut 0.3.0-rc.1 ZIP; 8 paket + 14 paket tarayıcı | Başarılı |
| H9 süreç/panel | Ayrı 0.9.x laboratuvarı; 12 Git + 6 panel | Başarılı, klinik kalite yerine geçmez |
| Bağımsız insan incelemesi | PR zinciri açık; gerçek yazar dışı değerlendirme kaydı yok | Bekliyor |
| NFR-01 kullanılabilirlik | Kullanıcı görev/başarı ölçümü | Ölçülmedi |
| NFR-02 yanıt süresi | Aynı aday ve tanımlı ortamda ham zaman ölçümleri | Ölçülmedi |
| NFR-03 klavye | Görev ve odak sırası üzerinden gerçek kontrol | Ölçülmedi |
| Performans ve ölçek | Planın yük, p95, hata, iş hacmi ve toparlanma deneyi | Kanıt yok |
| Alıcı kabulü | Öğrencinin erişimi, çalıştırması ve kabul sonucu | Derste doğrulanacak |

Klinik paket SHA-256: `36822b44675d5df7d1613f9605f907e18fe3656cc74b64e614d19c277bde2dc5`. Ayrı bir performans veya kullanılabilirlik çalışması farklı commit üzerinde yapılırsa sonucu bu adaya doğrudan taşımayın; farkı inceleyip ilgili kontrolleri tekrarlayın.

Bir sonraki iş: gereksinimlerdeki kabul eşiklerini doğrula; uygun ortam/veri/iş yüküyle ölç; ham sonuç ve hesapları sakla; değişiklik gerekirse aynı adayı yeniden test et; bağımsız inceleme ve alıcı kabulü sonrasında kararı yenile. Kişi/süre ataması yapılmadı.

Güncel uygulama tek tarayıcıdaki yerel örnektir. Sunucu yükü veya çok kullanıcılı eşzamanlılık ölçülmüş gibi sunulamaz. Önce ölçüm sorusunu ve bu mimaride anlamlı deneyi seçin; sunucu ölçeği gerekiyorsa ayrı mimari ve deney çalışması planlayın.
