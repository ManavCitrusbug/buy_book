from django.db import models



class Author(models.Model):
    name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    date_of_death=models.DateField()
    age=models.IntegerField()
    birth_place=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Book(models.Model):
    book_name=models.CharField(max_length=50)
    book_language=models.CharField(max_length=20)
    book_price=models.IntegerField()
    book_page=models.IntegerField()
    Author=models.ForeignKey(Author,on_delete=models.CASCADE)
 



