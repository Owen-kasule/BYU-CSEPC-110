# Program: Word Puzzle || Owen Muhereza || 01/02/2024
# This adds an extra layer of challenge and customization for the player.

import random

print("\nWelcome to the word guessing game")
print("A secret word has been chosen, and you must guess it letter by letter.")
print("Hints will be provided based on your guesses.")

# List of secret words for variability
secret_words = ["mosiah", "enigma", "puzzle", "cipher", "decode"]
# Randomly select a secret word
secret_word = random.choice(secret_words).lower()
hint = ['_'] * len(secret_word)  # Initial hint setup

guess_count = 0  # To track the number of guesses
correct_guess = False

def generate_hint(guess, secret_word):
    '''Generates and returns a hint based on the guess and the secret word.'''
    new_hint = ""
    for i, char in enumerate(guess):
        if char == secret_word[i]:
            new_hint += char.upper()  # Correct letter, correct position
        elif char in secret_word:
            new_hint += char.lower()  # Correct letter, wrong position
        else:
            new_hint += "_"  # Letter not in word
    return new_hint

# Displaying the initial hint
print("Your hint is:", " ".join(hint))

while not correct_guess:
    guess = input("\nPlease enter your guess: ").lower()
    
    # Verify guess length
    if len(guess) != len(secret_word):
        print("The guess must be the same length as the secret word.")
        continue
    
    guess_count += 1  # Counting all guesses, including incorrect lengths
    hint = generate_hint(guess, secret_word)
    
    # Check if the guess is correct
    if guess == secret_word:
        correct_guess = True
        print("\nCongratulations! You've guessed the word correctly")
    else:
        # Provide updated hint
        print("Your hint is:", " ".join(hint))
    
print(f"It took you {guess_count} guesses.")

# Here, additional creativity could involve:
# - Adding difficulty levels that affect the number of allowed guesses or provide partial hints.
# - Incorporating a feature where the user can request an additional hint at the cost of extra guesses.
# - Using a broader list of words or importing a word list from an external source for greater variability.
