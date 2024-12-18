import random
import os

HANGMAN = ['''
  +---+
  |   |
  |
  |
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |   |
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |  /|
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |  /|\
  |
  |
=========''', '''
  +---+
  |   |
  |   O
  |  /|\
  |  /
  |
=========''', '''
  +---+
  |   |
  |   O
  |  /|\
  |  / \
  |
=========''']

def random_line():
    db = open("hangman_words.txt")
    line = next(db)
    for num, aline in enumerate(db, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

line = random_line().split(',')
word = line[random.randint(0, len(line)-1)].strip()

blank_list = ['_' for _ in word]

guessed_letters = []

display = 0

def guessing():
  global display
  correct_guess = False
  for index, letter in enumerate(word):
    if guess.lower() == letter:
      blank_list[index] = guess.lower()
      correct_guess = True

  if not correct_guess:
    print(f"\nThere is no {guess}, sorry.\t")
    if guess not in guessed_letters:
      guessed_letters.append(guess)
    display += 1

print("\nWelcome to Hangman!\n")
print(HANGMAN[display])
guess = input(f"\n{(' '.join(blank_list))}\n\nMake a guess?\t")

guessing()

print(HANGMAN[display]+'\n')
print(' '.join(blank_list))
print(f"\nGuessed letters: {' '.join(guessed_letters)}")


while display < 6:
    if (''.join(blank_list)) == word:
        print("\nYOU WIN!")
        break
    guess = input(f"\nMake another guess?\t")

    if guess in (blank_list or guessed_letters):
        print(f"\nYou already guessed {guess}.")
        continue

    if len(guess) > 1:
        print("\nPlease enter only one letter at a time.")
        continue

    guessing()
    print(HANGMAN[display]+'\n')
    print(' '.join(blank_list))

    print(f"\nGuessed letters: {' '.join(guessed_letters)}")

if display == 6:
    print("\nYOU LOST!")
    print(f"\nThe word was {''.join(word)}!\n")