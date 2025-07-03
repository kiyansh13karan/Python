# Write a program to wipe out the content of a file using python.


file_path = "File Handling/Practice Set/sample.txt"

# Wipe out the content of the file
with open(file_path, "w") as file:
    file.write("")

print(f"✅ The content of the file '{file_path}' has been wiped out.")
