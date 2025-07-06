# Write a class “Calculator” capable of finding square, cube and square root of a number.

import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

# Example usage
calc = Calculator(9)
print("Square :", calc.square())
print("Cube :", calc.cube())
print("Square Root :", calc.square_root())