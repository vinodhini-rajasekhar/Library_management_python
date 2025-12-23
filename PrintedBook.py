from Book import Book

class PrintedBook(Book):
    """ Book that represents a printed book."""
    def __init__(self: "PrintedBook", title: str, num_pages: int) -> None:
        """Create a printed book with a title and number of pages."""
        super().__init__(title)
        self.__num_pages = num_pages

    @property
    def num_pages(self: "PrintedBook") -> int:
        """Return the number of pages in the printed book."""
        return self.__num_pages

    def get_length(self: "PrintedBook") -> str:
        """Return a page count."""
        return f"{self.num_pages} pages"

    def __str__(self: "PrintedBook") -> str:
        """Return a string of the printed book."""
        return f"{super().__str__()} Printed {self.get_length()}."



  