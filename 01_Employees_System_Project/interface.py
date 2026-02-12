from manager import EmployeeManager

class Interface():
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
            input_action = input("Type number correspondent to the action number:  ")

            if not input_action.isdigit():
                print("Please insert valid input 1 - 6")
                continue

            match int(input_action):
                case 1:
                    name = input("Enter Employee Name :")
                    age = int(input("Enter Employee Age :"))
                    salary = int(input("Enter Employee Salary :"))
                    self.EmployeeManager.add_employee(name=name, age=age, salary=salary)
                case 2:
                    result = self.EmployeeManager.get_employees()
                    print(result)
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    break
                # end


running = Interface()
running.run()
