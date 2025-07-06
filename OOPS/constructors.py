# constructors in python

# A constructor in Python is a special method that is automatically called when an instance (object) of a class is created.
# It is defined using the `__init__` method and is used to initialize the attributes of the class.


'''
Python Constructor Method: __init__() :- 

1. The constructor method is always named __init__()
2. It is automatically called when an object is created
'''



'''
Syntax :- 

class ClassName:
    def __init__(self, parameters):
        self.attribute = value
'''




class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object (calls constructor)
p1 = Person("Alice", 25)

# Calling a method
p1.show()
'''
Output :- 

My name is Alice and I am 25 years old.
'''




'''
| Feature              | Description                                   |
| -------------------- | --------------------------------------------- |
| Method name          | `__init__()`                                  |
| Called automatically | Yes, when object is created                   |
| Purpose              | Initialize instance variables                 |
| First parameter      | `self` (refers to the instance being created) |
'''




# 1. Default Constructor :- 
# A default constructor is a constructor that does not take any parameters or takes only default parameters.
class DefaultConstructor:
    def __init__(self):
        self.message = "Hello, World!"

    def display(self):
        print(self.message)
# Creating an object of DefaultConstructor
default_obj = DefaultConstructor()
# Calling the display method
default_obj.display()
''' 
Output :-

Hello, World!
'''





# 2. Parameterized Constructor :-
# A parameterized constructor is a constructor that takes parameters to initialize instance variables.
class ParameterizedConstructor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of ParameterizedConstructor
param_obj = ParameterizedConstructor("Alice", 30)
# Calling the display method
param_obj.display()
'''
Output :-

Name: Alice, Age: 30
'''




# 3. Copy Constructor :-
# A copy constructor is a constructor that creates a new object as a copy of an existing object.
class CopyConstructor:
    def __init__(self, other):
        self.name = other.name
        self.age = other.age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Creating an object of CopyConstructor
original_obj = ParameterizedConstructor("Bob", 40)
copy_obj = CopyConstructor(original_obj)
# Calling the display method on the copied object
copy_obj.display()
'''
Output :-

Name: Bob, Age: 40
'''





# 4. Static Constructor (Not a standard Python feature, but can be simulated):
# A static constructor is not a standard feature in Python, but you can simulate it using class
# methods or static methods to initialize class-level attributes.
class StaticConstructor:
    class_variable = "Static Value"

    @classmethod
    def display_class_variable(cls):
        print(cls.class_variable)
# Calling the class method to display the class variable
StaticConstructor.display_class_variable()
'''
Output :-
Static Value
'''



