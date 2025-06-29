# write a python program to to input eight numbers from the user and display all the unique numbers (once)

def get_unique_numbers() :
    print("Enter eight numbers (press Enter after each number):")
    unique_numbers = set()  # Using a set to store unique numbers

    for _ in range(8) :
        try:
            number = int(input())
            unique_numbers.add(number)  # Add the number to the set
        except ValueError:
            print("Please enter a valid integer.")

    print("Unique numbers entered :", unique_numbers)

if __name__ == "__main__" :
    get_unique_numbers()
    