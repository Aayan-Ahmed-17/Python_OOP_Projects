from manager import EmployeeManager


def print_menu():
    return [
        "1. Add Employee",
        "2. See Employees",
        "3. Search first Employee by 'name'",
        "4. Update employee salary by 'name'",
        "5. Delete employee by 'name'",
    ]


print("\nPerform actions: ")
print('\n'.join(print_menu()))
