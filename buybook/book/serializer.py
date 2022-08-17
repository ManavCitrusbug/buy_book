from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Book,Author

class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','name','date_of_birth','date_of_death','age','birth_place']
    def validate(self, data):
        name = data.get('name')
        date_of_birth = data.get('date_of_birth')
        date_of_death=data.get('date_of_death')
        age=data.get('age')
        birth_place=data.get('birth_place')
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
        return data     

class Bookserializer(serializers.ModelSerializer):
    Author=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Book
        fields=['id','book_name','book_language','book_price','book_page','Author']
    def validate(self, data):
        book_name = data.get('book_name')
        book_language = data.get('book_language')
        book_price=data.get('book_price')
        book_page=data.get('book_page')
        Author=data.get('Author')
        if book_name == '':
            raise serializers.ValidationError('Enter the Book Name')
        if book_language == '':
            raise serializers.ValidationError('Enter the Book Language')
        if book_price == '':
            raise serializers.ValidationError('Enter the Book Price')
        if book_page == '':
            raise serializers.ValidationError('Enter the Book Page')
        if Author == '':
            raise serializers.ValidationError('Enter the Author')
        
        return data

class Booklistserializer(serializers.ModelSerializer):
    Author=serializers.StringRelatedField(read_only=True)
    birthdate=serializers.SerializerMethodField("get_birth")
    deathdate=serializers.SerializerMethodField("get_death")
    age=serializers.SerializerMethodField("get_age")
    def get_birth(self,obj):
        return obj.Author.date_of_birth
    def get_death(self,obj):
        return obj.Author.date_of_death
    def get_age(self,obj):
        return obj.Author.age


    class Meta:
        model=Book
        fields=['id','Author','birthdate','deathdate','age','book_name','book_language','book_page']



