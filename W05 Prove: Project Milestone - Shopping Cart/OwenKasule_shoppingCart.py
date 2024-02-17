#W05 Prove: Project Milestone - Shopping Cart || Muhereza Owen Kasule|| 1/02/202
def main():
    # Welcome message and menu
    print("Welcome to the Super Shopping Cart2")
    display_menu()

    # Main loop
    cart = {"items": [], "prices": []}  # Dictionary to store items and prices
    while True:
        choice = get_user_choice()
        handle_choice(choice, cart)

def display_menu():
    print("\nPlease choose an action:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def get_user_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def handle_choice(choice, cart):
    if choice == 1:
        add_item(cart)
    elif choice == 2:
        view_cart(cart)
    elif choice == 3:
        remove_item(cart)
    elif choice == 4:
        compute_total(cart)
    elif choice == 5:
        print("Thank you. Goodbye")
        exit()

def add_item(cart):
    item_name = input("Enter item name: ")
    price = float(input("Enter price (e.g., 12.99): "))
    cart["items"].append(item_name)
    cart["prices"].append(price)
    print(f"'{item_name}' added to cart for ${price:.2f}.")

def view_cart(cart):
    if not cart["items"]:
        print("There are no items in the cart.")
    else:
        print("\nYour shopping cart:")
        for i, item in enumerate(cart["items"], 1):
            price = cart["prices"][i - 1]  # Subtract 1 from i
            print(f"{i}. {item} - ${price:.2f}")

def remove_item(cart):
    if not cart["items"]:
        print("The cart is empty.")
        return
    while True:
        try:
            item_num = int(input("Enter item number to remove: "))
            if 1 <= item_num <= len(cart["items"]):
                item_name = cart["items"].pop(item_num - 1)
                price = cart["prices"].pop(item_num - 1)
                print(f"Removed '{item_name}' for ${price:.2f}.")
                break
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def compute_total(cart):
    if not cart["items"]:
        print("The cart is empty.")
        return
    total = sum(cart["prices"])
    print(f"The total price of your shopping cart is ${total:.2f}.")

if __name__ == "__main__":
    main()
