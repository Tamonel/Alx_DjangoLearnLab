# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    """Return a queryset of Book objects written by author_name."""
    return Book.objects.filter(author__name=author_name)

def books_in_library(library_name):
    """Return a queryset of Book objects in the given library."""
    library = Library.objects.get(name=library_name)
    return library.books.all()

def librarian_for_library(library_name):
    """Return the Librarian instance assigned to the library."""
    library = Library.objects.get(name=library_name)
    return library.librarian

# Optional demo usage when run inside Django shell:
def demo_create_sample_data():
    """Create a tiny dataset for quick testing. Run from manage.py shell."""
    a = Author.objects.create(name="Chinua Achebe")
    b1 = Book.objects.create(title="Things Fall Apart", author=a)
    b2 = Book.objects.create(title="No Longer at Ease", author=a)
    lib = Library.objects.create(name="Main Library")
    lib.books.add(b1, b2)
    Librarian.objects.create(name="Ada", library=lib)
    return a, (b1, b2), lib
