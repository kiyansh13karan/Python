# write a program to check whether inputed number is even or odd using user defined function :-

# function definition :- 
def check_num(x) :
    if(x % 2 == 0) :
        return 1
    elif(x % 2 != 0) :
        return 0
    else : 
        print("Invalid number.")

# main function :-
num = int(input("Enter any number : "))
res = check_num(num) 
if(res == 1) :
    print("Inputed number is EVEN")
elif(res == 0) :
    print("Inputed number is ODD.") 
