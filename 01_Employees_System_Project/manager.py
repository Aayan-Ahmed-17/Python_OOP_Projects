from models import Employee

"""
This file manages CRUD operations of Employee()
"""


class EmployeeManager:
    def __init__(self):
        self.employees = [
            # {"name": "aayan ahmed", "age": 19, "salary": 40000},
            # {"name": "aayan", "age": 21, "salary": 300000},
            # {"name": "ahmed", "age": 25, "salary": 1800000},
        ]

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
        if not self.employees:
            return []

        # Handle filter_by salary or name input validation in run function
        """take a look on to it in future"""
        # if filter_by:
        #     result = [
        #         emp
        #         for emp in self.employees
        #         if emp.name == filter_by or emp.salary == filter_by
        #     ]

        return self.employees

    def get_one_employee(self, name):
        for emp in self.employees:
            if emp["name"] == name:
                return emp

        return []

    # update employee salary by name filter
    def update_salary(self, name, new_salary):
        # is_empty??

        for emp in self.employees:
            if emp.name == name:
                emp.salary = int(new_salary)
                return emp

        return f"Employee {name} not found"

    def delete_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                return f"Employee {name} deleted"

        return f"Employee {name} not found"


"""Test case"""
# emp1 = EmployeesManager()
# print(emp1.add_employee())
# # print(emp1.employees[0])
