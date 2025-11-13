class Book:
    def __init__(self,book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies = self.available_copies - 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies = self.available_copies + 1
            return True
        return False
    
class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False