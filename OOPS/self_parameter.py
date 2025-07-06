# self parameter in python 

# The self parameter is a reference to the current instance of the class.
# It allows you to access instance attributes and methods from within the class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Example usage
person1 = Person("Karan Nayal" , 19)
person1.display_info()
# The code defines a class named `Person` with an initializer method `__init__` that takes two parameters: `name` and `age`.
# Inside the `__init__` method, these parameters are assigned to instance variables `self.name` and `self.age`.
# The class also has a method `display_info` that prints the name and age of the person using the instance variables.
# Finally, an instance of the `Person` class is created with the name "Karan Nayal" and age 19, and the `display_info` method is called on that instance to display the information.    




# The self parameter is used to refer to the instance of the class that is being created or manipulated.
# It is a convention in Python to use `self` as the first parameter of instance methods, but you can technically use any name.
# However, using `self` is a widely accepted convention and makes the code more readable and understandable.
# The self parameter is essential for accessing instance attributes and methods within the class.








'''
In Python, the self parameter refers to the current instance of the class and is used to access instance variables and methods within the class.

It must be the first parameter of every instance method in a class, though you do not pass it manually when calling the method — Python does it automatically.
# The self parameter allows you to differentiate between instance variables and local variables within the method.
'''