# class mtehod in python

'''
In Python, a class method is a method that is bound to the class, not the instance of the class. It can modify class state that applies across all instances of the class.
'''



'''
Key Points :- 

Defined using the @classmethod decorator.
First argument is cls (refers to the class, not the instance).
Can access or modify class variables (shared by all instances).
'''



# Syntax :-
'''
class MyClass:
    @classmethod
    def my_class_method(cls, args) :
        # method body
'''





# Example 1: Basic Class Method
class Employee:
    company_value = 50 

    @classmethod
    def show(cls) :
        print(f"The class attribute of company value is {cls.company_value}")

e = Employee()
e.change_company_value = 100

e.show()  # Calls the class method
    