from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def pub_date(request):
    template = 'books/books_list.html'
    sorted_books = Book.objects.order_by('pub_date')

    page_number = Book.pub_date
    for date in page_number:
        paginator = Paginator(sorted_books, 1)
        page = paginator.get_page(date)
        context = {
            'page': page
        }
        return render(request, template, context)
