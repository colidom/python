class Employee:
    pass

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = name + '.' + surname + '@company.com'

    def full_name(self):
        return f"{self.name} {self.surname}"  


emp_1 = Employee('Carlos', 'Oliva', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

print(emp_1.email.lower())  # Prints the employee 1 email
print(emp_2.email)          # Prints the employee 2 email

print(emp_2.full_name())    # Prints the employee 1 name + surname
