# Generated by Django 4.1 on 2022-08-23 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_page',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_price',
            field=models.IntegerField(),
        ),
    ]
