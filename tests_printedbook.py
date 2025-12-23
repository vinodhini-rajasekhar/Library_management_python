from Book import Book 
from PrintedBook import PrintedBook
import pytest

class MockPatron:
    """Dummy patron class"""

    def __init__(self: "MockPatron") -> None:
        """Initialize a dummy patron """
        self.removed_books: list[Book] = []

    def remove_checked_book(self: "MockPatron", book: Book) -> None:
        """book was removed from this patron."""
        self.removed_books.append(book)
    
def test_printedbook_instance_of_book()->None:
    """Asserts whether printed book is instance of book"""
    test = PrintedBook("Focus",100)
    assert isinstance(test,Book) 

def test_printedbook_inherits_book() -> None:
    """Asserts PrintedBook inherits from Book."""
    assert issubclass(PrintedBook, Book)

def test_printedbook_constructer_check()->None:
    """Asserts constructor"""
    test = PrintedBook("Focus",100)
    assert test.title=="Focus"
    assert test.num_pages==100


def test_num_pages_read_only_property() -> None:
    """Assert num_pages is read-only and cannot be assigned directly."""
    test = PrintedBook("Focus", 100)
    assert test.num_pages == 100
    try:
        test.num_pages = 200 
        assert False, "num_pages should be read-only and not assignable"
    except AttributeError:
        assert True

def test_getlength_returns_correct_string()->None:
    """Assert whether return page count"""
    test = PrintedBook("Focus",100)
    assert test.get_length() == "100 pages"

def test_string()->None:
    """assert string output"""
    test = PrintedBook("Focus",100)
    assert str(test) == 'Book: "Focus". Printed 100 pages.'
    _ = repr(test) 


def test_printedbook_equality_uses_title_only() -> None:
    """Assert equality for PrintedBook depends only on title, not page count."""
    t1 = PrintedBook("Same", 100)
    t2 = PrintedBook("Same", 200)
    t3 = PrintedBook("Other", 100)
    assert t1 == t2
    assert t1 != t3


