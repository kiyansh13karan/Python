# different methods of file handling in python



# 1. Opening a file :- 
'''
file = open("filename.txt", "mode")
'''


# 2. (a) Writng a file :- (writes a single string to the file)
'''
with open('file.txt', 'w') as f:
    f.write("Hello, World\n")
'''


# (b) writelines() :- Writes multiple lines (no newline auto-added).
'''
lines = ["Line 1\n", "Line 2\n"]
with open('file.txt', 'w') as f:
    f.writelines(lines)
'''


# 3. Reading from a file :- 
# (a) read() :- (Reads the whole file) 
'''
with open('file.txt', 'r') as f:
    content = f.read()
'''

# (b) readline() :- (Reads one line at a time.)
'''
with open('file.txt', 'r') as f:
    line = f.readline()
'''


# (c) readlines() :- (Returns a list of all lines.)
'''
with open('file.txt', 'r') as f:
    lines = f.readlines()
'''



# 4 . Appending to a File :- 
'''
with open('file.txt', 'a') as f:
    f.write("This will be added at the end.\n")
'''



# 5. Using with Statement :- 
'''
with open('file.txt', 'r') as f:
    data = f.read()
'''
# Advantages of using 'with' statement:
# 1. Automatically closes the file
# 2. Cleaner and safer
# 3. Reduces the risk of file corruption or memory leaks



# 6. Closing a File
'''
f = open('file.txt', 'r')
data = f.read()
f.close()
'''
# Note: It's important to close the file to free up system resources.



# 7.  Check File Exists Before Writing (Optional)
'''
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")
'''
# Note: This is useful to avoid overwriting existing files unintentionally.