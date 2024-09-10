from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):          #bu article ı kayıt etmen gerekiyor admin.py den
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)  #django ile hazır gelen Users tablosunu burda kullnadık referans aldık, ondelete->o o user silinirse diğer her şeyi veritabanından silinecek
    title=models.CharField(max_length=50) 
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)     #verbose_name ile bu alanların admin panelindeki ismini değiştirebilirsin
    article_image = models.FileField(blank=True, null=True, verbose_name="Görsel ekleyin")   # Article modelinde değişiklik yaptığımızı bildirmek için pythonmanage.py makemigrations ve sonra yine " " migrate 
                                    #bunları eklemezsem cleanup gücelleme sırasında görsel ekleme yerine temizle seçeneği geitrmez
    #article tablosunda article ların article1 2 gibi sıralanmasını değil de başlıkları ile sıralanmasının istersem;
    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created_date']

class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")   #article.comments deyince commentlerşne de ulaşılbilmeyi sağlıyor
    comment_author=models.CharField(max_length=50, verbose_name="İsim")
    comment_content=models.CharField(max_length=200, verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)
#admin.py de model in içine bunu dahil edeceğiz şimdi
#terminelden migrations ve migrate komutları
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering=["comment_date"]          #modeli değiştirdiğimiz için yine migrateion vs işlemlerini yapman lazım
