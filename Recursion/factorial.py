# write a program to find factorial of n number using recursion :-

# function definition :-
def cal_fact(n) :
    if(n==0 or n==1) :
        return 1 
    else :
        return cal_fact(n-1) * n 
    

# main function :-
num = int(input("Enter n number : ")) 
x = cal_fact(num) 
print("Factorial of inputed number is : " , x)
