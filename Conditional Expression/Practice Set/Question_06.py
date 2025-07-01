# Write a program to calculate the grade of a student from his marks from the following scheme:
'''90 - 100 => Excellent

80 - 90 => A

70 - 80 => B

60 - 70 => C

50 - 60 => D

< 50 => F'''




# Input marks from user
marks = float(input("Enter your marks (0-100): "))

# Check grade based on given scheme
if(marks>=90 and marks<=100) :
    print("Grade : Excelllent")
elif(marks>=80 and marks<90) :
    print("Grade : A")
elif(marks>=70 and marks<80) :
    print("Grade : B")
elif(marks>=60 and marks<70) :
    print("Grade : C")
elif(marks>=50 and marks<60) :
    print("Grade : D")
elif(marks<50 and marks>=0) :
    print("Grade : F")
else:
    print("Invalid marks! Please enter a value between 0 and 100.")
