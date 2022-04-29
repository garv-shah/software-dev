import PySimpleGUI as sg

sg.theme('LightBrown2')

# Create layout for calculator in pysimplegui
layout = [
    [sg.InputText("7", key="7", size=(1, 1), justification="center"), sg.InputText("8", key="8", size=(1, 1), justification="center"), sg.InputText("9", key="9", size=(1, 1), justification="center"), sg.InputText("/", key="/", size=(1, 1), justification="center")],
]

my_window = sg.Window("My first GUI window", layout)

while True:
    event, values = my_window.read()
    if event in (None, 'Cancel'):
        print(f"The user pressed {event}")
        break
    my_window["result"].Update(f"The user pressed {event} with name {values['name']} and age {values['age']}")

my_window.close()
