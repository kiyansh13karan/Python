'''
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi-
score whenever the game() function breaks the Hi-score.
'''



def game():
    # Dummy game function
    import random
    return random.randint(0, 100)

# Get the score from game
score = game()
print("Your score :", score)

# Try to read the current high score
try:
    with open("File Handling/Practice Set/Hi-score.txt", "r") as f :
        high_score = f.read()
        if high_score == '':
            high_score = 0
        else:
            high_score = int(high_score)
except FileNotFoundError :
    high_score = 0

# Compare and update if new score is higher
if score > high_score :
    print("Congratulations! New High Score 🎉")
    with open("File Handling/Practice Set/Hi-score.txt", "w") as f:
        f.write(str(score))
else:
    print("Try Again to Beat the High Score!")

# Print current high score
print("Current High Score:", max(score, high_score))
