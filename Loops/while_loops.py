# while loops in python
# A while loop in Python is used to repeatedly execute a block of code as long as a condition is True.
'''
while condition:
    # Code block to execute

'''

# Example 1: Print numbers from 1 to 5
i = 1
while (i <= 5) :
    print(i)
    i += 1





# Example 2: Sum of numbers from 1 to 10
total = 0
num = 1

while (num <= 10) :
    total += num
    num += 1
print("Sum : ", total)




# print a list using for loop 
list1 = ["Karan" , "Yahsu" , "Anjali" , "Manju" , "Rajender"] 
i=0 
while(i < len(list1)) :
    print(list1[i]) 
    i = i + 1 

