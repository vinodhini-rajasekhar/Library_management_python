from typing import Optional
from datetime import date
from Book import Book
from Patron import Patron
from AudioBook import AudioBook
from PrintedBook import PrintedBook
from EBook import EBook
from Loan import Loan
from LinkedList import LinkedList


class Library:
    """Represents a library that holds books, patrons and loans."""

    def __init__(self: "Library", name: str) -> None:
        """Create a library with the given name."""
        self.__name = name
        self.patrons = LinkedList()
        self.books = LinkedList()
        self.loans = LinkedList()


    @property
    def name(self: "Library") -> str:
        """Return the name of the book."""
        return self.__name

    def search_book(self: "Library", title: str) -> Optional[Book]:
        """Search for a book by title and return it, or None."""
        result = self.books.search(
            title,
            key=lambda b: b.title if isinstance(b, Book) else None,
        )
        return result if isinstance(result, Book) else None
        

    def search_patron(self: "Library", name: str) -> Optional[Patron]:
        """Search for a patron by name and return it, or None."""
        result = self.patrons.search(
            name,
            key=lambda p: p.name if isinstance(p, Patron) else None,
        )
        return result if isinstance(result, Patron) else None


    def add_printed_book(self: "Library", title: str, num_pages: int) -> None:
        """Add a new printed book to the library."""
        if self.search_book(title) is not None:
            return
        self.books.insert(PrintedBook(title,num_pages))


    def add_ebook(self: "Library", title: str, size_chars: int, chars_pp: int) -> None:
        """Add a new ebook to the library."""
        if self.search_book(title) is not None:
            return
        self.books.insert(EBook(title, size_chars, chars_pp))

    def add_audio_book(self: "Library", title: str, duration_seconds: int) -> None:
        """Add a new audio book to the library."""
        if self.search_book(title) is not None:
            return
        self.books.insert(AudioBook(title, duration_seconds))

    def add_patron(self: "Library", name: str, address: str, phone: str) -> None:
        """Add a new patron to the library."""
        if self.search_patron(name) is not None:
            return
        self.patrons.insert(Patron(name, address, phone))

    def check_out_book(self: "Library", a_book: Book, a_patron: Patron, due: date) -> None:
        """Check out a book to a patron until the given due date."""
        if a_book is None or a_patron is None or due is None:
            return

        if a_book.is_checked_out():
            return

        loan = Loan(a_book, a_patron, due)
        self.loans.insert(loan)

        a_patron.add_checked_book(a_book)
        a_book.check_out(a_patron)

    def return_book(self: "Library", a_book: Book, a_patron: Patron) -> None:
        """Return a book from a patron to the library."""
        if a_book is None or a_patron is None:
            return
        
        loan = self.loans.search((a_book, a_patron),key=lambda loan: ( loan.book,loan.patron,) 
                if isinstance(loan, Loan) else None,
        )
        if loan is None:
            return
        a_book.return_book()

        self.loans.delete(
            (a_book, a_patron),key=lambda l: (l.book,l.patron,)
            if isinstance(l, Loan) else None,
            )

    def __str__(self: "Library") -> str:
        """Return a string representation of the library."""

        def build_section(title: str, lst: any) -> str:
          """Helper to print sections like Books:, Patrons:, Loans:"""
          result = f"\t- {title}:\n"
          if hasattr(lst, 'iterator'):
              iterator = lst.iterator()
              while iterator.hasMore():
                  item = iterator.next()
                  result += f"\t\t- {item}\n"
          else:
              for item in lst:
                  result += f"\t\t- {item}\n"
          return result

        s = f"Library {self.name}:\n"
        s += build_section("Books", self.books)
        s += build_section("Patrons", self.patrons)
        s += build_section("Loans", self.loans)
        return s

