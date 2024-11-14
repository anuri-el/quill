from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books_list, name="catalog"),
    # path('new-review/', views.review_new, name="new-review"),
    path('<slug:book_slug>/review/', views.new_review, name="new-review"),
    path('<slug:slug>', views.book_page, name="page"),
]
