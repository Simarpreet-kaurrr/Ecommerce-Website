# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='ShopAbout'),
    path('tracker/', views.tracker, name='ShopTracker'),
    path('contact/', views.contact, name='ShopContact'),
    path('checkout/', views.checkout, name='ShopCheckout'),
    path("productview<int:myid>/", views.productview, name='productview'),
]


