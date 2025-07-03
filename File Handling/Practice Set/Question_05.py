# Write a program to mine a log.txt file and find out whether it contains ‘python’. (case sensitive)    

def check_python_in_log(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if 'python' in content.lower() :
                print("The log file contains the word 'python'.")
            else:
                print("The log file does not contain the word 'python'.")
    except Exception as e:
        print(f"An error occurred: {e}")

check_python_in_log("File Handling/Practice Set/logfile.txt")
