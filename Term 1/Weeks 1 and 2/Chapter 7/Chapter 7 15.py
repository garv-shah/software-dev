import random
import string
user_input = input("please enter a string:\n")
user_key = input("if you want to decrypt, enter your key here. if not, leave this field empty and i will encrypt for "
                 "you instead:\n")

print("\nThanks!\n")


charList = list(string.ascii_lowercase)
list_of_letters = []
list_of_numbers = []
counter = 0
if user_key == '':
    for x in range(len(user_input)):
        num = random.randint(1, 26)
        if user_input[x].lower() in charList:
            list_of_letters.append(charList[(charList.index(user_input[x]) + num) % len(charList)])
            list_of_numbers.append(num)
        else:
            list_of_letters.append(user_input[x])
else:
    for x in range(len(user_input)):
        if user_input[x].lower() in charList:
            num = int(user_key.split(", ")[counter])
            list_of_letters.append(charList[(charList.index(user_input[x]) - num) % len(charList)])
            list_of_numbers.append(num)
            counter += 1
        else:
            list_of_letters.append(user_input[x])

print(''.join(list_of_letters))
if user_key == '':
    print(''.join(str(list_of_numbers))[1:-1])
