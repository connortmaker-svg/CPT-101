# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M10 Lab - Functions
# Letter Grade
# ----------------------------------

# Function that Determines the Grade that assigns letter grades based on numeric score

def letter_grade(score):
    grade = "" #Empty String

    #If else block logic
    if score >= 93:
        grade = "A"
    if score >= 90:
        grade = "A-"
    if score >= 87:
        grade = "B+"
    if score >= 83:
        grade = "B"
    if score >= 80:
        grade = "B-"
    if score >= 77:
        grade = "C+"
    if score >= 73:
        grade = "C"
    if score >= 70:
        grade = "C-"
    if score >= 67:
        grade = "D+"
    if score >= 63:
        grade = "D"
    if score >= 60:
        grade = "D-"
    else:
        grade = "F"
    
    return grade #Single return for grade (make it clean)

def main():
    for i in range(3):
        input_score = float(input("PLease Enter your Numeric Grade [0 - 100]"))
        letter = letter_grade(input_score)

        # User Output
        print(f"Your Letter grade is {letter}!\n\n")

# Runs the Program
main()