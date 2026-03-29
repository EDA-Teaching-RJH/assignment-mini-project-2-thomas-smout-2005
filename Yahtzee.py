import random


# Main function where everything starts and ends
def main():
    # Starting list before any dice are rolled
    kept_dice = [0, 0, 0, 0, 0]
    current_dice = [0, 0, 0, 0, 0]
    # Runs all three dice rolls
    end_dice_result = player_turn(kept_dice, current_dice)


# Function generates one random number from 1 to 6 to simulate a dice
def dice_roll():
    dice = random.randint(1, 6)
    return dice

# Function checks each position in the kept_dice list, to see if  value equal 0. If so, that means that number is a blank and needs to be rolled
def player_roll(kept_dice, current_dice, turn):
    # Checks each position in kept_dice
    for x in range(5):
        # If position is equal to zero, then a dice roll needs to be proformed
        if kept_dice[x] == 0:
            # Dice roll is put into current dice so player can later chose what to keep
            current_dice[x] = dice_roll()
    print(f"Roll {current_dice}")
    # This is command checks if it's the 3rd roll yet. If so, then it doesn't fun this code as theres no need
    if turn < 3:
        # Uses function to allow use to choose what to keep
        kept_dice = choose_keep(current_dice)
        return kept_dice
    return current_dice


# Function asks user what rolls they want to keep
def choose_keep(current_dice):
    # User input of what they want
    keep = input("Keep:").strip()
    # Split the user input so we can read each choice
    final = keep.split()
    # Reset any dice rolls that aren't being kept back to zero, so they can be rolled on the next loop
    kept_dice = [0, 0, 0, 0, 0]
    # For loop to only last the length of the user's input
    for y in range(len(final)):
        # Position in the list starts at 0, not 1, so all positions need to be moved one less
        position = int(final[y]) - 1
        # kept_dice will be taken to next turn, whist current_dice just shows what was rolled this turn
        kept_dice[position] = current_dice[position]
    return kept_dice

    
def player_turn(kept_dice, current_dice):
    # Use this loop to rerun the rolls three times
    for z in range(3):
        # turn equals the current number of player throws
        turn = z + 1
        # Display turn
        print(f"\n--- Turn {turn} ---")
        # Runs player roll funcion and returns up only what numbers the user is keeping
        kept_dice = player_roll(kept_dice, current_dice, turn)
    return kept_dice


# Function to work out score achieved in chosen catagory
def check_score(end_dice_result, catagory_name):
    # List created for any matches
    counts = {}
    # For loop, goes through all numbers a dice can produce
    for j in range(1, 7):
        counts[j] = end_dice_result.count(j)
    # This value will be used for scoring the straights, by sorting them into acending order
    straighten_values = sorted(end_dice_result)
    # Goes through each number and counts how many of that specific there are
    if catagory_name == "Aces":
        # Returns count times number it was counting for score
        return counts[1] * 1
    if catagory_name == "Twos":
        return counts[2] * 2
    if catagory_name == "Threes":
        return counts[3] * 3
    if catagory_name == "Fours":
        return counts[4] * 4
    if catagory_name == "Fives":
        return counts[5] * 5
    if catagory_name == "Sixes":
        return counts[6] * 6
    # Checks if this is the catagory chosen but also checks that the counts list has atleast three matching values
    if catagory_name == "Three of a Kind" and max(counts.values()) >= 3:
        # After check, three of a kind is just the sum of all dice
        return sum(end_dice_result)
    # Same as three of a kind but checks for atleast four of the same value
    if catagory_name == "Four of a Kind" and max(counts.values()) >= 4:
        # Same as three of a kind, sum of all dice
        return sum(end_dice_result)
    # Full house needs to check if the counts like has atleast three matching values and another two matching values ontop
    if catagory_name == "Full House" and sorted(counts.values())[-2:] == [2, 3]:
        return 25
    # short straight is needs to check for only four inclining numbers in a row, to do this it if the combinations of dice can match any of the correct types of short straights through every variation
    if catagory_name == "Short Straight" and any(set(seq).issubset(end_dice_result) for seq in ([1,2,3,4],[2,3,4,5],[3,4,5,6])):
        return 30
    # Long straight is simplier as we can just straighten the dice and check it against the two possible long straights
    if catagory_name == "Long Straight" and straighten_values in ([1,2,3,4,5],[2,3,4,5,6]):
        return 40
    # Yahtzee is just the same as three or four of a kind, but this time we check for five matching dice
    if catagory_name == "YAHTZEE" and max(counts.values()) == 5:
        return 50
    # Chance is just the addition of all dice
    if catagory_name == "Chance":
        # Add all dice and return
        return sum(end_dice_result)
    # If it fails any of the above, the score is zero
    return 0