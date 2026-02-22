from abc import ABC, abstractmethod

# PILLAR 1: ABSTRACTION
# ---------------------
# Abstraction means hiding the internal complexity and only showing the essential features.
# We use ABC (Abstract Base Class) to define a "template" that other classes must follow.
# You cannot create an object of 'LibraryItem' directly.

class LibraryItem(ABC):
    """Abstract base class representing any item in the library."""

    def __init__(self, item_id: str, title: str):
        self._item_id = item_id  # Encapsulation (protected attribute)
        self._title = title
        self._is_borrowed = False

    @property
    def title(self) -> str:
        return self._title

    @property
    def item_id(self) -> str:
        return self._item_id

    @property
    def is_borrowed(self) -> bool:
        return self._is_borrowed

    @abstractmethod
    def get_borrow_duration(self) -> int:
        """Each type of item (Book, Magazine) will define its own duration."""
        pass

    def borrow(self):
        if self._is_borrowed:
            raise ValueError(f"Item '{self._title}' is already borrowed.")
        self._is_borrowed = True
        print(f"Borrrowed: {self._title}")

    def return_item(self):
        self._is_borrowed = False
        print(f"Returned: {self._title}")

    def __str__(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"[{self.item_id}] {self.title} ({status})"
