from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [

    # path('test/', views.product, name='product'),
    path('product/<product_id>/', views.product, name='product')

]
