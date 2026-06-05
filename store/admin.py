'''
from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

'''
from django.contrib import admin
from .models import Product

admin.site.register(Product)
