# class in python
# A class in Python is a fundamental concept in object-oriented programming (OOP).
# A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
# Example usage
person1 = Person("Alice", 30)
person1.greet()
# The code defines a class named `Person` with an initializer method `__init__` that takes two parameters: `name` and `age`.
# Inside the `__init__` method, these parameters are assigned to instance variables `self.name` and `self.age`.
# The class also has a method `greet` that prints a greeting message using the instance variables.
# Finally, an instance of the `Person` class is created with the name "Alice" and age 30, and the `greet` method is called on that instance.










# CLASS ATTRIBUTES  
'''
An attribute that belongs to the class rather than a particular object.
Class attributes are shared by all instances of the class, meaning that if you change the value of a class attribute, it will affect all instances of that class.
'''
class Employee: 
    company = "Google" # Specific to Each Class 

harry = Employee() # Object Instatiation 
print(f"Before changing class attribute , company of Harry is {harry.company}") # Output: Google
Employee.company = "YouTube" # Changing Class Attribute
print(f"After changing class attribute , company of Harry is {harry.company}")  # Output: YouTube







# INSTANCE ATTRIBUTES
'''
An attribute that is specific to an instance of a class.
Each object (instance) of a class can have different values for its instance attributes.
'''
class Employee: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 25)    

emp1.salary = "30k" # adding instance attribute
emp2.salary = "25k" # adding instance attribute

print(f"Name of first employee: {emp1.name} and age is {emp1.age}")  # Output: Alice
print(f"Salary of first employee: {emp1.salary}")  # Output: 30k
print(f"Name of second employee: {emp2.name} and age is {emp2.age}")  # Output: Bob
print(f"Salary of second employee: {emp2.salary}")  # Output: 25k

# Note: Instance attributes, take preference over class attributes during assignment & retrieval.