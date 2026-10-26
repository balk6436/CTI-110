# Kainoa Bal
# 10/25/2026
# P4HW2 - Salary Calculator for Multiple Employees
# This program calculates regular pay, overtime pay, and gross pay for multiple employees. It also displays totals when the user enters done.

# Totals.
employee_count = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Ask for the first employee name. Enter done to stop.
name = input("Enter employee's name or "done" to terminate: ")

# Continue processing employees until the name is exactly "done".
while name != "done":
    # Input hours worked and pay rate.
    hours = float(input(f"How many hours did {name} work? "))
    rate = float(input(f"What is {name}'s pay rate? "))

    # Calculate regular pay, overtime pay, and gross pay.
    if hours > 40:
        OT_Hours = hours - 40
        OT_Pay = OT_Hours * (rate * 1.5)
        reg_pay = rate * 40
    else:
        OT_Hours = 0
        OT_Pay = 0
        reg_pay = hours * rate

    gross = OT_Pay + reg_pay

    # Display this employee's salary information.
    print()
    print(f"{'Employee name:':<20}{name}")
    print()
    print(f"{'Hours Worked':<16}{'Pay Rate':<16}{'OverTime':<16}{'OverTime Pay':<24}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print("--------------------------------------------------------------------------------------------------------------")
    print(f"{hours:<16.1f}{rate:<16.2f}{OT_Hours:<16.1f}{OT_Pay:<24.2f}${reg_pay:<19.2f}${gross:<19.2f}")
    print()

    # Update totals for all employees.
    employee_count += 1
    total_overtime_pay += OT_Pay
    total_regular_pay += reg_pay
    total_gross_pay += gross

    # Ask for the next employee name.
    name = input('Enter employee\'s name or "done" to terminate: ')

# Display total after the user enters done.
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
