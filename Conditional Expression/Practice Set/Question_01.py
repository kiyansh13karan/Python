# write a program to find greatest of four numbers entered by the user 


# Input from user
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

# Compare numbers using if-elif-else
if(a >= b and a >= c and a >= d) :
    print("\nThe greatest number is:", a)
elif(b >= a and b >= c and b >= d) :
    print("\nThe greatest number is:", b)
elif(c >= a and c >= b and c >= d) :
    print("\nThe greatest number is:", c)
else :
    print("\nThe greatest number is:", d)
