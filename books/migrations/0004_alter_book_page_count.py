# Generated by Django 5.1.1 on 2024-11-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(blank=True, default='not_found.png', null=True),
        ),
    ]
