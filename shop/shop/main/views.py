from django.shortcuts import render
from django.http import HttpResponse
from main.models import Product, Category, Busket, Busketitems


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {"products": products, "categories": categories})


def about(request):
    return render(request, 'about.html', {"name": "Dima"})

def detail(request, index):
    request.session['name'] = 'Ludwik'
    product = Product.objects.get(pk=index)
    if request.method == "POST":
        print(request.POST.get('product_count'))
        print(request.session._session_key)
        if not Busket.objects.filter(sessionid=request.session._session_key).exists():
            b = Busket()
            b.sessionid = request.session._session_key
            b.save()
        busket = Busket.objects.get(sessionid=request.session._session_key)
        bi = Busketitems()
        bi.basket = busket
        bi.product = product
        bi.count = request.POST.get('product_count')
        bi.save()
    return render(request, 'detail.html', {'object': product})