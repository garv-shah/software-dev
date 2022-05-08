# Write a program that generates 100 random integers that are either 0 or 1. Then find the longest run of zeros,
# the largest number of zeros in a row. For instance, the longest run of zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random

run_number = [0]

for x in range(100):
    num = random.randint(0, 1)
    if num == 0:
        run_number[-1] += 1
    else:
        if run_number[-1] != 0:
            run_number.append(0)

print(max(run_number))
