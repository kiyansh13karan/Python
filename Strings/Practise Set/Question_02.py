# Python program to detect double spaces in a string

def detect_double_space(input_string):
    if "  " in input_string:
        print("Double space detected in the string.")
    else:
        print("No double space found in the string.")

# Example usage
text = input("Enter a string: ")
detect_double_space(text)





