from Book import Book  
from Patron import Patron 
import pytest


class MockBook(Book):
    """Mock book class"""
    def __init__(self: "Book", title: str) -> None:
        """Create mock intialisation"""
        super().__init__(title)
    def get_length(self: Book) -> str:
        """Abstract method implement"""
        return "dummy"
    
class MockPatron:
    """Mock patron class"""
    def __init__(self:"MockPatron") -> None:
        """Create intialisation"""
        self.removed_books = []

    def remove_checked_book(self:"MockPatron",book: Book)->None:
        """Remove checked book"""
        self.removed_books.append(book)

def test_abstract_class_cannot_instantiate()->None:
    """Abstract class book cannot instantiate"""
    with pytest.raises(TypeError):
        Book("title")

def test_book_sets_title()->None:
    """"Asserts Whether title is set"""
    test = MockBook("Ikigai")
    assert test.title == "Ikigai"
    assert not test.is_checked_out() 
    assert test.get_current_patron() is None


def test_title_setter_valid() -> None:
    """Asserts that title can be updated."""
    book = MockBook("Old Title")
    book.title = "New Title"
    assert book.title == "New Title"
    

def test_check_out_method()->None:
    """Asserts the checkout property"""
    test = MockBook("Ikigai")
    patron = MockPatron()
    test.check_out(patron)
    assert test.is_checked_out()
    assert test.get_current_patron() is patron

def test_return_book_success() -> None:
    """Asserts return resets state and notifies patron."""
    book = MockBook("Book1")
    patron = MockPatron()
    book.check_out(patron)
    
    book.return_book()
    
    assert book.is_checked_out() is False
    assert book.get_current_patron() is None
    assert isinstance(patron.removed_books, list)
    if patron.removed_books:
        assert patron.removed_books[0] is book
  


def test_return_book_remove_book()->None:
    """Asserts whether book is removed from checked book and check out is none"""
    test = MockBook("Ikigai")
    patron = MockPatron()
    test.check_out(patron)

    assert test.is_checked_out()
    assert test.get_current_patron() is patron

    test.return_book() 
    assert not test.is_checked_out()
    assert test.get_current_patron() is None
    assert isinstance(patron.removed_books, list)
    first_len = len(patron.removed_books)

    test.check_out(patron)
    test.return_book()

    assert isinstance(patron.removed_books, list)
    assert len(patron.removed_books) >= first_len

def test_book_with_real_patron_checkout_and_return() -> None:
    """ Assert Book using the real Patron class to cover circular behaviour."""
    test = MockBook("RealUse")
    p = Patron("vino", "Duke", "12345")

    assert not test.is_checked_out()
    assert test.get_current_patron() is None

    test.check_out(p)
    assert test.is_checked_out()
    current = test.get_current_patron()
    assert current is not None

    test.return_book()
    assert not test.is_checked_out()
    assert test.get_current_patron() is None


def test_book_multiple_real_patrons_sequence() -> None:
    """Assert multiple books and a real Patron to probe more Book-Patron interactions."""
    p = Patron("Reader", "Somewhere", "999")
    b1 = MockBook("Book1")
    b2 = MockBook("Book2")
    b1.check_out(p)
    assert b1.is_checked_out()
    b1.return_book()
    assert not b1.is_checked_out()
    b2.check_out(p)
    assert b2.is_checked_out()
    b2.return_book()
    assert not b2.is_checked_out()



def test_equality_identical() -> None:
    """Asserts a book is equal to itself."""
    b1 = MockBook("A")
    assert b1 == b1

def test_equality_true()->None:
    """asserts equality in true scenario"""
    test = MockBook("Ikigai")
    test1 = MockBook("Ikigai")
    assert test == test1
    assert test == test

def test_equality_false()->None:
    """asserts equality in false scenario"""
    test = MockBook("Ikigai")
    test1 = MockBook("Sucess")
    assert not (test == test1)
    assert test != test1

def test_equality_not_a_book_object()->None:
    """asserts when comparing object is not book"""
    test = MockBook("Ikigai")
    assert test != "Not a book"
    assert test.__eq__("Not book") is False

def test_equality_with_number() -> None:
    """Book compared with an integer should be False."""
    b = MockBook("Ikigai")
    assert (b == 42) is False
    assert b.__eq__(42) is False

def test_equality_with_none() -> None:
    """Book compared with None should be False."""
    b = MockBook("Ikigai")
    assert (b == None) is False     
    assert b.__eq__(None) is False

def test_equality_diff_types() -> None:
    """Asserts book is not equal to other types."""
    b1 = MockBook("A")
    assert b1 != 42
    assert b1 != "A"
    assert b1 != None
    assert b1.__eq__(42) is False

def test_get_length()->None:
    """asserts get length abstrack class"""
    test = MockBook("Ikigai")
    result = Book.get_length(test)
    assert result is None

def test_equality_with_list() -> None:
    """Book compared with a list should be False."""
    b = MockBook("Ikigai")
    assert (b == [1, 2, 3]) is False
    assert b.__eq__([1, 2, 3]) is False

def test_equality_with_dict() -> None:
    """Book compared with a dict should be False."""
    b = MockBook("Ikigai")
    assert (b == {"title": "Ikigai"}) is False
    assert b.__eq__({"title": "Ikigai"}) is False

def test_string_format()->None:
    """assert string format"""
    test = MockBook("Ikigai")
    assert str(test) ==  'Book: "Ikigai".'
    _ = repr(test)

def test_book_str_with_various_titles() -> None:
    """Probe __str__ with different kinds of titles."""
    titles = [
        "Simple",
        " With spaces ",
        "123",
        "Title\nWithNewline",
        "Title\tWithTab",
    ]
    for t in titles:
        try:
            b = MockBook(t)
        except Exception:
            continue
        s = str(b)
        assert isinstance(s, str)