# Question : write a program to find multiple of 7 . 

num = int(input("Enter any number : ")) 

if(num % 7 == 0) : 
    print("Entered number  is multiple of 7.")
elif(num % 7 != 0) : 
    print("Entered number is not a multiple of 7.")
else : 
    print("Invalid number.")