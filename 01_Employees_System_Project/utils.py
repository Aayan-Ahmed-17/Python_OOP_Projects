def input_str_val():
    return input("Enter Employee Name: ").strip().lower()


def input_int_val(variable):
    while True:
        valid_int_inp = input(f"Enter Employee {variable}: ")

        if not valid_int_inp.isdecimal():
            print("Invalid input value. Please enter numbers only.")
            continue

        return int(valid_int_inp)
