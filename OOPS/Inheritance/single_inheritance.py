# single inheritance in python 

# Single Inheritance means that a child class inherits from only one parent class.
'''
Single inheritance is a type of inheritance where a class (child/derived class) inherits from only one class (parent/base class). This allows the child class to access the attributes and methods of the parent class, promoting code reuse and a clear hierarchical structure.
'''


# Example 1 :-

# Parent class
class Vehicle:
    def start(self):
        print("Vehicle started.")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is being driven.")

# Creating object of child class
c = Car()
c.start()  # Inherited method from Vehicle
c.drive()  # Method defined in Car
'''
Output :- 

Vehicle started.
Car is being driven.
'''

'''
Vehicle is the parent (superclass).
Car is the child (subclass) that inherits from Vehicle.
Car gets access to all the public methods and attributes of Vehicle.
'''
