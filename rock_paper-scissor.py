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

player_input = int(input("Rock Paper Scissors: Choose Rock(0) Paper(1) Scissors(2)\n"))

if player_input >= 3 and player_input < 0:
    print(f"{player_input} is not a valid number!!!!")

graphics = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

if player_input == computer_choice:
    print("Draw")
elif player_input == 0 and computer_choice == 1:
    print("You Lose")
elif player_input == 1 and computer_choice == 2:
    print("You Lose")  
elif player_input == 2 and computer_choice == 0:
    print("You Lose")
else:
    print("You Win")
    
print(f"You picked: {graphics[player_input]}")
print(f"Computer Picked: {graphics[computer_choice]}")