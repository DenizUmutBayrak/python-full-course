#While Loop = execute some code While some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter a name.")
    name = input("Enter your name: ")
print(f"Your name is {name}")