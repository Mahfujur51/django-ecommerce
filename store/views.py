from multiprocessing import context
from django.shortcuts import render

from django.views.generic import ListView

from store.models import Product

class HomeView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name='products'
    
    
def product_details(request,pk):
    item = Product.objects.get(id=pk)
    context={
        'item':item
    }
    return render(request,'shop/product.html',context)


# # Create your views here.
# def Store(reuquest):
#     return render(reuquest,'shop/index.html')
