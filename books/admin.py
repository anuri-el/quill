from django.contrib import admin
from .models import Book, Author, Publisher, Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author__first_name', 'author__last_name'] 
    list_display = ('title', 'author', 'genre', 'price', 'publication_date') 
    list_filter = ('author', 'genre', 'publication_date')  

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name'] 
    list_display = ( 'last_name', 'first_name', 'nationality', 'birth_date')  
    list_filter = ('nationality', 'birth_date')  

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['title', 'address']
    list_display = ('title', 'address', 'year_founded')
    list_filter = ('year_founded',)  

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'target_audience', 'literature_type') 
    list_filter = ('target_audience', 'literature_type')  