from codes.day14 import game_data
import random

print("---- HigherLower ----")


more_followers = 0
variableLetter = ""
end_of_game = False
currentScore = 0

while not end_of_game:
    firstPerson = random.randint(0, (len(game_data.data)) - 1)
    secondPerson = random.randint(0, (len(game_data.data)) - 1)

    firstPersonName = game_data.data[firstPerson]["name"]
    firstPersonFollowerCount = game_data.data[firstPerson]["follower_count"]
    firstPersonDescription = game_data.data[firstPerson]["description"]
    firstPersonCountry = game_data.data[firstPerson]["country"]

    secondPersonName = game_data.data[secondPerson]["name"]
    secondPersonFollowerCount = game_data.data[secondPerson]["follower_count"]
    secondPersonDescription = game_data.data[secondPerson]["description"]
    secondPersonCountry = game_data.data[secondPerson]["country"]

    print(f"Compare A: {firstPersonName}, {firstPersonDescription}, {firstPersonCountry}")
    print("Vs")
    print(f"Compare B: {secondPersonName}, {secondPersonDescription}, {secondPersonCountry}")

    more_followers = input("Who has more followers? Type 'A' or 'B': ").lower()

    if firstPersonFollowerCount == secondPersonFollowerCount:
        end_of_game = False
    elif firstPersonFollowerCount > secondPersonFollowerCount:
        currentScore += 1
        variableLetter = "a"
    elif secondPersonFollowerCount > firstPersonFollowerCount:
        variableLetter = "b"
        end_of_game = True

    if more_followers == variableLetter:
        print(f"You're right! Current Score: {currentScore}")
    else:
        print(f"Sorry, that's wrong. Final Score: {currentScore}")
