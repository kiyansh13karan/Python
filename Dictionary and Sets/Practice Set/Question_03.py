# can we have a set with 18 (int) and ' 18 ' (str) as a value in it ? 



# Yes, absolutely! You can have both 18 (an int) and '18' (a str) in the same Python set.

# They are considered distinct values because they are of different types (int vs str), even though they may look similar.


my_set = {18, '18'}
print(my_set)         # Output: {18, '18'}
print(len(my_set))    # Output: 2
print(type(my_set))   # Output: <class 'set'>
# The set contains two elements: the integer 18 and the string '18'.
