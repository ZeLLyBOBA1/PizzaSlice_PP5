from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.db.models import Q

# Create your views here.
def products_list(request):
    """ A view to return the products page """
    products = Product.objects.all() 
    query = None 
    categories = None
    sort_by = None
    
    if request.GET:
        if 'sort' in request.GET:
            sort_by = request.GET.get('sort', 'price')
            if sort_by not in ['price', '-price']:
                sort_by = 'price'
            products = Product.objects.all().order_by(sort_by)  

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products_list'))

            queries = Q(title__icontains=query) |  Q(description__icontains=query) |  Q(sku__icontains=query)
            products = products.filter(queries)
        
    return render(request, 'products/products_list.html', {'products': products,'search_term': query, 'current_categories': categories, 'sort_by': sort_by, })
