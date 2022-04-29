try:  # Try to import the required modules
    import PySimpleGUI as sg, os
    from PIL import Image
except ModuleNotFoundError:  # If the required modules aren't found then throw a controlled error and exit the program
    print("Error: Unable to import required modules")
    exit()

sizes = ["Small", "Medium", "Large"]
juiceTypes = ["Apple", "Tropical", "Orange", "Pineapple"]
fruitsVeg = ["Apple", "Pineapple", "Banana", "Strawberry", "Orange", "Spinach", "Cucumber",
             "Beetroot", "Carrot"]
extras = ["Ginger", "Honey", "Muesli", "Chia Seeds"]
snacks = [{"Name": "Hazelnut Protein Ball Pack of 4", "Price": 5.5}, {"Name": "Chocolate Brownie", "Price": 3.5},
          {"Name": "Almond Energy Bites Pack of 4", "Price": 4.5}, {"Name": "Passion fruit Muesli Bar", "Price": 3.25}]

sg.theme('BlueMono')  # Sets application theme

try:  # Tries to import and resize the image
    image = Image.open(os.getcwd() + "/task3Resource.png")
    image = image.resize((35, 35), resample=Image.BICUBIC)
    image.save("task3Resource.png")
except FileNotFoundError:  # If the image is not present then throw a controlled error and exit the program
    print("Error: Unable to Import Required Image")
    exit()

titleFont = ("SF Pro Display Bold", 14)

layout = [
    [
        sg.Image(os.getcwd() + "/task3Resource.png"),
        sg.Push(),
        sg.Text('CGS Juice Bar', font=titleFont, ),
        sg.Push(),
        sg.Image(os.getcwd() + "/task3Resource.png"),
    ],

    [
        [
            sg.Push(),
            sg.Text("Order Name: "), sg.InputText(size=(20, 150), key="orderName"),
            sg.Push(),
        ],

        sg.Push(),  # Left Side Push for Juice Elements
        [
            [sg.Frame("Juice Size",
                      [
                          [sg.VPush()],
                          [sg.DropDown(sizes, default_value="Small", key="size")],
                          [sg.VPush()],
                      ],
                      size=(100, 60)
                      ),

             sg.Frame("Juice Type",
                      [
                          [sg.VPush()],
                          [sg.DropDown(juiceTypes, default_value="Apple", key="juiceType")],
                          [sg.VPush()],
                      ],
                      size=(100, 60)
                      ),
             ],

            [sg.Frame("Fruits/Veggies",
                      [
                          [sg.Checkbox(item, key=item)] for item in fruitsVeg
                      ],
                      size=(100, 250)
                      ),

             sg.Frame("",
                      [
                          [sg.Frame("Ice or No Ice",
                                    [[sg.Radio("Add Ice", "Ice", default=True, key="ice")],
                                     [sg.Radio("No Ice", "Ice", default=False, key="noIce")],
                                     ],
                                    size=(100, 90)
                                    ),
                           ],
                          [sg.Frame("Extras",
                                    [
                                        [sg.Checkbox(item, key=item)] for item in extras
                                    ],
                                    size=(100, 155)
                                    ),
                           ],
                      ],
                      border_width=0
                      ),
             ],

            [sg.Frame("Snacks",
                      [
                          [sg.Checkbox(item["Name"], key=item["Name"])] for item in snacks
                      ],
                      size=(215, 125)
                      ),
             ],
        ],

        sg.Push(),  # Right Side Push for Juice Elements
    ],

    [
        sg.Push(),
        sg.Button('Finish', key="doneButton"),
        sg.Button('Cancel'),
        sg.Push(),
    ],
]

window = sg.Window('CGS Juice Bar', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "doneButton":
        cost = 0
        fruitVegCount = 0
        receiptInfo = ""

        if not values["orderName"]:  # Check if order has been given proper name
            sg.popup("You need to give your order a name,\notherwise it cannot be processed", title="Incomplete Order")
        else:
            # Calculate Cost For Size
            if values["size"] == "Small":
                cost += 3.5
            elif values["size"] == "Medium":
                cost += 4.5
            elif values["size"] == "Large":
                cost += 6

            for item in values:  # Goes through all items
                if values[item]:  # If the item is ticked
                    if item in fruitsVeg:  # Add 25c for every fruit or veg item
                        cost += 0.25
                        fruitVegCount += 1
                        receiptInfo += " • {} - 25c\n".format(item)
                    elif item in extras:  # Adds 30c for every extra item
                        cost += 0.3
                        receiptInfo += " • {} - 30c\n".format(item)
                    for snack in snacks:  # Run through snacks, if snack is ticked, add snack price to cost
                        if item == snack["Name"]:
                            cost += snack["Price"]
                            receiptInfo += " • {} - ${}\n".format(snack["Name"], "{:.2f}".format(snack["Price"]))
            if not values["ice"]:
                receiptInfo += "\n • NO ICE\n"

            if fruitVegCount <= 4:
                sg.popup(
                    "Thankyou for your order {}\n\n{} {} Juice:\n\n{}\nTotal Price: ${}".format(values["orderName"],
                                                                                                values["size"],
                                                                                                values["juiceType"],
                                                                                                receiptInfo,
                                                                                                "{:.2f}".format(cost)),
                    title="Receipt", )
            else:  # The user has exceeded the permitted amount of Fruit/Veg
                sg.popup("You can only have a max of 4 Fruit/Veg items :)", title="Too Many Fruit/Veg")

window.close()
