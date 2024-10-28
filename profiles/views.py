from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages

# Create your views here.
def profile(request):
    """ A view to return the index page """
    return render(request, 'profiles/profile.html')

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('index') 
    return redirect('profile')  

@login_required
def update_profile(request):
    profile = request.user.profile  # Получаем профиль текущего пользователя

    if request.method == 'POST':
        # Извлекаем данные из формы
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Обновляем профиль
        profile.first_name = first_name
        profile.last_name = last_name
        profile.phone = phone
        profile.address = address
        profile.save()  # Сохраняем изменения

        return redirect('profile')  # Перенаправляем на страницу профиля

    return render(request, 'profile_update.html', {'profile': profile})
