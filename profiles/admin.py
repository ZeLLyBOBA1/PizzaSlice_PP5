from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'address')
    search_fields = ('user__username', 'first_name', 'last_name', 'phone', 'address')
    list_filter = ('user',) 