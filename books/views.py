from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Book
from .converters import DateConverter


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)


def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    books = Book.objects.filter(pub_date=pub_date)

    try:
        next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first().pub_date
    except AttributeError:
        next_date = None

    try:
        prev_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first().pub_date
    except AttributeError:
        prev_date = None

    context = {
        'books': books,
        'next_date': next_date,
        'prev_date': prev_date
    }
    return render(request, template, context)


