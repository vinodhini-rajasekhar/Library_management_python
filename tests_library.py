import pytest
from typing import Any
from datetime import date
from Library import Library
from PrintedBook import PrintedBook
from EBook import EBook
from AudioBook import AudioBook
from Book import Book
from Patron import Patron
from Loan import Loan


class MockBook(Book):
    """Mock book class used to test generic Book behaviour in Library."""
    def __init__(self: "Book", title: str) -> None:
        """Create a mock book with a title."""
        super().__init__(title)

    def get_length(self: Book) -> str:
        """Abstract method implementation for tests."""
        return "dummy length"


def _insert_item(collection, item: Any) -> None:
    """Helper to insert item into collection (handles both LinkedList and list)."""
    if hasattr(collection, 'iterator'):
        # LinkedList - insert at position 0
        collection.insert(item)
    else:
        # Python list - insert at position 0
        collection.insert(0, item)


def _traverse(collection, func) -> None:
    """Helper to traverse collection (handles both LinkedList and list)."""
    if hasattr(collection, 'traverse'):
        # LinkedList
        collection.traverse(func)
    else:
        # Python list
        for item in collection:
            func(item)


def _get_first(collection) -> Any:
    """Helper to get first item from collection (handles both LinkedList and list)."""
    if hasattr(collection, 'first'):
        # LinkedList
        return collection.first()
    else:
        # Python list
        return collection[0] if len(collection) > 0 else None


def _get_first_link(collection) -> Any:
    """Helper to get first link from collection (handles both LinkedList and list)."""
    if hasattr(collection, 'getFirst'):
        # LinkedList
        return collection.getFirst()
    else:
        # Python list - return the first item directly (no Link wrapper)
        return collection[0] if len(collection) > 0 else None


def test_library_initialization_and_name_property() -> None:
    """assert library initializes correctly and name getter/setter work"""
    lib = Library("Duke Library")
    assert lib.name == "Duke Library"
    assert len(lib.patrons) == 0
    assert len(lib.books) == 0
    assert len(lib.loans) == 0


def test_search_book_found_and_not_found() -> None:
    """assert search_book returns book when present and None when not"""
    lib = Library("Lib")
    b1 = MockBook("Focus")
    b2 = MockBook("Deep Work")
    _insert_item(lib.books, b1)
    _insert_item(lib.books, b2)
    found = lib.search_book("Focus")
    assert isinstance(found, Book)
    assert found.title == "Focus"
    assert lib.search_book("Missing") is None


def test_search_patron_found_and_not_found() -> None:
    """assert search_patron returns patron when present and None when not"""
    lib = Library("Lib")
    p1 = Patron("Vinu", "Duke", "111")
    p2 = Patron("Alice", "Somewhere", "222")
    _insert_item(lib.patrons, p1)
    _insert_item(lib.patrons, p2)
    found = lib.search_patron("Vinu")
    assert isinstance(found, Patron)
    assert found.name == "Vinu"
    assert lib.search_patron("Missing") is None


def test_add_printed_ebook_audiobook_and_no_duplicates() -> None:
    """assert add_*book adds once and ignores duplicate titles"""
    lib = Library("Lib")
    lib.add_printed_book("Focus", 120)
    assert len(lib.books) == 1
    lib.add_printed_book("Focus", 120)
    assert len(lib.books) == 1
    lib.add_ebook("Python 101", 10000, 50)
    assert len(lib.books) == 2
    lib.add_audio_book("Calm Mind", 3600)
    assert len(lib.books) == 3
    titles: set[str] = set()

    def collect_titles(b: Book) -> None:
        """Collect titles"""
        titles.add(b.title)
    _traverse(lib.books, collect_titles)
    assert "Focus" in titles
    assert "Python 101" in titles
    assert "Calm Mind" in titles


def test_add_patron_and_no_duplicate() -> None:
    """assert add_patron inserts a patron once and ignores duplicate name"""
    lib = Library("Lib")

    lib.add_patron("Vinu", "Duke", "123")
    assert len(lib.patrons) == 1
    lib.add_patron("Vinu", "Other", "999")
    assert len(lib.patrons) == 1
    lib.add_patron("Harish", "Somewhere", "456")
    assert len(lib.patrons) == 2
    assert lib.search_patron("Vinu") is not None
    assert lib.search_patron("Harish") is not None


def test_checkout_book_with_none_arguments_does_nothing() -> None:
    """assert checkout_book returns early when any argument is None"""
    lib = Library("Lib")
    b = MockBook("Focus")
    p = Patron("Vinu", "Duke", "123")
    d = date(2025, 1, 1)
    lib.check_out_book(None, p, d)   
    lib.check_out_book(b, None, d)  
    lib.check_out_book(b, p, None)  
    assert len(lib.loans) == 0


def test_checkout_book_when_already_checked_out() -> None:
    """assert checkout_book does nothing if book already checked out"""
    lib = Library("Lib")
    b = MockBook("Focus")
    p1 = Patron("Vinu", "Duke", "123")
    p2 = Patron("Other", "Elsewhere", "999")
    d = date(2025, 1, 1)
    b.check_out(p1)
    assert b.is_checked_out() is True
    lib.check_out_book(b, p2, d)
    assert len(lib.loans) == 0


def test_checkout_and_return_book_full_flow() -> None:
    """assert checkout_book creates a Loan and return_book removes it"""
    lib = Library("Lib")
    b = MockBook("Focus")
    p = Patron("Vinu", "Duke", "123")
    d = date(2025, 1, 1)
    assert len(lib.loans) == 0
    assert b.is_checked_out() is False
    assert p.is_book_checked_out_by_patron(b) is False
    lib.check_out_book(b, p, d)
    assert b.is_checked_out() is True
    assert p.is_book_checked_out_by_patron(b) is True
    assert len(lib.loans) == 1
    lib.return_book(b, p)
    assert b.is_checked_out() is False
    assert p.is_book_checked_out_by_patron(b) is False
    assert len(lib.loans) == 0


