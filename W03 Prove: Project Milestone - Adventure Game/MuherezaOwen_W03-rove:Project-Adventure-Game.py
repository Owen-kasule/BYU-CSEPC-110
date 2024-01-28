# W03 Prove:Program: Adventure Game| Owen Muhereza| 28/01/2024

def get_user_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).upper()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

# First Level
print("You've arrived at a mysterious island.")
first_choice = get_user_choice("Do you go LEFT, RIGHT, or STRAIGHT into the jungle? ", ["LEFT", "RIGHT", "STRAIGHT"])

# Second Level
if first_choice == "LEFT":
    print("\nYou encounter an ancient temple.")
    second_choice = get_user_choice("Do you ENTER the temple or SEARCH around it? ", ["ENTER", "SEARCH"])

    # Third Level for Left Choice
    if second_choice == "ENTER":
        print("\nInside, you find a hidden treasure!")
    else:  # SEARCH
        print("\nYou find a secret passage behind the temple.")

elif first_choice == "RIGHT":
    print("\nYou find a hidden beach with a stranded ship.")
    second_choice = get_user_choice("Do you EXPLORE the ship or LOOK for survivors? ", ["EXPLORE", "LOOK"])

    # Third Level for Right Choice
    if second_choice == "EXPLORE":
        print("\nYou discover a map inside the ship.")
    else:  # LOOK
        print("\nYou help survivors and learn about the island's history.")

else:  # STRAIGHT
    print("\nYou come across a talking parrot.")
    second_choice = get_user_choice("Do you FOLLOW the parrot, ASK it questions, or IGNORE it? ", ["FOLLOW", "ASK", "IGNORE"])

    # Third Level for Straight Choice
    if second_choice == "FOLLOW":
        print("\nThe parrot leads you to a hidden cave.")
    elif second_choice == "ASK":
        print("\nThe parrot reveals a clue about the island.")
    else:  # IGNORE
        print("\nYou continue your journey deeper into the jungle.")

# End of Game
print("\nYour adventure on the mysterious island concludes. Thanks for playing")



