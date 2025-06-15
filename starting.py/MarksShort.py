#  marks sorting :-

marks = [] 

s1 = int(input("Marks in Physics : ")) 
marks.append(s1) 
s2 = int(input("Marks in Chemistry : "))
marks.append(s2)
s3 = int(input("Marks of Maths : "))
marks.append(s3)
s4 = int(input("Marks of English : "))
marks.append(s4)
s5 = int(input("Marks of Hindi : "))
marks.append(s5)

marks.sort()

print(marks)






#  using loop
# n = int(input("Enter number of subjects : "))
# i = 0
# marks = [] 

# for el in range(n) : 
#     x = int(input("Enter marks : "))
#     marks.append(x)
#     i+=1

# marks.sort()
# print(marks)
