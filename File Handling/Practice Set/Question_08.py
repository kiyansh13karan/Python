# Write a program to find out whether a file is identical & matches the content of another file.



# File paths (change these as needed)
file1 = "File Handling/Practice Set/poems.txt"
file2 = "File Handling/Practice Set/copy_of_poem.txt"

# Function to compare two files
def are_files_identical(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()
        return content1 == content2

# Check and print result
if are_files_identical(file1, file2):
    print("✅ The files are identical and their content matches.")
else:
    print("❌ The files are different.")


