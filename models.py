class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = int(age)
        self.salary = int(salary)

    def __repr__(self):
        return f"Employee(name={self.name!r}, age={self.age}, salary={self.salary})"

    def __str__(self):
        return f"{self.name} | {self.age} yrs | Rs {self.salary}"

