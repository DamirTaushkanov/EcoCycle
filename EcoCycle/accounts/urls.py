from django.urls import path
from .views import profile_view, set_locate

urlpatterns = [
    path('profile/', profile_view),  # URL для аутентификации allauth
    path('locate/', set_locate),
]