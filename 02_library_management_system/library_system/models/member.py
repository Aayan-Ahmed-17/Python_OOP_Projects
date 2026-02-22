from typing import List

# PILLAR 4: ENCAPSULATION
# -----------------------
# Encapsulation is the bundling of data and the methods that operate on that data.
# We restrict direct access to some components using underscores (e.g., _borrowed_items).
# This prevents accidental modification and keeps the internal state safe.

class Member:
    """Represents a library member."""

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self._borrowed_items: List[str] = []  # Encapsulated (Private-ish)

    @property
    def borrowed_items(self):
        # Providing a read-only view of borrowed items
        return self._borrowed_items.copy()

    def add_item(self, item_id: str):
        if item_id in self._borrowed_items:
            raise ValueError("Item already in member's list.")
        self._borrowed_items.append(item_id)

    def remove_item(self, item_id: str):
        if item_id in self._borrowed_items:
            self._borrowed_items.remove(item_id)

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id}, Items: {len(self._borrowed_items)})"
