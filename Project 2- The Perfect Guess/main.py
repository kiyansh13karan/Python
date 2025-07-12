'''
We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number. 
Hint: Use the random module. 
'''


import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    guess = None
    attempts = 0

    print("Guess the number between 1 and 100:")

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess > number_to_guess:
                print("Lower number please")
            elif guess < number_to_guess:
                print("Higher number please")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Run the game
guess_the_number()
