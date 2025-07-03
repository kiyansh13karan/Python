# Write a program to find out the line number where python is present in Question_06.py file.



# File path to the log file
file_path = "File Handling/Practice Set/logfile.txt"  # Replace with your actual file name

# Track whether 'python' was found
found = False

# Open and read the file line by line
with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        if 'python' in line.lower():
            print(f"✅ 'python' found on line {line_number}: {line.strip()}")
            found = True

if not found:
    print("❌ The word 'python' was not found in the log file.")


