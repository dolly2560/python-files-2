from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name      # private attribute
        self.__salary = salary  # private attribute

    
    def display_info(self):
        print("Employee Name:", self.__name)

    
    def get_salary(self):
        return self.__salary

    # abstract method
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary()   # full salary

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary() / 2   # half salary


emp1 = FullTimeEmployee("Joy", 10000)
emp2 = PartTimeEmployee("John", 10000)


employees = [emp1, emp2]


for emp in employees:
    emp.display_info()
    print("Salary:", emp.calculate_salary())
    print()
    
#Encapsulation
#Private attributes __name and __salary hide the internal data of the class.

#Inheritance
#FullTimeEmployee and PartTimeEmployee inherit from the Employee class.

#Abstraction
#Employee is an abstract class and defines the abstract method calculate_salary().

#Polymorphism
#The method calculate_salary() behaves differently in each subclass:
#FullTimeEmployee returns full salary.
#PartTimeEmployee returns half salary.
    
