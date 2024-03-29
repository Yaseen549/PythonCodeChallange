#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?"))

tip = float(input("How much tip would you like to give? 10, 12, or 15?"))

people = float(input("How many people to split the bill?"))

percentage = tip / 100

tips = total_bill * percentage

total_amount = total_bill + tips

eachoneget = total_amount / people

# final_amount = round(eachoneget, 2)
final_amount = "{:.2f}".format(eachoneget)
print(f"Each person should pay: ${final_amount}")
