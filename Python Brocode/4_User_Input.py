# input() = a function that prompts the user to enter data
# Returned the entered data as a string

name = input("What is your name?: ")
print(f"Hello {name}")

age = int(input("How old are you?: "))
print("Happy Birthday!")
print(f"You are {age} years old.")

#I can also use age = int(age) instead of using it before input()
age += 1
print(f"Next year your age will be {age}")
