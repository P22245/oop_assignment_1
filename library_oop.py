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
    
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.id] = book

    def add_member(self, member):
        self.members[member.id] = member

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            return self.members[member_id].borrow_book(self.books[book_id])
        return False

    def return_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            return self.members[member_id].return_book(self.books[book_id])
        return False

    def display_books(self):
        for book in self.books.values():
            print(f"{book.id}: {book.title} by {book.author} - {book.available_copies}/{book.total_copies} available")

    def display_members(self):
        for member in self.members.values():
            borrowed = [b.title for b in member.borrowed_books]
            print(f"{member.id}: {member.name} - Borrowed: {borrowed}")