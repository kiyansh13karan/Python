# write a program to rename a file 


import os

# Old file name (the file that already exists)
old_name = "File Handling/Practice Set/text.txt"   # Replace with your existing file name

# New file name (the name you want to give)
new_name = "File Handling/Practice Set/renamed_text_file.txt"  # Replace with your desired new name

# Rename the file
os.rename(old_name, new_name)

print(f"✅ File renamed from '{old_name}' to '{new_name}'.")
