#  reading of file :- 

# f = open("File Handling/first.txt" , "r") 
# data = f.read()
# print(data)
# print(type(data))
# f.close()


#  reading of file one line at a time :- 

f = open("File Handling/first.txt" , "r") 
line1 = f.readline() 
line2 = f.readline()
line3 = f.readline()
print(line1) 
print(line2)
print(line3)
f.close() 
