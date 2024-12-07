from django.urls import path
from . import views   # views.py'yi import ediyoruz

urlpatterns = [

    path('login/', views.login_view, name='login'), #login sayfasına yönlendirir
    path('', views.index, name='index'),  # Ana sayfa URL'si
    path('singup/', views.signup_view, name='singup'),  # singup sayfasına yönlendirir

    path('', views.book_list, name='book_list'),   # Ana URL, kitap listesini gösterir
]
