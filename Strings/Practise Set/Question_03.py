# Python program to detect double spaces in a string and replace them with a single space
def replace_double_space(input_string):
    # Replace double spaces with a single space
    modified_string = input_string.replace("  ", " ")
    return modified_string

# Example usage
text = input("Enter a string : ")
result = replace_double_space(text) 
print("Modified string :", result)

