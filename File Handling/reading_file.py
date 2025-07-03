# reading a file in python 

# Open a file in read mode
file_path = 'reading.txt'
with open(file_path, 'r') as file :
    content = file.read()
    print(content)
# Close the file
file.close()

# Note: The 'with' statement automatically closes the file after the block is executed, so explicit close is not necessary.


# If you want to read the file line by line, you can use a loop:
with open(file_path, 'r') as file :
    for line in file :
        print(line)




# Alternatively, you can read all lines into a list:
with open(file_path, 'r') as file :
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes leading/trailing whitespace including newlines




# You can also read a specific number of characters from the file:
with open(file_path, 'r') as file :
    content = file.read(10)  # Read the first 10 characters
    print(content)




# To read the file in binary mode, you can use 'rb':
with open(file_path, 'rb') as file:
    content = file.read()
    print(content)  # This will print the binary content of the file




# To read a file with error handling, you can use try-except:
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")



# To read a file with a specific encoding (e.g., UTF-8):
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)  # This will read the file with UTF-8 encoding



# To read a file and handle different line endings (e.g., Windows vs. Unix):
with open(file_path, 'r', newline='') as file:
    content = file.read()
    print(content)  # This will read the file and handle different line endings correctly



# To read a file and handle large files efficiently, you can read it in chunks:
chunk_size = 1024  # Read 1 KB at a time
with open(file_path, 'r') as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        print(chunk)