"""Správa knihovny (OOP)
Vytvořte třídu Book s atributy title (název knihy), author (autor knihy) a year (rok vydání).
Vytvořte třídu Library, která umožňuje přidávat knihy a vyhledávat knihy podle autora.
"""

import pytest
from p14_Exercise_library import Book, Library


def test_book():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"
    assert book.year == 1925


def test_library():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("1984", "George Orwell", 1949)
    library.add_book(book1)
    library.add_book(book2)

    assert len(library.books) == 2
    assert library.find_books_by_author("F. Scott Fitzgerald") == [book1]
    assert library.find_books_by_author("George Orwell") == [book2]
    assert library.find_books_by_author("J.K. Rowling") == []


def test_book_exception():
    with pytest.raises(ValueError):
        Book("title", "author", 2030)


if __name__ == "__main__":
    pytest.main()
