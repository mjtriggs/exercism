"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter

# We define each of the possible scoring hands as functions. Each function will
# return the score of a particular set of dice (if applicable).

# Define Singles
# These all have a very similar format, so no individual docstrings are needed.
def ONES(dice):
    return dice.count(1)

def TWOS(dice):
    return 2 * dice.count(2)

def THREES(dice):
    return 3 * dice.count(3)

def FOURS(dice):
    return 4 * dice.count(4)

def FIVES(dice):
    return 5 * dice.count(5)

def SIXES(dice):
    return 6 * dice.count(6)

# Full House
def FULL_HOUSE(dice):
    # Full House is defined as three of one number and two of another.
    # Check that the Counter works both ways
    if list(Counter(dice).values()) == [2,3]:
        return sum(dice)
    elif list(Counter(dice).values()) == [3,2]:
        return sum(dice)
    else:
        return 0

# Define CHOICE option
def CHOICE(dice):
    return sum(dice)

# Define Yacht
def YACHT(dice):
    # Use set logic to check that they're all the same number.
    if len(set(dice)) == 1:
        return 50
    else:
        return 0

# Four of a Kind
def FOUR_OF_A_KIND(dice):
    count = list(Counter(dice).values())
    if max(count) >= 4:
        return Counter(dice).most_common()[0][0] * 4
    else:
        return 0

# Little and Big Straights use set logic to check if the values are correct
def LITTLE_STRAIGHT(dice):
    if set(dice) == set([1,2,3,4,5]):
        return 30
    else:
        return 0

def BIG_STRAIGHT(dice):
    if set(dice) == set([6,2,3,4,5]):
        return 30
    else:
        return 0

# Finally, the scoring function calls on one of the other defined functions as
# an input to score the dice.
def score(dice, category):
    return category(dice)
