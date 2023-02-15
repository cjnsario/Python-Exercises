import random

words_bank = ["hello", "mister", "regular"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

random_word = random.choice(words_bank)
word_length = len(random_word)
blank_word = []
blank_word_display = ""

for i in random_word:
    blank_word += "_"
for i in random_word:
    blank_word_display += "_ "

print(blank_word_display)

def check():
    b_word = ""
    for i in blank_word:
        b_word += i + " "
    print(b_word)
    
life = 7
end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    for u in range(word_length):
        letter = random_word[u]
        if letter == guess: 
            blank_word[u] = letter     

    if guess not in random_word:
        life -= 1
        print(stages[life])
        if life == 0:
            end_of_game = True

    if "_" not in blank_word:
        end_of_game = True
        print("You Win!")
    
    check()
    
if life == 0:
    print("You Lose!")

        









        

