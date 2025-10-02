#if = Do some code only If some condition is True, Else do something else

age = float(input("What is your age? "))

if age >= 60:
    print("You are old. ")
elif age >= 18:
    print("You are young. ")
else:
    print("You are too young. ")

response = (input("Do you like me? "))

if response == "Y":   # == comparison operator
    print("Thanks. ")
else:
    print("Sorry, I didn't get that. ")