# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 3
# Unit Conversions via a TUI
# ----------------------------------

# Main Starting loop to get and verify the option of the user
def menu_option():
    choice = 0
    is_valid = False
    while is_valid == False:
        try:
            choice = int(input("Choose an Option (1-8):  "))
            if 1<= choice <= 8:
                is_valid = True
            else:
                print("ENTER A VALID NUMBER")
        except ValueError:
            print("INVALID INPUT")
    return choice

# Checks if the temperature that the user inputed is a valid input
def good_temp():
    temp = 0.0
    is_valid = False
    while is_valid == False:
        try:
            temp = float(input("Enter the temperature in Fahrenheit"))
            is_valid = True
        except ValueError:
            print("INVALID INPUT")
    return temp

# Checks if the users input is a valid positive number
def positive_value():
    val = 0.0
    is_valid = False
    while is_valid == False:
        try:
            val = float(input("Enter the value to be converted:  "))
            if val > 0:
                is_valid = True
            else:
                print("ENTER A VALUE GREATER THAN 0")
        except ValueError:
            print("INVALID INPUT")
    return val
    
# All Math Functions
def to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def to_centimeters(inches):
    return inches * 2.54

def to_meters(feet):
    return feet / 3.281

def to_kilometers(miles):
    return miles * 1.60934

def to_grams(ounces):
    return ounces * 28.3495

def to_kilograms(pounds):
    return pounds / 2.205

def to_liters(quarts):
    return quarts / 1.057

def convert_temp():
    f = good_temp()
    c = to_celsius(f)
    print(f"\nResult: {f} Fahrenheit is {c:.2f} Celsius")

def convert_inches():
    inches = positive_value()
    cm = to_centimeters(inches)
    print(f"\nResult: {inches} Inches is {cm:.2f} Centimeters")

def convert_feet():
    feet = positive_value()
    m = to_meters(feet)
    print(f"\nResult: {feet} Feet is {m:.2f} Meters")

def convert_miles():
    miles = positive_value()
    km = to_kilometers(miles)
    print(f"\nResult: {miles} Miles is {km:.2f} Kilometers")

def convert_ounces():
    oz = positive_value()
    g = to_grams(oz)
    print(f"\nResult: {oz} Ounces is {g:.2f} Grams")

def convert_pounds():
    lbs = positive_value()
    kg = to_kilograms(lbs)
    print(f"\nResult: {lbs} Pounds is {kg:.2f} Kilograms")

def convert_quarts():
    qts = positive_value()
    liters = to_liters(qts)
    print(f"\nResult: {qts} Quarts is {liters:.2f} Liters")

# Main Starting loop for the program
def main():
    user_input = 0

    while user_input != 8:
        print("\n" + "="*35)
        print("UNIT CONVERTER")
        print("="*35)
        print(" 1. Fahrenheit to Celsius")
        print(" 2. Inches to Centimeters")
        print(" 3. Feet to Meters")
        print(" 4. Miles to Kilometers")
        print(" 5. Ounces to Grams")
        print(" 6. Pounds to Kilograms")
        print(" 7. Quarts to Liters")
        print(" 8. Exit Program")
        print("="*35)
        # Pass the users input to the option checker
        user_input = menu_option()

        # Logic Checker for the menu options 
        if user_input == 1:
            convert_temp()
        elif user_input == 2:
            convert_inches()
        elif user_input == 3:
            convert_feet()
        elif user_input == 4:
            convert_miles()
        elif user_input == 5:
            convert_ounces()
        elif user_input == 6:
            convert_pounds()
        elif user_input == 7:
            convert_quarts()
        elif user_input == 8:
            print("GODDBYE")

main()