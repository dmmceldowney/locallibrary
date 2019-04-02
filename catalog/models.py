from django.db import models
from django.urls import reverse # used to generate URLs by reversing the URL patterns (??????? WHAT?????)
import uuid # used for unique book instances

# Create your models here.
class Genre(models.Model): # inherits properties from the Model class
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')


    def __str__(self):
        """String representing the Model object."""
        return self.name
        

class Book(models.Model):
    """Model representing a book (but not the specific copy of a book)"""
    title = models.CharField(max_length=200)

    # Author is a string because Author hasn't been defined yet in the file
    # on_delete, set all of the references to the author as NULL on this book
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', 
        max_length= 13, 
        help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn"> ISBN number</a>')

    # genre class has already been defined so we can reference the object in this declaration
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')


    def __str__(self):
        """String for representing the Model object"""
        return self.title


    def get_absolute_url(self):
        """Returns the url to access a detail record for this book"""
        return reverse('book-detail', args=[str(self.id)])

    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])


    def copy_count(self):
        return len(BookInstance.objects.filter(book=self.id))

    
    display_genre.short_description = 'Genre'


# Implement the Language model
class Language(models.Model):
    """Model representing the book's language"""
    name = models.CharField(max_length=200, help_text="Enter the book's language")

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    """Model representing a specific COPY of a book"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book at the library.")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'


class Author(models.Model):
    """Model representing an actor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Born', null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)


    class Meta:
        ordering = ['last_name', 'first_name']

    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
