# wtite a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user 


# Input marks for 3 subjects
sub1 = float(input("Enter marks of subject 1 (out of 100) : "))
sub2 = float(input("Enter marks of subject 2 (out of 100) : "))
sub3 = float(input("Enter marks of subject 3 (out of 100) : "))

# Calculate total and percentage
total = sub1 + sub2 + sub3
percentage = total / 3

# Check conditions
if(sub1 < 33 or sub2 < 33 or sub3 < 33) :
    print("\nFail : Less than 33% in one or more subjects.")
elif(percentage < 40) :
    print("\nFail : Total percentage is less than 40%.")
else :
    print("\nPass : Congratulations! You passed the exam.")

