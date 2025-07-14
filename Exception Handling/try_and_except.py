# Try and Except in python :- 

'''
The try and except block in Python is used for handling exceptions (errors). It lets you run code that might cause an error, without crashing your program.
'''


# Syntax :- 
'''
try:
    # Code that might raise an error
    risky_code()
except SomeError:
    # Code to run if that error happens
    handle_the_error()
'''




# Basic Structure: try-except
try:
    # Code that might raise an error
    x = 10 / 0
except ZeroDivisionError:
    # Code that runs if an error occurs
    print("You can't divide by zero!")




# Common Exception :- 
'''
| Exception           | Description                                    |
| ------------------- | ---------------------------------------------- |
| `ZeroDivisionError` | Dividing by zero                               |
| `ValueError`        | Invalid value (e.g. converting letters to int) |
| `TypeError`         | Invalid type operation                         |
| `IndexError`        | Accessing invalid list index                   |
| `KeyError`          | Accessing missing dictionary key               |
| `FileNotFoundError` | File not found                                 |
'''




# try-except-else-finally Full Syntax
try:
    x = int(input("Enter a number: "))
    y = 100 / x
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("Result is:", y)
finally:
    print("Code Executed.")
'''
Explanation :-

try: Code that may cause an exception.
except: Block that handles specific exceptions.
else: Runs if no exception occurs.
finally: Always runs (used for cleanup code like closing files).
'''





#  Catching Multiple Exceptions :-
try:
    # some code
    pass
except (ValueError, TypeError):
    print("Caught a ValueError or TypeError")






# Catch All Exceptions (Not Recommended Always)
try:
    # risky code
    pass
except Exception as e:
    print("Error occurred:", e)





# Raising Your Own Exception :-
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    return "Access granted."

print(check_age(20))  # Works
# print(check_age(15))  # Raises ValueError








# SUMMARY :- 
'''
| Keyword   | Use                               |
| --------- | --------------------------------- |
| `try`     | Wrap code that may throw an error |
| `except`  | Handle specific error types       |
| `else`    | Run code if no errors occur       |
| `finally` | Always runs (e.g., for cleanup)   |
| `raise`   | Manually raise an exception       |
'''