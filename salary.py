# inheritance in python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, salary=0):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"


class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        self.salary = self.hourly_rate * self.hours_worked
        return self.salary


class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        self.salary = self.monthly_salary
        return self.salary


emp1 = HourlyEmployee(100, "Joy", 2062, 160)
emp2 = SalariedEmployee(109, "Davi", 500000)

emp1.calculate_salary()
emp2.calculate_salary()

print(emp1)
print(emp2)
