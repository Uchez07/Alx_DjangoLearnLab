
## Delete Operation

### Python Command

```python
from your_app_name.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
