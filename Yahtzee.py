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


