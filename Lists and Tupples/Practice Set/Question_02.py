# write a program to accept marks of 6 students and display them in a sorted manner

marks = []
for i in range(6):
    mark = int(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)
marks.sort()
print("The sorted marks of the students are:", marks)
