from django.shortcuts import render
from .models import Product, ProductImage


def product(request, product_id):

    single_product = Product.objects.get(id=product_id)

    img = ProductImage.objects.get(product=single_product, is_main=True)
    non_main_imgs = ProductImage.objects.filter(product=single_product, is_main=False, is_active=True)

    return render(request, 'products/product.html', locals())