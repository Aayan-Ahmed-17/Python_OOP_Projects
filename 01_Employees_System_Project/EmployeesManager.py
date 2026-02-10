from Employee import Employee

"""
This file manages CRUD operation of Employee()
"""

class EmployeesManager():
    def __init__(self):
        self.employees = []
        
    #Create Employee() instance
    def create_employee(self):
        print("\nEnter Employee data")
        name = input("Enter Employee name: ")
        age = input("Enter Employee age: ")
        salary = input("Enter Employee salary: ")
        self.employees.append(Employee(name, age, salary))
        
    #Read Employees (All Employees)
    def get_employees(self):
        if not len(self.employees):
            print("No employee data")
            return
        
        for emp in self.employees:
            print(emp)
            return
    
"""Test case"""
emp1 = EmployeesManager()
emp1.get_employees()
# print(emp1.employees[0])