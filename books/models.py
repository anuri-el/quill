from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author',on_delete=models.CASCADE, null=True, blank=True)
    isbn = models.BigIntegerField(unique=True)
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    language = models.CharField(max_length=255)
    page_count = models.IntegerField(default='not_found.png', null=True, blank=True)
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    year_founded = models.PositiveIntegerField(null=True, blank=True, validators=[
            MinValueValidator(0),
            MaxValueValidator(datetime.now().year)
        ])
    description = models.TextField()
    contact_phone = models.CharField(max_length=25, null=True, blank=True)
    site = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_audience = models.CharField(max_length=255)
    literature_type = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, blank=True, related_name="reviews")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    # rating = models.PositiveIntegerField(null=True, blank=True, validators=[
    #         MinValueValidator(0),
    #         MaxValueValidator(5)
    #     ])
    review_text = models.TextField(null=True, blank=True)
    review_date = models.DateField(auto_now_add=True, null=True, blank=True)
    recommendation = models.BooleanField(null=True, blank=True)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.user} review on {self.book.title} - {self.rating} stars"


