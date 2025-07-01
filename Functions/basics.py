# Functions in python 
# A function in Python is a block of reusable code that performs a specific task. You can define your own functions (user-defined) or use built-in ones like print(), len(), etc.




# Defining a function 
def greet():
    print("Hello!")

greet() # calling a function 
'''
def -> keyword to defining a function 
greet() -> function name
() -> parentheses for parameters(if any) 
 '''






# Function with Parameters
def greet(name):
    print("Hello", name)

greet("Kiyansh")

'''
Output :- 
Hello Kiyansh
'''



# Function with Return Value
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum :", result)

'''
Output :-
Sum: 8
'''





# Default Parameters
def greet(name="User"):
    print("Hello", name)

greet()          # uses default
greet("Karan")    # overrides default
'''
Output :-
Hello User
Hello Karan
'''





# Keyword arguments
def student(name, age):
    print(name, "is", age, "years old")

student(age=19 , name="Karan")
'''
Output :-
Karan is 19 years old
'''





#  Variable Number of Arguments
'''
*args → multiple positional arguments
**kwargs → multiple keyword arguments
'''

def show(*args):
    for item in args:
        print(item)

show("Python", "Java", "C++")

'''
Output :-
Python 
Java
C++
'''


