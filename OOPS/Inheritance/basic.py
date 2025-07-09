# inheritance in python 


'''
Inheritance is an important feature of Object-Oriented Programming that allows one class (child/derived class) to inherit the attributes and methods of another class (parent/base class).

This promotes code reuse and enables hierarchical class structures.
'''


# Example 1 :- 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
# Example usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy barks.
print(cat.speak())  # Output: Whiskers meows.





# Example 2  :- 
class Parent:
    # Parent class
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    # Child class inheriting from Parent
    def child_method(self):
        print("This is the child method.")

# Creating an object of Child
obj = Child()
obj.parent_method()  # Inherited from Parent
obj.child_method()   # Defined in Child






# Example 3 :-
# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound.")

# Child class that inherits from Animal
class Dog(Animal):
    pass  # No extra code added here

# Creating an object of the child class
d = Dog()
d.speak()  # Inherited method from Animal class
'''
Output :- 

The animal makes a sound.
'''




'''
Types of Inheritance in Python :- 

      Type	                              Description
Single Inheritance	            One child inherits from one parent
Multiple Inheritance	        One child inherits from multiple parents
Multilevel Inheritance	        Inheritance through multiple levels
Hierarchical Inheritance    	One parent, multiple children
Hybrid Inheritance	            Combination of multiple types
'''