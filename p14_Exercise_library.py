from datetime import date


class Book:
    """
    Vytvořte třídu Book s atributy:
    title (název knihy)
    author (autor knihy)
    year (rok vydání)
    """
    _title = ""
    _author = ""
    _year = 0

    def __init__(self, title_, author_, year_):
        self.title = title_
        self.author = author_
        self.year = year_

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_):
        self._title = title_

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_):
        self._author = author_

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year_):
        if year_ > date.today().year:
            raise ValueError
        self._year = year_

    def __repr__(self):
        return f"Book(title={self._title}, author={self._author}, year={self.year})"

    def __str__(self):
        return f"Book: {self.title} written by {self._author} in year {self._year}"


class Library:
    _books = []

    def __init__(self):
        self.books = []

    @property
    def books(self):
        return self._books

    def __repr__(self):
        return f"Library({self.books})"

    def __str__(self):
        return f"Library with {len(self.books)} books."

    def add_book(self, book_):
        self.books.append(book_)

    def find_books_by_author(self, author_):
        return [book for book in self.books if book.author == author_]

    @books.setter
    def books(self, value):
        self._books = value


if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(book1)
    book2 = Book("1984", "George Orwell", 1949)
    print(book2)
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    print(library)
    print(library.find_books_by_author("F. Scott Fitzgerald"))
