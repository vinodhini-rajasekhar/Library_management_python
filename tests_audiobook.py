from Book import Book
from AudioBook import AudioBook
import pytest

def test_audiobook_valid_init() -> None:
    """Assert valid AudioBook."""
    ab = AudioBook("The Hobbit", 36000)
    assert ab.title == "The Hobbit"
    assert ab.duration_seconds == 36000
    assert isinstance(ab, Book)
    assert isinstance(ab, AudioBook)


def test_get_length_formatting() -> None:
    """Assert get_length formats large numbers with commas."""
    ab = AudioBook("Long Book", 120500)
    assert ab.get_length() == "120,500 sec"

def test_str_representation() -> None:
    """Assert the full string representation."""
    ab = AudioBook("Dune", 75000)
    expected = 'Book: "Dune". Audio - Duration: 75,000 sec.'
    assert str(ab) == expected

def test_duration_is_read_only() -> None:
    """Assert that duration_seconds cannot be modified after creation."""
    ab = AudioBook("Test", 100)
    with pytest.raises(AttributeError):
        ab.duration_seconds = 200