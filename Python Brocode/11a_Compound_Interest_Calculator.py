#Python Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0: #True
    principle = float(input("Enter a principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than zero or equal to zero")
#   else:
#        break
while rate <= 0:
    rate = float(input("Enter a interest rate: "))
    if rate <= 0:
        print("Interest rate cannot be less than zero or equal to zero")

while time <= 0:
    time = int(input("Enter a principle amount: "))
    if time <= 0:
        print("Time cannot be less than zero or equal to zero")


total = principle * pow((1 + rate / 100),time)

print(f"Balance after{time} years is ${total:.2f}")

