from models import Employee

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

        # if filter_by is None
        return [emp for emp in self.employees]

    # update employee salary by name filter
    def update_employee_salary(self, name, new_salary):
        for emp in self.employees:
            if emp["name"] == name:
                emp["salary"] = int(new_salary)
                return emp

        return f"Employee {name} not found"
    
    def delete_one_employee(self, name):
        for emp in self.employees:
            if emp["name"] == name:
                del emp
                return f"Employee {name} deleted"
            
        return f"Employee {name} not found"


"""Test case"""
emp1 = EmployeesManager()
print(emp1.add_employee())
# print(emp1.employees[0])
