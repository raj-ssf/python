class Employee:
    def __init__(self, name, age, role, team="staff"):
        self.name = name
        self.age = age
        self.role = role
        self.team = team
        self.company = "Adobe"
        self.salary = 0

    def set_salary(self, amount):
        self.salary = amount

    def raise_salary(self, percent):
        self.salary *= 1 + percent / 100

    def __str__(self):
        return f"{self.name}, age {self.age}, {self.role} in {self.team} at {self.company} | Salary: ${self.salary:,.2f}"

    
emp = Employee("Alice", 30, "QA")
emp.set_salary(80000)
print(emp)                 # should show name, role, salary
emp.raise_salary(10)       # 10% raise
print(emp)