
def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

if height > 0:
    bmi = calculate_bmi(weight, height)
    print("Your BMI is:", format(bmi, ".2f"))
else:
    print("Height must be greater than zero.")
