# Built in module in python :- 

'''
Built-in modules in Python are modules that come pre-installed with Python. You don’t need to install them separately — just import and use them.

They are part of the Python Standard Library, which is a large collection of useful tools for file handling, math, time, system interaction, and more.
'''


import math
print(f"Square root of 25 is : {math.sqrt(25)}")  # Output: 5.0
print(f"Square root of 81 is : {math.sqrt(81)}")  # Output: 9.0




import calendar
# Display the calendar for a specific month and year
year = int(input("Enter year (e.g. 2025): "))
month = int(input("Enter month (1-12): "))
# Display calendar for the selected month
print("\nHere is the calendar:")
print(calendar.month(year, month))
