# Break statement in python 

# The break statement is used to immediately exit a loop (for or while) — regardless of the loop's condition.


# Example 1: break in a for loop
for i in range(1, 10):
    if i == 5:
        break
    print(i)
'''
Output :-
1
2
3
4
'''




# Example 2: break in a while loop
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
'''
Output :- 
1
2
3
4
5
'''




# Example 3: break with user input
while True:
    name = input("Enter your name (or 'quit' to exit): ")
    if name == "quit":
        break
    print("Hello,", name)
