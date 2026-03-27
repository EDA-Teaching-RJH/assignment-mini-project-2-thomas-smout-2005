# Mini Project 2 Development Journal

I am try to make a Yahtzee Game, where 5 dice will be rolled across 3 turns, with the goal of getting the highest score possible on a spreadsheet of goals.
The goals are as follows:
    Upper Section:
        Aces - Count and add only Aces
        Twos - Count and add only Twos
        Threes - Count and add only Threes
        Fours - Count and add only Fours
        Fives - Count and add only Fives
        Sixes - Count and add only Sixes
        Bonus - If total score is 63 or over (Score 35)
    Lower Secion:
        3 of a Kind - Add total of all dices if three are the same
        4 of a Kind - Add total of all dices if four are the same
        Full House - 3 of a kind + 2 of a kind e.g.) 2 2 2 3 3 (Score 25)
        Small Straight - Sequence of 4 dice e.g.) 1 2 3 4 (Score 30)
        Long Straight - Sequence of 5 dice e.g.) 2 3 4 5 6 (Score 40)
        YAHTZEE - 5 of a kind (Score 50)
        Chance - Score total of all dice
    GRAND TOTAL:
        Grand Total = Upper Section Total + Lower Section Total


# Development Log:

I thought the best starting place would be to create a function that randomly generates a number from 1 - 6, like a dice does, using the random function.

Next I should add a the abibility generate 5 different numbers in one go and choose which numbers can be kept. I'll use a for loop to loop the dice roll 3 times, and use a list to hold our 5 chosen numbers on each turn, before clearing the list again for the next turn