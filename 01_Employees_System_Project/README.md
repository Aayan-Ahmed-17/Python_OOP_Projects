# Employee Management System

A command-line interface (CLI) based Employee Management System built with Python, demonstrating Object-Oriented Programming (OOP) principles. This project provides a simple yet effective way to manage employee records with full CRUD (Create, Read, Update, Delete) operations.

## Table of Contents

- [Overview](#overview)
- [File Structure](#file-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [OOP Concepts Used](#oop-concepts-used)
- [Current Functionality](#current-functionality)
- [Future Goals](#future-goals)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Employee Management System is a learning project focused on implementing Object-Oriented Programming concepts in Python. The application provides a text-based interface for managing employee data including name, age, and salary information.

## File Structure

```
employee-management-system/
│
├── main.py           # Entry point of the application
├── interface.py      # CLI-based user interface and command handling
├── manager.py        # EmployeeManager class with CRUD operations
├── models.py         # Employee class definition with dunder methods
└── utils.py          # Utility functions for input validation and display
```

### File Descriptions

- **main.py**: The main file that runs the application and initializes the program flow
- **interface.py**: Handles all CLI-based user interactions, menu display, and command processing
- **manager.py**: Contains the `EmployeeManager` class that manages all CRUD operations for employees
- **models.py**: Defines the `Employee` base class with `__init__`, `__str__`, and `__repr__` dunder methods
- **utils.py**: Provides utility functions for input validation and result display

## Features

- ✅ Add new employees with name, age, and salary
- ✅ View all employees or filter by specific criteria
- ✅ Retrieve individual employee details
- ✅ Update employee salary information
- ✅ Delete employee records
- ✅ Input validation for strings and integers
- ✅ Clean CLI-based interface

## Prerequisites

- Python 3.6 or higher
- Basic understanding of Python programming
- Command-line interface (Terminal/Command Prompt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/employee-management-system.git
```

2. Navigate to the project directory:
```bash
cd employee-management-system
```

3. Run the application:
```bash
python main.py
```

## Usage

Run the main script to start the application:

```bash
python main.py
```

Follow the on-screen prompts to:
- Add new employees
- View employee list
- Search for specific employees
- Update employee salaries
- Delete employee records

## OOP Concepts Used

### Currently Implemented:
- **Classes and Objects**: `Employee` class representing employee entities, `EmployeeManager` class for operations
- **Dunder Methods**: Implementation of `__init__`, `__str__`, and `__repr__` in the Employee class
- **Encapsulation**: Data and methods grouped within appropriate classes

### Planned for Future Implementation:
- **Inheritance**: Creating specialized employee types (Manager, Developer, Intern)
- **Polymorphism**: Method overriding for different employee behaviors
- **Abstraction**: Abstract base classes for common employee functionalities
- **Encapsulation (Advanced)**: Private and protected attributes using name mangling

## Current Functionality

### EmployeeManager Class Methods

- `__init__(self)`: Initializes the employee manager
- `add_employee(self, name, age, salary)`: Adds a new employee to the system
- `get_employees(self, filter_by=None)`: Retrieves all employees or filtered list
- `get_one_employee(self, name)`: Fetches a specific employee by name
- `update_salary(self, name, new_salary)`: Updates an employee's salary
- `delete_employee(self, name)`: Removes an employee from the system

### Utility Functions

- `input_str_val()`: Validates and accepts string input (used for employee names)
- `input_int_val(msg)`: Validates and accepts integer input (used for age and salary)
- `show_result_list(result_list)`: Displays employee records in a formatted manner

## Future Goals

### Short-term Goals:
- [ ] Implement the four pillars of OOP (Inheritance, Polymorphism, Encapsulation, Abstraction)
- [ ] Create specialized employee classes (Manager, Developer, HR, Intern)
- [ ] Add data persistence using JSON or CSV files
- [ ] Implement search and filter by multiple criteria (age range, salary range)
- [ ] Add input validation and error handling improvements

### Long-term Goals:
- [ ] Implement SQLite database integration
- [ ] Add department management functionality
- [ ] Create reporting and analytics features
- [ ] Build a GUI using Tkinter or PyQt
- [ ] Add unit tests using pytest
- [ ] Implement logging functionality
- [ ] Create user authentication system
- [ ] Export reports to PDF/Excel formats

## Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This is a learning project created to understand and implement Object-Oriented Programming concepts in Python. The codebase is actively being developed and improved.
