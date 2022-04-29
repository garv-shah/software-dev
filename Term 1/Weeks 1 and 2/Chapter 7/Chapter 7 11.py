# Using a for loop, create the list below, which consists of ones separated by increasingly many zeroes. The last two
# ones in the list should be separated by ten zeroes. [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

starting_list = []

for x in range(11):
    starting_list.append(1)
    starting_list += [0]*x

starting_list.append(1)
print(starting_list)
