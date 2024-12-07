from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from items.models import Products

@api_view(['GET'])
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