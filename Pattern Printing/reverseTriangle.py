'''
****
***
**
*
'''

def reverse_triangle(num) :
    for i in range(num , 0 , -1) :
        print('*' * i)

num = int(input("Enter the number of lines : "))
reverse_triangle(num)