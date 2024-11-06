from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Authors',on_delete=models.CASCADE, null=True, blank=True)
    isbn = models.BigIntegerField(max_length=13, unique=True)
    genre = models.ForeignKey('Genres',on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('Publishers',on_delete=models.CASCADE, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    language = models.CharField(max_length=255)
    page_count = models.IntegerField(null=True, blank=True)
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    biography = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Publishers(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    year_founded = models.PositiveIntegerField(null=True, blank=True, validators=[
            MinValueValidator(0),
            MaxValueValidator(datetime.now().year)
        ])
    description = models.TextField()
    contact_phone = models.CharField(max_length=25)
    site = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Genres(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_audience = models.CharField(max_length=255)
    literature_type = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


# class Reviewing(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, blank=True)
#     rating = models.PositiveIntegerField(null=True, blank=True, validators=[
#             MinValueValidator(0),
#             MaxValueValidator(5)
#         ])
#     review_text = models.TextField()
#     review_date = models.DateField(auto_now_add=True, null=True, blank=True)
#     recommendation = models.BooleanField(null=True, blank=True)
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return {self.title}


