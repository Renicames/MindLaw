===============
Katkıda Bulunma
===============

Katkılarınızı bekliyoruz ve çok takdir ediyoruz! Küçük bir katkı bile büyük fark yaratır ve her zaman takdir edilecektir. Birçok farklı şekilde katkıda bulunabilirsiniz.

Katkı Türleri
-----------------

Hata Bildirme
~~~~~~~~~~~~~
Hataları https://github.com/Renicames/MindLaw/issues adresinden bildirebilirsiniz.

Bir hata bildiriyorsanız, lütfen şunları ekleyin:

* İşletim sistemi adınızı ve sürümünüzü.
* Sorunun giderilmesinde yardımcı olabilecek yerel ayarlarınızla ilgili ayrıntılar.
* Hatanın tekrarlanabilir olması için ayrıntılı adımlar.

Hataları Düzeltme
~~~~~~~~~~~~~
GitHub'daki issues kısmını inceleyerek hataları bulun. "bug" ve "help wanted" etiketli her şey, ilgilenmek isteyenler için açıktır.

Özellikler Ekleyin
~~~~~~~~~~~~~
GitHub issues kısmında yeni özellik isteklerini inceleyin. "enhancement" ve "help wanted" etiketli her şey, ilgilenmek isteyenler için açıktır.

Dokümantasyon Yazın
~~~~~~~~~~~~~
MindLaw projesi her zaman daha fazla dokümantasyondan faydalanabilir. Bu, resmi dokümantasyon, docstringler ve hatta web üzerindeki blog yazıları ve makaleleri içerebilir.

Geri Bildirimde Bulunun
~~~~~~~~~~~~~
En etkili geri bildirim sağlama yolu, MindLaw GitHub deposunda bir issue oluşturmaktır: https://github.com/Renicames/MindLaw/issues.

Yeni bir özellik önermek istiyorsanız:
- Özelliğin nasıl çalışacağını net bir şekilde açıklayın.
- Özelliğin kapsamını dar tutarak uygulanmasını kolaylaştırın.
- Unutmayın, bu gönüllülerin katkılarıyla sürdürülen bir projedir, bu nedenle katkılar her zaman memnuniyetle karşılanır.

Katkıda Bulunmaya Hazır mısınız?
---------------------------------
MindLaw için yerel geliştirme ortamını kurmak için aşağıdaki adımları izleyin:

1. GitHub'da `mindlaw` deposunu forkladıktan sonra:

    $ git clone https://github.com/Renicames/MindLaw.git

2. Yerel geliştirme için yeni bir dal oluşturun:

    $ git checkout -b dal-adi

   Bu, yerel değişikliklerinizi master dalını etkilemeden yapmanızı sağlar.

3. Gerekli değişiklikleri yapın ve bunları aşağıdaki komutlarla dalınıza commit edin:

    $ git add .
    $ git commit -m "Yaptığınız değişikliklerin detaylı açıklaması."

4. Değişiklikleri GitHub'daki forked repository'nize gönderin:

    $ git push origin dal-adi

5. Değişikliklerinizin gözden geçirilmesi ve ana depoya eklenmesi için GitHub üzerinden bir pull request gönderin.

Pull Request Yönergeleri
-------------------------

Bir pull request göndermeden önce, aşağıdaki yönergeleri karşıladığından emin olun:

1. Temel özellikleri değiştirirken, özel bir dal oluşturmanızı öneriyoruz. Bu, başkaları tarafından kolayca test edilebilir ve daha sonra **main** dalına entegre edilebilir.
   
2. Yeni bir özellik, işlev vb. ekliyorsanız, pull request göndermeden önce test vakaları yazmayı unutmayın.
   
3. Tüm testlerin her kod değişikliği için gerekli olmayabileceğini unutmayın.
   
4. Pull request yeni işlevsellik ekliyorsa, dokümantasyon güncellenmelidir. Yeni işlevsellik için docstring ekleyin ve gerekiyorsa dokümantasyonu güncelleyin. (Numpy-docstring stilini kullanın)

5. Pull request, Python 3.8 ile 3.10 arasındaki Python sürümleriyle uyumlu olmalıdır.
