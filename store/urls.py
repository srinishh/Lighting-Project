from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
   ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('product/<int:id>/',
         views.product_detail,
         name='product_detail'),

]

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'category/<str:category_name>/',
        views.category_products,
        name='category_products'
    ),
]

urlpatterns = [
    path('', views.home, name='home'),
    
    path('indoor/', views.indoor, name='indoor'),

    path('outdoor/', views.outdoor, name='outdoor'),

    path('poles/', views.poles, name='poles'),

    path('contact/', views.contactus, name='contact'),
]

