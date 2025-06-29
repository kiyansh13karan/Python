# Dictionary in Python
# A dictionary is a collection of key-value pairs. in which each key is unique and values can be same if keys are same then it will update the value of key
# Each key is unique and maps to a value.

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair
my_dict["job"] = "Engineer"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Updating an existing value
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}

# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary")  # Output: Name exists in the dictionary

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 31
# job: Engineer

# Getting the keys and values
print(my_dict.keys())   # Output: dict_keys(['name', 'age', 'job'])
print(my_dict.values()) # Output: dict_values(['Alice', 31, 'Engineer'])

# Getting the items (key-value pairs)
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('job', 'Engineer')])

# Copying a dictionary
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}

# Clearing a dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Merging dictionaries
another_dict = {
    "country": "USA",
    "language": "English"
}

# Merging with the update method
my_dict.update(another_dict)
print(my_dict)  # Output: {'country': 'USA', 'language': 'English'}

# Merging with the union operator (Python 3.9+)
my_dict = my_dict | another_dict
print(my_dict)  # Output: {'country': 'USA', 'language': 'English'}







# Nested dictionaries
nested_dict = {
    "person": {
        "name": "Bob",
        "age": 25
    },
    "address": {
        "city": "Los Angeles",
        "state": "CA"
    }
}

# Accessing nested dictionary values
print(nested_dict["person"]["name"])  # Output: Bob
print(nested_dict["address"]["city"])  # Output: Los Angeles

# Adding a new key-value pair to a nested dictionary
nested_dict["person"]["job"] = "Designer"
print(nested_dict)  # Output: {'person': {'name': 'Bob', 'age': 25, 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'CA'}}

# Updating a value in a nested dictionary
nested_dict["address"]["state"] = "California"
print(nested_dict)  # Output: {'person': {'name': 'Bob', 'age': 25, 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'California'}}

# Removing a key-value pair from a nested dictionary
del nested_dict["person"]["age"]
print(nested_dict)  # Output: {'person': {'name': 'Bob', 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'California'}}

# Checking if a key exists in a nested dictionary
if "job" in nested_dict["person"]:
    print("Job exists in the person dictionary")  # Output: Job exists in the person dictionary

# Iterating through a nested dictionary
for outer_key, outer_value in nested_dict.items():
    print(f"{outer_key}:")
    for inner_key, inner_value in outer_value.items():
        print(f"  {inner_key}: {inner_value}")
# Output:
# person:
#   name: Bob
#   job: Designer
# address:
#   city: Los Angeles
#   state: California

# Getting keys and values from a nested dictionary
print(nested_dict["person"].keys())   # Output: dict_keys(['name', 'job'])
print(nested_dict["address"].values()) # Output: dict_values(['Los Angeles', 'California'])

# Getting items from a nested dictionary
print(nested_dict["person"].items())  # Output: dict_items([('name', 'Bob'), ('job', 'Designer')])

# Copying a nested dictionary
nested_copy = nested_dict.copy()
print(nested_copy)  # Output: {'person': {'name': 'Bob', 'job': 'Designer'}, 'address': {'city': 'Los Angeles', 'state': 'California'}}

# Clearing a nested dictionary
nested_dict.clear()
print(nested_dict)  # Output: {}

# Merging nested dictionaries
another_nested_dict = {
    "person": {
        "name": "Charlie",
        "age": 28
    },
    "address": {
        "city": "San Francisco",
        "state": "CA"
    }
}

# Merging with the update method
nested_dict.update(another_nested_dict)
print(nested_dict)  # Output: {'person': {'name': 'Charlie', 'age': 28}, 'address': {'city': 'San Francisco', 'state': 'CA'}}

# Merging with the union operator (Python 3.9+)
nested_dict = nested_dict | another_nested_dict
print(nested_dict)  # Output: {'person': {'name': 'Charlie', 'age': 28}, 'address': {'city': 'San Francisco', 'state': 'CA'}}

# Nested dictionaries can also be used to represent more complex data structures
# like JSON objects, configurations, or any hierarchical data.
