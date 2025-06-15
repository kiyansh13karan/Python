#  Question : Write a program to fid largest of three number. 

a = int(input("Enter first number a : "))
b = int(input("Enter second number b : "))
c = int(input("Enter third number c : "))

if(a >= b and a >=c) : 
    print("\nLargest number is a : " , a) 
elif(b >= a and b >= c) : 
    print("\nLargest number is b : " , b) 
else : 
    print("\nLargest number is c : " , c)
