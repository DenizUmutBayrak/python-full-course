#Variable: A container for value (string, integer, float, boolean)

#Strings
first_name = "Deniz"
thing = "games"

#Integers
age = 22
num_of_family = 4

#Float
price = 10.99
gpa = 3.31

#Boolean
is_student = True

print(first_name)

#f or F are formatted string literals
print(f"Hello {first_name}")
print(f"You like {thing}")

print(F"You are {age} years old")
print(f"You have {num_of_family} family members")

print(f"The price of that game is {price}")
print(f"My gpa is {gpa}")

print(f"Are you a student : {is_student}")
if is_student:
    print("You are a student")
else:
    print("You are not a student")