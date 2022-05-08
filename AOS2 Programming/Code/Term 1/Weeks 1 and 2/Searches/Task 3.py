# Binary Search (iterative)
def binary_search(my_list, search_item):
    low_index = 0
    high_index = len(my_list) - 1

    while low_index <= high_index:
        midpoint_index = (low_index + high_index) // 2
        if my_list[midpoint_index] < search_item:
            low_index = midpoint_index + 1
        elif my_list[midpoint_index] > search_item:
            high_index = midpoint_index - 1
        else:
            return midpoint_index
    return None


example_list = [1, 8, 12, 18, 31, 75, 77]
example_item = 77

result = binary_search(example_list, example_item)

if result is not None:
    print(f"Found {example_item} at index {result}")
else:
    print(f"{example_item} not found")
