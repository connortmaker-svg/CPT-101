# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M12 Lab - Lists
# Score Tracker program
# ----------------------------------

# Getting the Scores from the user
def get_score():
    # ask the user for the number of scores, then collects each one
    num_scores = int(input("How many scores do you have?  "))
    # Empty List
    scores = []
    # Main Loop
    for i in range(num_scores):
        score = float(input(f"Input Score {i+1}:   "))
        scores.append(score)
    return scores

def display(scores):
    # Prints all the scores found within the list
    print("\nTHE SCORES")
    for score in scores:
        print(f"{score:.1f}")

def calc_avg(scores):
    return sum(scores) / len(scores)

def main():
    # Get User Data:
    scores = get_score()

    # User Interaction
    print("\nAll Scores have been entered")
    print("Find Additional Information Below")

    # Run the display Function
    display(scores)

    # Run the calcuation for the averages
    avg = calc_avg(scores)
    print(f"The Average of all scores is {avg:.2f}.")

    # Finding the Lowest and Highest Scores
    low_score = min(scores)
    high_score = max(scores)
    print(f"The lowest Score is {low_score:.1f}.")
    print(f"The highest score is {high_score:.1f}")
    
    # Dropping the Lowest score and recalculating
    print("\nLowest score dropped")
    scores.remove(low_score)
    new_avg = calc_avg(scores)
    print(f"The average of the scores is now {new_avg:.2f}")

main()

