from django.db import models



class Author(models.Model):
    name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    date_of_death=models.DateField()
    age=models.CharField(max_length=3)
    birth_place=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Book(models.Model):
    book_name=models.CharField(max_length=50)
    book_language=models.CharField(max_length=20)
    book_price=models.CharField(max_length=10)
    book_page=models.CharField(max_length=10)
    Author=models.ForeignKey(Author,on_delete=models.CASCADE)
 



