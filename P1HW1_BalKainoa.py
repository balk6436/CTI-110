# Kainoa Bal
# 9/12/2026
# P1HW1
# Calculating exponets and addition and subtraction.

# calculate exponent

print("----------Exponets----------")
print()

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent number: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is:", result)
print()

# calculate addition and subtraction
print("----------Addition and Subtraction----------")
print()

num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the second number to add: "))
num3 = int(input("Enter the third number to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result)