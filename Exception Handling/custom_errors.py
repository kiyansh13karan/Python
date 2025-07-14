# Custom Errors in Python :- 

'''
In Python, you can raise custom errors using the raise keyword along with a user-defined exception class.
'''

'''
Step-by-Step to Raise a Custom Error :- 

1. Define a custom exception (by inheriting from Exception)
2. Use raise to trigger it where needed
'''



class AgeTooLowError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is below the minimum allowed.")

def register(age):
    if age < 18:
        raise AgeTooLowError(age)
    print("Registered successfully!")

try:
    register(16)
except AgeTooLowError as e:
    print("Registration failed:", e)
