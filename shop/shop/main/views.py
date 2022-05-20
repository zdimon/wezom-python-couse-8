from django.shortcuts import redirect, render
from django.http import HttpResponse
from main.models import Product, Category, Busket, Busketitems
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as quit
from main.models import Profile
from django.core.paginator import Paginator
from django.utils.translation import gettext as _
from django.utils import translation

def index(request):
    translation.activate('en')
    request.LANGUAGE_CODE = translation.get_language()
    welcome = _('Hello my friend!')
    page_number = request.GET.get('page',1)
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    categories = Category.objects.all()
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {"page_obj": page_obj, "categories": categories, 'welcome': welcome})

def filter(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'index.html', {"page_obj": page_obj, "categories": categories})

def signin(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'welcome.html')
        else:
            messages.add_message(request, messages.ERROR, 'Login or password is invalid!!!')
            return redirect('/')        
    
def logout(request):
    quit(request)
    messages.add_message(request, messages.ERROR, 'Goodbuy')
    return redirect('/')   

def registration(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        phone = request.POST['phone']
        p = Profile()
        p.phone = phone
        p.username = username
        p.set_password(password)
        p.is_active = True
        p.is_superuser = True
        p.save()
        messages.add_message(request, messages.ERROR, 'Thank you!!!')
        return redirect('/')
    return render(request, 'registration.html')

def profile(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        profile = request.user.profile
        profile.phone = phone
        profile.save()
        messages.add_message(request, messages.ERROR, 'Your data was saved')
    return render(request, 'profile.html')

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