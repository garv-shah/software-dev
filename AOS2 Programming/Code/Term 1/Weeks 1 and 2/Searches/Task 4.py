# Binary Search (recursive)
def binary_search(my_list, low_index, high_index, search_item):
    if high_index >= low_index:
        mid_index = (low_index + high_index) // 2

        if my_list[mid_index] == search_item:
            return mid_index
        elif my_list[mid_index] > search_item:
            return binary_search(my_list, low_index, mid_index - 1, search_item)
        else:
            return binary_search(my_list, mid_index + 1, high_index, search_item)
    else:
        return None


example_list = [1, 8, 12, 18, 31, 75, 77]
example_item = 77

result = binary_search(example_list, 0, len(example_list) - 1, example_item)

if result is not None:
    print(f"Found {example_item} at index {result}")
else:
    print(f"{example_item} not found")
