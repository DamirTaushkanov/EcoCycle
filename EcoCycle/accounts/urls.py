from django.urls import path
from .views import get_profile, set_profile, get_locate, set_locate, register

urlpatterns = [
    path('register/', register.register),
    path('profile/', get_profile.get_profile),
    path('profile/set/', set_profile.set_profile),
    path('locate/', get_locate.get_locate),
    path('locate/set/', set_locate.set_locate)
]