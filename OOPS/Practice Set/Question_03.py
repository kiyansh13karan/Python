# Add a static method in problem 2, to greet the user with hello.


import math

class Calculator:
    @staticmethod
    def greet_user():
        print("Hello! Welcome to the Calculator.")


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
calc.greet_user()
print("Square :", calc.square())
print("Cube :", calc.cube())
print("Square Root :", calc.square_root())


'''
Output :- 

Output:
Hello! Welcome to the Calculator.
Square : 81
Cube : 729
Square Root : 3.0 
'''