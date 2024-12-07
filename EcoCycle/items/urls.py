from django.urls import path
from .views import create_delete_product, products_list, products_feed

urlpatterns = [
    path('add/', create_delete_product.create_product, name='create_product'),
    path('delete/<int:product_id>/', create_delete_product.delete_product, name='delete_product'),
    path('list/', products_list.products_list, name='products_list'),
    path('feed/', products_feed.products_feed, name='products_feed')
]
