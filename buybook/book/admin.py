from django.contrib import admin

from book.models import Author, Book

# Register your models here.
@admin.register(Author)
class Author(admin.ModelAdmin):
        list_display=('id','name','date_of_birth','date_of_death','age','birth_place')

@admin.register(Book)
class Book(admin.ModelAdmin):
         list_display=('id','book_name','book_language','book_price','book_page','Author')
