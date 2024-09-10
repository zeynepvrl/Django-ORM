from django.shortcuts import render, redirect, HttpResponse, get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "index.html")     #setting.py de templates klasörünün yeri belirtildi, oraya bakacak

def about(request):
    return render(request, "about.html")

@login_required
def dashboard(request):
    articles= Article.objects.filter(author= request.user)
    context={
        "articles":articles
    }
    return render(request, "dashboard.html", context)

@login_required
def addArticle(request):
    form=ArticleForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        article= form.save(commit=False)   #kaydet ama veritabanına sen gönderme ben user ını da ekleyip kendim göndericem demek
        article.author=request.user
        article.save()      #kendimiz commit ediyoruz yani kaydediyoruz veritabanına
        messages.success(request, "Makale Başarı ile yüklendi")
        return redirect("index")
 
    return render(request, "addarticle.html", {"form":form})
@login_required
def detail(request, id):
    #article=Article.objects.filter(id=id).first()   #gördüğü ilk article döndür demek için, first yazmazsak bir obje döndürüyor query set döndürüyor
    article=get_object_or_404(Article, id=id )
    comments=article.comments.all()
    return render(request, "detail.html", {"article":article , "comments":comments})

@login_required
def ArticleUpdate(request, id):     
    article=get_object_or_404(Article, id=id)
    form=ArticleForm(request.POST or None, request.FILES or None, instance=article)  #post ise ilk ikisi kullanılacak get ise 3.

    if form.is_valid():      #get requestte yukardaki form boş oluşturulacağı için valid olmaz ve bu bloc atlanır
        form.save()
        messages.success(request, "Makale Başarı ile güncellendi")
        return redirect("article:detail", id=id)  # Detay sayfasına yönlendir
    return render(request, "update.html", {"form":form} )

@login_required
def ArticleDelete(reqest, id):
    article=get_object_or_404(Article, id=id)
    article.delete()
    messages.info(reqest, "Silme işlemi başarılı")
    return redirect("article:dashboard")

def articles(request):         #bu fonksiyon iki farklı get requestinde çalışacal
    keyword=request.GET.get('keyword')     #arama çubuğuna basıldığında gönderilen GET requesti bu keyword ü taşır
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles":articles})
    articles=Article.objects.all()
    return render(request, "articles.html", {"articles":articles})

def addComment(request,id):
    article=get_object_or_404(Article, id=id)
    if request.method=="POST":
        comment_author=request.POST.get('comment_author')
        comment_content=request.POST.get('comment_content')

        newComment=Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article=article

        newComment.save()
        return redirect(reverse("article:detail", kwargs={"id":id}))   #dinamik bir url redirct ederken reverse fonksiyonu kullanılmalı
        #return redirect("/article/detail/"+ str(id))

