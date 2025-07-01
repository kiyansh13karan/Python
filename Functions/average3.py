# average of three numbers 

def cal_avg(x , y , z) :
    sum = x + y + z 
    avg = sum/3 
    return avg

num1 = int(input("Enter first number : ")) 
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : ")) 

res = cal_avg(num1 , num2 , num3)
print("\nAverage of three number is : " , res)