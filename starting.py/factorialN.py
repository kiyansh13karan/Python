# using range function and for loop :-
num = int(input("Enter n : "))

fact = 1 
i = 1 
for el in range(1 , num+1) : 
    fact = fact * i
    i+=1
print("Factorial of n number is : " , fact)



# Using while loop :-
# num = int(input("Enter n : ")) 

# fact = 1 
# i = 1 
# while(i<=num) :
#     fact = fact * i
#     i+=1 
# print("Fcatorial of given number is : " , fact)
