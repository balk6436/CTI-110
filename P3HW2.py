# P3HW2
# Kainoa Bal
# 10/5/2026
# Salary Calculator

# Input for employee name.
name = input("Enter employee name:")
# print(name)

# Input for hours worked.
hours = float(input("Enter the amount of hours worked:"))
#print(hours)

# Input for employee pay rate.
rate = float(input("Enter employee's pay rate:"))
# print(rate)

# If statement if having overtime
if hours > 40:
    OT_Hours = hours - 40
    OT_Pay = OT_Hours * (rate * 1.5)
    reg_pay = rate * 40
    gross = OT_Pay + reg_pay

else:
    OT_Hours = 0
    OT_Pay = 0
    reg_pay = hours * rate
    gross = reg_pay


# Prints the results in a formatted manner.
print("------------------------------------------------------")
print(f"{'Employee name:':<20}{name}")
print()
print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<25}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("--------------------------------------------------------------------------------------------------------------")
print(f"{hours:<20.1f}{rate:<20.1f}{OT_Hours:<20.1f}{OT_Pay:<25.2f}${reg_pay:<19.2f}${gross:<19.2f}")