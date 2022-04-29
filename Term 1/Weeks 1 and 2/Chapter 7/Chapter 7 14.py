# Write a program that asks the user to enter a length in feet. The program should then give the user the option to
# convert from feet into inches, yards, miles, millimeters, centimeters, meters, or kilometers. Say if the user
# enters a 1, then the program converts to inches, if they enter a 2, then the program converts to yards, etc. While
# this can be done with if statements, it is much shorter with lists and it is also easier to add new conversions if
# you use lists.

print("This program converts feet to other units of measurement.")
feet = eval(input("Enter a number of feet: "))

choice_list = [
    ['inches', feet * 12],
    ['yards', feet / 3],
    ['miles', feet / 5280],
    ['millimeters', feet * 304.8],
    ['centimeters', feet * 30.48],
    ['meters', feet * 0.3048],
    ['kilometers', feet / 3280.84]
]

for x in choice_list:
    print(f"{choice_list.index(x)}. Feet to {x[0]}")

choice = eval(input("\nEnter your choice: "))

print(f"{feet} feet is {choice_list[choice][1]} {choice_list[choice][0]}")
