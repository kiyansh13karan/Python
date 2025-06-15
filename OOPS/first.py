class Student : 

    def __init__(self , name , marks) : 
        self.name = name
        self.marks = marks 
        print("adding new student to Database....")



s1 = Student("Karan Nayal" , "89")
print(s1.name , s1.marks)

s2 = Student("Yash Nayal" , "99")
print(s2.name , s2.marks)

