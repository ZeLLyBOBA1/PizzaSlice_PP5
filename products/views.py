from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def products_list(request):
    """ A view to return the products page """
    sort_by = request.GET.get('sort', 'price')  

    if sort_by not in ['price', '-price', 'category']:
        sort_by = 'price' 

    products = Product.objects.all().order_by(sort_by)  
    return render(request, 'products/products_list.html', {'products': products, 'sort_by': sort_by})
