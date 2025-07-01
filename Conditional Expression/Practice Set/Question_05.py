# write a program which finds out whether a given name is present in list or not 

# List of names
names = ["Karan", "Yash", "Rohan", "Rohit", "Suraj"]

# Input name from user
name_to_check = input("Enter the name to search : ").capitalize()

# Check if the name is in the list
if name_to_check in names:
    print(f"{name_to_check} is present in the list.")
else:
    print(f"{name_to_check} is not present in the list.")
