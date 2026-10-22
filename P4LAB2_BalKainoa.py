# Kainoa Bal
# October 21 2026
# P4LAB2 - Multiplication Table
# Displays a multiplication table for a non-negative integer also lets the user choose whether to run the program again.


run_again = "yes"
#Repeats the program until the user puts in "yes"
#Program ends when the user puts in anything other than "yes"
while run_again == "yes":
    user_num = int(input("Enter an integer: "))

    if user_num < 0:
        # Display error message for negative values
        print("Negative values are not accepted.")
    else:
        # Display multiplication table for 1-12
        for multiplier in range(1, 13):
            print(f"{user_num} * {multiplier} = {user_num * multiplier}")

    run_again = input("Would you like to run the program again? ")
#Loop has ended, print exit message
print("Exiting program...")
