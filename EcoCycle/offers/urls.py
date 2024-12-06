from django.urls import path
from offers.views import create_offer_web

urlpatterns = [
    path('trade/', create_offer_web, name='send_trade'),
]
