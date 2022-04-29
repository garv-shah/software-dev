import random

num_list = []
for x in range(20):
    num_list.append(random.randint(1, 100))

# Print the list.
print(num_list)

# Print the average of the elements in the list.
print("The average of the elements in the list is:", sum(num_list) / len(num_list))

# Print the largest and smallest values in the list.
print("The largest value in the list is:", max(num_list))
print("The smallest value in the list is:", min(num_list))

# Print the second largest and second smallest entries in the list
print("The second largest value in the list is:", sorted(num_list)[-2])
print("The second smallest value in the list is:", sorted(num_list)[1])

# Print how many even numbers are in the list.
print(f"There are {len([x for x in num_list if x % 2 == 0])} even numbers in the list.")
