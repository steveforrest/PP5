from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.all_products, name='products'),
    path('order/product/<int:pk>/', views.identify_product, name='product'),
    path('order/product_search/', views.all_products, name='search_result'),
    path('add/', views.add_product, name='add_product'),
]