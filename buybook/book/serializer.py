from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Book,Author
class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','book_name','book_language','book_price','book_page','book_title']
    def validate(self, data):
        book_name = data.get('book_name')
        book_language = data.get('book_language')
        book_price=data.get('book_price')
        book_page=data.get('book_page')
        book_title=data.get('book_title')
        if book_name == '':
            raise serializers.ValidationError('Enter the Book Name')
        if book_language == '':
            raise serializers.ValidationError('Enter the Book Language')
        if book_price == '':
            raise serializers.ValidationError('Enter the Book Price')
        if book_page == '':
            raise serializers.ValidationError('Enter the Book Page')
        if book_title == '':
            raise serializers.ValidationError('Enter the Book Title')
        return data


class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','name','date_of_birth','date_of_death','age','birth_place','book_write']
    def validate(self, data):
        name = data.get('name')
        date_of_birth = data.get('date_of_birth')
        date_of_death=data.get('date_of_death')
        age=data.get('age')
        birth_place=data.get('birth_place')
        book_write=data.get('book_write')
        if name == '':
            raise serializers.ValidationError('Enter the Author Name')
        if date_of_birth == '':
            raise serializers.ValidationError('Enter the Author Birthdate')
        if date_of_death == '':
            raise serializers.ValidationError('Enter the Author Deathdate')
        if age == '':
            raise serializers.ValidationError('Enter the Author age')
        if birth_place == '':
            raise serializers.ValidationError('Enter the Author Birth place')
        if book_write == '':
            raise serializers.ValidationError('Enter the Author Book write')
        return data       

class Booknameserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['book_name']

class Authorlistserializer(serializers.ModelSerializer):
    book_write=Booknameserializer(many=True,read_only=True)
    class Meta:
        model=Author
        fields=['id','name','date_of_birth','date_of_death','age','birth_place','book_write']



class Booklistserializer(serializers.ModelSerializer):
    writer=serializers.SerializerMethodField("get_writer")
    place=serializers.SerializerMethodField("get_place")
    birth=serializers.SerializerMethodField("get_birth")
    death=serializers.SerializerMethodField("get_death")

    def get_writer(self,obj):
        name=Author.objects.filter(book_write=obj).first()
        return name.name
    def get_place(self,obj):
        auther_place=Author.objects.filter(book_write=obj).first()
        return auther_place.birth_place
    def get_birth(self,obj):
        auther_birth=Author.objects.filter(book_write=obj).first()
        return auther_birth.date_of_birth
    def get_death(self,obj):
        auther_birth=Author.objects.filter(book_write=obj).first()
        return auther_birth.date_of_death


    class Meta:
        model=Book
        fields=['id','book_name','book_price','book_page','book_language','writer','place','birth','death']

