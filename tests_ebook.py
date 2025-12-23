from Book import Book
from EBook import EBook
import pytest

class MockBook(Book):
    """Mock book class"""
    def __init__(self: "Book", title: str) -> None:
        """Create mock intialisation"""
        super().__init__(title)
    def get_length(self: Book) -> str:
        """Abstract method implement"""
        return "dummy"

def test_book_valid_creation() -> None:
        """Test creating a simple Book instance."""
        b = MockBook("Just a Book")
        assert b.title == "Just a Book"
        assert str(b) == 'Book: "Just a Book".'
        assert isinstance(b, Book)
        assert not isinstance(b, EBook)


def test_valid_ebook_creation() -> None:
        """Happy Path: Creating a standard valid ebook."""
        ebook = EBook("The Matrix", 50000, 250)
        
        assert ebook.title == "The Matrix"
        assert ebook.size_characters == 50000
        assert ebook.chars_per_page == 250
        assert issubclass(EBook, Book)
        
        assert isinstance(ebook, Book)
        assert isinstance(ebook, EBook)

def test_boundary_zero_size() -> None:
        """Edge Case: An empty book (0 characters) is technically valid."""
        ebook = EBook("Empty Notes", 0, 100)
        assert ebook.size_characters == 0

def test_boundary_min_chars_per_page() -> None:
        """Edge Case: Minimum valid chars per page is 1."""
        ebook = EBook("One Word Page", 100, 1)
        assert ebook.chars_per_page == 1


def test_get_length_format() -> None:
        """Verify the exact string format of get_length."""
        ebook = EBook("Harry Potter", 100, 10)
        expected = "size 100, 10 c/p"
        assert ebook.get_length() == expected

def test_str_representation() -> None:
        """
        Verify the full __str__ method.
        Should combine Book __str__ and EBook details.
        """
        ebook = EBook("Dune", 9000, 300)
        expected = 'Book: "Dune". Ebook (size 9000, 300 c/p).'
        assert str(ebook) == expected

def test_properties_are_read_only() -> None:
        """
        CRITICAL FOR COVERAGE: Verify that size and chars_per_page cannot be set directly.
        This tests the property definition itself.
        """
        ebook = EBook("Test", 100, 10)
        with pytest.raises(AttributeError):
            ebook.size_characters = 500
            
        with pytest.raises(AttributeError):
            ebook.chars_per_page = 20





