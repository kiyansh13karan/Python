# multilevel inheritance in python :-

'''
Multilevel Inheritance means a class is derived from a class which is already derived from another class — forming a chain of inheritance.
'''



# Base class
class Grandfather:
    def show_grandfather(self):
        print("Grandfather: Loves storytelling")

# Intermediate class inheriting from Grandfather
class Father(Grandfather):
    def show_father(self):
        print("Father: Loves gardening")

# Derived class inheriting from Father
class Child(Father):
    def show_child(self):
        print("Child: Loves video games")

# Create object of Child class
c = Child()
c.show_grandfather()  # From Grandfather
c.show_father()       # From Father
c.show_child()        # From Child

'''
Output :- 

Grandfather: Loves storytelling
Father: Loves gardening
Child: Loves video games
'''

'''
Grandfather → base class
Father inherits from Grandfather
Child inherits from Father
So Child indirectly inherits everything from Grandfather too
'''