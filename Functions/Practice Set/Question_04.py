# Write a python function to remove a given word from a list ad strip it at the same time.


def remove_and_strip(word_list, word_to_remove):
    cleaned_list = []
    for word in word_list :
        stripped_word = word.strip()
        if stripped_word != word_to_remove:
            cleaned_list.append(stripped_word)
    return cleaned_list

# Example usage
words = ["  apple", "banana ", "  mango", "banana", " grapes "]
word_to_remove = "banana"

result = remove_and_strip(words, word_to_remove)
print("Updated List :", result)
