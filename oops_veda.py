# # # # # # # ##Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
# # # # # # # class Car:
# # # # # # #     def __init__(self, brand, model, year):
# # # # # # #         self.brand = brand
# # # # # # #         self.model = model
# # # # # # #         self.year = year
# # # # # # #
# # # # # # #     def display_details(self):
# # # # # # #         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
# # # # # # #
# # # # # # # my_car = Car("Honda", "Civic", 2022)
# # # # # # # my_car.display_details()
# # # # # # #
# # # # # # # ##Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?
# # # # # # #
# # # # # # #
# # # # # # # class Student:
# # # # # # #     def __init__(self, name, roll_number, marks):
# # # # # # #         self.name = name
# # # # # # #         self.roll_number = roll_number
# # # # # # #         self.marks = marks
# # # # # # #
# # # # # # #     def display_info(self):
# # # # # # #         print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")
# # # # # # #
# # # # # # # student1 = Student("Raja", 7, 99)
# # # # # # # student1.display_info()
# # # # # # #
# # # # # # #
# # # # # # # ###Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?
# # # # # # #
# # # # # # #
# # # # # # # class Rectangle:
# # # # # # #     def __init__(self, length, breadth):
# # # # # # #         self.length = length
# # # # # # #         self.breadth = breadth
# # # # # # #
# # # # # # #     def area(self):
# # # # # # #         return self.length * self.breadth
# # # # # # #
# # # # # # #     def perimeter(self):
# # # # # # #         return 2 * (self.length + self.breadth)
# # # # # # #
# # # # # # # rectangle1 = Rectangle(22, 6)
# # # # # # # rectangle2 = Rectangle(6, 4)
# # # # # # # rectangle3 = Rectangle(23, 9)
# # # # # # # rectangle4 = Rectangle(40,60)
# # # # # # #
# # # # # # # print(f"Rectangle 1 - Area: {rectangle1.area()}, Perimeter: {rectangle1.perimeter()}")
# # # # # # # print(f"Rectangle 2 - Area: {rectangle2.area()}, Perimeter: {rectangle2.perimeter()}")
# # # # # # # print(f"Rectangle 3 - Area: {rectangle3.area()}, Perimeter: {rectangle3.perimeter()}")
# # # # # # #
# # # # # # #
# # # # # # # ##Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?
# # # # # # #
# # # # # # import math
# # # # # #
# # # # # # class Circle:
# # # # # #     def __init__(self, radius):
# # # # # #         self.radius = radius
# # # # # #
# # # # # #     def get_area(self):
# # # # # #         return math.pi * self.radius ** 2
# # # # # #
# # # # # #     def get_circumference(self):
# # # # # #         return 2 * math.pi * self.radius
# # # # # #
# # # # # # circle = Circle(5)
# # # # # # check = Circle(2)
# # # # # # print(f"Area: {circle.get_area()}")
# # # # # # print(f"Circumference: {circle.get_circumference()}")
# # # # # # print(f"Area: {check.get_area()}")
# # # # # # print(f"Circumference: {check.get_circumference()}")
# # # # # #
# # # # # # ##Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
# # # # #
# # # # # class Account:
# # # # #     def __init__(self, account_no, balance=0):
# # # # #         self.account_no = account_no
# # # # #         self.balance = balance
# # # # #
# # # # #     def debit(self, amount):
# # # # #         if amount > self.balance:
# # # # #             print("Insufficient funds")
# # # # #         else:
# # # # #             self.balance -= amount
# # # # #             print(f"Debited {amount}. New balance: {self.balance}")
# # # # #
# # # # #     def credit(self, amount):
# # # # #         self.balance += amount
# # # # #         print(f"Credited {amount}. New balance: {self.balance}")
# # # # #
# # # # #     def print_balance(self):
# # # # #         print(f"Account No: {self.account_no}, Balance: {self.balance}")
# # # # #
# # # # # # Create an Account instance
# # # # # account1 = Account(12345, 500)
# # # # # acc2 = Account(999,5000)
# # # # # # Credit and debit actions
# # # # # account1.credit(200)
# # # # # account1.debit(100)
# # # # # account1.print_balance()
# # # # #
# # # # # acc2.credit(1000)
# # # # # acc2.debit(1000)
# # # # # acc2.print_balance()
# # # #
# # # #
# # # # ### Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.
# # # # class Employee:
# # # #     employee_count = 0
# # # #
# # # #     def __init__(self, name, position):
# # # #         self.name = name
# # # #         self.position = position
# # # #         Employee.increment_employee_count()
# # # #
# # # #     @classmethod
# # # #     def increment_employee_count(cls):
# # # #         cls.employee_count += 1
# # # #
# # # #     @classmethod
# # # #     def get_employee_count(cls):
# # # #         return cls.employee_count
# # # #
# # # #
# # # # employee1 = Employee("Raja", "Manager")
# # # # print("Employee Count:", Employee.get_employee_count())
# # # #
# # # # employee2 = Employee("Ramu", "Developer")
# # # # print("Employee Count:", Employee.get_employee_count())
# # # #
# # # # employee3 = Employee("Ananya", "Designer")
# # # # print("Employee Count:", Employee.get_employee_count())
# # # #
# # # # employee4 = Employee("Kumara", "Farmer")
# # # # print("Employee Count:", Employee.get_employee_count())
# # #
# # #
# # # # ###Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.
# # # # class Book:
# # # #     def __init__(self, title, author, price=20.0):
# # # #         self.title = title
# # # #         self.author = author
# # # #         self.price = price
# # # #
# # # #     def display_details(self):
# # # #         print(f"Title: {self.title}")
# # # #         print(f"Author: {self.author}")
# # # #         print(f"Price: ${self.price}")
# # # #
# # # # book1 = Book("Moodu pani", "Balumahendra", 15.0)
# # # # book1.display_details()
# # # #
# # # # book2 = Book("Gentle man", "Shankar")
# # # # book2.display_details()
# # # #
# # # # book3 = Book("with dragon", "kumara")
# # # # book3.display_details()
# # #
# # # ####Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.
# # # # class TemperatureConverter:
# # # #     def celsius_to_fahrenheit(self, celsius):
# # # #         return (celsius * 9/5) + 32
# # # #
# # # # converter = TemperatureConverter()
# # # #
# # # # temperatures = [0, 25, 100]
# # # # for temp in temperatures:
# # # #     print(converter.celsius_to_fahrenheit(temp))
# # #
# # # ####Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.
# # #
# # # class Time:
# # #     def __init__(self, hours, minutes):
# # #         self.hours = hours
# # #         self.minutes = minutes
# # #
# # #     def add_time(self, other_time):
# # #         total_minutes = self.hours * 60 + self.minutes + other_time.hours * 60 + other_time.minutes
# # #         result_hours = total_minutes // 60
# # #         result_minutes = total_minutes % 60
# # #         return Time(result_hours, result_minutes)
# # #
# # # time1 = Time(5, 45)
# # # time2 = Time(6, 30)
# # # result_time = time1.add_time(time2)
# # #
# # # print(f"Resulting Time: {result_time.hours} hours and {result_time.minutes} minutes")
# # #
# # ####Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.
# # class EmployeeSalary:
# #     basic_salary = 50000
# #     bonus_percentage = 10
# #
# #     @classmethod
# #     def set_bonus_percentage(cls, new_bonus_percentage):
# #         cls.bonus_percentage = new_bonus_percentage
# #
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def calculate_total_salary(self):
# #         bonus = (EmployeeSalary.basic_salary * EmployeeSalary.bonus_percentage) / 100
# #         total_salary = EmployeeSalary.basic_salary + bonus
# #         return total_salary
# #
# # employee1 = EmployeeSalary("Raja")
# # employee2 = EmployeeSalary("Rani")
# #
# # print(f"{employee1.name}'s Total Salary: {employee1.calculate_total_salary()}")
# # print(f"{employee2.name}'s Total Salary: {employee2.calculate_total_salary()}")
# #
# # EmployeeSalary.set_bonus_percentage(15)
# #
# # print(f"After updating bonus percentage:")
# # print(f"{employee1.name}'s Total Salary: {employee1.calculate_total_salary()}")
# # print(f"{employee2.name}'s Total Salary: {employee2.calculate_total_salary()}")
#
#
# # ##Create a class MathOperations that contains:
# # ##A static method add_numbers that takes two arguments and returns their sum.
# # ##A static method multiply_numbers that takes two arguments and returns their product.
# # class MathOperations:
# #     @staticmethod
# #     def add_numbers(a, b):
# #         return a + b
# #
# #     @staticmethod
# #     def multiply_numbers(a, b):
# #         return a * b
# #
# # # Example usage
# # sum_result = MathOperations.add_numbers(5, 3)
# # product_result = MathOperations.multiply_numbers(5, 3)
# #
# # print(f"Sum: {sum_result}")
# # print(f"Product: {product_result}")
#
# ##Assignment 2: Class Methods
# ###Create a class Person that keeps track of the number of people created. The class should have:
# ###A class variable count to count instances of the class.
# ###A class method get_count that returns the current count.
#
# class Person:
#     count = 0
#
#     def __init__(self):
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# p1 = Person()
# p2 = Person()
# p3 = Person()
#
# print(Person.get_count())
#
# ###Assignment 3: Using Both Static and Class Methods
# Create a class TemperatureConverter with the following:
# A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
# A class method info that returns a message about temperature conversions.
# class TemperatureConverter:
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#
#     @classmethod
#     def info(cls):
#         return "This class converts temperatures between Celsius and Fahrenheit."
#
# print(TemperatureConverter.celsius_to_fahrenheit(25))
# print(TemperatureConverter.info())
##Assignment 4: Single Inheritance
###Create two classes:
###Animal with a method sound that prints "Animal sound".
###Dog that inherits from Animal and overrides the sound method to print "Bark".
# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# animal = Animal()
# dog = Dog()
#
# animal.sound()
# dog.sound()

