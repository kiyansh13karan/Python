# Write a program to make a copy of a text file “poems. txt”


# Original and copy file paths
original_file = "File Handling/Practice Set/poems.txt"       # Replace with your source file name
copy_file = "File Handling/Practice Set/copy_of_poem.txt"   # Replace with desired name for the copied file

# Read from original and write to copy
with open(original_file, "r") as source:
    content = source.read()

with open(copy_file, "w") as destination:
    destination.write(content)

print(f"✅ File copied successfully from '{original_file}' to '{copy_file}'.")
