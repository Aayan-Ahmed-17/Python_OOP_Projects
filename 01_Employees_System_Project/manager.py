from models import Employee

"""
This file manages CRUD operations of Employee()
"""


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        """
        PURPOSE: Creates Employee() instance
        RETURN: [emp]
        """
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        return [emp]

    # Read Employees (Get All by condition or without)
    def get_employees(self, filter_by=None):
        """
        PURPOSE: Get all employees with or without "filter_by"
        RETURN: [], self.employees
        """
        if not self.employees:
            return []

        return self.employees

    def get_one_employee(self, name):
        """
        PURPOSE: Get all employees with or without "filter_by"
        RETURN: [], [emp], []
        """
        if not self.employees:
            return []

        for emp in self.employees:
            if emp["name"] == name:
                return [emp]

        return []

    # update employee salary by name filter
    def update_salary(self, name, new_salary):
        """
        PURPOSE: Update employee salary through name filter
        RETURN: [], [emp], [] #for not found
        """
        if not self.employees:
            return []

        for emp in self.employees:
            if emp.name == name:
                emp.salary = int(new_salary)
                return [emp]

        return f"Employee {name} not found"

    def delete_employee(self, name):
        """
        PURPOSE: delete employee through name filter
        RETURN: [], [emp], [] #for not found
        """
        if not self.employees:
            return []

        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                return [emp]

        return []
