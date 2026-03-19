# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 1 - M1 - M6
# Area Calculator
# ----------------------------------

print("Rectangle Area/Perimeter Calculator\n")

# Ask user for height -> then ask for width [error any invalid inputs]
height = float(input("Input the height of the rectangle:  "))

if height < 0:
    print("\nDistance values cannot be negative. Please restart the Calculator.")
else:
    width = float(input("Input the width of the rectangle:  "))

    if width < 0:
        print("\nDistance value are not negative. Please restart the Calculator.")
    else:
        # Perform Area Calculations Needed
        area = height * width
        perimeter = (height * 2) +(2 * width)

        # User Outputs
        print("\nRESULTS\n")
        print(f"Height Entered: {height:.2f}")
        print(f"Width Entered: {width:.2f}")
        print(f"Area Calculated: {area:.2f}")
        print(f"Perimeter Calculated: {perimeter:.2f}")

    