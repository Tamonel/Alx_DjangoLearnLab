from relationship_app.models import Author, Book, Library, Librarian


def demo_create_sample_data():
    author = Author.objects.create(name="Chinua Achebe")
    book1 = Book.objects.create(title="Things Fall Apart", author=author)
    book2 = Book.objects.create(title="No Longer at Ease", author=author)
    library = Library.objects.create(name="Main Library")
    library.books.set([book1, book2])
    librarian = Librarian.objects.create(name="Ada", library=library)
    return author, (book1, book2), library


def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

