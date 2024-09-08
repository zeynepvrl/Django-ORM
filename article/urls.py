from django.urls import path,include
from . import views      # . bu dizinden bir şey ekleyeceğini belirtiyor

app_name="article"

urlpatterns=[
    path('create/', views.index , name='index')
]