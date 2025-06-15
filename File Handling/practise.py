# WAP to store :-
# "Hiee everyone."
# "I am learning File I/O"
# "I like Python language."
# *******Solution**********
# with open("File Handling/practise.txt" , "w") as f :
#     f.write("Hiee everyone.\nI am learning file I/O in Java Script.\n")
#     f.write("I like Java Script language. \n")





#  write a function to replace all occurance of JAVA with PYTHON in above file
# ******Solution*******
# with open("File Handling/practise.txt" , "r") as f :
#     data = f.read()

# newdata = data.replace("Java Script" , "Python")
# print(newdata) 

# with open("File Handling/practise.txt" , "w") as f :
#     f.write(newdata)




#  search if the word "learning" exist in file or not 
# ********Solution**********
# word = "learning"
# with open("File Handling/practise.txt" , "r") as f :
#     data = f.read() 
#     if(data.find(word) != -1) :
#         print("Found")
#     else :
#         print("Not Found")

 



# WAF to find in which line of the file does the word "learning" occur first
# ********Solution*********
# def check_for_line() :
#     word = "learning" 
#     data = True
#     line_no = 1 
#     with open("File Handling/practise.txt" , "r") as f :
#         while data :
#             data = f.readline()
#             if(word in data) :
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()

        






# WAP to check file containig numbers separated by commas , print the count of even numbers
# **********Solution********
# with open("File Handling/practise.txt" , "w") as f :
#     f.write("1 , 4 , 6 , 24 , 10 , 3 , 33 , 76 , 99") 
    

# count = 0
# with open("File Handling/practise.txt" , "r") as f :
#     data = f.read() 

#     num = data.split(",")
#     for val in num :
#         if(int(val) % 2 == 0) :
#             count += 1

# print(count) 

