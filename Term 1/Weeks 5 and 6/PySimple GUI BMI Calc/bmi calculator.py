import PySimpleGUI as sg

layout = [
    [sg.Text("Height: "), sg.Input(key="height")],
    [sg.Text("Weight: "), sg.Input(key="weight")],
    [sg.Button("Calculate")]
]

my_window = sg.Window("BMI Calculator", layout)

while True:
    event, values = my_window.read()
    if event in (None, 'Cancel'):
        break

    if event == "Calculate":
        height = eval(values["height"])
        weight = eval(values["weight"])

        bmi = weight / (height / 100) ** 2

        if bmi < 16:
            sg.Popup(f"Your BMI is {bmi:.2f}", "Severely underweight")
        elif bmi < 18.5:
            sg.Popup(f"Your BMI is {bmi:.2f}", "Underweight")
        elif bmi < 25:
            sg.Popup(f"Your BMI is {bmi:.2f}", "Normal")
        elif bmi < 30:
            sg.Popup(f"Your BMI is {bmi:.2f}", "Overweight")
        else:
            sg.Popup(f"Your BMI is {bmi:.2f}", "Obese")

my_window.close()
