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
# Create a Member class with the following attributes: name, member_id, borrowed_books
# The member class must contain the following methods:
# borrow_book(book) to add a book to the borrowed_books list.
# return_book(book) to remove a book from the borrowed_books list.
# __str__ method to return a string representation of the member.
# @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".
# Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
# The library class must contain the following methods:
# add_book(book) to add a book to the library and increment total_books.
# remove_book(book) to remove a book from the library and decrement total_books.
# register_member(member) to add a member to the library.
# lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.
# __str__ method to return a string representation of the library with the list of books and members.
# @classmethod library_statistics(cls) to print the total number of books.
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str: str):
       return cls(book_str.split(", "))
    

    

book = "La Divina Commedia", "D. Alighieri", 999000666
divina_commedia: Book = Book.from_string(book)


# Exercise 4: University Management System
# Create a system to manage a university with departments, courses, professors, and students. 
# Create an abstract class Person:

# Attributes:
# name (string)
# age (int)

# Methods:
# __init__ method to initialize the attributes.
# Abstract method get_role to be implemented by subclasses.
# __str__ method to return a string representation of the person.

# Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

# Student:
# Additional attributes: student_id (string), courses (list of Course instances)
# Method enroll(course) to enroll the student in a course.

#Professor:
# Additional attributes: professor_id (string), department (string), courses (list of Course instances)
# Method assign_to_course(course) to assign the professor to a course.

# Create a class Course:

# Attributes:
# course_name (string)
# course_code (string)
# students (list of Student instances)
# professor (Professor instance)

# Methods:
# __init__ method to initialize the attributes.
# add_student(student) to add a student to the course.
# set_professor(professor) to set the professor for the course.
# __str__ method to return a string representation of the course.

# Create a class Department:

# Attributes:
# department_name (string)
# courses (list of Course instances)
# professors (list of Professor instances)

# Methods:
# __init__ method to initialize the attributes.
# add_course(course) to add a course to the department.
# add_professor(professor) to add a professor to the department.
# __str__ method to return a string representation of the department.

# Create a class University:

# Attributes:
# name (string)
# departments (list of Department instances)
# students (list of Student instances)

# Methods:
# __init__ method to initialize the attributes.
# add_department(department) to add a department to the university.
# add_student(student) to add a student to the university.
# __str__ method to return a string representation of the university.
