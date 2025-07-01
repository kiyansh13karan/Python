# continue statement in python 

# The continue statement is used inside loops to skip the rest of the code in the current iteration and move to the next iteration of the loop.


#  Example 1: continue in a for loop
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
'''
Output :- 
1
2
4
5
'''



# Example 2: continue in a while loop
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)
'''
Output :- 
1
3
4
5
'''



# Example 3: Skipping even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)
'''
Output :- 
1
3
5
'''
