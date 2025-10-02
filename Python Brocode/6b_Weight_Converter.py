#Weight Converter

weight = float(input("What is your weight "))
unit = input("Kilograms or Pounds? (K or L) ")

if unit == "K":
    weight = weight * 2.205
    weight = round(weight, 3)
    unit = "Lbs."
    print(f"Your weight is: {weight} {unit} ")

elif unit == "L":
    weight = weight / 2.205
    weight = round(weight, 3)
    unit = "Kilograms."
    print(f"Your weight is: {weight} {unit} ")

else:
    print(f"{unit}-invalid unit")

