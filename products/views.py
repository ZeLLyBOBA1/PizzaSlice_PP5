from django.shortcuts import render
from .models import Product

# Create your views here.
def products_list(request):
    """ A view to return the products page """
    products = Product.objects.all()  # Получаем все продукты
    return render(request, 'products/products_list.html', {'products': products})
