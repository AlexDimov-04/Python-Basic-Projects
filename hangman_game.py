# import module
import random

# the hangman drawing
hangman = [
    """
    +---+
        |
        |
        |
        ===""", """
+---+
  | |
  O |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    ===""", """
+---+
  | |
  O |
 /|\|
    ===""", """
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / 
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / \
"""
]

# list of word to pick from
words = ['car', 'keyboard', 'tree', 'telephone', 'mouse', 'lamp', 'water', 'building', 'lion', 'flower', 'camera']

# random word
word = random.choice(words)

# lists of guessed letters
correctly_guessed = []
incorrectly_guessed = []

# attempts count
attempts = 6
# hangman drawing to pick from the hangman list drawings
hangman_count = -1

# additional hangman data
while attempts > 0:
    output = ''
    for letter in word:
        if letter in correctly_guessed:
            output += letter
        else:
            output += '_ '
    if output == word:
        break
    print(f"Current word: {output}")
    print(f"{attempts} attempts left\n")

    guess = input("Guess a letter: ")
    if guess in correctly_guessed or guess in incorrectly_guessed:
        print(f"You have already guessed that {guess}")
    elif guess in word:
        print(f"Well done! You guessed correctly!")
        correctly_guessed.append(guess)
    else:
        print(f"Sorry, you have guessed a wrong letter!")
        hangman_count += 1
        attempts -= 1
        incorrectly_guessed.append(guess)
        print(hangman[hangman_count])

# check for the attempts
if attempts > 0:
    print(f"Congratulations! You guessed the word {word} correctly!")
else:
    print("Sorry you ran out of attempts! Try again!")
