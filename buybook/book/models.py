from django.db import models

class Book(models.Model):
    book_name=models.CharField(max_length=50)
    book_language=models.CharField(max_length=20)
    book_price=models.CharField(max_length=10)
    book_page=models.CharField(max_length=10)
    book_title=models.CharField(max_length=50)
    def __str__(self):
        return self.book_name

class Author(models.Model):
    name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    date_of_death=models.DateField()
    age=models.CharField(max_length=3)
    birth_place=models.CharField(max_length=20)
    # book_id=models.ForeignKey(Book,on_delete=models.CASCADE)
    book_write=models.ManyToManyField(Book,related_name='book')

    
    def Book(self):
        return ",".join([str(b) for b in self.book_write.all() ])


