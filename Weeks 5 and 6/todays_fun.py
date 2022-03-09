import PySimpleGUI as sg

sg.theme('LightBrown2')

subject_list = ["Software Development", "Computer Science", "Applied Computing"]

layout = [
    [sg.Text("Subject"), sg.Input(key="fun")],
    [[sg.Radio(subject, group_id='subjects')] for subject in subject_list],
    [sg.DropDown(('Yellow', 'Blue', 'Green', 'Red'), key='colours', default_value='Yellow'), sg.Button('Done')],
]

my_window = sg.Window("Today's Fun", layout)

while True:
    event, values = my_window.read()
    if event in (None, 'Cancel'):
        break

    if event == 'Done':
        for x in range(len(subject_list)):
            if values[x]:
                sg.Popup('Chosen Subject:', f'You chose {subject_list[x]}')

my_window.close()
