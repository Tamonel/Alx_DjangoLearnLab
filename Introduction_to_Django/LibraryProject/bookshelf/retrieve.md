# Retrieve Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title  # Expected Output: "1984"
book.author  # Expected Output: "George Orwell"
book.publication_year  # Expected Output: 1949

