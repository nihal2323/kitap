from django.urls import path
from . import views   # views.py'yi import ediyoruz
from kitap_ozel.views import LoginView, SignupView
from .views import register_view





urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa URL'si
    path('login/', views.login_view, name='login'),
    path('login/', views.custom_login, name='login'),  # Giriş URL'si

    path('cart/', views.cart_view, name='cart'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),  # Kayıt olma sayfası
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('user_dashboard/', views.user_dashboard_view, name='user_dashboard'),
   # path('staff_dashboard/', views.staff_dashboard_view, name='staff_dashboard'),
    path('staff_login/', views.staff_login, name='staff_login'),  # URL'yi doğru şekilde tanımla

    #path('login/register.html', views.register_view, name='register'),

    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Ürün ekleme
    #path('update_cart/<int:product_id>/<str:action>/', views.update_cart, name='update_cart'),  # Sepet güncelleme






    #path('login/', LoginView.as_view(), name='login'),

    #path('signup/', SignupView.as_view(), name='signup'),

    #path('', views.book_list, name='book_list'),   # Ana URL, kitap listesini gösterir
]
