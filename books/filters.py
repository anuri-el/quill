from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter, DateFilter, ModelChoiceFilter
from .models import Book, Genre

class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Title')
    author = CharFilter(field_name='author__last_name', lookup_expr='icontains', label='Author Last Name')
    genre = ModelChoiceFilter(queryset=Genre.objects.all(), label='Genre')
    min_price = NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    max_price = NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    language = CharFilter(lookup_expr='icontains', label='Language')
    # min_pub_date = DateFilter(field_name='publication_date', lookup_expr='gte', label='Publication After')
    # max_pub_date = DateFilter(field_name='publication_date', lookup_expr='lte', label='Publication Before')
    min_pub_year = NumberFilter(method='filter_min_pub_year', label='Publish After')
    max_pub_year = NumberFilter(method='filter_max_pub_year', label='Publish Before')

    def filter_min_pub_year(self, queryset, name, value):
        return queryset.filter(publication_date__year__gte=value)

    def filter_max_pub_year(self, queryset, name, value):
        return queryset.filter(publication_date__year__lte=value)

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'min_price', 'max_price', 'language', 'min_pub_year', 'max_pub_year']