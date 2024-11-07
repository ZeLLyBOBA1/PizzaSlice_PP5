# homepage/adapters.py

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        email = form.cleaned_data.get('email')
        if email:
            username = email.split('@')[0]
            user.username = username
        return super().save_user(request, user, form, commit)
