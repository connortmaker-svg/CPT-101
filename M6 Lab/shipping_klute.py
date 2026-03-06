# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M6 Lab - if-elif-else Statements
# Shipping Cost Program
# ----------------------------------

# User Inquiry
print("Welcome to the Shipping Cost Calculator\ns")
weight = float(input("Please enter the weight of the package in pounds(lb): "))

# Checking if User inputs are valid
if weight <=0:
    print("Error: Weight Cannot be 0")
elif weight > 20:
    print("20lbs or heavy packages cannot be shipped")
else:
    #Checking shipping type
    shipping_type = input("Enter Shipping Type ('D' for Domestic, 'I' for International): ")

    # Determine the base cost based on weights
    if weight <= 2:
        base_cost = 5.00
    elif weight <= 5:
        base_cost = 8.00
    elif weight <= 10:
        base_cost = 12.00
    else:
        base_cost = 18.00

    # Caculate final cost
    valid_input = True
    final_cost = base_cost
    if shipping_type == "I":
        final_cost = base_cost + 15.00
    elif shipping_type == "D":
        final_cost = base_cost
    else:
        print("invalid Input")
        valid_input = False

    # Give final Summary
    if valid_input:
        print("\nSummary")
        print(f"Package Weight: {weight} lbs")
        print(f"Shipping Type: {shipping_type}")
        print(f"Total Shipping Cost: ${final_cost:.2f}")