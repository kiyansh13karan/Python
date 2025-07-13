# How to take user input in python 


# In Python, you use the input() function to get input from the user.
# Example :- 
name = input("Enter your name: ")
print("Hello,", name)


'''
Important Points :- 

input() always returns a string (even if you type numbers).
You need to typecast if you want numbers.
'''

# Example :- 

# Taking two numbers and adding them
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum is:", sum)






# Typecasting input example :- 
'''
| Input Code                      | What it Does                                     |
| ------------------------------- | ------------------------------------------------ |
| `int(input("Enter age: "))`     | Converts input to an integer                     |
| `float(input("Enter price: "))` | Converts input to a float                        |
| `str(input("Enter name: "))`    | Converts input to a string (default)             |
| `bool(input("True/False: "))`   | Converts string to boolean (not always reliable) |
'''