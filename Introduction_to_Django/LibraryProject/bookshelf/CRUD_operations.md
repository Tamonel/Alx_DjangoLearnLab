# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book  # Expected Output: <Book: 1984>

# Retrieve Operation

```python
from bookshelf.models import Book
Book.objects.all()
# Expected Output: <QuerySet [<Book: 1984>]>

# Update Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book  # Expected Output: <Book: Nineteen Eighty-Four>

# Delete Operation

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()  # Expected Output: <QuerySet []>

