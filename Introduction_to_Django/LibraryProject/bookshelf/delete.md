## Delete Operation

### Python Command

```python
from bookshelf.objects import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
