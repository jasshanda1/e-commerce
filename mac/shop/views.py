from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products,"namo")
    n = len(products)
    nslides = n//4 + round((n/4)+(n//4))
    params ={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    return render(request,'shop/index.html',params)


def about(request):
    return render(request,'shop/about.html')    

def contact(request):
    return render(request,'shop/index.html')

def tracker(request):
    return render(request,'shop/index.html')


def search(request):
    return render(request,'shop/index.html')

def prodView(request):
    return render(request,'shop/index.html')

def checkout(request):
    return render(request,'shop/index.html')

              