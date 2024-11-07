from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books':books})


def book_page(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_page.html', {'book' : book})

@login_required(login_url="/users/login/")
def review_new(request):
    return render(request, 'books/review_new.html')