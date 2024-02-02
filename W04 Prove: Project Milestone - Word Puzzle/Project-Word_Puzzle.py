# Program: Word Puzzle || Owen Muhereza || 01/02/2024
# This program selects a secret word randomly from a list and provides enhanced hints according to the user's guesses. It includes guess length verification and displays hints following specific rules for underscores, lowercase, and uppercase letters.

import random

# Welcome message and creative element description
print("\nWelcome to the advanced word guessing game")
print("Guess the secret word. After each guess, you'll receive hints to guide you")

# List of secret words for variability
secret_words = ["mosiah", "enigma", "puzzle", "cipher", "decode"]
secret_word = random.choice(secret_words).lower()  # Randomly select and lowercase the secret word

# Initialize variables for hints and guess count
hint = ['_'] * len(secret_word)
guess_count = 0
incorrect_length_guess_count = 0  # Track guesses of incorrect length

# Display the initial hint
print("Your initial hint is: " + ' '.join(hint))

# Function to update hint based on user's guess
def update_hint(guess, secret_word, hint):
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            hint[i] = letter.upper()  # Correct letter at correct position
        elif letter in secret_word:
            hint[i] = letter.lower()  # Correct letter at wrong position
    return hint

# Main game loop
while ''.join(hint).lower() != secret_word:
    guess = input("\nWhat is your guess? ").lower()
    
    if len(guess) != len(secret_word):
        print(f"Hint is not displayed as the guess length ({len(guess)}) does not match the secret word length ({len(secret_word)}).")
        incorrect_length_guess_count += 1
        continue
    
    guess_count += 1
    hint = update_hint(guess, secret_word, list(hint))
    
    # Display updated hint
    print("Your hint is: " + ' '.join(hint))
    
    # Check if the user has correctly guessed the secret word
    if ''.join(hint).lower() == secret_word:
        print(f"\nCongratulations, You guessed the secret word '{secret_word}' correctly")
        print(f"It took you {guess_count} guesses, with {incorrect_length_guess_count} incorrect length guesses.")
        break

# End, thanks for playing.

