# write a program to find whether a given username contains less than 10 characters or not 

# Input username
username = input("Enter your username: ")

# Check length
if len(username) < 10:
    print("Username is too short (less than 10 characters).")
else:
    print("Username is acceptable (10 or more characters).")
