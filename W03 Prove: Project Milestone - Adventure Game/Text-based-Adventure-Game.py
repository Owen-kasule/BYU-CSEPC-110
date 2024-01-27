# Text-based Adventure Game || Muhereza Owen Kasule || 

print("You find yourself at the edge of an enchanted forest.")
print("Do you go LEFT or RIGHT?")

choice1 = input().strip().lower()

if choice1 == "left":
    print("\nYou walk left and encounter a talking tree.")
    print("The tree asks you to choose a GIFT: a MAGIC SWORD or a HEALING POTION.")

    choice2 = input().strip().lower()
    
    if choice2 == "magic sword":
        print("\nThe tree gives you a glowing sword, and you feel empowered.")
    elif choice2 == "healing potion":
        print("\nThe tree hands you a potion that heals your wounds.")
    else:
        print("\nConfused, you receive nothing from the tree.")
        
elif choice1 == "right":
    print("\nYou turn right and find a treasure chest.")
    print("Do you OPEN it or LEAVE it be?")

    choice2 = input().strip().lower()

    if choice2 == "open":
        print("\nThe chest is filled with gold and jewels")
    elif choice2 == "leave":
        print("\nYou decide not to risk it and walk away.")
    else:
        print("\nYou hesitate and the chest disappears in a puff of smoke.")

else:
    print("\nConfused, you stand still. A fairy appears and urges you to choose a path.")
