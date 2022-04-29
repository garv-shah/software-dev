import PySimpleGUI as sg

sg.theme('LightBrown2')

# Create layout for calculator in pysimplegui
layout = [
    [sg.Image('green_earth.png', size=(400, 400)), sg.Text('GREEN EARTH RECYCLING', size=(30, 1), justification='center', font=('Helvetica', 36))],
    [sg.Push(), sg.Frame(layout=[[sg.Checkbox('Recycle', size=(16, 1), font=('Helvetica', 18)), sg.Checkbox('Recycle', size=(16, 1), font=('Helvetica', 18)), sg.Checkbox('Recycle', size=(16, 1), font=('Helvetica', 18)), sg.Checkbox('Recycle', size=(16, 1), font=('Helvetica', 18)), sg.Checkbox('Recycle', size=(16, 1), font=('Helvetica', 18))]], element_justification='center', title='', title_color='white', relief=sg.RELIEF_SUNKEN, border_width=1, tooltip='Recycle', key='recycle'), sg.Push()],
    [sg.Push(), sg.Frame(layout=[[sg.Radio('Recycle', size=(16, 1), font=('Helvetica', 18), group_id='bins'), sg.Radio('Recycle', size=(16, 1), font=('Helvetica', 18), group_id='bins')], [sg.Radio('Recycle', size=(16, 1), font=('Helvetica', 18), group_id='bins'), sg.Radio('Recycle', size=(16, 1), font=('Helvetica', 18), group_id='bins'), sg.Radio('Recycle', size=(16, 1), font=('Helvetica', 18), group_id='bins')]], element_justification='center', title='', title_color='white', relief=sg.RELIEF_SUNKEN, border_width=1, tooltip='Recycle', key='recycle'), sg.Push()],
]

my_window = sg.Window("My first GUI window", layout)

while True:
    event, values = my_window.read()
    if event in (None, 'Cancel'):
        print(f"The user pressed {event}")
        break
    my_window["result"].Update(f"The user pressed {event} with name {values['name']} and age {values['age']}")

my_window.close()
