def input_str_val():
    return input("Enter Employee Name: ").strip().lower()


def input_int_val(msg):
    while True:
        valid_int_inp = input(msg)

        if not valid_int_inp.isdigit():
            print("\nInvalid input value. Please enter numbers only.")
            continue

        return int(valid_int_inp)


def show_result_list(result_list):
    if not result_list:
        print("\nNo employees found.")
    else:
        for emp in result_list:
            print("\n".join(emp))
