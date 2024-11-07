from django.shortcuts import render

# Create your views here.
def checkout(request):
    """ A view to return the index page """
    total_items = 2

    return render(request, 'checkout/cart.html', {'total_items': total_items,})