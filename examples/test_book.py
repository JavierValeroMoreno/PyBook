from Book.book import Book
import os

libro = Book()
libro.load_file(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "test.bg"))
libro.init()
