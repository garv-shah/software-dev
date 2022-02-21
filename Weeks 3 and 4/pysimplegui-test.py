from io import BytesIO

import PySimpleGUI as sg
import os
from PIL import Image

sg.theme('LightBrown2')

layout = [[sg.Txt('' * 10)],
          [sg.Text('', size=(15, 1), font=('Helvetica', 18),
                   text_color='black', key='input')],
          [sg.Txt('' * 10)],
          [sg.ReadFormButton('c'), sg.ReadFormButton('«')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('/')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('*')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')],
          ]

my_window = sg.Window("Convert Temperature", layout)

while True:
    event, values = my_window.read()
    if event in (None, 'Cancel'):
        print(f"The user pressed {event}")
        break

    if values['fah']:
        my_window["result"].Update(
            f"{values['degrees']} degrees celsius is {(eval(values['degrees']) * 9 / 5) + 32} degrees fahrenheit")
    else:
        my_window["result"].Update(
            f"{values['degrees']} degrees fahrenheit is {(eval(values['degrees']) - 32) * 5 / 9} degrees celsius")

my_window.close()
