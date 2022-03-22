import base64
from threading import Timer
import PySimpleGUI as sg
import collections

# sets the pysimplegui theme
sg.theme('Topanga')

# creates a dict of possible choices for the different tabs. this allows for easy iteration without having to
# redeclare the choices multiple times. it also makes it a lot easier to count the final sum in the end. the lists
# are nested as to provide the ability to have different rows inside the frames, if not they'd all be on one row,
# which doesn't look too good
choices_dict = {
    'fruit_vegetable': [['Apple', 'Pineapple', 'Banana'],
                        ['Strawberry', 'Orange', 'Spinach'],
                        ['Cucumber', 'Beetroot', 'Carrot']],
    'sizes': [['Small ($3.50)', 'Medium ($4.50)'], ['Large ($6.00)']],
    'juice_type': [['Apple', 'Tropical'],
                   ['Orange', 'Pineapple']],
    'extras': [['Ginger', 'Honey', 'Muesli'],
               ['Chia', 'Seeds']],
    'snacks': [['Hazelnut Protein Balls\n4 for $5.50', 'Chocolate Brownies\n1 for $3.50'],
               ['Almond Energy Bites\n4 for $4.50', 'Passion Fruit Muesli Bar\n1 for $3.25']]
}

category_name_dict = {
    'fruit_vegetable': 'Fruits/Vegetables',
    'sizes': 'Size',
    'juice_type': 'Juice Type',
    'extras': 'Extras',
    'snacks': 'Snacks'
}


# this function is used to create the layout of the tabs. it essentially creates a frame that is centered,
# and the input 'frame_layout' is the internal layout of the frame. as such, it just helps avoid repeated code for
# the tabs, centering the contents of each
def get_tab_layout(name, frame_layout, price_description=None):
    if price_description is None:
        return [
            [
                sg.VPush(),
                sg.Push(),
                sg.Frame(
                    layout=frame_layout,
                    element_justification='center',
                    title='',
                    border_width=0,
                    key=name + '_frame'
                ),
                sg.Push(),
                sg.VPush()
            ]
        ]
    else:
        return [
            [
                sg.VPush(),
                sg.Push(),
                sg.Frame(
                    layout=[
                               [sg.VPush()],
                               [sg.Text(price_description, font=('Helvetica', 20))],
                               [sg.VPush()]
                           ] + frame_layout + [
                               [sg.Text('')]
                           ],
                    element_justification='center',
                    title='',
                    border_width=0,
                    key=name + '_frame'
                ),
                sg.Push(),
                sg.VPush()
            ]
        ]


# this function is used to limit the values of a checkbox group from the choices_dict, which is also in the layout
def limit_checkbox_selection(name, limit, internal_values):
    # global variable declaration to interact with the external choices_dict variable, not the internal one
    global choices_dict

    # this creates a dictionary of the different fruit vegetable options, and whether they are currently selected or not
    # this is done just by selecting the correct value from the values' dictionary using the keys in choices_dict
    fruit_vegetable_dict = {}
    for array in choices_dict[name]:
        for choice in array:
            fruit_vegetable_dict[choice] = internal_values[name + choice]

    # over here, we get the sum of all the True values, meaning they are selected, and if the number of checkboxes
    # selected is above or equal to the specified limit, all other checkboxes are marked as disabled
    if sum(fruit_vegetable_dict.values()) >= limit:
        for internal_key in fruit_vegetable_dict.keys():
            # if not selected, disable the checkbox
            if not fruit_vegetable_dict[internal_key]:
                my_window.Element(name + internal_key).Update(disabled=True)
    else:
        # if the number of checkboxes selected is below the limit, we want to enable the deselected ones again
        for internal_key in fruit_vegetable_dict.keys():
            my_window.Element(name + internal_key).Update(disabled=False)


