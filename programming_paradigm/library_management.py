class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def checked_out(self):
        if not self._is_checked_out:
            self._is_checked_out= True
            return f"You have checked out {self.title}."
        return f"{self.title} is already checked out"
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"You have returned {self.title}."
        return f"{self.title} was not checked out."
    def available_book(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.checked_out()
        return f"Book {title} is unavailable."        
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f"Book {title} is unavailable."
    def list_available_books(self):
        available = [f'{book.title} by {book.author}' for book in self._books if book.available_book()]
        return "\n   ".join(available) if available else "No books are currently available."
    
            
