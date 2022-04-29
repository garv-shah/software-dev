# Linear Search
my_list = [12, 8, 31, 1, 77, 75, 18]
search_item = 1
found = False

for current_element in my_list:
    if current_element == search_item:
        found = True
        break

print(found)
