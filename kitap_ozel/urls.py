from django.urls import path
from . import views   # views.py'yi import ediyoruz

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa URL'si

    path('', views.book_list, name='book_list'),   # Ana URL, kitap listesini gösterir
]
