# Here is an old puzzle question you can solve with a computer program. There is only one five-digit number n that is
# such that every one of the following ten numbers shares exactly one digit in common in the same position as n. Find
# n.

import itertools

num_list = ["01265", "12171", "23257", "34548", "45970", "56236", "67324", "78084", "89872", "99414"]

for x in list(itertools.product("0123456789", repeat=5)):
    counter = 0
    for y in num_list:
        if sum(x == y for x, y in zip(x, list(y))) == 1:
            counter += 1
    if counter == 10:
        print(''.join(x))

