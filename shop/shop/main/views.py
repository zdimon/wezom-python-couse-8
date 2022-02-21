from django.shortcuts import render
from django.http import HttpResponse
from main.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products": products})


def about(request):
    return render(request, 'about.html', {"name": "Dima"})