from Book import Book, Patron  
from LinkedList import LinkedList

class Patron:
    """Represents a library patron."""
    def __init__(self: "Patron", name: str, address: str, phone_number: str) -> None:
        """Create a patron with name, address and phone number."""
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__list_checked_books = LinkedList()

    @property
    def name(self: "Patron") -> str:
        """Return the patron's name."""
        return self.__name

    @name.setter
    def name(self: "Patron", value: str) -> None:
        """Set the patron's name."""
        self.__name = value

    @property
    def address(self: "Patron") -> str:
        """Return the patron's address."""
        return self.__address

    @address.setter
    def address(self: "Patron", value: str) -> None:
        """Set the patron's address."""
        self.__address = value

    @property
    def phone_number(self: "Patron") -> str:
        """Return the patron's phone number."""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self: "Patron", value: str) -> None:
        """Set the patron's phone number."""
        self.__phone_number = value

    @property
    def list_checked_books(self: "Patron") -> LinkedList:
        """Return the list of checked out books."""
        return self.__list_checked_books

    def add_checked_book(self: "Patron", book: Book) -> None:
        """Add a checked out book to the patron's list."""
        self.list_checked_books.insert(book)

    def remove_checked_book(self: "Patron", book: Book) -> None:
        """Remove a checked out book from the patron's list."""
        if self.list_checked_books.isEmpty():
          return
        found = self.list_checked_books.search(book)
        if found is None:
         return
        self.list_checked_books.delete(book)

    
    def is_book_checked_out_by_patron(self: "Patron", book: Book) -> bool:
        """Return True if this patron has the given book checked out. """
        found = self.list_checked_books.search(book)
        return found is not None

    def __eq__(self: "Patron", rhs: object) -> bool:
        """Return True if this patron is equal to rhs."""
        if  isinstance(rhs,Patron):
             return self.__name == rhs.__name
        return False

    def __str__(self: "Patron") -> str:
        """Return a string representation of the patron."""
        return f"Patron: {self.name}, {self.address} ({self.phone_number}). {len(self.list_checked_books)} books checked out."