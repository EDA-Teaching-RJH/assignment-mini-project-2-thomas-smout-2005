import random


kept_dice = [0, 0, 0, 0, 0]
current_dice = [0, 0, 0, 0, 0]


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