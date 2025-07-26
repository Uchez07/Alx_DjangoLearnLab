# CRUD Operations in Django Shell

This document contains the full Create, Retrieve, Update, and Delete operations performed in the Django shell using the `Book` model.

---

## ✅ CREATE

### Command

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
