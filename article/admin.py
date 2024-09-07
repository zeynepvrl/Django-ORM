from django.contrib import admin
from .models import Article

# Register your models here.
#admin.site.register(Article)  admin panelini özelleştirmek için bu işlemi dekorator olarak yazıcaz. Decorator her zzaman fonksiyonlar için kullanılmaz class için de kullanılır

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title", "author", "created_date"]
    list_display_links=["title", "created_date"]
    search_fields=["title"]
    list_filter=["created_date"]
    class Meta:
        model=Article

""" Bu kod, Django yönetici panelinde (admin panel) Article modelini özelleştirilmiş bir şekilde yönetebilmek için kaydeder.
ArticleAdmin sınıfı, admin.ModelAdmin sınıfından türetilmiş olup, Meta iç sınıfında belirtilen model=Article satırı,
bu özel yönetim sınıfının Article modeline ait olduğunu belirtir. @admin.register(Article) dekoratörü ise,
Article modelini ArticleAdmin sınıfı ile birlikte yönetici paneline kaydeder.
Sonuç olarak, bu kod Article modelini Django yönetici panelinde yönetmek için özelleştirilmiş bir görünüm sağlar. """