from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")     #setting.py de templates klasörünün yeri belirtildi, oraya bakacak

def about(request):
    return render(request, "about.html")
