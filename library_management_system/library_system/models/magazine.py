from .library_item import LibraryItem

# PILLAR 3: POLYMORPHISM
# ----------------------
# Polymorphism allows different classes to be treated as instances of the same parent class,
# BUT they can have different implementations of the same method.
# Here, 'get_borrow_duration' behaves differently for Book and Magazine.

class Magazine(LibraryItem):
    """Represents a magazine in the library."""

    def __init__(self, item_id: str, title: str, issue_number: int):
        super().__init__(item_id, title)
        self.issue_number = issue_number

    # Different implementation than Book
    def get_borrow_duration(self) -> int:
        return 3  # Magazines can only be borrowed for 3 days

    def __str__(self):
        return f"Magazine: {super().__str__()} (Issue #{self.issue_number})"
