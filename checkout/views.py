from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

# Create your views here.
def checkout(request):
    """ A view to return the index page """
    return render(request, 'checkout/cart.html',)
