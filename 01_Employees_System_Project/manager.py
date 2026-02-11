from Employee import Employee

"""
This file manages CRUD operation of Employee()
"""


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        """
        PURPOSE: Creates Employee() instance
        RETURN: Created Employee() instance
        """
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        return emp
            

    # Read Employees (Get All by condition or without)
    def get_employees(self, filter_by=None):
        if not len(self.employees):
            return []

        # Handle filter_by salary or name input validation in run function
        if filter_by:
            return [
                emp
                for emp in self.employees
                if emp["name"] == filter_by or emp["salary"] == filter_by
            ]

        return [emp for emp in self.employees]


"""Test case"""
emp1 = EmployeesManager()
print(emp1.add_employee())
# print(emp1.employees[0])
