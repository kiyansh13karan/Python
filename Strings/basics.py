name = "KARAN" 


# 1.length
length = len(name) ; # This code calculates the length of the string stored in the variable 'name' 
print("Length of the string is : ", length)


# 2. Slicing

# sl = name[firstindex : lastindex] , first index included but last index will not be included
# it gives us the substring from firstindex to lastindex-1
sl = name[1 : 4] 
print("Slicing the string from index 1 to 4 gives us : ", sl)


# 3. negative slicing
# sl = name[-firstindex : -lastindex] , first index included but last index will not be included
sl = name[-5 : -2]
print("Negative Slicing the string from index -5 to -2 gives us : ", sl)

print("Without starting index : " , name[:5]) # Slicing from start to index 5 
print("Without ending index : " , name[0:]) # Slicing from zero index to end 


 # 4. slicing with step 
sl = name[0:5:2] # Slicing from index 0 to 5 with step of 2
print("Slicing the string from index 0 to 5 with step of 2 gives us : ", sl)