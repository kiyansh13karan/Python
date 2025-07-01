# write a program to find sum of first n natural number using loop

n = int(input("Enter the value of n : "))
total = 0
for i in range(1 , n + 1) :
    total = total + i
print("Sum of first", n, "natural numbers is :", total)