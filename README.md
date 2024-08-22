


# MindLaw - Türk Hukuku Üzerine Eğitilmiş T5 Tabanlı Chatbot

**MindLaw**, T5 modelinin Renicames tarafından geliştirilmiş 14,854 veriden oluşan bir veri setiyle eğitilerek hazırlanmış bir Yapay Zeka Danışmanlık Hizmeti (ChatBot) projesidir. Bu proje, kullanıcıların Türk hukuku ile ilgili sorularına doğru ve hızlı yanıtlar sunmayı amaçlamaktadır.

## Bu Projeye Katkıda Bulunma
Projemize katkıda bulunmak istiyorsanız, lütfen [CONTRIBUTING](https://github.com/Renicames/MindLaw/blob/main/CONTRIBUTING.rst) dosyasına göz atın.


## Projenin Amacı ve Motivasyonu

MindLaw, Türk hukuk sistemine dair doğru ve hızlı bilgiye erişim sağlamak amacıyla geliştirilmiştir. Türkiye’nin çeşitli hukuk kaynaklarından derlenen verilerle oluşturulan bu proje, kullanıcıların hukuki sorularına etkin çözümler sunmayı hedeflemektedir. Projede kullanılan veri seti, Renicames tarafından ülkemizde ilk kez açık kaynak olarak paylaşılan, Türk hukuku üzerine özel olarak hazırlanmış bir soru-cevap veri setidir. Bu veri seti, Türk Anayasası ve diğer yasal belgelerden derlenmiş olup, Türkiye'de hukuk alanında yapay zeka kullanımı için önemli bir adım teşkil etmektedir.


## Proje Arayüzü 
![image](https://github.com/user-attachments/assets/51c19e18-1c27-486b-88dd-132e0ce31998)


## Veri Seti Geliştirme Süreci

Veri setimizin geliştirilme süreci aşağıdaki adımları içermektedir:

1. **Araştırma**: Türk Anayasası, çeşitli hukuk siteleri ve diğer yasal belgeler kapsamlı bir şekilde incelenmiştir.
2. **Veri Toplama**: Resmi kaynaklardan hukuki veriler titizlikle toplanmıştır.
3. **Veri Temizleme**: Toplanan veriler, tekrar eden bilgilerden arındırılarak yapılandırılmıştır.
4. **Veri Seti Oluşturma**: Temizlenmiş veriler, modelin eğitimi için kullanılmak üzere JSON formatında bir veri setine dönüştürülmüştür. Veri setinde toplam 14,854 soru-cevap çifti bulunmaktadır.

Veri Setine erişmek için [buraya tıklayabilirsiniz](https://huggingface.co/datasets/Renicames/turkish-law-chatbot).

## Model Detayları

**Model Şeması**

![Model Şeması](https://github.com/user-attachments/assets/4d4f656a-ab96-4b8d-9c8d-84cdab56a7dc)

**Model Bilgisi**

Projede, T5 Base modeli kullanılmıştır ve bu model, hukuk veri seti ile eğitilerek özelleştirilmiştir.

## Performans Değerlendirmesi

Modelimizin performansı ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metrikleri ile değerlendirilmiştir. Aşağıdaki görselde, T5 Base modelinin ROUGE-1, ROUGE-2 ve ROUGE-L değerleri gösterilmektedir:

![ROUGE Değerleri](https://github.com/user-attachments/assets/ce2bcd85-f240-41e6-aed5-7cb833ebc1b0)

T5 Base modelinin parametre optimizasyonu sonuçları ise aşağıda verilmiştir:

![Parametre Optimizasyonu](https://github.com/user-attachments/assets/62656a8d-8626-458e-b1fd-396d258389c4)




## Kullanım

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
   ```sh
   git clone https://github.com/Renicames/MindLaw.git
   ```

2. Gerekli bağımlılıkları yükleyin:
   ```sh
   cd Mindlaw
   pip install -r requirements.txt
   ```

3. Chatbot'u başlatın:
   ```sh
   cd WebSite
   python mindlaw.py
   ```


## Youtube Linki

Projemizin tanıtım videosunu izlemek için [tıklayın.](https://youtu.be/zFq64Aul54U)




## Lisans

Bu proje Apache 2.0 Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

---


