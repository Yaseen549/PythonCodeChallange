#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# print(art.logo)

levelValue = 0

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 & 100.")
level = input("choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    levelValue = 10
else:
    levelValue = 5

randomNumber = random.randint(1, 100 + 1)
# print("-------",randomNumber,"--------")


end_of_game = False

while not end_of_game:
    print("You have ", levelValue, " attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    # next_guess = int(input(""))
    if guess > randomNumber:
        print("Too high.\nGuess Again.")
    elif guess < randomNumber:
        print("Too low.\nGuess Again.")
    elif guess == randomNumber:
        print("You got it: ", randomNumber)
        end_of_game = True

    levelValue -= 1
    if levelValue < 1:
        print("You've run out of guesses, you lose.")
        end_of_game = True

