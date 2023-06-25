from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    if sort == "min_price":
        sort_method = 'price'
    elif sort == "max_price":
        sort_method = '-price'
    else:
        sort_method = 'name'

    context = {
        'phones': Phone.objects.order_by(sort_method),
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.filter(slug=slug)[0]

    context = {
        'phone': phone,
    }

    return render(request, template, context)
