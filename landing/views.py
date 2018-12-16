from django.shortcuts import render
from .forms import SubscriberForm

from products.models import ProductImage


def landing(request):

    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():        # !!!!!!!!!!!!!!!!!!! Консольный вывод
        print(request.POST)  # print(form)                  # !!!!!!!!!!!!!!!!!!!
        data = form.cleaned_data                            # !!!!!!!!!!!!!!!!!!!
        print(data['name'])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products = ProductImage.objects.filter(is_main=True, is_active=True, product__is_active=True)
    products_jackets = products.filter(product__category__id=1)   # !!!!!!
    products_sweats = products.filter(product__category__id=2)    # !!!!!!
    products_winter = products.filter(product__category__id=3)    # !!!!!!

    return render(request, 'landing/home.html', locals())