from django.contrib import admin
from .models import *

# суперпользователь: логин - admin, пароль - admin
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)


# admin.site.register(BookInstance)

class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')  # для отображения в админпанели
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]  # для подробного представления записи автора
    inlines = [BooksInline]


admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):  # для отображения физических копий какой-то книги на странице самой книги
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]  # для отображения физических копий какой-то книги на странице самой книги


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')})
    )  # для группировки полей при подробном отображении записи. Availability и None - это заголовок вверху для полей внизу. None означает, что заголовок не нужен
