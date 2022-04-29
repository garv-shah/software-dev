

#MENU :)

cal = input('''HELLO AND WELCOME TO RAF'S CALCULATOR. WHAT WOULD YOU LIKE TO CALCULATE?
TEMPERATURE(1)
AREA OF SHAPES(2)''')
#Temperature Calc Menu
if cal == "1":
    temp = input('''Now would you like to calculate
Farenheit -> Celcius(1)
Celcius -> Farenheit(2)''')
    if temp == "1":
#-------------Farenheit to Celcius Calc-----------------------------------
        f = (float(input('''WELCOME TO THE FARENHEIT TO CELCIUS CONVERTER
WHAT TEMPERATURE (Fº) WOULD YOU LIKE TO CONVERT TO CELCIUS?''')))

        f = round((f-32)*5/9,2)
        print(f"That is {f}ºC (Rounded to 2 dp)")
#------------Celcius to Farenheit Calc--------------------------------------
    elif temp == "2":
        c = (float(input('''WELCOME TO THE CELCIUS TO FARENHEIT CONVERTER
WHAT TEMPERATURE (Cº) WOULD YOU LIKE TO CONVERT TO FARENHEIT?''')))

        c = round((c*9/5) + 32,2)
        print(f"That is {c}ºC (Rounded to 2 dp)")
#Response to invalid Answers
    else:
        print("Only 1 or 2")
    
#Area of Trapeziod

print("This is the Trapeziod area calculator")
base = float(input("Please input the length of a base"))
base2 = float(input("Please input the length of the other base"))
height = float(input('''Now enter the height of the trapeziod.
*Please note that this is not the lenght of the side of the trapeziod,
but rather the height perpandicular to the base'''))


tarea = round(((base+base2)/2)*height,2)
print(f"The Area of that Trapezoid is {tarea}")









