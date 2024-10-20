# homepage/adapters.py

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # Получаем email из формы
        email = form.cleaned_data.get('email')
        if email:
            # Извлекаем username из email
            username = email.split('@')[0]
            user.username = username  # Устанавливаем username
        return super().save_user(request, user, form, commit)