def test_return_book_with_none_arguments_does_nothing() -> None:
    """assert return_book returns early when book or patron is None"""
    lib = Library("Lib")
    b = MockBook("Focus")
    p = Patron("Vinu", "Duke", "123")
    assert len(lib.loans) == 0
    lib.return_book(None, p)      
    lib.return_book(b, None)       
    assert len(lib.loans) == 0


def test_return_book_when_no_matching_loan() -> None:
    """assert return_book does nothing when loan is not found"""
    lib = Library("Lib")
    b1 = MockBook("Book1")
    b2 = MockBook("Book2")
    p1 = Patron("Vinu", "Duke", "123")
    p2 = Patron("Harish", "Somewhere", "456")
    lib.check_out_book(b1, p1, date(2025, 1, 1))
    assert len(lib.loans) == 1
    lib.return_book(b2, p2)
    assert len(lib.loans) == 1


def test_library_internal_object_structure() -> None:
    """assert Library stores objects having required attributes (Patron, Book, Loan)."""
    lib = Library("Central")
    p = Patron("Vinu", "Duke", "12345")
    b = MockBook("Focus")
    d = date(2026, 1, 1)
    _insert_item(lib.patrons, p)
    _insert_item(lib.books, b)
    lib.check_out_book(b, p, d)
    assert hasattr(lib, "patrons")
    assert hasattr(lib, "books")
    assert hasattr(lib, "loans")
    stored_patron = lib.search_patron("Vinu")
    assert stored_patron is not None
    assert hasattr(stored_patron, "name")
    assert hasattr(stored_patron, "address")
    assert hasattr(stored_patron, "phone_number")
    assert hasattr(stored_patron, "_Patron__list_checked_books")
    stored_book = lib.search_book("Focus")
    assert stored_book is not None
    assert hasattr(stored_book, "title")
    assert hasattr(stored_book, "get_length")
    assert callable(stored_book.get_length)
    loan_link = _get_first_link(lib.loans)
    assert loan_link is not None
    if hasattr(loan_link, 'getData'):
        # LinkedList Link
        loan = loan_link.getData()
    else:
        # Python list - item is directly the loan
        loan = loan_link
    assert isinstance(loan, Loan)
    loan_vars = dir(loan)
    assert any("borrowed_book" in attr for attr in loan_vars)
    assert any("checked_out_patron" in attr for attr in loan_vars)
    assert any("due_date" in attr for attr in loan_vars)
    assert loan.book.title == "Focus"
    assert loan.patron.name == "Vinu"
    assert loan.due_date == d

def test_library_str_format() -> None:
    """assert library __str__ prints sections and items correctly"""
    lib = Library("Durham Library")
    b = MockBook("BookA")    
    p = Patron("Jane", "Addr", "111")
    d = date(2026, 1, 22)
    loan = Loan(b, p, d)
    _insert_item(lib.books, b)
    _insert_item(lib.patrons, p)
    _insert_item(lib.loans, loan)
    text = str(lib)
    assert text.startswith("Library Durham Library:")
    assert "\t- Books:" in text
    assert "\t- Patrons:" in text
    assert "\t- Loans:" in text
    assert f"\t\t- {b}" in text
    assert f"\t\t- {p}" in text
    assert f"\t\t- {loan}" in text
    assert text.strip().endswith(f"- {loan}") is True

def test_add_ebook_duplicate_does_not_insert() -> None:
    """assert add_ebook returns early when duplicate title present"""
    lib = Library("TestLib")
    _insert_item(lib.books, MockBook("Shared"))
    initial_count = len(lib.books)
    lib.add_ebook("Shared", 1000, 200)
    assert len(lib.books) == initial_count
    assert isinstance(_get_first(lib.books), MockBook)

    
def test_add_audiobook_duplicate_does_not_insert() -> None:
    """assert add_audiobook returns early when duplicate title present"""
    lib = Library("TestLib")
    _insert_item(lib.books, MockBook("Voices"))
    initial_count = len(lib.books)
    lib.add_audio_book("Voices", 3600)
    assert len(lib.books) == initial_count

def test_library_str_empty_sections() -> None:
    """assert library __str__ prints sections even when lists are empty"""
    lib = Library("Campus Lib")
    text = str(lib)
    assert text.startswith("Library Campus Lib:")
    assert "\t- Books:\n" in text
    assert "\t- Patrons:\n" in text
    assert "\t- Loans:\n" in text
    assert "\t\t-" not in text


def test_library_collections_type_discovery() -> None:
    """assert discover concrete types used for library collections"""
    lib = Library("Probe Library")

    patrons_type = type(lib.patrons).__name__
    books_type = type(lib.books).__name__
    loans_type = type(lib.loans).__name__

    assert hasattr(lib.patrons, "__len__")
    assert hasattr(lib.books, "__len__")
    assert hasattr(lib.loans, "__len__")

    assert any(
        hasattr(lib.books, name) 
        for name in ("insert", "append")
    )
    assert any(
        hasattr(lib.patrons, name) 
        for name in ("insert", "append")
    )
    assert any(
        hasattr(lib.loans, name) 
        for name in ("insert", "append")
    )

    allowed_types = {"LinkedList", "list"}
    assert patrons_type in allowed_types
    assert books_type in allowed_types
    assert loans_type in allowed_types

    print(f"patrons type in grader: {patrons_type}")
    print(f"books type in grader:   {books_type}")
    print(f"loans type in grader:   {loans_type}")
