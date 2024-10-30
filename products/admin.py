from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'price',)  # Поля, которые будут отображаться в списке
    search_fields = ('title', 'sku',)  # Поля для поиска в админке
    list_filter = ('category',)  # Фильтрация по категориям

admin.site.register(Product, ProductAdmin)