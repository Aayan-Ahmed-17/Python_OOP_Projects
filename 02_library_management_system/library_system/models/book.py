from .library_item import LibraryItem

# PILLAR 2: INHERITANCE
# ---------------------
# Inheritance allows a class (Book) to inherit attributes and methods from another class (LibraryItem).
# 'Book' IS A 'LibraryItem'.

class Book(LibraryItem):
    """Represents a book in the library."""

    def __init__(self, item_id: str, title: str, author: str, isbn: str):
        # Call the parent class constructor
        super().__init__(item_id, title)
        self.author = author
        self.isbn = isbn

    # Implementation of the abstract method defined in LibraryItem
    def get_borrow_duration(self) -> int:
        return 14  # Books can be borrowed for 14 days

    def __str__(self):
        # Extending the parent's __str__ method
        return f"Book: {super().__str__()} by {self.author}"
