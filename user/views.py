from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm    # .user da yazılabilir
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

def register(request):
        form = RegisterForm(request.POST or None)     #post edilen formdaki bilgilerle doldurulmuş form nesnesi, post request yoksa boş form-> get requesti yani
        if form.is_valid():               #is_valid() register formda oluşturduğumuz clean methodunu çağırır, get req de form valid olmadığı için bu bloğa girmaz
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")       #bu aldığımız bilgilerle user modelinden bir obje oluşturup kaydetmemiz gerekiyor. user modeli django da hazır vardu yukarıda import ediyoruz

            newuser= User(username=username)
            newuser.set_password(password)
            newuser.save()                       
            login(request, newuser)
            messages.success(request, "Başarıyla giriş yaptınız")
            return redirect("index")        #urls.py belirlediğimiz isimlerden baz alarak
        
        context={
            "form":form
        }
        return render(request, 'register.html', context) 

def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
         "form":form
    }
    if form.is_valid():
         username=form.cleaned_data.get("username")
         password=form.cleaned_data.get("password")
         user =authenticate(username=username , password=password)
         if user ==None:
              messages.info(request, "Kullanıcı adı veya şifre hatalı")
              return render(request, "login.html", context)
         
         messages.success(request, "Başarı ile giriş yaptınız")
         login(request,user)
         return render(request, "index.html")
    
    return render(request, "login.html", context)

def logout(request):
    pass