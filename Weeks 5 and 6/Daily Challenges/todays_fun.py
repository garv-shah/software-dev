import PySimpleGUI as sg
import csv

sg.theme('LightBrown2')

subject_list = ["Software Development", "Computer Science", "Applied Computing"]

layout = [
    [sg.Text("Subject"), sg.Input(key="fun")],
    [[sg.Radio(subject, group_id='subjects')] for subject in subject_list],
    [sg.Push(), sg.Frame(layout=[[sg.Checkbox("Fish & Chips", key="chips"), sg.Checkbox("Pizza", key="pizza"), sg.Checkbox("Pasta", key="pasta")]], title="Food"), sg.Push()],
    [sg.Push(), sg.Multiline(size=(30, 10), key="multiline", default_text="yay this is some default text"), sg.Push()],
    [sg.Text("")],
    [sg.DropDown(('Yellow', 'Blue', 'Green', 'Red'), key='colours', default_value='Yellow'), sg.Button('Done')],
]

my_window = sg.Window("Today's Fun", layout)

while True:
    event, values = my_window.read()
    if event in (None, 'Cancel'):
        break

    if event == 'Done':
        final_dict = {}

        for key in values.keys():
            if type(key) == str:
                final_dict[key] = values[key]

        final_dict['multiline'] = repr(final_dict['multiline'])

        for x in range(len(subject_list)):
            if values[x]:
                final_dict['subjects'] = subject_list[x]
                sg.Popup('Chosen Subject:', f'You chose {subject_list[x]}')

        with open('todays_fun.csv', 'w+', newline='') as csvfile:
            fieldnames = ['fun', 'subjects', 'chips', 'pizza', 'pasta', 'multiline', 'colours']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(final_dict)
            csvfile.close()


my_window.close()
