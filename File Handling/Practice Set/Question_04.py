# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.



def replace_word_in_file(file_path, target_word, replacement_word):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replace the target word with the replacement word
        updated_content = content.replace(target_word, replacement_word)
        
        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)
        
        print(f"Successfully replaced '{target_word}' with '{replacement_word}' in {file_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

replace_word_in_file("File Handling/Practice Set/Donkey.txt", "Donkey", "#####")
# Example usage
# replace_word_in_file("path/to/your/file.txt", "Donkey", "#####")
# Make sure to replace "path/to/your/file.txt" with the actual path to your file.
# The file "Donkey.txt" should contain the word "Donkey" multiple times for testing.
# The function will read the file, replace all occurrences of "Donkey" with "#####", and save the changes back to the same file.
# Ensure that the file exists and contains the word "Donkey" for the function to work correctly.