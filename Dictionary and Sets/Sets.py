# Sets in Python
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set :", my_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding 6:", my_set)

# Adding multiple elements to a set
my_set.update([7, 8, 9])
print("Set after adding 7, 8, 9:", my_set)

# Removing elements from a set
my_set.remove(2)  # Raises KeyError if the element is not found
print("Set after removing 2:", my_set)

# Discarding elements from a set
my_set.discard(3)  # Does not raise an error if the element is not found
print("Set after discarding 3:", my_set)

# Popping an element from a set
popped_element = my_set.pop()  # Removes and returns an arbitrary element
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)

# Checking membership in a set
is_member = 4 in my_set
print("Is 4 in the set?", is_member)







# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union of two sets
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection of two sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference of two sets
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)

# Symmetric difference of two sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", symmetric_difference_set)

# Checking if a set is a subset of another set
is_subset = {1, 2}.issubset(set_a)
print("Is {1, 2} a subset of set_a?", is_subset)

# Checking if a set is a superset of another set
is_superset = set_a.issuperset({1, 2})
print("Is set_a a superset of {1, 2}?", is_superset)

# Clearing a set
my_set.clear()
print("Set after clearing:", my_set)

# Copying a set
copied_set = set_a.copy()
print("Copied set:", copied_set)

# Converting a list to a set to remove duplicates
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print("Unique set from list:", unique_set)

# Set comprehensions
set_comprehension = {x for x in range(10) if x % 2 == 0}
print("Set comprehension (even numbers from 0 to 9):", set_comprehension)

# length of a set
set_length = len(set_a)
print("Length of set_a:", set_length)
















# Frozen sets
# A frozenset is an immutable version of a set.
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", frozen_set)

# Attempting to add an element to a frozenset will raise an error
try:
    frozen_set.add(6)
except AttributeError as e:
    print("Error:", e)
# Attempting to remove an element from a frozenset will raise an error
try:
    frozen_set.remove(2)
except AttributeError as e:
    print("Error:", e)

# However, you can still perform set operations with frozensets
frozen_set_a = frozenset([1, 2, 3])
frozen_set_b = frozenset([3, 4, 5])

# Union of two frozensets
frozen_union = frozen_set_a.union(frozen_set_b)
print("Union of frozen_set_a and frozen_set_b:", frozen_union)

# Intersection of two frozensets
frozen_intersection = frozen_set_a.intersection(frozen_set_b)
print("Intersection of frozen_set_a and frozen_set_b:", frozen_intersection)

# Difference of two frozensets
frozen_difference = frozen_set_a.difference(frozen_set_b)
print("Difference of frozen_set_a and frozen_set_b:", frozen_difference)

# Symmetric difference of two frozensets
frozen_symmetric_difference = frozen_set_a.symmetric_difference(frozen_set_b)
print("Symmetric difference of frozen_set_a and frozen_set_b:", frozen_symmetric_difference)

# Checking if a frozenset is a subset of another frozenset
is_frozen_subset = frozenset([1, 2]).issubset(frozen_set_a)
print("Is frozenset([1, 2]) a subset of frozen_set_a?", is_frozen_subset)

# Checking if a frozenset is a superset of another frozenset
is_frozen_superset = frozen_set_a.issuperset(frozenset([1, 2]))
print("Is frozen_set_a a superset of frozenset([1, 2])?", is_frozen_superset)

# Copying a frozenset
copied_frozen_set = frozen_set_a.copy()
print("Copied frozenset:", copied_frozen_set)

# Converting a list to a frozenset to remove duplicates
list_with_duplicates_frozen = [1, 2, 2, 3, 4, 4, 5]
unique_frozen_set = frozenset(list_with_duplicates_frozen)
print("Unique frozenset from list:", unique_frozen_set)
