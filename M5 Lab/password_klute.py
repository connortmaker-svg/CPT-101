# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M5 Lab - Python Input/Output
# Username and Password Validation
# ----------------------------------

# Constants
USERNAME = "Connor"
PASSWORD = "Robot"

# Logic for Password Checking
print("SYSTEM LOGIN")

input_user = input("Enter your username: ")

if input_user == USERNAME:
    input_pass = input("Enter your password: ")
    if input_pass == PASSWORD:
        print("Congrats you have access now! \n\n Goodbye")
    else:
        print("INCORRECT")
else:
    print("STAY AWAY NO ACCESS")