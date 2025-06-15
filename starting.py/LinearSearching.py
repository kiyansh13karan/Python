nums = [1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100] 
print(nums)

x = int(input("Enter any number from nums : ")) 

i = 0 
for val in nums : 
    if(val == x) :
        print("Element found at index : " , i) 
    i += 1
