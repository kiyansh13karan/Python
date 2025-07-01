# Write a program using functions to find greatest of three numbers.

def find_greatest(num1 , num2 , num3) : 
    if(num1>num2 and  num1>num3) :
        print(f"{num1} is greatest")
    elif(num2>num1 and num2>num3) : 
        print(f"{num2} is greatest")
    else :
        print(f"{num3} is greatest") 


num1 = int(input("Enter first number : ")) 
num2 = int(input("Enter second number : ")) 
num3 = int(input("Enter third number : ")) 

find_greatest(num1 , num2 ,num3) 