from manager import EmployeeManager
from utils import input_str_val, input_int_val, show_result_list


class Interface:
    def __init__(self):
        self.EmployeeManager = EmployeeManager()

    def print_menu(self):
        return [
            "1. Add Employee",
            "2. See Employees",
            "3. Search first Employee by 'name'",
            "4. Update employee salary by 'name'",
            "5. Delete employee by 'name'",
            "6. Exit",
        ]

    def run(self):
        while True:
            print("\nPerform actions: ")
            print("\n".join(self.print_menu()))
            input_action = input_int_val("Type number correspondent to the action: ")

            if not (0 < input_action <= len(self.print_menu())):
                print("\nOnly numbers 1 - 6 are allowed")
                continue

            match int(input_action):
                case 1:
                    name = input_str_val()
                    age = input_int_val("Enter Employee age: ")
                    salary = input_int_val("Enter Employee salary: ")
                    result = self.EmployeeManager.add_employee(
                        name=name, age=age, salary=salary
                    )
                    show_result_list(result)
                case 2:
                    result = self.EmployeeManager.get_employees()
                    show_result_list(result)
                case 3:
                    name = input_str_val()
                    result = self.EmployeeManager.get_one_employee(name)
                    show_result_list(result)
                case 4:
                    name = input_str_val()
                    new_salary = input_int_val("Enter Employee age: ")
                    result = self.EmployeeManager.update_salary(
                        name=name, new_salary=new_salary
                    )
                    show_result_list(result)
                case 5:
                    name = input("Enter Employee name: ")
                    result = self.EmployeeManager.delete_employee(name=name)
                    show_result_list(result)
                case 6:
                    break

