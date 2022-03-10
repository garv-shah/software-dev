import PySimpleGUI as sg
import csv

sg.theme('LightBrown2')

subject_list = ["Software Development", "Computer Science", "Applied Computing"]

# Creates the layout for the window
layout = [
    [
        sg.Text("Subject"), sg.Input(key="fun")
    ],
    [
        [sg.Radio(subject, group_id='subjects')] for subject in subject_list
        # Uses list comprehension to create a list of radio buttons from the subject list above
    ],
    [
        sg.Push(),
        sg.Frame(layout=[
            [
                sg.Checkbox("Fish & Chips", key="chips"),
                sg.Checkbox("Pizza", key="pizza"),
                sg.Checkbox("Pasta", key="pasta")
            ]
        ], title="Food"),
        sg.Push()
    ],
    [
        sg.Push(),
        sg.Multiline(size=(30, 10), key="multiline", default_text="yay this is some default text"),
        sg.Push()
    ],
    [
        sg.DropDown(('Yellow', 'Blue', 'Green', 'Red'), key='colours', default_value='Yellow'),
        sg.Button('Done'),
        sg.Button('Cancel')
    ],
]

my_window = sg.Window("Today's Fun", layout)

# Persistent window logic
while True:
    event, values = my_window.read()

    # If the user closes the window or clicks cancel, the program will close
    if event in (None, 'Cancel'):
        break

    # Logic for if the user clicks done
    if event == 'Done':
        final_dict = {}

        # Creates a dictionary that is a copy of the values' dictionary without the 0, 1, 2, etc. keys
        # This is because we want these to be the 'subjects' key in the csv file
        for key in values.keys():
            if type(key) == str:
                final_dict[key] = values[key]

        # Makes the multiline entry a raw string, as if not, it creates new lines in the csv file, which breaks it
        final_dict['multiline'] = repr(final_dict['multiline'])

        # Iterates through the radios, and if any of them are true, creates a popup window with the subject name
        for x in range(len(subject_list)):
            if values[x]:
                final_dict['subjects'] = subject_list[x]
                sg.Popup('Chosen Subject:', f'You chose {subject_list[x]}')

        # Writes the final dictionary to a csv file
        with open("today's_fun.csv", 'w+', newline='') as csvfile:
            fieldnames = ['fun', 'subjects', 'chips', 'pizza', 'pasta', 'multiline', 'colours']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(final_dict)
            csvfile.close()

my_window.close()
