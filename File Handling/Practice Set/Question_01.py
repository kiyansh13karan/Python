# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.


# Open the file in read mode
with open('File Handling/Practice Set/poems.txt', 'r') as file :
    content = file.read()

# Check if 'twinkle' is in the content
if 'twinkle' in content.lower():
    print("Yes, the word 'twinkle' is present in the file.")
else:
    print("No, the word 'twinkle' is not found in the file.")