from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):          #bu article ı kayıt etmen gerekiyor admin.py den
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)  #django ile hazır gelen Users tablosunu burda kullnadık referans aldık, ondelete->o o user silinirse diğer her şeyi veritabanından silinecek
    title=models.CharField(max_length=50) 
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True)     #verbose_name ile bu alanların admin panelindeki ismini değiştirebilirsin

    #article tablosunda article ların article1 2 gibi sıralanmasını değil de başlıkları ile sıralanmasının istersem;
    def __str__(self):
        return self.title
