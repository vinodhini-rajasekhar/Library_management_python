import pytest
from Book import Book
from Patron import Patron

class DummyBook(Book):
    """Dummy concrete Book for patron tests."""
    def __init__(self: "DummyBook", title: str) -> None:
        """Asserts constructor sets title."""
        super().__init__(title)

    def get_length(self: "DummyBook") -> str:
        """Asserts dummy length implementation."""
        return "dummy"


def test_patron_initialization_and_attributes() -> None:
    """Asserts patron initializes name address and phone correctly."""
    p = Patron("Vinu", "Duke", "12345")
    assert p.name == "Vinu"
    assert p.address == "Duke"
    assert p.phone_number == "12345"
    b = DummyBook("Some Book")
    assert p.is_book_checked_out_by_patron(b) is False


def test_name_getter_and_setter() -> None:
    """Asserts name property get and set work."""
    p = Patron("Vinu", "Duke", "12345")
    assert p.name == "Vinu"
    p.name = "New Name"
    assert p.name == "New Name"


def test_address_getter_and_setter_valid() -> None:
    """Asserts address property get and set with valid value."""
    p = Patron("Vinu", "Duke", "12345")
    assert p.address == "Duke"
    p.address = "Durham"
    assert p.address == "Durham"


def test_phone_number_getter_and_setter() -> None:
    """Asserts phone_number property get and set work."""
    p = Patron("Vinu", "Duke", "12345")
    assert p.phone_number == "12345"
    p.phone_number = "99999"
    assert p.phone_number == "99999"


def test_add_checked_book_inserts_into_list() -> None:
    """Asserts add_checked_book makes is_book_checked_out_by_patron true."""
    p = Patron("Vinu", "Duke", "12345")
    b1 = DummyBook("Book1")
    b2 = DummyBook("Book2")

    p.add_checked_book(b1)
    p.add_checked_book(b2)

    assert p.is_book_checked_out_by_patron(b1) is True
    assert p.is_book_checked_out_by_patron(b2) is True
    s = str(p)
    assert "books checked out" in s

def test_remove_checked_book_not_in_list_no_error() -> None:
    """assert remove does nothing when book not present"""
    p = Patron("Vinu", "Duke", "12345")
    present = DummyBook("Present")
    missing = DummyBook("Missing")
    p.add_checked_book(present)
    assert p.is_book_checked_out_by_patron(present) is True
    result = p.remove_checked_book(missing)
    assert result is None
    assert p.is_book_checked_out_by_patron(present) is True



def test_remove_checked_book_empty() -> None:
    """Asserts remove_checked_book on empty list does not raise."""
    p = Patron("Vinu", "Duke", "12345")
    b = DummyBook("Book1")
    p.remove_checked_book(b)
    assert p.is_book_checked_out_by_patron(b) is False


def test_remove_checked_book_existing_book() -> None:
    """Asserts remove_checked_book removes only that book."""
    p = Patron("Vinu", "Duke", "12345")
    b1 = DummyBook("Book1")
    b2 = DummyBook("Book2")
    p.add_checked_book(b1)
    p.add_checked_book(b2)
    assert p.is_book_checked_out_by_patron(b1) is True
    assert p.is_book_checked_out_by_patron(b2) is True
    p.remove_checked_book(b1)
    assert p.is_book_checked_out_by_patron(b1) is False
    assert p.is_book_checked_out_by_patron(b2) is True

def test_remove_checked_book_from_empty_list_no_error() -> None:
    """assert removing on empty list does nothing"""
    p = Patron("Vinu", "Duke", "123")
    result = p.remove_checked_book(DummyBook("X"))
    assert result is None
   


def test_is_book_checked_out_by_patron_true_and_false() -> None:
    """Asserts is_book_checked_out_by_patron returns correct boolean."""
    p = Patron("Vinu", "Duke", "12345")
    b1 = DummyBook("Book1")
    b2 = DummyBook("Book2")
    p.add_checked_book(b1)
    assert p.is_book_checked_out_by_patron(b1) is True
    assert p.is_book_checked_out_by_patron(b2) is False


def test_patron_equality_same_name_true() -> None:
    """Asserts patrons with same name are equal."""
    p1 = Patron("Vinu", "Addr1", "111")
    p2 = Patron("Vinu", "Addr2", "222")
    assert p1 == p2


def test_patron_equality_different_name_false() -> None:
    """Asserts patrons with different names are not equal."""
    p1 = Patron("Vinu", "Addr1", "111")
    p2 = Patron("Other", "Addr2", "222")
    assert p1 != p2
    assert (p1 == p2) is False


def test_patron_equality_with_other_type_false() -> None:
    """Asserts patron compared to non patron returns False."""
    p = Patron("Vinu", "Duke", "12345")
    assert p != "Vinu"
    assert p.__eq__("Vinu") is False


def test_patron_str_representation_content() -> None:
    """Asserts __str__ includes name address phone and mentions books."""
    p = Patron("Vinu", "Duke", "12345")
    b1 = DummyBook("Book1")
    p.add_checked_book(b1)
    s = str(p)
    assert "Vinu" in s
    assert "Duke" in s
    assert "12345" in s
    assert "books checked out" in s
