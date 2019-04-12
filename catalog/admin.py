from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


# Register your models here.
# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(Author)
# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


@admin.register(BookInstance)
# admin.site.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = ( # tuple containing
        (None, { # a tuple with a label and a dict 
            'fields': ('book', 'imprint', 'id') # of fields
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )


admin.site.register(Language)
admin.site.register(Genre)