from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from books.models import Book, Genre

def homepage(request):
    recent_books = Book.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:5]
    popular_genres = Genre.objects.all()[:5]
    coming_soon_books = Book.objects.filter(publication_date__gt=timezone.now()).order_by('publication_date')[:5]

    return render(request, 'index.html', {
        'recent_books': recent_books, 
        'popular_genres': popular_genres,
        'coming_soon_books': coming_soon_books});

def about(request):
    return render(request, 'about.html');

def faq(request):
    return render(request, 'faq.html');