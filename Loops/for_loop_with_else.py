# Python allows you to use an else clause with a for loop. This may seem unusual but can be very useful.
'''
Syntax :-

for item in sequence:
    # Loop body
else:
    # Executes when loop is NOT terminated by 'break'

'''



# Example 1: for loop with else (no break)
for i in range(5):
    print(i)
else:
    print("Loop completed without break.")
'''
Output :-
0
1
2
3
4
Loop completed without break.
'''
# Note :- The else block runs because the loop was not broken.





# Example 2: for loop with break
for i in range(5):
    print(i)
    if i == 2:
        break
else:
    print("Loop completed.")
'''
Output :- 
0
1
2
''' 
# Note :-  The else block does not run because the loop was terminated with break.






# Example 3: Searching an item
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print("Found!")
        break
else:
    print("Not found.")
'''
Output :-
Not found.
'''






