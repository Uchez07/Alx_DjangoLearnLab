from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter =('publication_year')
    search_field = ('title', 'author')

admin.site.register(Book)