###Assignment 5: Multiple Inheritance
##Create two classes:
##Bird with a method fly that prints "Flying".
##Fish with a method swim that prints "Swimming".
# class Bird:
#     def fly(self):
#         print("Flying")
#
# class Fish:
#     def swim(self):
#         print("Swimming")
#
# class Duck(Bird, Fish):
#     pass
#
# duck = Duck()
# duck.fly()
# duck.swim()

###Assignment 6: Abstract Class
###Use the abc module to create an abstract class Shape that contains:
###An abstract method area().
###Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method.

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# circle = Circle(5)
# print(f"Circle area: {circle.area()}")
#
# rectangle = Rectangle(4, 6)
# print(f"Rectangle area: {rectangle.area()}")

###Assignment 7: Encapsulation
###Create a class BankAccount that uses encapsulation:
###Private attributes _balance.
###Public methods deposit() and withdraw() that modify _balance safely.
# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self._balance:
#             self._balance -= amount
#
#     def get_balance(self):
#         return self._balance
#
#
# account = BankAccount(1000)
# account.deposit(50)
# account.withdraw(20)
# print(account.get_balance())


###Assignment 8: Polymorphism with Method Overriding
###Create two classes Cat and Dog with a method speak().
###The Dog class should implement speak() to print "Woof".
###The Cat class should implement speak() to print "Meow".
#
# class Dog:
#     def speak(self):
#         print("Woof")
#
# class Cat:
#     def speak(self):
#         print("Meow")
#
#
# dog = Dog()
# cat = Cat()
#
# dog.speak()
# cat.speak()

###Assignment 9: Polymorphism with Method Overloading
###Create a class Calculator with a method add() that:
###Can accept 2 or 3 arguments and returns their sum.
###Hint: Use default parameters to handle method overloading in Python.
# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
#
# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.add(5, 3, 2))

###Assignment 10: Multilevel Inheritance
# Create three classes:
# LivingBeing with a method breathe() that prints "Breathing".
# Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
# Human that inherits from Mammal and adds a method think() that prints "Thinking"
# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
#
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
#
#
# class Human(Mammal):
#     def think(self):
#         print("Thinking")
#
#
# human = Human()
# human.breathe()
# human.walk()
# human.think()





