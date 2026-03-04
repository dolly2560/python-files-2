# python classes and objects
class Temperature:

    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print("Temperature in Celsius:", celsius)


temp = Temperature()
temp.convertFahrenheit(25)  
temp.convertCelsius(77)      



import math

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return  math.pi * self.radius ** 2
    
    def circumference(self):
        return  2 * math.pi * self.radius
        
c = Circle(7)
print("area: {:.2f}" .format(c.area()))
print("circumference: {:.2f}".format(c.circumference()))



