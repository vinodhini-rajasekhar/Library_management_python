from Book import Book

class EBook(Book):
    """ Book that represents an electronic book."""
    def __init__(self: "EBook", title: str, size_characters: int, chars_per_page: int) -> None:
        """Create an ebook with total size and characters per page."""
        super().__init__(title)
        self.__size_characters = size_characters
        self.__chars_per_page = chars_per_page

    @property
    def size_characters(self: "EBook") -> int:
        """Return the size of the ebook in characters."""
        return self.__size_characters

    @property
    def chars_per_page(self: "EBook") -> int: 
        """Return the number of characters per page."""
        return self.__chars_per_page

    def get_length(self: "EBook") -> str:
        """Return a human readable description of the ebook length."""
        return f"size {self.size_characters}, {self.chars_per_page} c/p"

    def __str__(self: "EBook") -> str:
        """Return a string representation of the ebook."""
        return f"{super().__str__()} Ebook ({self.get_length()})."
