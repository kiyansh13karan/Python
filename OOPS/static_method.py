# static method in python
## A static method in Python is a method that belongs to the class rather than an instance of the class.
# It does not require an instance to be called and does not have access to the instance or class variables.
# Static methods are defined using the `@staticmethod` decorator.

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y
    
# Example usage
result_add = MathOperations.add(5, 3)
result_subtract = MathOperations.subtract(5, 3) 
print(f"Addition Result: {result_add}")        # Output: Addition Result: 8
print(f"Subtraction Result: {result_subtract}")  # Output: Subtraction Result: 2


# The code defines a class named `MathOperations` with two static methods: `add` and `subtract`.
# The `add` method takes two parameters `x` and `y`, and returns their sum.
# The `subtract` method takes two parameters `x` and `y`, and returns their difference.
# Both methods are decorated with `@staticmethod`, indicating that they do not require an instance of the class to be called.
# Example usage shows how to call these static methods directly on the class without creating an instance.




# Static methods are useful when you want to perform operations that are related to the class but do not require access to instance-specific data.
# They can be called directly on the class without creating an instance, making them more efficient for certain operations.
# Static methods can be used for utility functions, mathematical operations, or any functionality that does not depend on instance-specific data.
# Static methods are defined using the `@staticmethod` decorator, and they do not take `self` or `cls` as the first parameter.