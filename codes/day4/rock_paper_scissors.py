import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computerChoice = random.randint(0,2)

rock1 = 0
paper1 = 1
scissor1 = 2

optionList = [rock, paper, scissors]

print(f"Your Choice: {userChoice} {optionList[userChoice]}")
print(f"Computer Choose: {computerChoice} {optionList[computerChoice]}")

if userChoice >= 3 or userChoice < 0:
  print("Invalid input")
elif userChoice == computerChoice:
    print("it is a draw!")
elif userChoice == 2 and computerChoice == 0:
  print("Computer wins")
elif userChoice == 0 and computerChoice == 2:
  print("You win")
elif userChoice > computerChoice:
  print("You Win")
elif userChoice < computerChoice:
  print("Computer Wins")











