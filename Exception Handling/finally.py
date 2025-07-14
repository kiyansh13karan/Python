# Finally keyword in python :- 

'''
The finally block in Python is used to execute code no matter what, whether an exception was raised or not. It's commonly used for cleanup actions like closing files, releasing resources, or disconnecting from databases.
'''


# Syntax of try-except-finally :- 
'''
try:
    # Code that might raise an error
    risky_code()
except SomeError:
    # Handle the error
    handle_error()
finally:
    # Always runs
    cleanup_code()
'''



# Example :- 
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Not a number.")
finally:
    print("Code Executed.")





# SUMMARY :-
'''
| Block     | Purpose                                   |
| --------- | ----------------------------------------- |
| `try`     | Code that might raise an error            |
| `except`  | Handle specific errors                    |
| `finally` | Code that runs **no matter what** happens |
'''