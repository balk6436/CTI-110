# Kainoa Bal
# 10/25/2026
# P4HW1
# Collect scores, validate them, drop the lowest score, and calculate them modified list average and letter grade.

# Ask how many scores the user wants to enter.
number_of_scores = int(input("How many scores do you want to enter?"))

# Collect and validate each score.
score_list = []

for score_number in range(1, number_of_scores + 1):
    score = float(input(f"Enter score #{score_number}: "))

    # Keep asking until the score is between 0 and 100. If a negative score is entered, it will display a different message than if a score greater than 100 is entered.
    while score < 0 or score > 100:
        print()
        print("Negative Score entered!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))

    score_list.append(score)

# Finds the lowes score and remove one of them.
lowest_score = min(score_list)
modified_list = score_list.copy()
modified_list.remove(lowest_score)

# Calculate the average of the remaining scores.
average_score = sum(modified_list) / len(modified_list)

# Determine the letter grade from the modified list average.
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results.
print()
print("-------------Results-------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {modified_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("---------------------------------")
