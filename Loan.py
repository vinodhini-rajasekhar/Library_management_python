from datetime import date
from typing import Optional
from Book import Book
from Patron import Patron


class Loan:
    """Represents a loan of a book to a patron."""
    def __init__(self: "Loan", book: Book, patron: Patron, due_date: date) -> None:
        """Create a loan for the given book, patron and due date."""
        self.__due_date = due_date
        self.__checked_out_patron = patron
        self.__borrowed_book = book
   
    @property
    def book(self: "Loan") -> Book:
        """Return the borrowed book."""
        return self.__borrowed_book
    
    @property
    def patron(self: "Loan") -> Patron:
        """Return the patron who checked out the book."""
        return self.__checked_out_patron
    
    @property
    def due_date(self: "Loan") -> date:
        """Return the due date for this loan."""
        return self.__due_date
    
    def __eq__(self: "Loan",other:object ) -> bool:
        """Returns the equalilty check"""
        if  not isinstance(other, Loan):
            return False
        return (
            self.book == other.book
            and self.patron == other.patron
            and self.due_date == other.due_date
        )

    def __str__(self: "Loan") -> str:
        """Return a string representation of the loan."""
        if not isinstance(self.due_date,date):
            due = "Not Set"
        else:
            due = self.due_date.strftime("%m-%d-%Y")
        return (
            f"Loan of {str(self.book)} "
            f"to {str(self.patron)} "
            f"Due on: {due}."
        )


