name = input("What is your name? ")
print(len(name)) #gives us length, includes spaces

print(name.find(" ")) #gives us the first character which is in the method's index number(first index is 0)
print(name.rfind(" ")) #reverse find: begins the other way and say its index.
# If we don't have that character it gives -1

print(name.capitalize()) #UpperCase just first letter
print(name.upper()) #UpperCase all letter
print(name.lower()) #LowerCase all letter

print(name.isdigit()) #True or False only digit
print(name.isalpha()) #True or False only alphabetical not even space

print(name.count(" ")) #Count that character

print(name.replace(" ", "-")) #Count that character

#print(help(str)) gives us all methods with strings







