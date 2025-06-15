# write a program to print counting till n number , using recursion :-

# function definition :-
def count(x) :
    if(x == 0) :
        return
    print(x)
    count(x-1)
    print("KARAN")

# main function :-
num = int(input("Enter the value of n ")) 
count(num)


