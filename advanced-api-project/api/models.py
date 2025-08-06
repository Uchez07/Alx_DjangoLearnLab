from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.DateField(max_length=100)
    author = models.ForeignKe(Author, ondelete=models.CASCADE related_name='book')

class Author(models.Models):
    name = models.CharField(max_length=100)
