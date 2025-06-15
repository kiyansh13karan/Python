# write a program to find the length of any string using user defined function :-

# function defination 
def lent(x) :
    count = 0
    i=0
    for el in x : 
        count = count + 1 
        i+=1 
    return count

# main function :-
inp = input("Enter any string : ")
res = lent(inp) 
print("Length of inputed string is : " , res)

