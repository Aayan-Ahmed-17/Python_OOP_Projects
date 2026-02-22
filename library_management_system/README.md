# 📚 Library Management System (Python OOP)

Welcome! This project is a beginner-friendly Library Management System designed to demonstrate core **Object-Oriented Programming (OOP)** principles in a real-world scenario.

---

## 📋 Prerequisites

- **Python 3.x**

## 🧠 Concepts Used

### Object-Oriented Programming (OOP)

- **Abstraction** (Abstract Base Classes)
- **Inheritance** (Child classes inheriting from Base)
- **Polymorphism** (Method Overriding)
- **Encapsulation** (Private/Protected attributes)
- **Composition** (Classes containing other objects)
- **Classes and Objects**
- **Methods and Attributes**
- **Properties** (`@property` decorator)
- **Constructors** (`__init__`)
- **String Representation** (`__str__`)

### General Python Concepts

- **Type Hinting** (`List`, `Dict`)
- **Dictionaries**
- **Lists**
- **Modules and Packages**
- **Imports** (Relative and Absolute)
- **Exception Handling** (`try`, `except`, `raise`)
- **Conditionals** (`if`, `else`)
- **Loops** (`for`)
- **Functions**
- **F-Strings** (String formatting)
- **Entry Point Pattern** (`if __name__ == "__main__":`)

---

## 🏗️ Project Architecture

To understand how this system works, you should look at it as three main layers:

1.  **The Base (Models)**: Where we define "what" things are (Books, Magazines, Members).
2.  **The Controller (Services)**: Where the rules are enforced (LibraryManager).
3.  **The Entry Point (main.py)**: Where the simulation actually starts.

---

## 🛤️ Code Flow (Reverse Engineering Guide)

If you want to understand the code, follow this trail:

### 1. `main.py` (The Director)

- **Purpose**: Orchestrates the entire program.
- **What to look for**: It creates objects (like `Book` and `Member`) and passes them to the `LibraryManager`.
- **Flow**: It calls `library.add_item()` ➡️ `library.register_member()` ➡️ `library.borrow_item()`.

### 2. `library_system/models/library_item.py` (The Blueprint)

- **Concept**: **Abstraction**.
- **Logic**: This is an "Abstract Base Class" (ABC). It defines that every item _must_ have an ID and a title, and it _must_ define how long it can be borrowed via `get_borrow_duration()`.

### 3. `library_system/models/book.py` & `magazine.py` (The Variants)

- **Concept**: **Inheritance** & **Polymorphism**.
- **Logic**:
  - They "Inherit" all the logic from `LibraryItem`.
  - They "Override" the `get_borrow_duration()`. A book returns 14, a magazine returns 3. This is Polymorphism: the same method name giving different results based on the object type.

### 4. `library_system/models/member.py` (The Data Guard)

- **Concept**: **Encapsulation**.
- **Logic**: The list of borrowed items is "private" (denoted by `_borrowed_items`). You can't reach in and change it directly; you must use the `add_item()` method. This keeps your data safe from bugs.

### 5. `library_system/services/library_manager.py` (The Brain)

- **Concept**: **Composition**.
- **Logic**: This class "has-a" collection of Items and Members. It doesn't inherit from them; it uses them to perform complex actions like "Borrowing," which involves checking if an item exists and then updating both the Item status and the Member's record.

---

## 🚀 How to Run

1.  Ensure you have Python installed.
2.  Open your terminal/command prompt.
3.  Navigate to the `library_management_system` folder.
4.  Run the following command:
    ```bash
    python main.py
    ```

## 🛠️ Key Learning Exercises for You

To level up your OOP skills, try adding these features:

1.  **Late Fees**: Add a method to calculate a fine if the item is returned late.
2.  **Search**: Add a method to `LibraryManager` to find a book by its title.
3.  **DVDs**: Create a new class `DVD` that inherits from `LibraryItem`. How long should the borrow duration be?
