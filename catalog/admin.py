from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_dispay = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

@admin.register(BookInstance)
# admin.site.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Language)
admin.site.register(Genre)