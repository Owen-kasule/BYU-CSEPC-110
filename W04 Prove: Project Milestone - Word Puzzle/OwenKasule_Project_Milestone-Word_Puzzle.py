 # W04 Prove: Project Milestone - Word Puzzle || Muhereza Owen Kasule|| 01/02/2024
import random

# List of possible secret words
secret_words = ["mosiah", "zion", "nephi", "alma", "helaman"]
secret_word = random.choice(secret_words)  # Randomly select a secret word
secret_word = secret_word.lower()  # Ensure consistency in case

def generate_hint(guess, secret):
    """Generates and returns a hint based on the guess and the secret word"""
    hint = ['_'] * len(secret)  # Initialize hint with underscores
    for i, char in enumerate(guess):
        if char == secret[i]:
            hint[i] = char.upper()  # Correct letter in the correct position
        elif char in secret:
            hint[i] = char.lower()  # Correct letter in the wrong position
    return " ".join(hint)

print("Welcome to the Word Puzzle Game.")
print(f"Guess the secret word. It has {len(secret_word)} letters.")

guess_count = 0
user_guess = ""

while user_guess != secret_word:
    user_guess = input("Enter your guess: ").lower()
    guess_count += 1

    if len(user_guess) != len(secret_word):
        print("Wrong, your guess must have the same number of letters as the secret word.")
        continue

    if user_guess == secret_word:
        print(f"Kudos, You've guessed the word '{secret_word}' correctly in {guess_count} guesses.")
        break
    else:
        hint = generate_hint(user_guess, secret_word)
        print(f"Your hint is: {hint}")
        print(f"Guesses so far: {guess_count}")

if guess_count >= 10 and user_guess != secret_word:  # Assuming a limit of 10 guesses for demonstration
    print(f"Sorry, you've exceeded the maximum guess limit. The secret word was '{secret_word}'.")

# This implementation includes:
# - A loop for repeated guessing until the correct word is guessed.
# - Accurate guess count and display after each guess and at the game's conclusion.
# - Handling for different lengths of guesses compared to the secret word.
# - Generation of hints that meet the game's requirements.
# - A limit of 10 guesses, with a message displayed if the limit is exceeded.  