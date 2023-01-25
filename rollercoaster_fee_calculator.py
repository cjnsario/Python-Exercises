print("Welcome to height checker")
height = int(input("Please enter your height in cm: "))
recommended_height = 120
bill = 0

if height > recommended_height:
  print("Congratulations! You passed!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 800
    print("You will pay Php 800")
  elif age <= 18:
    bill = 900
    print("You will pay Php 900")
  elif age >= 45 and age <= 55:
   print("You're free!")
  else:
    bill = 1000
    print("You will pay Php 1000")

  question = input("But, do you want to have a picture? (Yes or No) ")
  if question == "Yes":
    bill += 100
    print(f"You need to pay a total of {bill}.")
 
else:
  print("Please get taller!")