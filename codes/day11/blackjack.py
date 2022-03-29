import os
from codes.day11 import art
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculation(final_user_total, final_computer_total):

    print(f"\tYour cards: {listOfCards}, current score: {final_user_total}")
    print(f"\tComputer's first card: {listOfComputerCards[0]}")

    if final_user_total == final_computer_total:
        print(f"\tYour final hand: {listOfCards}, final score: {final_user_total}")
        print(f"\tComputer's final hand: {listOfComputerCards}, final score: {final_computer_total}")
        print("Draw")
    elif (21 >= final_user_total >= final_computer_total) or (final_user_total <= final_computer_total <= 21):
        function()
    elif final_user_total <= 21 < final_computer_total:
        print(f"\tYour final hand: {listOfCards}, final score: {final_user_total}")
        print(f"\tComputer's final hand: {listOfComputerCards}, final score: {final_computer_total}")
        print("Opponent went over. You win 😃")

    elif final_user_total > 21 or final_user_total < final_computer_total:
        print(f"\tYour final hand: {listOfCards}, final score: {final_user_total}")
        print(f"\tComputer's final hand: {listOfComputerCards}, final score: {final_computer_total}")
        print("You went over. You lose 😭")


def function():
    choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if choice == "y":
        new_random_card = random.randint(0, len(cards) - 1)
        new_computer_random_card = random.randint(0, len(cards) - 1)
        listOfCards.append(cards[new_random_card])
        listOfComputerCards.append(cards[new_computer_random_card])

        user_score = sum(listOfCards)
        computer_score = sum(listOfComputerCards)

        calculation(final_user_total=user_score, final_computer_total=computer_score)

    else:
        # print(user_total, computer_total)
        if user_total <= computer_total <= 21:
            print(f"\tYour final hand: {listOfCards}, final score: {user_total}")
            print(f"\tComputer's final hand: {listOfComputerCards}, final score: {computer_total}")
            print("You went over. You lose 😭")
        elif 21 >= user_total >= computer_total:
            print(f"\tYour final hand: {listOfCards}, final score: {user_total}")
            print(f"\tComputer's final hand: {listOfComputerCards}, final score: {computer_total}")
            print("Opponent went over. You win 😃")

    # print(f"\tYour final hand: {listOfCards}, final score: {final_user_total}")
    # print(f"\tComputer's final hand: {listOfComputerCards}, final score: {final_computer_total}")


is_play = True
while is_play:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == 'n':
        is_play = False
    else:
        clear_screen()
        print(art.logo)
        listOfCards = []
        listOfComputerCards = []
        for i in range(2):
            randomCard = random.randint(0, len(cards) - 1)
            computerRandomCard = random.randint(0, len(cards) - 1)

            cardsScore = cards[randomCard]
            computerCardsScore = cards[computerRandomCard]

            listOfCards.append(cardsScore)
            listOfComputerCards.append(computerCardsScore)

        user_total = sum(listOfCards)
        computer_total = sum(listOfComputerCards)

        ace = 11
        # print(listOfCards)
        # print(listOfComputerCards)
        # print(user_total)
        # print(computer_total, "\n\n")

        # print("\n\n")
        if ace in listOfCards:
            position = listOfCards.index(ace)
            listOfCards[position] = 1
        if ace in listOfComputerCards:
            position = listOfComputerCards.index(ace)
            listOfComputerCards[position] = 1

        # print(listOfCards)
        # print(listOfComputerCards)

        # print(user_total)
        # print(computer_total)

        print(f"\tYour cards: {listOfCards}, current score: {user_total}")
        print(f"\tComputer's first card: {listOfComputerCards[0]}")

        function()
