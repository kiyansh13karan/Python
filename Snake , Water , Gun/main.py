# write a python program of Snake , water , Gun game 
'''
Rules :-
    Snake drinks water → Snake wins
    Water douses gun → Water wins
    Gun kills snake → Gun wins
    Same choice → Draw
'''


import random

def game_result(user, comp) :
    if user == comp :
        return "It's a draw!"
    elif (user == 's' and comp == 'w') or \
         (user == 'w' and comp == 'g') or \
         (user == 'g' and comp == 's'):
        return "You win!"
    else :
        return "You lose!"

print("Welcome to Snake, Water, Gun Game!")
print("Enter your choice :")
print("s for Snake")
print("w for Water")
print("g for Gun")

# List of options
options = ['s', 'w', 'g']

# Computer randomly selects one
comp_choice = random.choice(options)

# User input
user_choice = input("Your turn : ").lower()

if user_choice not in options :
    print("Invalid input! Please choose s, w, or g.")
else :
    print(f"Computer chose: {comp_choice}")
    print(f"You chose: {user_choice}")
    print(game_result(user_choice, comp_choice))
