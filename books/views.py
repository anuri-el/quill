from django.shortcuts import render
from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Book
from .filters import BookFilter
from django.contrib.auth.decorators import login_required

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=books)

    search_query = request.GET.get('search', '')
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(author__first_name__icontains=search_query) |
            Q(author__last_name__icontains=search_query)
        )

    sort_by = request.GET.get('sort_by', 'publication_date')
    order = request.GET.get('order', 'desc') 
    if sort_by in ['title', 'price', 'publication_date']:
        if order == 'desc':
            sort_by = f'-{sort_by}'
        books = book_filter.qs.filter(pk__in=books).order_by(sort_by)
    else:
        books = book_filter.qs.filter(pk__in=books)

    return render(request, 'books/books_list.html', {'books': books, 'filter': book_filter, 'sort_by': sort_by, 'order': order, 'search_query': search_query})

def book_page(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_page.html', {'book' : book})

@login_required(login_url="/users/login/")
def review_new(request):
    return render(request, 'books/review_new.html')