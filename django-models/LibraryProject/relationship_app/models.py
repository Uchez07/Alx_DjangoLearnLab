from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=10)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = ('Book'))

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='Library')

    def __str__(self):
        return self.name
        
class Librarian(models.Model):
    name =models.CharField(max_length=100)
    library = OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
