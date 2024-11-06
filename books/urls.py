from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books_list, name="catalog"),
    path('<slug:slug>', views.book_page, name="page"),
]
