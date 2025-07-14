# Match Case Statement :- 

'''
In Python 3.10 and later, you can use the match-case statement — it's Python’s version of the switch statement (also called structural pattern matching).
'''


def calculator(a, b, op):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b if b != 0 else "Cannot divide by zero"
        case _:
            return "Invalid operator"

print(calculator(10, 5, '*'))  # Output: 50
