#  append mode :- (this mode adds conttent at the end of file)

f = open("File Handling/second.txt" , "a") 
f.write("I am learning Python.\n")
f.close() 

# write mode :- (This mode erase the old data and overwrite the content)

f = open("File Handling/second.txt" , "w") 
f.write("I am learning Python.\n")
f.close() 