# this is the main layout of the pysimplegui page, including all visual elements
layout = [
    # this is the first row, containing the logo and company name, 'CGS Juice Bar'. the image is quite big,
    # so the resolution is decreased to a 20th of what it originally was, via the sub-sample parameter
    [
        sg.Push(),
        sg.Image('logo.png', subsample=20, key='logo'),
        sg.Text('CGS Juice Bar', font=('Helvetica', 36)),
        sg.Push()
    ],
    # empty text rows like this are used for a bit of padding, to make everything look a bit nicer and spaced out
    [
        sg.Text('')
    ],
    # the column with the input name of the user, relatively simple, is used to process the order. a size is defined
    # so that it doesn't take up the whole width, which imo looks a bit better
    [
        sg.Push(),
        sg.Text("Name", font=('Helvetica', 20)), sg.Input(key="user_name", font=('Helvetica', 20), size=(20, 1)),
        sg.Push()
    ],
    # another row created for padding
    [
        sg.Text('')
    ],
    # this is probably the *main* row, containing the tabs for each of the different categories
    [
        sg.TabGroup(
            [
                [
                    # this first tab group is for the juice types, using the get_tab_layout function to create the
                    # layout. list comprehension is used to iterate through each of the choices in the choice dict
                    # and return a radio, all of which belong to the same group. similarly, different properties such
                    # as the key or text for the radio are defined based on the 'choice'
                    sg.Tab(category_name_dict['juice_type'], get_tab_layout(
                        'juice_type',
                        [
                            [
                                sg.Radio(
                                    choice, size=(10, 1), font=('Helvetica', 18),
                                    key='juice_type' + choice, group_id='juice_type'
                                ) for choice
                                in array
                            ] for array in choices_dict['juice_type']
                        ]
                    ), key='juice_type_tab'),
                    # same as previous tab, but for sizes
                    sg.Tab(category_name_dict['sizes'], get_tab_layout(
                        'sizes',
                        [
                            [
                                sg.Radio(
                                    choice, font=('Helvetica', 18),
                                    key='sizes' + choice, group_id='sizes'
                                ) for choice
                                in array
                            ] for array in choices_dict['sizes']
                        ]
                    ), key='sizes_tab'),
                    # similarly, the third tab uses the same function, but this time returns a checkbox instead.
                    # this one is slightly special though, because unlike the extras tab, these checkboxes have
                    # enable_events set to True. This allows them to fire events, which lets us process how many are
                    # selected to disable when the limit of 4 is reached
                    sg.Tab(category_name_dict['fruit_vegetable'], get_tab_layout(
                        'fruit_vegetable',
                        [
                            [
                                sg.Checkbox(
                                    choice, size=(10, 1), font=('Helvetica', 18),
                                    key='fruit_vegetable' + choice, enable_events=True
                                ) for choice
                                in array
                            ] for array in choices_dict['fruit_vegetable']
                        ],
                        '25 cents per'
                    ), key='fruit_vegetable_tab'),
                    # the extras tab is the same as the fruits/vegetables tab, just without the event firing
                    sg.Tab(category_name_dict['extras'], get_tab_layout(
                        'extras',
                        [
                            [
                                sg.Checkbox(
                                    choice, font=('Helvetica', 18), key='extras' + choice,
                                ) for choice
                                in array
                            ] for array in choices_dict['extras']
                        ],
                        '30 cents per'
                    ), key='extras_tab'),
                    # finally, the last tab for snacks
                    sg.Tab(category_name_dict['snacks'], get_tab_layout(
                        'snacks',
                        [
                            [
                                sg.Checkbox(
                                    choice, font=('Helvetica', 18), key='snacks' + choice, size=(20, 1)
                                ) for choice
                                in array
                            ] for array in choices_dict['snacks']
                        ]
                    ), key='snacks_tab'),
                ]
            ],
        )
    ],
    # padding row
    [
        sg.Text('')
    ],
    # this row contains the buttons to submit and cancel, as well as a little note, which changes if errors occur.
    # custom colours are set with the button colour property
    [
        sg.Text('* means required', font=('Helvetica', 12), justification='center', key='error_text',
                text_color='white'),
        sg.Checkbox('Ice?', font=('Helvetica', 10), key='ice_checkbox', default=True),
        sg.Push(),
        sg.Button('Submit', font=('Helvetica', 16), key='submit_button', button_color=('#7FFFD4', '#50C878')),
        sg.Button('Cancel', font=('Helvetica', 16), key='cancel_button', button_color=('#FAA0A0', '#EE4B2B')),
    ]
]

# creates the window and sets a title + icon. the base64 encoding is required as pysimplegui doesn't support the png
# for some reason, so it just converts it
icon = base64.b64encode(open('./logo.png', 'rb').read())
my_window = sg.Window("CGS Juice Bar", layout, icon=icon)

# main event loop where logic can be handled
while True:
    # reads the event and values in the event loop
    event, values = my_window.read()

    # if the cancel button is clicked, or the user closes the window, break out of the loop (closes the window)
    if event in (None, 'cancel_button'):
        break

    if event == 'submit_button':
        def reset_error_text():
            my_window.Element('error_text').Update('* means required', text_color='white')


        bool_keys = []
        choice_keys = collections.defaultdict(list)

        for key in values.keys():
            if isinstance(values[key], bool):
                bool_keys.append(key)
            if isinstance(key, str):
                for choice_key in choices_dict.keys():
                    if choice_key in key:
                        choice_keys[choice_key].append(key)

        if all(not values[key] for key in bool_keys):
            my_window.Element('error_text').Update('Please select at least one option!', text_color='red')
            Timer(2.5, reset_error_text).start()
        elif values['user_name'] == '':
            my_window.Element('error_text').Update('Please enter a name for your order!', text_color='red')
            Timer(2.5, reset_error_text).start()
        elif all(not values[key] for key in choice_keys['juice_type']):
            my_window.Element('error_text').Update('A juice type needs to be selected!', text_color='red')
            Timer(2.5, reset_error_text).start()
        elif all(not values[key] for key in choice_keys['sizes']):
            my_window.Element('error_text').Update('A size needs to be selected!', text_color='red')
            Timer(2.5, reset_error_text).start()
        else:
            submission_popup = sg.Window("Success!", [
                [sg.Text(f'Thank you {values["user_name"]}, your order has been placed!',
                         font=('Helvetica', 16), justification='center')],
                [sg.Text('')],
                [
                    sg.Frame(
                        layout=[
                            [
                                sg.Text(
                                    choice, font=('Helvetica', 12), justification='center'
                                ) for choice
                                in array if values[category + choice]
                            ] for array in choices_dict[category]
                        ],
                        element_justification='center',
                        title=category_name_dict[category],
                        border_width=1,
                        key=category + '_popup__frame',
                        relief=sg.RELIEF_SUNKEN,
                    ) for category in choices_dict.keys()
                ],
                [sg.Push(), sg.Button('OK!')]
            ], icon=icon, modal=True)

            submission_popup.read()
            submission_popup.close()

    # limits the maximum number of selections for fruits/vegetables to 4
    limit_checkbox_selection('fruit_vegetable', 4, values)

my_window.close()
