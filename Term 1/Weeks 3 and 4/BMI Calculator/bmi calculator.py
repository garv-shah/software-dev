height = eval(input("Enter your height in cm: "))
weight = eval(input("Enter your weight in kg: "))
bmi = weight / (height / 100) ** 2
print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
