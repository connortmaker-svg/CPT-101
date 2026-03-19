# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M8 Lab - Loop Basics
# Countdown Timer
# ----------------------------------

# Get User input to start the Countdown Timer
print("Countdown Timer")
start_num = int(input("What Number should the Countdown start at?  "))

# Start the Count Down and Reiterate the loop until zero
for current_num in range(start_num, -1, -1):
    elapsed_sec = start_num - current_num
    print(f"Countdown: {current_num} ({elapsed_sec} seconds have passed)")

print("explode")