from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Book, Review
from .filters import BookFilter
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def chunked(iterable, size):
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:  
        yield chunk


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
    
    sorted_books = list(chunked(books, 5))

    return render(request, 'books/books_list.html', {'sorted_books': sorted_books, 'filter': book_filter, 'sort_by': sort_by, 'order': order, 'search_query': search_query})

def book_page(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_page.html', {'book' : book})

@login_required(login_url="/users/login/")
def review_new(request):
    return render(request, 'books/review_new.html')

@login_required
def new_review(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('books:page', slug=book.slug)
    else:
        form = ReviewForm()
    return render(request, 'books/new_review.html', {'form': form, 'book': book})