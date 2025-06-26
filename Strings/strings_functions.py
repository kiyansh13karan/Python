# Inbuilt Functions in python 

name = "Karan Nayal"

# 1. Length 
length = len(name) 
print("Length of string name is : " , length) 

# 2. Ends with 
ends_with = name.endswith("YAL")  # Check if the string ends with "YAL"
print("Does the string end with 'YAL'? :", ends_with)

# 3. Starts with
starts_with = name.startswith("KAR")  # Check if the string starts with "KAR"
print("Does the string start with 'KAR'? :", starts_with)

# 4. Count
count_a = name.count("A")  # Count occurrences of "A"
print("Count of 'A' in the string is : ", count_a)

# 5. Find
find_index = name.find("N")  # Find the index of first occurrence of "N"
print("Index of first occurrence of 'N' is : ", find_index)

# 6. Replace
replace_name = name.replace("NAYAL", "SINGH")  # Replace "NAYAL" with "SINGH"
print("String after replacing 'NAYAL' with 'SINGH' is : ", replace_name)

# 7. Uppercase
uppercase_name = name.upper()  # Convert the string to uppercase
print("String in uppercase is : ", uppercase_name)

# 8. Lowercase
lowercase_name = name.lower()  # Convert the string to lowercase
print("String in lowercase is : ", lowercase_name)

# 9. Title Case
title_case_name = name.title()  # Convert the string to title case
print("String in title case is : ", title_case_name)

# 10. Split
split_name = name.split(" ")  # Split the string by spaces
print("String split by spaces is : ", split_name)

# 11. Join
joined_name = " ".join(split_name)  # Join the list back into a string with spaces
print("Joined string from list is : ", joined_name)

# 12. Strip
strip_name = name.strip()  # Remove leading and trailing whitespace
print("String after stripping leading and trailing whitespace is : ", strip_name)

# 13. Is Alpha
is_alpha = name.isalpha()  # Check if the string contains only alphabetic characters
print("Does the string contain only alphabetic characters? :", is_alpha)

# 14. Is Numeric
is_numeric = name.isnumeric()  # Check if the string contains only numeric characters
print("Does the string contain only numeric characters? :", is_numeric)

# 15. Is Alphanumeric
is_alphanumeric = name.isalnum()  # Check if the string contains only alphanumeric characters
print("Does the string contain only alphanumeric characters? :", is_alphanumeric)

# 16. Is Lower
is_lower = name.islower()  # Check if the string is in lowercase
print("Is the string in lowercase? :", is_lower)

# 17. Is Upper
is_upper = name.isupper()  # Check if the string is in uppercase
print("Is the string in uppercase? :", is_upper)

# 18. Is Title
is_title = name.istitle()  # Check if the string is in title case
print("Is the string in title case? :", is_title)

# 19. Swap Case
swap_case_name = name.swapcase()  # Swap the case of each character in the string
print("String after swapping case is : ", swap_case_name)

# 20. Capitalize
capitalize_name = name.capitalize()  # Capitalize the first character of the string
print("String after capitalizing the first character is : ", capitalize_name)

# 21. Center
centered_name = name.center(20, '-')  # Center the string within a width of 20, padding with '-'
print("String centered with '-' padding is : ", centered_name)

