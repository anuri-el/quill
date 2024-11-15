from django_filters import FilterSet, CharFilter, NumberFilter, ModelChoiceFilter
from django.forms import TextInput, Select
from .models import Book, Genre

class BookFilter(FilterSet):
    title = CharFilter(
        lookup_expr='icontains', 
        label='Title', 
        widget=TextInput(attrs={'class': 'form-control buttons_fire form-field', 'placeholder': ''})
    )
    author = CharFilter(
        field_name='author__last_name', 
        lookup_expr='icontains', 
        label='Author', 
        widget=TextInput(attrs={'class': 'form-control buttons_fire form-field', 'placeholder': ''})
    )
    genre = ModelChoiceFilter(
        queryset=Genre.objects.all(), 
        label='Genre', 
        widget=Select(attrs={'class': 'form-control buttons_fire form-field'})
    )
    min_price = NumberFilter(
        field_name='price', 
        lookup_expr='gte', 
        label='Min Price', 
        widget=TextInput(attrs={'class': 'form-control buttons_fire form-field', 'placeholder': ''})
    )
    max_price = NumberFilter(
        field_name='price', 
        lookup_expr='lte', 
        label='Max Price', 
        widget=TextInput(attrs={'class': 'form-control buttons_fire form-field', 'placeholder': ''})
    )
    language = CharFilter(
        lookup_expr='icontains', 
        label='Language', 
        widget=TextInput(attrs={'class': 'form-control buttons_fire form-field', 'placeholder': ''})
    )
    min_pub_year = NumberFilter(
        method='filter_min_pub_year', 
        label='Publish After', 
        widget=TextInput(attrs={'class': 'form-control buttons_fire form-field', 'placeholder': ''})
    )
    max_pub_year = NumberFilter(
        method='filter_max_pub_year', 
        label='Publish Before', 
        widget=TextInput(attrs={'class': 'form-control buttons_fire form-field', 'placeholder': ''})
    )

    def filter_min_pub_year(self, queryset, name, value):
        return queryset.filter(publication_date__year__gte=value)

    def filter_max_pub_year(self, queryset, name, value):
        return queryset.filter(publication_date__year__lte=value)

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'min_price', 'max_price', 'language', 'min_pub_year', 'max_pub_year']