# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M10 Lab - Functions
# Box Math
# ----------------------------------

# This defines a function for calculating volume
def volume(length, height, width):
    return length * height * width

#This defines a function for calculating surface area
def surface_area(length, height, width):
    return 2 * ((length * width) + (length * height) + (width * height)) 

# Check users input for a positive number function
def check_input():
    num = float(input("Please Enter a Positive Number:  "))

    # Loop to make sure the user actually puts in a positive number
    while num <= 0:
        print("NUMBER IS NOT POSITIVE\n")
        num = float(input("Please Enter a Positive Number:  "))
    
    return num

# Main running of program
def main():
    print("Volume and Surface Area Calculator")

    print("Input the Length of the Box")
    leg = check_input()
    print("Input the Length of the Box")
    wid = check_input()
    print("Input the Length of the Box")
    hgt = check_input()

    # Do calucations with functions
    vol = volume(leg, wid, hgt)
    sura = surface_area(leg, wid, hgt)

    # Display results to user
    print(f"\nLength: {leg}")
    print(f"Width: {wid}")
    print(f"Height: {hgt}")
    print(f"Volume: {vol}")
    print(f"Surface Area: {sura}")

main()