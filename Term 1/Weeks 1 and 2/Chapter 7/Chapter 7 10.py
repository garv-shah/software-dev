# Write a program that rotates the elements of a list so that the element at the first index moves to the second
# index, the element in the second index moves to the third index, etc., and the element in the last index moves to
# the first index.

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def rotate_list(inlist, n):
    return_list = []
    for x in range(len(inlist)):
        return_list.append(inlist[(x - n) % len(inlist)])

    return return_list


print(rotate_list(input_list, 1))
