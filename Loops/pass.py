# pass statement in python 

# The pass statement is a null operation — it does nothing. It’s used when a statement is syntactically required, but you don’t want any code to run.


'''
Why use pass ?

As a placeholder for future code
To define empty functions, loops, classes, or if statements without errors
'''



# Example 1: pass in a function
def my_function():
    pass  # Placeholder for future code

# Note :- This function does nothing but doesn’t raise an error.







# Example 2: pass in an if statement
x = 10

if x > 0:
    pass  # We'll add logic later
else:
    print("x is non-positive")






# Example 3: pass in a loop
for i in range(5):
    if i == 3:
        pass  # Skipping processing for 3
    else:
        print(i)
'''
Output :- 
0
1
2
4
'''
# Note :-  It silently skips over i == 3 without doing anything.







#  Example 4: pass in a class
class MyClass:
    pass

# Note :- This creates an empty class without error.




