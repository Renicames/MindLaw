# MindLaw - Türk Hukuku Üzerine Eğitilmiş T5 Tabalı Chatbot

MindLaw, T5 modelinin kendi geliştirmiş olduğumuz veri seti ile eğitilerek Türk hukuku üzerine özelleştirilmiş bir  Yapay Zeka Danışmanlık Hizmeti (ChatBot) projesidir. Bu proje, kullanıcıların Türk hukuku ile ilgili sorularına doğru ve hızlı yanıtlar vermeyi amaçlamaktadır. Bu projede kullanılan veri seti Renicames tarafından ülkemizde ilk kez açık kaynaklı olarak paylaşılan hukuk soru-cevap veri setidir. 

## Projenin Motivasyonu

Türk hukuk sistemine ilişkin doğru bilgiye hızlı erişim sağlamak amacıyla bu projeyi geliştirdik. Projemiz, Türkiye'nin çeşitli hukuk kaynaklarından elde edilen verilerle oluşturulmuştur. Veri seti, Türk Anayasası ve diğer yasal belgelerden derlenmiştir. Bu kapsamlı veri seti, Türk hukuku üzerine daha önce açık kaynak olarak mevcut olmayan bir veri setini sunmaktadır. Bu anlamda bir ilk olan veri setimiz, ülkemizde hukuk alanında yapay zekanın kullanılması yönünde atılan bir adımdır.

## Veri Setinin Oluşum Süreci

Veri setimizin oluşturulması süreci aşağıdaki adımları içermektedir:

1. **Araştırma**: Türk Anayasası, çeşitli hukuk siteleri ve diğer yasal belgeler araştırıldı.
2. **Veri Kazıma**: Hukuk forumları ve resmi hukuk sitelerinden veriler kazınarak toplandı.
3. **Veri Toplama**: Resmi sitelerde bulunan pdflerdeki veriler toplandı.
4. **Veri Temizleme**: Toplanan verilerden tekrar niteliğinde olan bilgiler temizlendi ve yapılandırıldı.
5. **Veri Seti Oluşturma**: Temizlenmiş veriler, modelin eğitimi için kullanılacak json formatında bir veri setine dönüştürüldü.

**Veri Seti Bağlantısı ->** https://huggingface.co/datasets/Renicames/turkish-law-chatbot


## Modelin Detayları

**Model Şeması**

![image](https://github.com/user-attachments/assets/4d4f656a-ab96-4b8d-9c8d-84cdab56a7dc)




***Model**
Projede, T5 Base modeli kullanılmıştır.

## ROUGE Değerleri

Modelimizin performansını ROUGE (Recall-Oriented Understudy for Gisting Evaluation) metrikleri ile değerlendirdik. Aşağıdaki görselde T5 Modellerinin ROUGE-1, ROUGE-2 ve ROUGE-L değerleri verilmiştir :

![image](https://github.com/user-attachments/assets/ce2bcd85-f240-41e6-aed5-7cb833ebc1b0)

T5 Base modeli parametre optimizasyonu skorları aşağıda verilmiştir :

![image](https://github.com/user-attachments/assets/62656a8d-8626-458e-b1fd-396d258389c4)






## Kullanım

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi klonlayın:
   ```sh
   git clone https://github.com/Renicames/MindLaw.git
   ```

2. Gerekli bağımlılıkları yükleyin:
   ```sh
   pip install -r requirements.txt
   ```

3. Chatbot'u başlatın:
   ```sh
   python run_chatbot.py
   ```
## Hugging Face Üzerinde Modeli Kullanma
 
https://huggingface.co/spaces/Renicames/MindLaw_Interface

## Youtube Linki

https://youtu.be/zFq64Aul54U


## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakabilirsiniz.

---


