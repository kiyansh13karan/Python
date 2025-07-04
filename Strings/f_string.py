# f string in python 

# f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces `{}`. They are prefixed with the letter `f` or `F`.

name = "John"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)




# f-strings can also include expressions and function calls
def double_age(age):
    return age * 2

doubled_greeting = f"Hello, my name is {name} and I am {double_age(age)} years old."
print(doubled_greeting)



# f-strings can handle complex expressions
complex_expression = f"The sum of 2 and 3 is {2 + 3}, and the product of {age} and 2 is {age * 2}."
print(complex_expression)




# f-strings can also format numbers
pi = 3.14159
formatted_pi = f"The value of pi is approximately {pi:.2f}."
print(formatted_pi)




# f-strings can include dictionary values
person = {"name": "Alice", "age": 28}
person_greeting = f"Hello, my name is {person['name']} and I am {person['age']} years old."
print(person_greeting)



# f-strings can also include lists
fruits = ["apple", "banana", "cherry"]
fruits_greeting = f"Hello, my favorite fruits are {', '.join(fruits)}."
print(fruits_greeting)




# f-strings can include conditional expressions
is_adult = age >= 18
conditional_greeting = f"Hello, my name is {name} and I am {'an adult' if is_adult else 'a minor'}."
print(conditional_greeting)



# f-strings can include nested expressions
nested_expression = f"Hello, my name is {name} and I am {age + (5 if is_adult else 0)} years old in 5 years."
print(nested_expression)



# f-strings can also include escape sequences
escaped_greeting = f"Hello, my name is {name}.\nI am {age} years old.\nNice to meet you!"
print(escaped_greeting)



# f-strings can be used with multi-line strings
multi_line_greeting = f"""Hello, my name is {name}.
I am {age} years old.
Nice to meet you!"""
print(multi_line_greeting)




# f-strings can also include Unicode characters
unicode_greeting = f"Hello, my name is {name}.\nI am {age} years old.\nNice to meet you! \u263A"
print(unicode_greeting)



# f-strings can include escape sequences for special characters
special_char_greeting = f"Hello, my name is {name}.\nI am {age} years old.\nNice to meet you! \tThis is a tabbed line."
print(special_char_greeting)



# f-strings can also include raw strings
raw_string_greeting = rf"Hello, my name is {name}.\nI am {age} years old.\nNice to meet you! \nThis is a raw string with no escape sequences."
print(raw_string_greeting)



# f-strings can include backslashes
backslash_greeting = f"Hello, my name is {name}.\nI am {age} years old.\nNice to meet you! \\ This is a backslash."
print(backslash_greeting)



# f-strings can also include special formatting for dates
from datetime import datetime
today = datetime.today()
date_greeting = f"Hello, today is {today:%B %d, %Y}."
print(date_greeting)



