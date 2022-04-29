# The following is useful in implementing computer players in a number of different games. Write a program that
# creates a 5 × 5 list consisting of zeroes and ones. Your program should then pick a random location in the list
# that contains a zero and change it to a one. If all the entries are one, the program should say so. [Hint: one way
# to do this is to create a new list whose items are the coordinates of all the ones in the list and use the choice
# method to randomly select one. Use a two-element list to represent a set of coordinates.]


import random
from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


board = [[random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)] for i in range(5)]
list_of_zeros = []

for y in board:
    for x in y:
        if x == 0:
            list_of_zeros.append([board.index(y), y.index(x)])
print(board)

random_index = random.choice(list_of_zeros)
board[random_index[0]][random_index[1]] = 1

print(f"All items are 1: {all_equal(board)}")
