class Employee:
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first: str = first
        self.last: str = last
        self.pay: int = pay
        self.email = first + "." + last + "@gmail.com"


emp1 = Employee("sandesh", "pokhrel", 5000)


print(emp1.first)
print(emp1.last)
print(emp1.email)
