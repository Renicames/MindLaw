# MindLaw - Türk Hukuku Üzerine Eğitilmiş T5 Tabalı Chatbot

MindLaw, T5 modeli kullanılarak Türk hukuku üzerine eğitilmiş bir chatbot projesidir. Bu proje, kullanıcıların Türk hukuku ile ilgili sorularına doğru ve hızlı yanıtlar vermeyi amaçlamaktadır. Bu projede kullanılan veri seti Renicames tarafından Türkiye'de ilk geliştirilen hukuk soru-cevap veri setidir. 

## Projenin Motivasyonu

Türk hukuk sistemine ilişkin doğru bilgiye hızlı erişim sağlamak amacıyla bu projeyi geliştirdik. Projemiz, Türkiye'nin çeşitli hukuk kaynaklarından elde edilen verilerle oluşturulmuştur. Veri seti, Türk Anayasası ve diğer yasal belgelerden derlenmiştir. Bu kapsamlı veri seti, Türk hukuku üzerine daha önce açık kaynak olarak mevcut olmayan bir veri setini sunmaktadır. Bu anlamda bir ilk olan veri setimiz, ülkemizde hukuk alanında yapay zekanın kullanılması yönünde atılan bir adımdır.

## Veri Setinin Oluşum Süreci

Veri setimizin oluşturulması süreci aşağıdaki adımları içermektedir:

1. **Araştırma**: Türk Anayasası, çeşitli hukuk siteleri ve diğer yasal belgeler araştırıldı.
2. **Veri Kazıma**: Hukuk forumları ve resmi hukuk sitelerinden veriler kazınarak toplandı.
2. **Veri Toplama**: Resmi sitelerde bulunan pdflerdeki veriler toplandı.
4. **Veri Temizleme**: Toplanan verilerden tekrar niteliğinde olan bilgiler temizlendi ve yapılandırıldı.
5. **Veri Seti Oluşturma**: Temizlenmiş veriler, modelin eğitimi için kullanılacak json formatında bir veri setine dönüştürüldü.

![Veri Seti Bağlantısı](https://user-images.githubusercontent.com/your-data-process-image.png)

## Modelin Detayları

Proje iki ana bileşenden oluşur: image encoder ve text decoder. Image encoder, verilen resmi 512 uzunluğunda bir vektöre dönüştürür. Bu vektör, resimdeki önemli detayları içerir. Oluşturulan bu vektör, text decoder'a verilmek üzere başka bir model tarafından genişletilir. Text decoder modeli, bu vektöre bakarak yeni bir metin oluşturur. Bu metin, modelin resimde gördüklerini ifade eder.

| ![Model Schema](https://user-images.githubusercontent.com/your-model-schema.png) |
|:--:|
| Model Şeması |

Projede, Türkçe verilerle eğitilmiş GPT-2 modeli kullanılmıştır. Image encoder olarak OpenAI'ın CLIP modeli kullanılmıştır.

## ROUGE Değerleri

Modelimizin performansını ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metrikleri ile değerlendirdik. Aşağıdaki görselde ROUGE-1, ROUGE-2 ve ROUGE-L değerlerini görebilirsiniz:

![ROUGE Değerleri](https://user-images.githubusercontent.com/your-rouge-image.png)

## Kullanım

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
   ```sh
   git clone https://github.com/kullanici-adi/mindlaw.git
   ```

2. Gerekli bağımlılıkları yükleyin:
   ```sh
   cd mindlaw
   pip install -r requirements.txt
   ```

3. Chatbot'u başlatın:
   ```sh
   python run_chatbot.py
   ```
## Web Sitesi

Projemizin web sitesini aşağıdaki görselden inceleyebilirsiniz:

![Web Sitesi](https://user-images.githubusercontent.com/your-website-image.png)

## Gelecek Hedefler

1. Veriyi genişletmek.
2. Modelin videoları daha iyi anlaması için video encoder modeli kullanmak.
3. Projenin mobil uygulama olarak kullanılabilir hale getirilmesi.
4. Giyilebilir teknoloji ile projeyi hayata geçirmek.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

---

Bu proje, Türk hukuk sistemine ilişkin doğru bilgiye hızlı erişim sağlamak amacıyla geliştirilmiştir. Umarız ki hukuk öğrencileri, avukatlar ve hukuka ilgi duyan herkes için faydalı olur.
