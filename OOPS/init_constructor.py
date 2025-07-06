# __init__ constructor

# The `__init__` method is a special method in Python classes, known as the constructor.
# It is automatically called when an instance of the class is created.# It takes ‘self’ argument and can also take further arguments



class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# Example usage
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.



# The code defines a class named `Person` with an initializer method `__init__` that takes two parameters: `name` and `age`.
# Inside the `__init__` method, these parameters are assigned to instance variables `self.name` and `self.age`.
# The class also has a method `greet` that prints a greeting message using the instance variables.
# Finally, an instance of the `Person` class is created with the name "Alice" and age 30, and the `greet` method is called on that instance to display the greeting message.


