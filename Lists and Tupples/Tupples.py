# Tupples
# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are defined using parentheses.

# Example of a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 2


# Tuples are immutable, so we cannot modify elements
# my_tuple[0] = 10  # This will raise a TypeError

# Adding elements to a tuple is not allowed, but we can concatenate tuples
new_tuple = my_tuple + (6,)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Removing elements from a tuple is not allowed, but we can create a new tuple without the element
new_tuple = my_tuple[:2] + my_tuple[3:]  # Removing the element
print(new_tuple)  # Output: (1, 2, 4, 5)

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Tuple comprehensions are not available, but we can create tuples using generator expressions
squared_tuple = tuple(x**2 for x in my_tuple)
print(squared_tuple)  # Output: (1, 4, 9, 16, 25)


# Nested tuples
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# Accessing elements in a nested tuple
print(nested_tuple[0][1])  # Output: 2
print(nested_tuple[1][2])  # Output: 6
# Modifying elements in a nested tuple is not allowed, but we can create a new nested tuple
new_nested_tuple = ((10, 2, 3), nested_tuple[1], nested_tuple[2])
print(new_nested_tuple)  # Output: ((10, 2, 3), (4, 5, 6), (7, 8, 9))
# Adding a new sub-tuple to a nested tuple is not allowed, but we can create a new nested tuple
new_nested_tuple = nested_tuple + ((10, 11, 12),)
print(new_nested_tuple)  # Output: ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
# Removing a sub-tuple from a nested tuple is not allowed, but we can create a new nested tuple
new_nested_tuple = nested_tuple[:2] + nested_tuple[3:]  # Removing the
# second sub-tuple
print(new_nested_tuple)  # Output: ((1, 2, 3), (7, 8, 9))






# Tuple methods
# Tuple methods are functions that can be called on tuple objects to perform various operations
# Common tuple methods include:

# count() - Returns the number of times a specified value appears in the tuple
my_tuple = (1, 2, 3, 2, 4, 5)
print(my_tuple.count(2))  # Output: 2
# index() - Returns the index of the first occurrence of a specified value in the tuple
print(my_tuple.index(3))  # Output: 2


# Tuple methods are limited compared to list methods since tuples are immutable
# and do not support methods that modify the tuple.
# However, they can still be used to retrieve information about the tuple.
# Example of tuple methods
my_tuple = (1, 2, 3, 4, 5)
# Count the occurrences of a value
print(my_tuple.count(2))  # Output: 1
# Find the index of a value
print(my_tuple.index(3))  # Output: 2









# Tuple unpacking
# Tuple unpacking allows you to assign the elements of a tuple to multiple variables
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Tuple unpacking with fewer variables than elements
a, b, *rest = my_tuple
print(a, b, rest)  # Output: 1 2 [3, 4, 5]

# Tuple unpacking with more variables than elements
a, b, c, d, e, f = my_tuple + (6,)
print(a, b, c, d, e, f)  # Output: 1 2 3 4 5 6

# Tuple unpacking with nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
a, (b, c), (d, e) = nested_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5 6

# Tuple unpacking with nested tuples and variable-length unpacking
a, (b, c), *rest = nested_tuple
print(a, b, c, rest)  # Output: 1 2 3 [(5, 6)]

