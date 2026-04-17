# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M11 Lab - File Input/Ouput
# File Sume
# ----------------------------------

# Looping Logic
try:
    # The Running Value Total
    running_total = 0

    # Show User the Numbers in the File
    print("Here are the numbers in your file:")
    print("_" * 35 )

    # Open the FIle
    with open("numbers.txt", "r") as file:
        
        # Search line by line and add the values together
        for line in file:
            value = float(line.strip())
            print(value)
            running_total += value
    # Show 
    print(f"\nSum of all numbers: {running_total}")

# Error Handling 
except FileNotFoundError:
    print("Error: File Not Found")
except ValueError:
    print("Error: Non-numeric Values in file")
except Exception:
    print("Error: It broke")