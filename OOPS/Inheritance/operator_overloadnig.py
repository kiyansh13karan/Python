# operator overloading in python :- 

'''
Operator overloading in python means giving extended meaning to built-in-operators so that they behave differently baseed in the operands. For example, the + operator can be used to add numbers, concatenate strings, or even add two objects of a custom class (like complex numbers , vectors, etc.)
'''

class Number : 
    def __init__(self , n):
        self.n = n 

    def __add__(self , num) :
        return self.n + num.n 
    
n = Number(19)
m = Number(1) 

print(n + m) 

'''
p1 + p2  => p1.__add__(p2)
p1 - p2 => p1.__sub__(p2)
p1*p2 => p1.__mul__(p2)
p1/p2 => p1.__truediv__(p2)
p1//p2 => p1.__floordiv__(p2)
p1==p2 => p1.__eq__(p2) 
p1<p2 => p1.__it__(p2)
p1>p2 => p1.__gt__(p2) 
'''


'''
Why we use operator overloading :- 

makes your custom classes behave like built-in-types. 
Improves code readability and usabilit. 
Adds flexibility and power to your classes. 
'''





