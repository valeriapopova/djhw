from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


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


def pub_date_pagi(request):
    template = 'books/books_list.html'
    sorted_books = Book.objects.filter('pub_date')
    page_number = Book.pub_date
    paginator = Paginator(sorted_books, 1)
    page = paginator.get_page(page_number)
    context = {
           'page': page
        }
    return render(request, template, context)
