from django.contrib import admin
from django.urls import path
from my_app import views  # Import your app views here
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home', views.car_accessories_shop, name='car_accessories_shop'),  # Home page URL
    path('products/', views.products, name='products'),
    path('shop_products/', views.shop_products, name='shop_products'),  # Shop Products URL
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('special_offers/', views.special_offers, name='special_offers'),
]



