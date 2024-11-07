
from django.contrib import admin
from django.urls import path
from . import views
from .views import delete_account, update_profile, profile_view

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('delete-account/', delete_account, name='delete_account'),
    path('profile/update/', update_profile, name='profile_update'),
]
