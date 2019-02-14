"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""

TEAM_NAME = 'vice' # Change this line!

def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    first_digit = score // 10
    second_digit = score % 10
    points = abs(first_digit - second_digit) + 2
    return points
    # END PROBLEM 2

def is_swap(score0, score1):
    """Return whether one of the scores is an integer multiple of the other."""
    # BEGIN PROBLEM 4
    if (score0 <= 1) or (score1 <= 1):
        return False
    elif ((score0 % score1) == 0):
        return True
    elif ((score1 % score0) == 0):
        return True
    return False
    # END PROBLEM 4

def swap_strategy(score, opponent_score, margin=9, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 11

    could_be_player_score = score + free_bacon(opponent_score)
    could_be_free = free_bacon(opponent_score)

    #can swap? will benefit?
    if (is_swap(could_be_player_score, opponent_score) == True):
        if(opponent_score > could_be_player_score):
            return 0

    #if give at least margin points + result would not cause a swap
    if (free_bacon(opponent_score) >= margin):
        if(is_swap(could_be_player_score, opponent_score) == False):
            return 0

    return num_rolls  # Replace this statement
    # END PROBLEM 11

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    Let's roll tons of dice.
    """
    # BEGIN PROBLEM 12
    num_rolls = swap_strategy(score, opponent_score, 10, 10)
    safe_num = 1

    if (opponent_score <= 20) or (score <= 20):
        num_rolls = swap_strategy(score, opponent_score, 10, 10)
    if (abs(opponent_score - score) >= 30) and (score > 20):
        #num_rolls = swap_strategy(score, opponent_score, 30, 8)
        num_rolls = swap_strategy(score, opponent_score, 30, 8)
    if (abs(opponent_score - score) >= 30) or (opponent_score >= 29):
        num_rolls = 10

    if (score == 0):  # first player, extra turn
        return 0
    if (score == 0) and (opponent_score > 0): # second player, extra turn
        if (opponent_score >= 31):
            return 1
        return 8

    if (score <= 21):
        num_rolls = 10
    if (score == 1):
        return 1
    if (score >= 70 - safe_num):
        num_rolls = 9 #avg sum is 31/32
    if (score >= 73 - safe_num):
        num_rolls = 8 #avg sum is 28
    if (score >= 76 - safe_num) :
        num_rolls = 7 #average sum is 24
    if (score >= 79 - safe_num) or (abs(opponent_score-score) <= 15):
        num_rolls = 6 #average sum is 21
    if (score >= 83 - safe_num):
        num_rolls = 5 #average sum is 17/18
    if (score >= 86 - safe_num):
        num_rolls = 4 #average sum is 14
    if (score >= 90 - safe_num):
        num_rolls = 3 #average sum is 10/11
    if (score >= 93 - safe_num):
        num_rolls = 2 #average sum is 7
    if (score >= 97 - safe_num):
        num_rolls = 1 #average sum is 3
    if (free_bacon(opponent_score) >= (100 - score)):
        return 0
    return num_rolls  # Replace this statement
    # END PROBLEM 12
