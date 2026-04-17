# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M11 Lab - File Input/Ouput
# File Write
# ----------------------------------

# Main Logic Loop
try:
    #Initail USer Input
    count = int(input("How many numbers do you want to input?  "))

    # Opening file and doing things with it
    with open("numbers.txt","a") as file:
        for i in range(count):
            number = float(input(f"Input # {i + 1}:  "))
            file.write(f"{number}\n")
    
    # User Comfirmation
    print("\nAll Values were written to the file numbers.txt")

# Error Handling and Exceptions
except FileNotFoundError:
    print("Error: File Not Found")
except ValueError:
    print("Error: Wrong Data Type Entered")
except Exception:
    print("Error: It Broke")