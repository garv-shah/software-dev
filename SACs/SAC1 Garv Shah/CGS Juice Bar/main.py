import PySimpleGUI as sg

sg.theme('Topanga')

fruit_vegetable_choices = [['Apple', 'Pineapple', 'Banana'],
                           ['Strawberry', 'Orange', 'Spinach'],
                           ['Cucumber', 'Beetroot', 'Carrot']]

juice_type_choices = [['Apple', 'Tropical'],
                      ['Orange', 'Pineapple']]

extras_choices = [['Ginger', 'Honey', 'Muesli'],
                  ['Chia', 'Seeds']]

# Create layout for calculator in pysimplegui
layout = [
    [
        sg.Push(),
        sg.Image('logo.png', subsample=20, key='logo'),
        sg.Text('CGS Juice Bar', font=('Helvetica', 36)),
        sg.Push()
    ],
    [
        sg.Text('')
    ],
    [
        sg.Push(),
        sg.Text("Name", font=('Helvetica', 20)), sg.Input(key="user_name", font=('Helvetica', 20), size=(20, 1)),
        sg.Push()
    ],
    [
        sg.Text('')
    ],
    [
        sg.Push(),
        sg.Frame(
            layout=[
                [
                    sg.Radio(choice, size=(16, 1), font=('Helvetica', 18), group_id='juice_type', key=choice) for choice
                    in array
                ] for array in juice_type_choices
            ],
            element_justification='center',
            title='Juice Type',
            relief=sg.RELIEF_SUNKEN,
            border_width=1,
            tooltip='Recycle',
            key='recycle'
        ),
        sg.Push()
    ],
    [
        sg.Push(),
        sg.Frame(
            layout=[
                [
                    sg.Checkbox(choice, size=(16, 1), font=('Helvetica', 18), key=choice, enable_events=True) for choice
                    in array
                ] for array in fruit_vegetable_choices
            ],
            element_justification='center',
            title='Fruits/Vegetables',
            relief=sg.RELIEF_SUNKEN,
            border_width=1,
            tooltip='Recycle',
            key='recycle'
        ),
        sg.Push()
    ],
]

my_window = sg.Window("CGS Juice Bar", layout)

while True:
    event, values = my_window.read()
    if event in (None, 'Cancel'):
        print(f"The user pressed {event}")
        break

    fruit_vegetable_dict = {}
    for array in fruit_vegetable_choices:
        for choice in array:
            fruit_vegetable_dict[choice] = values[choice]

    if sum(fruit_vegetable_dict.values()) >= 4:
        for key in fruit_vegetable_dict.keys():
            if not fruit_vegetable_dict[key]:
                my_window.Element(key).Update(disabled=True)
    else:
        for key in fruit_vegetable_dict.keys():
            my_window.Element(key).Update(disabled=False)

my_window.close()
