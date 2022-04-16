from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

registered_models = [Author, Genre, Book, BookInstance, Language]
admin.site.register(registered_models)
