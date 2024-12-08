import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from accounts.models import Profile, Locate
from accounts.forms import ProfileForm

def set_locate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude and longitude and request.user.is_authenticated:
            locate, created = Locate.objects.update_or_create(
                user=request.user,  # Поиск или создание записи по пользователю
                defaults={'latitude': latitude, 'longitude': longitude}
            )

            if created:
                message = 'Location created successfully!'
            else:
                message = 'Location updated successfully!'

            return JsonResponse({'message': message})
        return JsonResponse({'message': 'Invalid data or unauthorized'}, status=400)
    return render(request, 'accounts/locate.html')
