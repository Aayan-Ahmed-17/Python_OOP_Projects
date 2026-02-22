from typing import Dict, List
from ..models.library_item import LibraryItem
from ..models.member import Member

# CONCEPT: COMPOSITION
# --------------------
# Composition is a design principle where a class "has a" collection of other objects.
# The LibraryManager "has" many LibraryItems and Members.
# It delegates work to these objects.

class LibraryManager:
    """The central controller for library operations."""

    def __init__(self):
        self._items: Dict[str, LibraryItem] = {}
        self._members: Dict[str, Member] = {}

    def add_item(self, item: LibraryItem):
        self._items[item.item_id] = item
        print(f"Added to catalog: {item}")

    def register_member(self, member: Member):
        self._members[member.member_id] = member
        print(f"Registered member: {member}")

    def borrow_item(self, member_id: str, item_id: str):
        if member_id not in self._members:
            print(f"Error: Member ID '{member_id}' not found.")
            return
        if item_id not in self._items:
            print(f"Error: Item ID '{item_id}' not found.")
            return

        member = self._members[member_id]
        item = self._items[item_id]

        try:
            item.borrow()  # Call method on the item (Abstraction/Inheritance)
            member.add_item(item_id)  # Update member record (Encapsulation)
            print(f"Success: {member.name} borrowed {item.title}")
            print(f"Due in: {item.get_borrow_duration()} days") # Polymorphism at work
        except ValueError as e:
            print(f"Error: {e}")

    def return_item(self, member_id: str, item_id: str):
        if member_id not in self._members or item_id not in self._items:
            print("Error: Invalid IDs.")
            return

        member = self._members[member_id]
        item = self._items[item_id]

        item.return_item()
        member.remove_item(item_id)
        print(f"Success: {member.name} returned {item.title}")

    def show_catalog(self):
        print("\n--- Library Catalog ---")
        for item in self._items.values():
            print(item)

    def show_members(self):
        print("\n--- Library Members ---")
        for member in self._members.values():
            print(member)
