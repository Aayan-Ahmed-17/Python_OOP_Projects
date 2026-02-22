from library_system.services.library_manager import LibraryManager
from library_system.models.book import Book
from library_system.models.magazine import Magazine
from library_system.models.member import Member

def main():
    # Initialize the library system
    library = LibraryManager()

    # 1. Add some items (Books and Magazines)
    # Demonstrates Inheritance & Polymorphism
    book1 = Book("B001", "Python Crash Course", "Eric Matthes", "978-1593279288")
    book2 = Book("B002", "Clean Code", "Robert C. Martin", "978-0132350884")
    mag1 = Magazine("M001", "National Geographic", 1024)
    
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(mag1)

    # 2. Register a member
    # Demonstrates Encapsulation
    member1 = Member("MEM01", "John Doe")
    library.register_member(member1)

    # 3. Interactive Loop (Simplified for demo)
    print("\n--- Starting Library Simulation ---")
    
    # Borrowing a book (14 days)
    library.borrow_item("MEM01", "B001")
    
    # Borrowing a magazine (3 days - Polymorphism)
    library.borrow_item("MEM01", "M001")

    # Showing state
    library.show_catalog()
    library.show_members()

    # Returning items
    print("\n--- Returning process ---")
    library.return_item("MEM01", "B001")
    
    # Final check
    library.show_catalog()
    library.show_members()

if __name__ == "__main__":
    main()
