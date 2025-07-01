# write a program to find factorial of n number using user defined function :-


# factorial of n number using loop
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







# factorial of n number using recursion
def factorial(num) : 
    if(num==1 or num==0) : 
        return 1 
    return num * factorial(num-1)


num = int(input("Enter a number : "))
print(f"The factorial of {num} is : {factorial(num)}") 