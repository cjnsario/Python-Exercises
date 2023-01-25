print("Welcome to the tip calculator!")
bill = input("Place the total bill: ")
tip_percentage = input("Percentage of Tip: ")
people = input("How many people would split the bill? ")

bill_inter = float(bill)
tip_percentage_int = float(tip_percentage)
people_int = float(people)

percentage = tip_percentage_int / 100
calculation = ((bill_inter * percentage) + bill_inter) / people_int
total_pay = round(calculation, 2)

print(f"Each person should pay Php {total_pay}")