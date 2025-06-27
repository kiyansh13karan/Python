# Write a program to take 7 numbers from user and count the occurence of zero in that tupple

numbers = []
for i in range(7):
    number = int(input(f"Enter number {i + 1} : "))
    numbers.append(number)
numbers_tuple = tuple(numbers)
zero_count = numbers_tuple.count(0)
print("The tuple of numbers is :", numbers_tuple)
print("The count of zero in the tuple is :", zero_count)