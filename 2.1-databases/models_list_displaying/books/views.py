from django.shortcuts import render
from .models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'
    if pub_date:
        books = list(Book.objects.filter(pub_date=pub_date))
        context = {
            'books': books,
            'pub_date': pub_date
        }
    else:
        books = list(Book.objects.all())
        context = {
            'books': books
        }
    return render(request, template, context)


def pub_date_pagi(request, date):
    template = 'books/books_list.html'
    sorted_books = Book.objects.order_by('pub_date')
    # sorted_books = Book.objects.filter(pub_date=date)
    prev = Book.objects.filter(pub_date__lt=date).order_by('pub_date')
    next = Book.objects.filter(pub_date__gt=date).order_by('pub_date')
    prev_page = prev[prev.count() - 1].pub_date.strftime('%Y-%m-%d')
    next_page = next.pub_date.strftime('%Y-%m-%d')
    context = {
            'books': sorted_books,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        }
    return render(request, template, context)
