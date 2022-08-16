from django.contrib import admin

from book.models import Author, Book

# Register your models here.
@admin.register(Book)
class Book(admin.ModelAdmin):
         list_display=('id','book_name','book_language','book_price','book_page','book_title')
@admin.register(Author)
class Author(admin.ModelAdmin):
        list_display=('id','name','date_of_birth','date_of_death','age','birth_place','books_write')
        def books_write(self, obj):
            return ",".join([p.book_name for p in obj.book_write.all()])
