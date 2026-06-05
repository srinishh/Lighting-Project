'''
from django.shortcuts import render 

def home(request):
    return render(request, 'index.html')



from .models import Product

from django.shortcuts import render, get_object_or_404

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'product_detail.html', {'product': product})

def contact(request):
    return render(request, 'contactus.html')

from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'products': products,
        'categories': categories
    })


def category_products(request, category_name):

    category = get_object_or_404(Category, name=category_name)

    products = Product.objects.filter(category=category)

    categories = Category.objects.all()

    return render(request, 'index.html', {
        'products': products,
        'categories': categories
    })

def indoor(request):
    category = Category.objects.get(name="Indoor")
    products = Product.objects.filter(category=category)

    return render(request, 'indoor.html', {
        'products': products,
        'category': category
    })

def outdoor(request):
    category = Category.objects.get(name="Outdoor")
    products = Product.objects.filter(category=category)

    return render(request, 'outdoor.html', {
        'products': products,
        'category': category
    })



from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def indoor(request):
    return render(request, 'indoor.html')

def outdoor(request):
    return render(request, 'outdoor.html')

def poles(request):
    return render(request, 'poles.html')

'''
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def indoor(request):
    category = Category.objects.get(name='Indoor')
    products = Product.objects.filter(category=category)

    return render(request, 'indoor.html', {'products': products})


def outdoor(request):
    category = Category.objects.get(name='Outdoor')
    products = Product.objects.filter(category=category)

    return render(request, 'outdoor.html', {'products': products})


def poles(request):
    category = Category.objects.get(name='Poles')
    products = Product.objects.filter(category=category)

    return render(request, 'poles.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def contact(request):
    return render(request, 'contactus.html')