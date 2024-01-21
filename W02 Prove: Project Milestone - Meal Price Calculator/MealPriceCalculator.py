
# Meal Price Calculator with Tip Feature.
# Creative Feature: Option to add rcentage to the total bill.

def round_to_two(value):
    return round(value, 2)

# Input Phase
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

# Subtotal Calculation
subtotal = round_to_two(child_meal_price * number_of_children + adult_meal_price * number_of_adults)
print(f"Subtotal: ${subtotal:.2f}")

# Sales Tax Calculation
sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = round_to_two(subtotal * sales_tax_rate / 100)
total = round_to_two(subtotal + sales_tax)
print(f"Sales Tax: ${sales_tax:.2f}\nTotal: ${total:.2f}")

# Optional Tip Calculation
tip_percentage = 10  # 10% tip
tip_amount = round_to_two(total * tip_percentage / 100)
total_with_tip = round_to_two(total + tip_amount)
print(f"Tip (10%): ${tip_amount:.2f}\nTotal with Tip: ${total_with_tip:.2f}")

# Payment and Change Calculation
payment_amount = float(input("What is the payment amount? "))
change = round_to_two(payment_amount - total_with_tip)
print(f"Change: ${change:.2f}")

# End of the program

