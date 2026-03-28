class employee_class:
    def __init__(self, name, age, role, team="staff"):
        self.name = name
        self.age = age
        self.role = role
        self.team = team
        self.company = "Adobe"
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.role}, {self.team}"
    
    def manager_name(self):
        if self.role == "QA":
            print("Manager is John")
        elif self.role == "IT":
            print("Manager is David")
        elif self.role == "Sales":
            print("Manager is Thomas")
        else:
            print("Manager unknown")
            
    def salary(self, salary):
        self.salary = salary
        if self.role == "DEVOPS":
            print(f"{self.name}s salary is {self.salary}")
        elif self.role == "CHEF":
            print(f"{self.name}'s salary is {self.salary}")


emp1 = employee_class("Alice", 30, "Sales")
emp2 = employee_class("Chris", 40, "DEVOPS", "SRE")

emp1.manager_name()
emp2.salary(100000)