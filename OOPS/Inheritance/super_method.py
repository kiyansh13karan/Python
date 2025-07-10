# super method in python 

'''
In Python, the super() method is used to call a method from a parent (or superclass) inside a child (or subclass). It’s commonly used in inheritance to extend or modify the behavior of inherited methods without completely overriding them.
'''


# Syntax :- 
# super().method_name(arguments)



'''
Why use super() ? :- 

To call the parent class’s constructor (__init__) or methods.
To avoid explicitly naming the parent class (which helps in multiple inheritance).
To ensure maintainability and reduce code duplication.
'''



#  Example 1: Using super() in Constructor :- 
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent's __init__
        print("Child constructor")

obj = Child()
'''
Output :- 

Parent constructor
Child constructor
'''



# Example 2: super() with Other Methods
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the parent method
        print("Dog barks")

dog = Dog()
dog.speak()
'''
Output :- 

Animal speaks
Dog barks
'''




# Example 3: Multiple Inheritance with super() :-
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(B):
    def show(self):
        super().show()
        print("C")

c = C()
c.show()
'''
Output :- 

A
B
C
'''

