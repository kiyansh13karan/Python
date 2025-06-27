# Lists
# Lists are mutable, ordered collections of items
# They can contain mixed data types and are defined using square brackets


# Example of a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 2

# Modifying elements in a list
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Adding elements to a list
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4, 5, 6]

# Slicing a list
print(my_list[1:4])  # Output: [3, 4, 5]

# List comprehensions for creating lists
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [100, 9, 16, 25, 36]



# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
print(nested_list[0][1])  # Output: 2
print(nested_list[1][2])  # Output: 6

# Modifying elements in a nested list
nested_list[0][0] = 10
print(nested_list)  # Output: [[10, 2, 3], [4, 5, 6], [7, 8, 9]]

# Adding a new sublist to a nested list
nested_list.append([10, 11, 12])
print(nested_list)  # Output: [[10, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Removing a sublist from a nested list
nested_list.remove([4, 5, 6])
print(nested_list)  # Output: [[10, 2, 3], [7, 8, 9], [10, 11, 12]]






# List methods
# List methods are functions that can be called on list objects to perform various operations
# Common list methods include:

# append() - Adds an element to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# extend() - Adds elements from an iterable to the end of the list
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# insert() - Inserts an element at a specified index
my_list.insert(0, 0)
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6]

# remove() - Removes the first occurrence of a specified element
my_list.remove(3)
print(my_list)  # Output: [0, 1, 2, 4, 5, 6]

# pop() - Removes and returns the element at a specified index (default is the last element)
last_element = my_list.pop()
print(last_element)  # Output: 6
print(my_list)  # Output: [0, 1, 2, 4, 5]

# index() - Returns the index of the first occurrence of a specified element
index_of_2 = my_list.index(2)
print(index_of_2)  # Output: 2

# count() - Returns the number of occurrences of a specified element
count_of_1 = my_list.count(1)
print(count_of_1)  # Output: 1

# sort() - Sorts the list in ascending order (can take a key function and reverse flag)
my_list.sort()
print(my_list)  # Output: [0, 1, 2, 4, 5]

# reverse() - Reverses the order of the elements in the list
my_list.reverse()
print(my_list)  # Output: [5, 4, 2, 1, 0]

# clear() - Removes all elements from the list
my_list.clear()
print(my_list)  # Output: []

# Copying a list
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # Output: [1, 2, 3]

# List concatenation and repetition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Concatenation
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]
# Repetition
repeated_list = list1 * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]


# List unpacking
# List unpacking allows you to assign elements of a list to multiple variables
a, b, c = [1, 2, 3]
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
# You can also use the asterisk (*) operator to unpack multiple elements
first, *rest = [1, 2, 3, 4, 5]
print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]


# List comprehensions
# List comprehensions provide a concise way to create lists
# They consist of an expression followed by a for clause and can include optional if clauses
# Example of a list comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# List comprehensions with conditions
even_squared_numbers = [x**2 for x in range(10) if x % 2 == 0]
print(even_squared_numbers)  # Output: [0, 4, 16, 36, 64]


