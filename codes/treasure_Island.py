print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

left = "left"
right = "right"
swim = "swim"
wait = "wait"
redDoor = "red"
blueDoor = "blue"
yellowDoor = "yellow"

leftorRight = input("Where do you want to go? 'right' or 'left': ")


if leftorRight == right:
  print("Fall into a hole. Game over")
elif leftorRight == left:
  siwmOrWait = input("There is a lake, Do you want to swim or wait? 'swim' or 'wait': ")
  if siwmOrWait == swim:
    print("Attacked by trout. Game Over")
  elif siwmOrWait == wait:
    selectADoor = input("Select a Door, you need to enter: 'Red', 'Blue' or 'Yellow': ")
    if selectADoor == redDoor:
      print("Burned by fire. Game Over")
    elif selectADoor == blueDoor:
      print("Eaten by bests, game over.")
    elif selectADoor == yellowDoor:
      print("You got the treasure. You Win")
    else:
      print("Game Over.")
