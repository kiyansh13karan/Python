# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def display_info(self):
        print(f"Name : {self.name}, Age : {self.age}, Language : {self.language}")

# Creating objects for a few programmers
prog1 = Programmer("Karan Nayal", 19, "Python")
prog2 = Programmer("Yash Nayal", 18, "C#")
prog3 = Programmer("Anjali Nayal", 20, "JavaScript")

# Displaying information
prog1.display_info()
prog2.display_info()
prog3.display_info()

# Output:
# Name: Alice, Age: 30, Language: Python
# Name: Bob, Age: 28, Language: C#
# Name: Charlie, Age: 35, Language: JavaScript