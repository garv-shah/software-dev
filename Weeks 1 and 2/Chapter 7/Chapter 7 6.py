import string

# Create the following lists using a for loop.

# A list consisting of the integers 0 through 49

list_1 = []
for x in range(50):
    list_1.append(x)

print(list_1)

# A list containing the squares of the integers 1 through 50.
list_2 = []
for x in range(50):
    list_2.append((x + 1)**2)

print(list_2)

# The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
list_3 = []
for x in range(26):
    list_3.append(list(string.ascii_lowercase)[x]*(x + 1))

print(list_3)
