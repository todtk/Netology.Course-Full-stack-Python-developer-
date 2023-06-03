from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def hello(request):
    context = {
        'data': [3, 45, 532]
    }
    return render(request, "app.html", context)


CONTENT = [str(i) for i in range(1000)]

def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        "page": page
    }
    return render(request, "pagi.html", context)
