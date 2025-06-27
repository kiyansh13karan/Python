# write a program to to store seven fruits in a list entered by a user and then print the list

fruits = []
for i in range(7):
    fruit = input(f"Enter fruit {i + 1} : ")
    fruits.append(fruit)
print("The list of fruits is:", fruits)
