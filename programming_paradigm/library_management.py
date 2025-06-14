class Book:
    """Represents a book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return f'You have checked out "{self.title}".'
        return f'"{self.title}" is already checked out.'

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return f'You have returned "{self.title}".'
        return f'"{self.title}" was not checked out.'

    def is_available(self):
        """Checks whether the book is available."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books with checkout functionality."""

    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f'Error: "{title}" not found in the library.'

    def return_book(self, title):
        """Returns a book by title if it was checked out."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f'Error: "{title}" not found in the library.'

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [f'{book.title} by {book.author}' for book in self._books if book.is_available()]
        return "\n   ".join(available_books) if available_books else "No books are currently available."
