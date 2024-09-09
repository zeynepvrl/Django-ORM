from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
# Create your views here.
def index(request):
    return render(request, "index.html")     #setting.py de templates klasörünün yeri belirtildi, oraya bakacak

def about(request):
    return render(request, "about.html")

def dashboard(request):
    articles= Article.objects.filter(author= request.user)
    context={
        "articles":articles
    }
    return render(request, "dashboard.html", context)

def addArticle(request):
    form=ArticleForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        article= form.save(commit=False)   #kaydet ama veritabanına sen gönderme ben user ını da ekleyip kendim göndericem demek
        article.author=request.user
        article.save()      #kendimiz commit ediyoruz yani kaydediyoruz veritabanına
        messages.success(request, "Makale Başarı ile yüklendi")
        return redirect("index")
    return render(request, "addarticle.html", {"form":form})

def detail(request, id):
    #article=Article.objects.filter(id=id).first()   #gördüğü ilk article döndür demek için, first yazmazsak bir obje döndürüyor query set döndürüyor
    article=get_object_or_404(Article, id=id )
    return render(request, "detail.html", {"article":article})
