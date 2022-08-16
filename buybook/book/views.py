from django.shortcuts import render
from book.serializer import *
from rest_framework.permissions import AllowAny
from book.models import Book,Author
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import filters

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
# Create your views here.
class Bookapi(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class=Bookserializer
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['id','book_name','book_language','book_price','book_page','book_title']
    ordering_fields=['id','book_name','book_language','book_price','book_page','book_title']
    permission_classes=[AllowAny]

class Bookupdatedeletapi(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class=Bookserializer
    permission_classes=[AllowAny]

class Authorcreateapi(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class=Authorserializer
    permission_classes=[AllowAny]

class Authorlistapi(ListAPIView):
    queryset = Author.objects.all()
    serializer_class=Authorlistserializer
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['id','name','date_of_birth','date_of_death','age','birth_place','book_write__book_name']
    ordering_fields=['id','name','date_of_birth','date_of_death','age','birth_place','book_write__book_name']
    permission_classes=[AllowAny]


class Authorupdatedeletapi(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class=Authorserializer
    permission_classes=[AllowAny]

class Book_authorlistapi(ListAPIView):
    queryset = Book.objects.all()
    serializer_class=Booklistserializer
    permission_classes=[AllowAny]