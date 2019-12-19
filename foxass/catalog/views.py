from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()  # количество записей в моделе Book
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()  # количество доступных книг. __exact означает точное совпадение с учетом регистра
    num_authors = Author.objects.all().count()

    return render(request, 'index.html', context={'num_books': num_books, 'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available, 'num_authors': num_authors})


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # наше собственное имя переменной контекста в шаблоне
    # queryset = Book.objects.filter(title__icontains='war')[:5]  # получение 5 книг, содержащих слово war в заголовке
    template_name = 'book_list.html'  # определение имени нашего шаблона и его расположения
    paginate_by = 2  # с помощью параметра ?page=2 в url можно получить доступ к другой странице

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data()
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'author_list.html'

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
