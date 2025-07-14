## Retrieve Operation

### Python Command

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-four")
print(book.title)
print(book.author)
print(book.publication_year)
