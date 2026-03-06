# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M6 Lab - if-elif-else Statements
# Scholarship Eligibility
# ----------------------------------

# User Inquiry
print("Welcome to the Scholarship Eligibility Checker\nAnswer the Following questions")
gpa = float(input("Enter your GPA(4.0 Scale): "))
hours = int(input("Enter your number of completed credit hours: "))
extra = input("Do you participate in extracurricular activities? (Y/N): ")
misconduct = input("Do you have any academic misconduct violations? (Y/N): ")

# Checking if User inputs are valid
if gpa < 0.0 or gpa > 4.0:
    print("Cannot assess eligibility: GPA is out of valid range")
elif hours < 0:
    print("Cannot assess eligibility: Completed Credit Hours is out of valid range")
elif extra != "Y" and extra != "N" and extra != "y" and extra != "n":
    print("Cannot assess eligibility: Invalid Input")
elif misconduct != "Y" and misconduct != "N" and misconduct != "y" and misconduct != "n":
    print("Cannot assess eligibility: Invalid Input")

# if inputs are valid, check for eligibility
else:
    if gpa >= 3.8 and hours >= 30 and misconduct == "N" or gpa >= 3.8 and hours >= 30 and misconduct == "n":
        print("Soclarship Status = Eligible")
    elif gpa >= 3.5 and extra == "Y" and misconduct == "N" or gpa >= 3.5 and extra == "y" and misconduct == "n":
        print("Soclarship Status = Eligible")
    elif gpa >= 3.0 and hours >= 30 and extra =="Y" and misconduct == "N" or gpa >= 3.0 and hours >= 30 and extra =="y" and misconduct == "n" :
        print("Soclarship Status = Eligible")
    else:
        print("Scholarship Status: Ineligible")