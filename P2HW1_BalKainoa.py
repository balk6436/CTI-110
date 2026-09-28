# Kainoa Bal
# 9/27/2026
# P2HW1
# A travel budget calculator but fancier    

print("Welcome to the travel budget calculator but fancier :)")
print()

# Input for the total budget of the trip
budget = float(input("Enter Budget: "))
print()

# Input for the destination of the trip
destination = input("Enter your travel destination: ")
print()

# Input for fuel expenses
fuel = float(input("How much do you think you will spend on gas? "))
print()

# Input for accommodations
accommodation = float(input("How much will you need for accommodations? "))
print()

# Input for food expenses
food = float(input("How much do you need for food? "))
print()

remaining = budget - fuel - accommodation - food

print("-" * 60)
# Displays travel expenses
print(f"{'Travel Expenses':^60}")

# Displays each expense category and its cost
print(f"{'Location:':<20}{destination:>20}")
print(f"{'Initial Budget:':<20}{f'${budget:.2f}':>20}")
print(f"{'Fuel:':<20}{f'${fuel:.2f}':>20}")
print(f"{'Accommodation:':<20}{f'${accommodation:.2f}':>20}")
print(f"{'Food:':<20}{f'${food:.2f}':>20}")
print("-" * 60)
print()

# Displays the remaining balance
print(f"{'Remaining Balance:':<20}{f'${remaining:.2f}':>20}")