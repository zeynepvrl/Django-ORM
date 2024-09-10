from django.urls import path,include
from . import views      # . bu dizinden bir şey ekleyeceğini belirtiyor

app_name="article"

urlpatterns=[
    path('dashboard/', views.dashboard , name='dashboard'),
    path('addarticle/', views.addArticle, name="addarticle"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.ArticleUpdate, name="ArticleUpdate"),
    path('delete/<int:id>', views.ArticleDelete, name="ArticleDelete"),
    path('', views.articles, name="articles"),
]



