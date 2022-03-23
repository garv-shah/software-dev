import base64
import csv
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
# the tabs, centering the contents of each. it also allows for the creation of a frame with a description,
# which is used for displaying prices
def get_tab_layout(name, frame_layout, price_description=None):
    return [
        [
            sg.VPush(),
            sg.Push(),
            sg.Frame(
                layout=frame_layout if price_description is None else
                [
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
def limit_checkbox_selection(name, limit, fruit_vegetable_dict):
    # global variable declaration to interact with the external choices_dict variable, not the internal one
    global choices_dict

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


# this function is used to handle when the submit button is clicked
def submit_clicked(internal_values, internal_price):
    # global variable declaration to interact with the external variables, not the internal ones
    global choices_dict
    global my_window

    # this function is defined, so it can be called by the Timer() function, which allows the process to be
    # multithreaded, not interfering with the rest of the application while it runs
    def reset_error_text():
        my_window.Element('error_text').Update('* means required', text_color='white')

    # this dict stores the state of each category, essentially getting the keys of the internal_values variable and
    # splitting it up into its respective category
    choice_keys = collections.defaultdict(list)

    # looping through the keys in internal_values, if the key from inside internal_values contains the key from the
    # choices_dict, the key is added to the respective list. this is because the way we generate the keys is by
    # adding the key value of the choices_dict to some other string, so all of them must contain this string inside
    # them if they are of that category (sorry for the excessive use of the word key lmao, hopefully it makes sense.
    # if not just mess around with a few print statements, it's clearer if you see it in action)
    for selector in internal_values.keys():
        if isinstance(selector, str):
            for internal_key in choices_dict.keys():
                if internal_key in selector:
                    choice_keys[internal_key].append(selector)

    # this if else tree is all for error checking before showing the results. for example, if the user has not filled
    # in their name, they are told to do so, by replacing the text in the bottom right. thanks to the threading
    # library, this can be multithreaded, meaning the user can do other things while the process runs with its delay.
    # the all function also saves a few for loops, basically just returning true of everything in the iterator inside
    # is True as well.
    if internal_values['user_name'] == '':
        my_window.Element('error_text').Update('Please enter a name!', text_color='red')
        Timer(2.5, reset_error_text).start()
    elif all(not internal_values[selector] for selector in choice_keys['juice_type']):
        my_window.Element('error_text').Update('Please enter a juice type!', text_color='red')
        Timer(2.5, reset_error_text).start()
    elif all(not internal_values[selector] for selector in choice_keys['sizes']):
        my_window.Element('error_text').Update('Please enter a size!', text_color='red')
        Timer(2.5, reset_error_text).start()
    else:
        # finally, if everything is fine, a non-persistent window is displayed with the results of the order. this is
        # done by looping through each key in the choices_dict and creating a new frame for each,
        # with the appropriate values selected if they are True. an extra frame is also added for ice, as it is not
        # part of the normal categories, so it is added manually
        submission_popup = sg.Window("Success!", [
            [sg.Text(f'Thank you {internal_values["user_name"]}, your order has been placed!',
                     font=('Helvetica', 16), justification='center')],
            [sg.Text('')],
            [
                sg.Frame(
                    layout=[
                        [
                            sg.Text(
                                choice, font=('Helvetica', 12), justification='center'
                            ) for choice
                            in array if internal_values[category + choice]
                        ] for array in choices_dict[category]
                    ],
                    element_justification='center',
                    title=category_name_dict[category],
                    border_width=1,
                    key=category + '_popup__frame',
                    relief=sg.RELIEF_SUNKEN,
                ) for category in choices_dict.keys() if
                not all(not internal_values[selector] for selector in choice_keys[category])
            ] + [
                sg.Frame(
                    layout=[
                        [sg.Text(('No', 'Yes')[internal_values['ice_checkbox']],
                                 font=('Helvetica', 12), justification='center')]
                    ],
                    element_justification='center',
                    title='Ice?',
                    border_width=1,
                    key='ice_popup__frame',
                    relief=sg.RELIEF_SUNKEN,
                )
            ],
            [sg.Text('')],
            [sg.Text(f'This will cost you ${internal_price:.2f}!', font=('Helvetica', 12)), sg.Push(), sg.Button('OK!')]
        ], icon=icon, modal=True)

        submission_popup.read()
        submission_popup.close()

        # this saves the internal_values dictionary to a csv file :D
        with open("user_order.csv", 'w+', newline='') as csvfile:
            fieldnames = list(internal_values.keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(internal_values)
            csvfile.close()


# this function counts the total price. essentially, it goes through each using an if else tree, and adds the needed
# amount, which is relatively crude and not expandable, but it's fine for the scale of this application. It also uses
# the counting_selection_dict from before to sum up how many are selected from a given category, and then multiplies
# that by how much each costs. All of this is then updated in the UI, and then returned, so it can be used in the
# popup window
def count_total_price(input_dict, internal_values):
    internal_price = 0
    if internal_values['sizesSmall ($3.50)']:
        internal_price += 3.5
    if internal_values['sizesMedium ($4.50)']:
        internal_price += 4.5
    if internal_values['sizesLarge ($6.00)']:
        internal_price += 6

    if internal_values['snacksHazelnut Protein Balls\n4 for $5.50']:
        internal_price += 5.5
    if internal_values['snacksChocolate Brownies\n1 for $3.50']:
        internal_price += 3.5
    if internal_values['snacksAlmond Energy Bites\n4 for $4.50']:
        internal_price += 4.5
    if internal_values['snacksPassion Fruit Muesli Bar\n1 for $3.25']:
        internal_price += 3.25

    internal_price += sum(input_dict['fruit_vegetable_dict'].values()) * 0.25
    internal_price += sum(input_dict['extras_dict'].values()) * 0.30

    my_window.Element('price_text').Update(f'Total Price: ${internal_price:.2f}')
    return internal_price


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
        # the tab group could probably be looped over, which is what I initially had, but the functionality of each
        # is different enough to the point that it's not worth it, and functions help get rid of repeated code instead
        sg.TabGroup(
            [
                [
                    # this first tab group is for the juice types, using the get_tab_layout function to create the
                    # layout. list comprehension is used to iterate through each of the choices in the choice dict
                    # and return a radio, all of which belong to the same group. similarly, different properties such
                    # as the key or text for the radio are defined based on the 'choice'
                    sg.Tab(category_name_dict['juice_type'], get_tab_layout(
                        name='juice_type',
                        frame_layout=[
                            [
                                sg.Radio(
                                    choice, size=(10, 1), font=('Helvetica', 18),
                                    key='juice_type' + choice, group_id='juice_type', enable_events=True
                                ) for choice
                                in array
                            ] for array in choices_dict['juice_type']
                        ]
                    ), key='juice_type_tab'),
                    # same as previous tab, but for sizes
                    sg.Tab(category_name_dict['sizes'], get_tab_layout(
                        name='sizes',
                        frame_layout=[
                            [
                                sg.Radio(
                                    choice, font=('Helvetica', 18),
                                    key='sizes' + choice, group_id='sizes', enable_events=True
                                ) for choice
                                in array
                            ] for array in choices_dict['sizes']
                        ]
                    ), key='sizes_tab'),
                    # similarly, the third tab uses the same function, but this time returns a checkbox instead. this
                    # one is slightly special though, because unlike the extras tab, these checkboxes have
                    # enable_events set to True (actually all of them do now to calculate the price, but ignore
                    # that). This allows them to fire events, which lets us process how many are selected to disable
                    # when the limit of 4 is reached
                    sg.Tab(category_name_dict['fruit_vegetable'], get_tab_layout(
                        name='fruit_vegetable',
                        frame_layout=[
                            [
                                sg.Checkbox(
                                    choice, size=(10, 1), font=('Helvetica', 18),
                                    key='fruit_vegetable' + choice, enable_events=True
                                ) for choice
                                in array
                            ] for array in choices_dict['fruit_vegetable']
                        ],
                        price_description='25 cents per'
                    ), key='fruit_vegetable_tab'),
                    # the extras tab is the same as the fruits/vegetables tab, just without the event firing
                    sg.Tab(category_name_dict['extras'], get_tab_layout(
                        name='extras',
                        frame_layout=[
                            [
                                sg.Checkbox(
                                    choice, font=('Helvetica', 18), key='extras' + choice, enable_events=True
                                ) for choice
                                in array
                            ] for array in choices_dict['extras']
                        ],
                        price_description='30 cents per'
                    ), key='extras_tab'),
                    # finally, the last tab for snacks
                    sg.Tab(category_name_dict['snacks'], get_tab_layout(
                        name='snacks',
                        frame_layout=[
                            [
                                sg.Checkbox(
                                    choice, font=('Helvetica', 18), key='snacks' + choice,
                                    size=(20, 1), enable_events=True
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
        sg.Checkbox('Reset', font=('Helvetica', 10), key='reset_checkbox', enable_events=True),
        sg.Push(),
        sg.Text('Total Price: $0.00', font=('Helvetica', 12), justification='center', key='price_text'),
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

    # this loop counts how many checkboxes/radios are checked in each category. this is useful to calculate the total
    # price, as we can go through each category and sum them up, charging a certain amount for how many ever are
    # selected. it is also used to limit the number of checkboxes selected for the fruit/vegetables tab
    counting_selection_dict = collections.defaultdict(dict)
    for choice_key in choices_dict.keys():
        for array in choices_dict[choice_key]:
            for choice in array:
                counting_selection_dict[choice_key + '_dict'][choice] = values[choice_key + choice]

    total_price = count_total_price(counting_selection_dict, values)

    # limits the maximum number of selections for fruits/vegetables to 4
    limit_checkbox_selection('fruit_vegetable', 4, counting_selection_dict['fruit_vegetable_dict'])

    # if the cancel button is clicked, or the user closes the window, break out of the loop (closes the window)
    if event in (None, 'cancel_button'):
        break

    if event == 'submit_button':
        submit_clicked(values, total_price)

    if event == 'reset_checkbox':
        my_window['user_name'].update('')
        my_window['price_text'].update('Total Price: $0.00')
        for key in values.keys():
            if isinstance(values[key], bool) and key != 'ice_checkbox':
                my_window[key].update(False, disabled=False)

my_window.close()
