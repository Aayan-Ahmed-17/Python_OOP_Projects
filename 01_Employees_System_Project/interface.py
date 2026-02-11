from manager import EmployeeManager

def run():
    manager = EmployeeManager()

    # Create
    emp = manager.add_employee("Aayan", 22, 40000)
    print(emp)

    # Update
    # updated_emp = manager.update_employee_salary("Aayan", 50000)
    # print(updated_emp)

    # List
    print(manager.get_employees())
    
run()