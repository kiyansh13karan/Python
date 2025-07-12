'''
Create a class ‘Employee’ and add salary and increment properties to it. 
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary
'''




class Employee:
    def set_salary(self, salary):
        self.salary = salary
        self.increment = 1.1  # Default increment (10%)

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Adjust increment based on desired new salary
        self.increment = new_salary / self.salary



emp = Employee()
emp.set_salary(50000)

print("Current Salary:", emp.salary)
print("Salary After Increment:", emp.salaryAfterIncrement)

# Now change the increment by setting a new salary
emp.salaryAfterIncrement = 60000

print("New Increment Factor:", emp.increment)
print("Updated Salary After Increment:", emp.salaryAfterIncrement)
