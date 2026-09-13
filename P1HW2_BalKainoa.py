# Kainoa Bal
# 9/12/2026
# P1HW2
# A travel budget calculator

print("Welcome to the travel budget calculator.")
print()

budget = float(input("Enter your total budget for the trip: $"))

# Input for the destination of the trip
destination = input("Enter the destination of your trip: ")
print("Destination:", destination)

# How much will you spend on gas for the trip?
gas_cost = float(input("How much will you spend on gas for the trip? $"))

# Input for accommodations for the trip
accommodation_cost = float(input("How much will you spend on accommodations for the trip? $"))

# Input for food expenses for the trip
how_much_food = float(input("How much will you spend on food for the trip? $"))

# Summary of expenses and the remaining balance
print("--------Travel Expenses--------")
print("Location:", destination)
expenses = gas_cost + accommodation_cost + how_much_food

print("Initial budget: $", budget)
print()

# Summary of expenses
print(gas_cost, "Fuel")
print(accommodation_cost, "Accommodations")
print(how_much_food, "Food")
print() 

# Calculate the remaining balance after expenses
subtraction = budget - expenses
print("Remaining balance: $", subtraction)