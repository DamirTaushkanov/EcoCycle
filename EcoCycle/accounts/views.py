import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from accounts.models import Profile, Locate
from accounts.forms import ProfileForm

@login_required
def profile_view(request):
    # Получаем или создаем профиль для пользователя
    profile = Profile.objects.get_or_create(user_id=request.user)[0]

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Используем edit_profile для сохранения данных
            data = form.cleaned_data
            data['profile_pic'] = request.FILES.get('profile_pic')  # Обработка файла отдельно
            if data:
                for field, value in data.items():
                    if hasattr(profile, field):
                        setattr(profile, field, value)
                profile.save()
                profile.refresh_from_db()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)  # Инициализируем форму текущими данными профиля
        print(form.errors)
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})

@csrf_exempt
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
