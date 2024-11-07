from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'price',)
    search_fields = ('title', 'sku',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)