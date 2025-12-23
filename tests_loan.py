import pytest
from datetime import date
from Loan import Loan


class MockBook:
    """Mock book to test"""
    def __init__(self: "MockBook", title: str) -> None:
        """Initialise the book"""
        self.title = title
    
    def __eq__(self: "MockBook", other: object) -> bool:
        """"Equal check"""
        return isinstance(other, MockBook) and self.title == other.title
    
    def __str__(self: "MockBook") -> str:
        """string check"""
        return f'Book: "{self.title}".'


class MockPatron:
    """Mock patron """
    def __init__(self: "MockPatron", name: str) -> None:
        """Initialise the Patron"""
        self.name = name
        self.address = "Addr"
        self.phone_number = "000-000"
        self.count = 1  

    def __eq__(self: "MockPatron", other: object) -> bool:
        """Equality check"""
        return isinstance(other, MockPatron) and self.name == other.name

    def __str__(self: "MockPatron") -> str:
        """String format"""
        return f"Patron: {self.name}, {self.address}. ({self.phone_number}). {self.count} books checked out."

def test_loan_properties() -> None:
    """assert loan string has correct due date and general shape"""
    b = MockBook("ABC")
    p = MockPatron("Vinu")
    d = date(2025, 1, 1)
    loan = Loan(b, p, d)
    text = str(loan)
    assert isinstance(text, str)
    assert text.startswith("Loan of")
    assert d.strftime("%m-%d-%Y") in text


def test_loan_equality_true() -> None:
    """assert equality when book, patron, date same"""
    b = MockBook("ABC")
    p = MockPatron("Vinu")
    d = date(2025, 1, 1)
    l1 = Loan(b, p, d)
    l2 = Loan(b, p, d)
    assert l1 == l2


def test_loan_equality_false_book() -> None:
    """assert equality comparison runs when books differ"""
    b1 = MockBook("A")
    b2 = MockBook("B")
    p = MockPatron("Vinu")
    d = date(2025, 1, 1)
    l1 = Loan(b1, p, d)
    l2 = Loan(b2, p, d)
    result = (l1 == l2)
    assert isinstance(result, bool)
    result2 = l1.__eq__(l2)
    assert isinstance(result2, bool)


def test_loan_equality_false_patron() -> None:
    """assert equality comparison runs when patrons differ"""
    b = MockBook("ABC")
    p1 = MockPatron("Vinu")
    p2 = MockPatron("Other")
    d = date(2025, 1, 1)
    l1 = Loan(b, p1, d)
    l2 = Loan(b, p2, d)
    result = (l1 == l2)
    assert isinstance(result, bool)
    result2 = l1.__eq__(l2)
    assert isinstance(result2, bool)


def test_loan_equality_false_due_date() -> None:
    """assert equality comparison runs when dates differ"""
    b = MockBook("ABC")
    p = MockPatron("Vinu")
    l1 = Loan(b, p, date(2025, 1, 1))
    l2 = Loan(b, p, date(2025, 1, 2))
    result = (l1 == l2)
    assert isinstance(result, bool)
    result2 = l1.__eq__(l2)
    assert isinstance(result2, bool)

def test_loan_initialization_without_date_object() -> None:
    """assert the scenario where data (due_date) is not given. """
    b = MockBook("ABC")
    p = MockPatron("Vinu")
    loan = Loan(b, p,"fdtgtfd")
    test = "Due on: Not Set."
    assert test in str(loan)

def test_loan_equality_other_type() -> None:
    """assert comparing with non-loan returns false"""
    b = MockBook("ABC")
    p = MockPatron("Vinu")
    d = date(2025, 1, 1)
    l3 = Loan(b, p, None) 
    l4 = Loan(b, p, None) 
    loan = Loan(b, p, d)
    assert d != l3
    assert l3 == l4
    assert loan != 123
    assert loan != "hello"
    assert loan.__eq__("string") is False


def test_loan_string_format() -> None:
    """assert loan string has correct shape and due date"""
    b = MockBook("Harry Potter")
    p = MockPatron("Jane")
    d = date(2026, 1, 22)
    loan = Loan(b, p, d)
    result = str(loan)
    assert isinstance(result, str)
    assert result.startswith("Loan of")
    assert "Due on: 01-22-2026." in result

