from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books':books})


def book_page(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_page.html', {'book' : book})