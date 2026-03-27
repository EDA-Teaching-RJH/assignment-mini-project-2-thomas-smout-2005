import re
import random



def dice_roll():
    otter = random.randint(1, 6)
    print(otter)



def player_turn():
    a_check = False
    b_check = False
    c_check = False
    d_check = False
    e_check = False
    for i in range(3):
        holding_dice = []
        if a_check == False:
            a = dice_roll()
        if b_check == False:
            b = dice_roll()
        if c_check == False:
            c = dice_roll()
        if d_check == False:
            d = dice_roll()
        if e_check == False:
            e = dice_roll()
        print("{:<10} {:<10} {:<10} {:<10}".format("a", "b", "c", "d", "e"))
        print("{:<10} {:<10} {:<10} {:<10}".format(a, b, c, d, e))
        user_decision = input("Which numbers would you like to hold onto? (Example: a c d)")
        # if user_decision == g

