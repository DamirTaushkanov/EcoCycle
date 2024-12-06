from django.urls import path
from items.views import create_product_web, delete_product_web, products_list_web, products_feed_web

urlpatterns = [
    path('list/', products_list_web, name='products_list'),
    path('add/', create_product_web, name='create_product'),
    path('delete/', delete_product_web, name='delete_product'),
    path('feed/', products_feed_web, name='products_feed')
]
