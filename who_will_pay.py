import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
calculate_name = len(names)-1
random = random.randint(0, calculate_name)

print(f"{names[random]} is going to pay for the meal today!")