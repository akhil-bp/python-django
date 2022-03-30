from django.shortcuts import render
from django.http import HttpResponse
# to import product model
from .models import Product

# Create your views here.


def index(request):
    return HttpResponse("<h1>Products</h1>")


def about(request):
    return HttpResponse("<h1>Products / about</h1>")


def contact(request):
    return HttpResponse("<h1>Contact page works</h1>")


def detail(request):
    return HttpResponse("<h1>Detail page works</h1>")


def listAll(request):
    products = Product.objects.all()
    # products= Product.objects.filter()
    # products= Product.objects.get()
    # products= Product.objects.save()
    return render(request, 'index.html', {'products': products})
    # 'products' is dictionary
