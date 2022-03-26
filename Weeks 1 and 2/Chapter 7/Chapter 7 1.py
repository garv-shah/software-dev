import sys


user_list = input("please enter a list of integers: ").split(", ")

try:
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
except ValueError as err:
    print(f"\nInvalid input listy with error:\n{err}")
    sys.exit()

print("\n----------------------------------------------------")
print("The list of integers you entered is: ", user_list)
print("----------------------------------------------------\n")

print("Print the total number of items in the list.")
print(len(user_list))
print("")

print("Print the last item in the list.")
print(user_list[-1])
print("")

print("Print the list in reverse order.")
print(user_list[::-1])
print("")

print("Print Yes if the list contains a 5 and No otherwise.")
if "5" in user_list:
    print("Yes")
else:
    print("No")
print("")

print("Print the number of fives in the list.")
print(user_list.count(5))
print("")

print("Remove the first and last items from the list, sort the remaining items, and print the result.")
user_list.pop(0)
user_list.pop(-1)
user_list.sort()
print(user_list)
print("")

print("Print how many integers in the list are less than 5.")
int = 0
for i in range(len(user_list)):
    if user_list[i] < 5:
        int += 1

print(int)
