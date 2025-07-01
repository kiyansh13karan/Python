# for loops in python 
# A for loop in Python is used to iterate over a sequence like a list, string, tuple, or range.
'''
syntax :- 
for variable in sequence:
    # Code block to execute
'''



# Example 1: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry



# Example 2: Using range()
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4




# Example 3: Loop with custom start and step
for i in range(2, 11, 2):
    print(i)
# Output: 2, 4, 6, 8, 10




# Example 4: Loop through a string
for letter in "hello":
    print(letter)




# Example 5: Using break
for i in range(1, 6):
    if i == 3:
        break
    print(i)




# Example 6: Using continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
