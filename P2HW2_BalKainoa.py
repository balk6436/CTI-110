#Kainoa Bal
# 9/26/2026
# P2HW2
# A grade calculator that calculates the lowest, highest, total, and average of grades for 6 modules.

# Get grades from 1 to 6
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Post the lowest grade
lowest = min(grade1, grade2, grade3, grade4, grade5, grade6)
# Post the highest grade
highest = max(grade1, grade2, grade3, grade4, grade5, grade6)
# Calculate total
total = sum([grade1, grade2, grade3, grade4, grade5, grade6])
# Calculate average
average = total / 6


print()
print("-------------Results-------------")
# print lowest grade.
print(f"Lowest Grade:       {lowest:.1f}")

# print the highest grade.
print(f"Highest Grade:      {highest:.1f}")

# print the total of all grades.
print(f"Sum of Grades:      {total:.1f}")

# print the average of all grades.
print(f"Average:            {average:.2f}")
print("---------------------------------")