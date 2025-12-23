from __future__ import annotations
from datetime import date
from typing import Optional
from Library import Library
from Loan import Loan
from Patron import Patron
from Book import Book


def read_int(prompt: str) -> int:
    """Read an integer from input."""
    while True:
        value = input(prompt).strip()
        if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            return int(value)
        print("Please enter a valid integer.")


def read_date() -> Optional[date]:
    """Read a date in year month day format."""
    try:
        year_str = input("Enter due year (YYYY): ").strip()
        month_str = input("Enter due month (MM): ").strip()
        day_str = input("Enter due day (DD): ").strip()
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
        return date(year, month, day)
    except Exception:
        print("Invalid date. Loan will not be created.")
        return None


def add_patron_flow(lib: Library) -> None:
    """ option 1: add patron."""
    name = input("Enter patron name: ").strip()
    address = input("Enter patron address: ").strip()
    phone = input("Enter patron phone: ").strip()
    lib.add_patron(name, address, phone)
    patron = lib.search_patron(name)
    if patron is not None:
        print("Patron stored as:")
        print(patron)


def search_patron_flow(lib: Library) -> None:
    """ option 3: search patron and print info."""
    name = input("Enter patron name to search: ").strip()
    patron = lib.search_patron(name)
    if patron is None:
        print("Patron not found.")
    else:
        print("Patron found:")
        print(patron)


def search_book_flow(lib: Library) -> None:
    """ option 4: search book and print title and length."""
    title = input("Enter book title to search: ").strip()
    book = lib.search_book(title)
    if book is None:
        print("Book not found.")
    else:
        print("Book found:")
        print(book)
    


def checkout_book_flow(lib: Library) -> None:
    """ option 5: check out book."""
    title = input("Enter book title to check out: ").strip()
    patron_name = input("Enter patron name: ").strip()
    due = read_date()
    if due is None:
        return
    book = lib.search_book(title)
    patron = lib.search_patron(patron_name)
    if book is None:
        print("Book not found. Cannot check out.")
        return
    if patron is None:
        print("Patron not found. Cannot check out.")
        return
    if book.is_checked_out():
        print("Book is already checked out.")
        return
    lib.check_out_book(book, patron, due)
    loan = Loan(book, patron, due)
    print(str(loan))


def return_book_flow(lib: Library) -> None:
    """ option 6: return book."""
    title = input("Enter book title to return: ").strip()
    patron_name = input("Enter patron name: ").strip()
    book = lib.search_book(title)
    patron = lib.search_patron(patron_name)
    if book is None:
        print("Book not found. Cannot return.")
        return
    if patron is None:
        print("Patron not found. Cannot return.")
        return
    lib.return_book(book, patron)
    print(str(lib))


def add_book_flow(lib: Library) -> None:
    """ option 2: add book (printed, ebook, audio)."""
    while True:
        print("---------------------------------")
        print("            Add Book Menu")
        print("---------------------------------")
        print("A) Add Printed Book")
        print("B) Add Ebook")
        print("C) Add Audiobook")
        print("---------------------------------")
        choice = input("Enter choice (A/B/C) ").strip().upper()

        if choice not in {"A", "B", "C"}:
            print("Invalid choice. Please try again.")
            continue

        title = input("Enter book title: ").strip()

        if choice == "A":
            pages = read_int("Enter number of pages: ")
            lib.add_printed_book(title, pages)
        elif choice == "B":
            size_chars = read_int("Enter file size (chars): ")
            chars_pp = read_int("Enter characters per page: ")
            lib.add_ebook(title, size_chars, chars_pp)
        else:
            duration = read_int("Enter duration in seconds: ")
            lib.add_audio_book(title, duration)

        book = lib.search_book(title)
        if book is not None:
            print("Book stored as:")
            print(book)
        return

def main() -> None:
    """Main entry point for the library menu program."""
    library_name = input("Enter library name: ").strip() or "Library"
    lib = Library(library_name)

    while True:
        print("---------------------------------")
        print("       Library Main Menu")
        print("---------------------------------")
        print("1) Add Patron")
        print("2) Add Book")
        print("3) Search Patron")
        print("4) Search Book")
        print("5) Check Out Book")
        print("6) Return Book")
        print("99) Quit")
        print("---------------------------------")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_patron_flow(lib)
        elif choice == "2":
            add_book_flow(lib)
        elif choice == "3":
            search_patron_flow(lib)
        elif choice == "4":
            search_book_flow(lib)
        elif choice == "5":
            checkout_book_flow(lib)
        elif choice == "6":
            return_book_flow(lib)
        elif choice == "99":
            confirm = input("Are you sure you want to quit? (y/n): ").strip().lower()
            if confirm == "y":
                print("Goodbye.")
                break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
