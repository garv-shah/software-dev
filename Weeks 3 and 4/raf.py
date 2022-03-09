def fahrenheit_to_celsius():
    # -------------Fahrenheit to Celsius Calc-----------------------------------
    print('WELCOME TO THE FAHRENHEIT TO CELSIUS CONVERTER')
    print('WHAT TEMPERATURE (Fº) WOULD YOU LIKE TO CONVERT TO CELSIUS?')

    fahrenheit = get_float_input('Fahrenheit: ')

    celsius = (fahrenheit - 32) * 5 / 9
    print(f"That is {celsius:.2f}ºC (Rounded to 2 dp)")


def celsius_to_fahrenheit():
    # ------------Celsius to Fahrenheit Calc--------------------------------------
    print('WELCOME TO THE CELSIUS TO FAHRENHEIT CONVERTER')
    print('WHAT TEMPERATURE (Cº) WOULD YOU LIKE TO CONVERT TO FAHRENHEIT?')

    celsius = get_float_input('Celsius: ')

    fahrenheit = (celsius * 9 / 5) + 32
    print(f"That is {fahrenheit:.2f}ºC (Rounded to 2 dp)")


def temp_calc():
    print('Now would you like to calculate')
    print('Fahrenheit -> Celsius(1)')
    print('Celsius -> Fahrenheit(2)')
    temp = input()

    while True:
        if temp == "1":
            fahrenheit_to_celsius()
            break
        elif temp == "2":
            celsius_to_fahrenheit()
            break
        else:
            # Response to invalid Answers
            print('Invalid choice, can only be 1 or 2')
            continue


def area_of_trapezoid():
    # Area of Trapezoid

    print("This is the Trapezoid area calculator")
    base = get_float_input('Please input the length of a base: ')
    base2 = get_float_input('Please input the length of the other base: ')

    print('Now enter the height of the trapezoid.')
    print('*Please note that this is not the length of the side of the trapezoid')
    print('Rather, it is the height perpendicular to the base')
    height = get_float_input()

    trapezoid_area = ((base + base2) / 2) * height
    print(f"The Area of that Trapezoid is {trapezoid_area:.2f}")


def get_float_input(prompt=''):
    return_value = 0.0

    while True:
        try:
            return_value = float(input(prompt))
        except ValueError:
            print('ERROR: INVALID INPUT, PLEASE ENTER A NUMBER, TRY AGAIN')
            continue
        else:
            break

    return return_value


def main():
    print("HELLO AND WELCOME TO RAF'S CALCULATOR. WHAT WOULD YOU LIKE TO CALCULATE?")
    print('TEMPERATURE(1)')
    print('AREA OF SHAPES(2)')
    choice = input()

    # Temperature Calc Menu
    while True:
        if choice == "1":
            temp_calc()
            break
        elif choice == "2":
            area_of_trapezoid()
            break
        else:
            # Response to invalid Answers
            print('Invalid choice, can only be 1 or 2')
            continue


if __name__ == '__main__':
    main()
