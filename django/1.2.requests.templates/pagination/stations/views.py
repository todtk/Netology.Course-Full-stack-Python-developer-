from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, mode="r", encoding="utf-8") as csv_file:
        stations = list(DictReader(csv_file))

        page_number = int(request.GET.get("page", 1))
        stations = Paginator(stations, 10)
        page = stations.get_page(page_number)

    context = {
        'bus_stations': stations.page(page_number),
        'page': page,
    }
    return render(request, 'stations/index.html', context)
