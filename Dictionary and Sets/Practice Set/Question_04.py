# create an empty dictionary . Allow four friends to enter their favorite languages as values and use keys as theor names. Assume that the names are unique.


# Create an empty dictionary
favorite_languages = {}
# Allow four friends to enter their favorite languages
for _ in range(4):
    name = input("Enter your name: ")
    language = input(f"{name}, enter your favorite programming language: ")
    favorite_languages[name] = language
# Print the dictionary
print("Favorite Languages Dictionary :")
print(favorite_languages)
# Print the type of the dictionary
print("Type of the dictionary:", type(favorite_languages))
