import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(len(letters))
userLetters = int(input("How many letters you need?\n"))
userNumbers = int(input("How many numbers you need?\n"))
userSymbols = int(input("How many symbols you need?\n"))

letterPassword = []
for alphabet in range(0, userLetters):
    randomNumber = random.randint(0, len(letters)-1)
    letterPassword += letters[randomNumber]

for nums in range(0, userNumbers):
    randomNumber = random.randint(0, len(numbers)-1)
    letterPassword += numbers[randomNumber]

for syms in range(0, userSymbols):
    randomNumber = random.randint(0, len(symbols)-1)
    letterPassword += symbols[randomNumber]

random.shuffle(letterPassword)
randomPassword = "".join(letterPassword)
print(f"your password is: {randomPassword}")