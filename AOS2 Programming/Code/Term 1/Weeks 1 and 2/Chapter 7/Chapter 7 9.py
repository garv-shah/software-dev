# When playing games where you have to roll two dice, it is nice to know the odds of each roll. For instance,
# the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about 17%. You can compute these
# mathematically, but if you don’t know the math, you can write a program to do it. To do this, your program should
# simulate rolling two dice about 10,000 times and compute and print out the percentage of rolls that come out to be
# 2, 3, 4, . . . , 12.

import random

sums = [0] * 13
roll_amount = 1000000
for x in range(roll_amount):
    num = random.randint(1, 6)
    num2 = random.randint(1, 6)
    sums[num + num2] += 1

for x in range(1, 13):
    print(f"The percentage change of {x} after {roll_amount} rolls is: {sums[x]/(roll_amount-sums[x]) * 100}")
