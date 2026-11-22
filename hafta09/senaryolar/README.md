# Kontrollü Gitflow senaryosu girdileri

00–04 dosyalarındaki “İptal edilen randevu listeden silinir” cümlesi, mevcut Drive Gitflow rehberinden alınan **bilerek yanlış senaryo girdisidir**. Gerçek Klinik uygulamasının iptal davranışı değildir. 05-hotfix bu cümleyi düzeltir. Bu dosyaları gerçek uygulamanın src/ dosyalarıyla değiştirmeyin.

İki feature ortak başlangıçtaki duyuru satırını farklı değiştirdiği için gerçek bir Git çakışması oluşur. Çözüm dosyası her iki katkının anlamını korur. Beş JSON kontrolünün geçmesi cümlenin doğru olduğunu kanıtlamaz; sonradan eklenen A01 anlam kapısı yanlış sürümü reddeder.

Sürümler 0.9.0-dev, 0.9.0 ve 0.9.1 panel laboratuvarına aittir. Klinik uygulamanın 0.3.0-rc.1 adayıyla aynı sürüm değildir. Yerel eğitim etiketleri nihai yayın veya gerçek akran incelemesi anlamına gelmez.
