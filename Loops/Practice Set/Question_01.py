# write a program to print multiplcation table of user inputed number using for loop

# taking user input 
num = int(input("Enter a number : "))

# for loop
i = 0 
for i in range(1 , 11) : 
    print(f"{num} x {i} = {num*i}")
    i+=1 