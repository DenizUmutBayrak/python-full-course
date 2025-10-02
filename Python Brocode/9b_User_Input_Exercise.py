#User Input Exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Enter your name: ")

if len(name) > 12:
    name = input("Username is no more than 12 characters: ")
elif name.count(" ") > 0:     #elif not username.find(" ") == -1
    name = input("Username must not contain spaces: ")
elif not name.isalpha():
    name = input("Username must not contain numbers: ")
else:
    print(f"Your username is valid: {name}")