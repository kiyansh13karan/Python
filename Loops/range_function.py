# range function in python 
# The range() function is used to generate a sequence of numbers and is commonly used in for loops.
'''
range(stop)
range(start, stop)
range(start, stop, step)
'''


'''
Parameters:

start → Starting number (default is 0)
stop → End (not included in the result)
step → Difference between each number (default is 1)
'''



# Example 1: range(stop)
for i in range(5):
    print(i)
'''
Output :-
0
1
2
3
4
'''



# Example 2: range(start, stop)
for i in range(2, 6):
    print(i)
'''
Output :-
2
3
4
5
'''



# Example 3: range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
'''
Output :-
1
3
5
7
9
'''    




# Example 4: Reverse Counting with Negative Step
for i in range(5, 0, -1):
    print(i)
'''
Output :-
5
4
3
2
1
'''



# Example 5: Convert to list
print(list(range(5)))
'''
Output :-
[0, 1, 2, 3, 4]
'''
