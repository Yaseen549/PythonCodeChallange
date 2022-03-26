import random
from codes.day7 import hangman_art
from codes.day7 import hangman_words

# name_list = ["zeebra", "liion", "elephant"]
lives = 6
randomName = random.choice(hangman_words.word_list)
print(f"Secret: {randomName}")
word_length = len(randomName)
# print(word_length)
guess_list = []
for letter in randomName:
    guess_list.append("_")
print(guess_list)

print(len(randomName))

end_result = ""

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ")
    for position in range(word_length):
        if guess == randomName[position]:
            guess_list[position] = guess

    if "_" not in guess_list:
        end_of_game = True
        print(f"You Won the game, still you have {lives} lives remaining")
    if guess not in guess_list:
        if lives > 0:
            lives -= 1
            print(f"you have {lives} lives remaining")
        else:
            end_of_game = True
            print("Game Over")
    print(f"{' '.join(guess_list)}")

    print(hangman_art.stages[lives])

# for each_letter in randomName:
#     position = randomName.index(each_letter)
#     if guess == each_letter:
#         guess_list[position] = each_letter
# print(guess_list)


