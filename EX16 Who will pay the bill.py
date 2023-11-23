import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

payer = int(random.randint(0, len(names)))

bill = names[payer]

print(f"{bill} is going to buy the meal today!")
