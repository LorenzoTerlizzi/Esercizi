# Lorenzo Terlizzi
# 31/05/2024

# Exercise 1: Creating an Abstract Class with Abstract Methods
# Create an abstract class Shape with an abstract method area and another abstract method perimeter.
# Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods.

from abc import ABC, abstractmethod
import math
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
        
class Circle(Shape):
    def __init__(self, raggio: float):
        self.raggio = raggio

    def area(self):
        return math.pi * (self.raggio**2)
    def perimeter(self):
        return (self.raggio * 2) * math.pi
    
class Rectangle(Shape):
    def __init__(self, altezza: float, lunghezza: float):
        self.altezza = altezza
        self.lunghezza = lunghezza
    
    def area(self):
        return self.altezza * self.lunghezza
    def perimeter(self):
        return 2 * (self.altezza + self.lunghezza)

circle = Circle(5)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

rectangle = Rectangle(4, 7)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")


# Exercise 2: Implementing Static Methods
# Create a class MathOperations with a static method add that takes two numbers and returns their sum,
# and another static method multiply that takes two numbers and returns their product.
class MathOperations:

    @staticmethod
    def sum(num1: int, num2: int):
        return num1 + num2
    @ staticmethod
    def product(num1: float, num2: float):
        return num1 * num2
    

print(f"somma: {MathOperations.sum(5, 6)}")
print(f"prodotto: {MathOperations.product(5, 6)}")

# Exercise 3: Library Management System 
# Create a Book class containing the following attributes: title, author, isbn
# The book class must contains the following methods:
# __str__ method to return a string representation of the book.
# @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". 
# It means that you must use the class reference cls to create a new object of the Book class using a string.
