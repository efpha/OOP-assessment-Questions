# Method Overriding
class Employee:
    def calculate_salary(self):
        print("Calculating salary...")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating manager's salary with bonus...")

emp = Employee()
mgr = Manager()
emp.calculate_salary()
mgr.calculate_salary()
