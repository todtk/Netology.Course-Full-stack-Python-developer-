from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book
from datetime import datetime


def books_view(request):
    book_objects = Book.objects.all()

    context = {
        'books': book_objects
    }

    return render(request, 'books/books_list.html', context)


def books_view_from_date(request, date: str):
    date = datetime.date(datetime.strptime(date, "%Y-%m-%d"))
    dates = [date['pub_date'] for date in Book.objects.values("pub_date").distinct()]
    paginator = Paginator(dates, 1)
    page = paginator.get_page(dates.index(date) + 1)

    context = {
        'books': Book.objects.filter(pub_date=date),
        'page': page,
        'dates': dates
    }

    return render(request, 'books/books_list.html', context)
