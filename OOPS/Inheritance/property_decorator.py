# property decorator in python :- 

# The `property` decorator in Python is used to define properties in classes, allowing you to manage the access to instance attributes. It provides a way to use methods as attributes, enabling encapsulation and validation of data.

# It allows you to define getter, setter, and deleter methods for an attribute, making it easier to control how the attribute is accessed and modified.

# Here's a breakdown of how to use the `property` decorator:
'''
Why use @property? 

To access a method like an attribute.
To encapsulate (hide) internal variables and control access to them.
To define getter, setter, and deleter methods cleanly.
'''



'''
a decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.
''' 


class Person:
    name = "Unknown"  # class-level attribute

    @property
    def name(self):
        print("Getting name...")
        return Person._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        Person._name = value

# Using the class
p = Person()

p.name = "Alice"      # Calls the setter
print(p.name)         # Calls the getter
'''
Output :- 

Setting name...
Getting name...
Alice
'''





# getter and setter method 
class Student:
    def __init__(self):
        self._marks = 0  # underscore _marks means "private"

    @property
    def marks(self):
        print("Getting marks...")
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            print("Setting marks...")
            self._marks = value
        else:
            print("Invalid marks! Must be between 0 and 100.")

# Using the class
s = Student()

s.marks = 85         # Calls the setter
print(s.marks)       # Calls the getter

s.marks = 150        # Invalid value, won't set
