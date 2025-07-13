# Typecasting in Python :- 

'''
Typecasting means converting a value from one data type to another (e.g., from string to integer, integer to float, etc.).
'''


# Types of Typecasting :- 
'''
1. Implicit Typecasting. 
2. Explicit Typecasting. 
'''


'''
1. Implicit Typecasting :- (Automatic)
        Python automatically converts data types where no data loss happens. 
'''
a = 5       # int
b = 2.0     # float
c = a + b   # result is float
print(c)        # 7.0
print(type(c))  # <class 'float'>




'''
2. Explicit Typecasting :- 
        You manually convert data types using functions like int() , float() etc 
'''

# String to int
x = "10"
y = int(x)
print(y + 5)    # Output: 15

# Float to int
print(int(3.9))  # Output: 3

# Int to string
a = 100
b = str(a)
print(b + "5")  # Output: 1005








# Note :- Invalid conversions will raise errors (e.g., int("abc") causes a ValueError).