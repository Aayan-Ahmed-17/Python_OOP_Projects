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
    
    #Update employee (Replace one only)
    def update_employee(self):
        name = input("Find Employee by name: ")
        updated_name = input("Enter updated name: ")
        updated_age = input("Enter updated age: ")
        updated_salary= input("Enter updated salary: ")
        update_logic = [emp =  for emp in self.employees if emp["name"] == name]
        update_logic = [num for num in range(10) if num > 2]
    
    
"""Test case"""
emp1 = EmployeesManager()
emp1.get_employees()
# print(emp1.employees[0])