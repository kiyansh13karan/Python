# Enumerate Function in Python :- 

'''
The enumerate() function adds a counter (index) to an iterable (like a list, string, or tuple) and returns it as an enumerate object, which can be used in a loop.
'''

# Syntax :- 
'''
enumerate(iterable, start=0)
'''



# Example :- 
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")
