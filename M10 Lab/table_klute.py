# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M10 Lab - Functions
# Multiplication Table
# ----------------------------------

# Function for Getting user input
def get_input():
    num = int(input("Please enter a number between 1 and 20:  "))

    # Error Checking loop
    while num < 1 or num > 20:
        num = int(input("Please enter a valid number between 1 and 20:  "))

    return num

# Function for creating table
def print_table(rows, columns):
    for r in range(1, rows + 1):
        for c in range(1, columns + 1):
            pdt = r * c
            print(f"{pdt:5}", end="") 

        print()

# Main Running Function
def main():
    print("Customized Multiplication Table Creator\n")
    print("Input the Number of Rows")
    num_rows = get_input()
    print("\nInput the Number of Columns")
    num_cols = get_input()
    
    print("\nYour Mutiplication Table")
    print_table(num_rows, num_cols)

main()