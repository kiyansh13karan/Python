#  write a python program to create a dictionary of english words with values as their hindi translation. provide user with an option to look it up 

english_to_hindi = {
    "Hello": "नमस्ते",
    "Thank you": "धन्यवाद",
    "Please": "कृपया",
    "Absolutely": "बिल्कुल",
}

def translate_english_to_hindi():
    print("Welcome to the English to Hindi Dictionary!")
    print("Type 'exit' to quit the program.")
    
    while True:
        english_word = input("Enter a English word to translate: ")
        
        if english_word.lower() == 'exit':
            print("Exiting the dictionary. Goodbye!")
            break
        
        translation = english_to_hindi.get(english_word)
        
        if translation:
            print(f"The Hindi translation of '{english_word}' is: '{translation}'")
        else:
            print(f"Sorry, the word '{english_word}' is not in the dictionary.")

if __name__ == "__main__":
    translate_english_to_hindi()
