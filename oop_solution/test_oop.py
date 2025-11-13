class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False


class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print("Error: No copies available!")
            return False
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        else:
            print("Error: No copies available!")
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
            return True
        else:
            print("Error: This member hasn't borrowed this book!")
            return False


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully!")

    def add_member(self, member):
        self.members[member.id] = member
        print(f"Member '{member.name}' registered successfully!")

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Error: Member not found!")
            return False
        if book_id not in self.books:
            print("Error: Book not found!")
            return False
        return self.members[member_id].borrow_book(self.books[book_id])

    def return_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.books:
            print("Error: Member or book not found!")
            return False
        return self.members[member_id].return_book(self.books[book_id])

    def display_available_books(self):
        for book in self.books.values():
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available  ")

    def display_member_books(self, member_id):
        if member_id not in self.members:
            print("Error: Member not found!")
            return
        member = self.members[member_id]
        print(f"\n=== Books borrowed by {member.name} ===")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books currently borrowed")


def test_library_system():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    library = Library()

    # TEST 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    library.add_book(Book(1, "Python Crash Course", "Eric Matthes", 3))
    library.add_book(Book(2, "Clean Code", "Robert Martin", 2))
    library.add_book(Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1))
    library.add_book(Book(4, "Design Patterns", "Gang of Four", 2))

    # TEST 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    library.add_member(Member(101, "Alice Smith", "alice@email.com"))
    library.add_member(Member(102, "Bob Jones", "bob@email.com"))
    library.add_member(Member(103, "Carol White", "carol@email.com"))

    # TEST 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    # TEST 4: Successful Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    library.borrow_book(101, 1)
    library.borrow_book(101, 2)
    library.borrow_book(102, 1)

    # TEST 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)
    library.display_member_books(102)
    library.display_member_books(103)

    # TEST 6: Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    library.display_available_books()

    # TEST 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    library.borrow_book(103, 3)
    library.display_available_books()

    # TEST 8: Attempting to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    library.borrow_book(102, 3)

    # TEST 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    library.borrow_book(101, 4)
    library.display_member_books(101)
    library.borrow_book(101, 3)

    # TEST 10: Returning Books
    print("\n--- TEST 10: Returning Books ---")
    library.return_book(101, 1)
    library.return_book(102, 1)
    library.display_member_books(101)
    book = library.books[4]
    print(f"\n{book.title} by {book.author} - {book.available_copies} copies available")

    # TEST 11: Attempting Invalid Return
    print("\n--- TEST 11: Attempting Invalid Return ---")
    library.return_book(102, 2)

    # TEST 12: Return and Re-borrow
    print("\n--- TEST 12: Return and Re-borrow ---")
    library.return_book(103, 3)
    library.borrow_book(102, 3)
    library.display_member_books(102)

    # TEST 13: Error Handling
    print("\n--- TEST 13: Error Handling ---")
    library.borrow_book(999, 1)
    library.borrow_book(101, 999)
    library.return_book(999, 1)
    library.display_member_books(999)

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for member in library.members.values():
        for book in member.borrowed_books:
            print(f"  {member.name} has '{book.title}")

    print("\nAll Members and Their Books:")
    for member in library.members.values():
        print(f"\n{member.name} ({member.id}):")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")

    print("\n=== Available Books ===")
    library.display_available_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

# Run the comprehensive test
if __name__ == "__main__":
    test_library_system()