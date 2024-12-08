from django.urls import path
from .views import send_offer

urlpatterns = [
    path('send/', send_offer.send_offer, name='send_offer')
]
