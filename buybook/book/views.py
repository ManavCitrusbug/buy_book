from django.shortcuts import render
from book.serializer import *
from rest_framework.permissions import AllowAny
from book.models import Book,Author
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView
# Create your views here.


class Authorcreateapi(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class=Authorserializer
    permission_classes=[AllowAny]

class Authorlistapi(ListAPIView):
    queryset = Author.objects.all()
    serializer_class=Authorserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['id','name','date_of_birth','date_of_death','age','birth_place']

    permission_classes=[AllowAny]


class Authorupdatedeletapi(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class=Authorserializer
    permission_classes=[AllowAny]

class Bookapi(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class=Bookserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['id','book_name','book_language','book_price','book_page','Author__name']
    permission_classes=[AllowAny]

class Bookupdatedeletapi(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class=Bookserializer
    permission_classes=[AllowAny]

class Book_authorlistapi(ListAPIView):
    queryset = Book.objects.all()
    serializer_class=Booklistserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['book_name','book_language','book_page','Author__name','Author__age','Author__date_of_birth','Author__date_of_death']
    permission_classes=[AllowAny]