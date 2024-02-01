#W04 Prove: Project Milestone - Word Puzzle || Muhereza Owen Kasule|| 01/02/2024
# Welcome message for the game
print("Welcome to the Treasure Hunt Word Puzzle Game\n")

# Secret word the player needs to guess, stored in lowercase for consistency
secret_word = "treasure"
# Initialize the hint display with underscores for each letter in the secret word
hint_display = "_" * len(secret_word)

# Initialize a variable to count the number of guesses made by the player
guess_count = 0

# Function to update the hint based on the player's guess
def update_hint(player_guess, secret):
    updated_hint = ""
    for i in range(len(secret)):
        if player_guess[i] == secret[i]:
            # Letter is correct and in the correct position
            updated_hint += player_guess[i].upper()
        elif player_guess[i] in secret:
            # Letter is correct but in the wrong position
            updated_hint += player_guess[i].lower()
        else:
            # Letter is not in the secret word
            updated_hint += "_"
    return updated_hint

# Main game loop to prompt for guesses
while hint_display.lower() != secret_word:
    print("\nYour hint is:", hint_display)
    player_guess = input("Enter your guess: ").lower()

    # Validate the length of the guess
    if len(player_guess) != len(secret_word):
        print(f"Hint: The secret word has {len(secret_word)} letters. Please guess again.")
        continue  # Skips the rest of the loop and prompts for a new guess

    guess_count += 1  # Increment the guess count with each valid guess attempt

    # Update the hint based on the player's guess
    hint_display = update_hint(player_guess, secret_word)

    # Check if the player has guessed the secret word correctly
    if hint_display.lower() == secret_word:
        print(f"\nCongratulations, You've correctly guessed the secret word '{secret_word}' in {guess_count} guesses!")
        break  # Exits the loop once the correct word is guessed

# If the program exits the loop, it means the player has guessed the word correctly
print(f"\nThank you for playing You found the treasure in {guess_count} guesses.")
