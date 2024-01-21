# Function to round a value to two decimal places
def round_to_two(value):
    return round(value, 2)

# Input Phase - Meal Prices
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))

# Input Phase - Quantities of People
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

# Calculation Phase - Subtotal Amount
subtotal = round_to_two(child_meal_price * number_of_children + adult_meal_price * number_of_adults)
print(f"\nSubtotal: ${subtotal}")

# Additional functionalities (like sales tax, total calculation, etc.) can be included as per final requirements.
# Function to round a value to two decimal places
def round_to_two(value):
    return round(value, 2)

# Input
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

# Calculation
subtotal = round_to_two(child_meal_price * number_of_children + adult_meal_price * number_of_adults)
print(f"\nSubtotal: ${subtotal}")

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = round_to_two(subtotal * sales_tax_rate / 100)
total = round_to_two(subtotal + sales_tax)
print(f"Sales Tax: ${sales_tax}\nTotal: ${total}")

# Payment 
payment_amount = float(input("\nWhat is the payment amount? "))
change = round_to_two(payment_amount - total)
print(f"Change: ${change}")

# End 
