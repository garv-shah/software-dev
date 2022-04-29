# Write a program that asks the user for an integer and creates a list that consists of the factors of that integer.

import math

num = int(input("Please enter an integer: "))
factors = []
for i in range(1, round(math.sqrt(num)) + 1):
    if num % i == 0:
        factors.append(i)
        factors.append(num//i)
factors.sort()
print("The factors of", num, "are:", factors)
