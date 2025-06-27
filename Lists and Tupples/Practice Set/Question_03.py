# write a program to check that a tupple type cannot be changed in python

# Define a tuple
my_tuple = (10, 20, 30)

print("Original tuple:", my_tuple)

# Try to modify the first element
try:
    my_tuple[0] = 100
except TypeError as e:
    print("Error: Tuples are immutable. You cannot change their values.")
    print("Caught Exception:", e)
