# write a progrsm to calculate sum of first n number , using recursion :-

# function definition :_
def cal_sum(n) :
    if(n==0) :
        return 0 
    return cal_sum(n-1) + n 

# main function :-
num = int(input("Enter n number : ")) 
res = cal_sum(num)
print("Sum of first inputed natural number is : " , res)  