# write a program to find factorial of n number using user defined function :-


# function definition :-
def cal_fact(x) :
    fact = 1
    i = 1 
    while (i<=x) :
        fact = fact * i 
        i+=1
    return fact


# main function :-
num = int(input("Enter any number : "))
res = cal_fact(num) 
print("Factorial of inputed number is : " , res)
