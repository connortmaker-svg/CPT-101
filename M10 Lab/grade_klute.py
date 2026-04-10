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
    elif score >= 90:
        grade = "A-"
    elif score >= 87:
        grade = "B+"
    elif score >= 83:
        grade = "B"
    elif score >= 80:
        grade = "B-"
    elif score >= 77:
        grade = "C+"
    elif score >= 73:
        grade = "C"
    elif score >= 70:
        grade = "C-"
    elif score >= 67:
        grade = "D+"
    elif score >= 63:
        grade = "D"
    elif score >= 60:
        grade = "D-"
    else:
        grade = "F"
    
    return grade #Single return for grade (make it clean)

def main():
    # Variable to track which numbered student grade it is
    student_num = 1
    for i in range(3):      
        input_score = float(input("PLease Enter your Numeric Grade [0 - 100]"))
        letter = letter_grade(input_score)
        
        # User Output
        print(f"Student #{student_num}; Your Letter grade is {letter}!\n\n")
        student_num = student_num + 1

# Runs the Program
main()