from django.shortcuts import render,redirect
from .forms import RegisterForm    # .user da yazılabilir
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST) or None    #post edilen formdaki bilgilerle doldurulmuş form nesnesi, post request yoksa boş form-> get requesti yani
        if form.is_valid():               #is_valid() register formda oluşturduğumuz clean methodunu çağırır, get req de form valid olmadığı için bu bloğa girmaz
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")       #bu aldığımız bilgilerle user modelinden bir obje oluşturup kaydetmemiz gerekiyor. user modeli django da hazır vardu yukarıda import ediyoruz

            newuser= User(username=username)
            newuser.set_password(password)
            newuser.save()                       #bu model oluşturma işlemlerini djangonun sağladığı shell den de yabilabiliyor
            login(request)
            return redirect("index")        #urls.py belirlediğimiz isimlerden baz alarak
        
        context={
            "form":form
        }
        return render(request, 'register.html', context) 

def login(request):

    return render(request, 'login.html')

def logout(request):
    pass