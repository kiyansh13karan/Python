# writing a file in python 

# Open a file in write mode
file_path = 'File Handling/writing.txt'
with open(file_path, 'w') as file:
    file.write("Hello Karan!\n") # Write content to the file
    file.write("How are you doing ?") # Write content to the file
'''
Output :- 

Hello Karan!
How are you doing ?
'''
# Close the file
# Note: The 'with' statement automatically closes the file after the block is executed, so explicit close is not necessary.



# If you want to write multiple lines, you can use a loop or write them one by one:
with open(file_path, 'w') as file:
    lines = ["Hello Karan!\n", "How are you doing ?\n", "I am fine, thank you!\n"]
    file.writelines(lines)  # Write multiple lines to the file
'''
Output :-

Hello Karan!
How are you doing ?
I am fine, thank you!
'''




# Numbered custom text list (If you have a list of lines and want to number them)
lines = ["Apple", "Banana", "Cherry"]

with open(file_path, 'w') as f :
    for i , line in enumerate(lines, start=1) :
        f.write(f"{i}. {line}\n")

'''
Output :-

1. Apple
2. Banana
3. Cherry
'''