# Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the entries in the list that
# are greater than 10 with 10.

list = []
for i in range(12):
    list.append(int(input("Enter a number between 1 and 12: ")))
for i in range(len(list)):
    if list[i] > 10:
        list[i] = 10
print(list)
