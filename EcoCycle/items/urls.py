from django.urls import path
from .views import create_delete_product, products_list, products_feed, get_product

urlpatterns = [
    path('add/', create_delete_product.create_product, name='create_product'),
    path('delete/', create_delete_product.delete_product, name='delete_product'),
    path('list/', products_list.products_list, name='products_list'),
    path('feed/', products_feed.products_feed, name='products_feed'),
    path('get/', get_product.get_product, name='get_product')
]
