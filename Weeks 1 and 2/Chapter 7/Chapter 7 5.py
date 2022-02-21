# Ask the user to enter a list of strings. Create a new list that consists of those strings with their first
# characters removed.

new_list = []
user_input = input("Enter a list of strings: ")
user_list = user_input.split(", ")
for i in user_list:
    new_list.append(i[1:])
print(new_list)
