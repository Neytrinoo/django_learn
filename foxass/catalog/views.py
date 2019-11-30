from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()  # количество записей в моделе Book
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()  # количество доступных книг. __exact означает точное совпадение с учетом регистра
    num_authors = Author.objects.all().count()

    return render(request, 'index.html', context={'num_books': num_books, 'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available, 'num_authors': num_authors})
