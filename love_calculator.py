print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1.lower() + name2.lower()
t_true = int(combine_name.count('t'))
r_true = int(combine_name.count('r'))
u_true = int(combine_name.count('u'))
e_true = int(combine_name.count('e'))
true_final = str(t_true + r_true + u_true + e_true)
l_love = int(combine_name.count('l'))
o_love = int(combine_name.count('o'))
v_love = int(combine_name.count('v'))
e_love = int(combine_name.count('e'))
love_final = str(l_love + o_love + v_love + e_love)

calculation = int(true_final + love_final)

if calculation < 10 or calculation > 90:
    print(f"Your score is {calculation}, you go together like coke and mentos.")
elif calculation >= 40 and calculation <= 50:
    print(f"Your score is {calculation}, you are alright together.")
else:
    print(f"Your score is {calculation}.")