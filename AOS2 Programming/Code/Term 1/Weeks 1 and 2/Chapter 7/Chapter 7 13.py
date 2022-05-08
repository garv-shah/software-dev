# Write a program that removes any repeated items from a list so that each item appears at most once. For instance,
# the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

initial_list = [1, 1, 2, 3, 4, 3, 0, 0]
final_list = list(set(initial_list))
print(final_list)
