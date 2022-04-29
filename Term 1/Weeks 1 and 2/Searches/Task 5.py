# Selection Sort
array_list = [12, 31, 8, 1]

list_len = len(array_list)
print(array_list)

for counter in range(list_len):
    smallest = counter
    for i in range(counter + 1, list_len):
        if array_list[i] < array_list[smallest]:
            smallest = i
    if smallest != counter:
        array_list[counter], array_list[smallest] = array_list[smallest], array_list[counter]

print(array_list)
