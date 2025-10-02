# Typecasting = the process of converting a variable from one type to another
# str(), int(), float(), bool()

name = "Deniz"
name2 = ""
age = 22
gpa = 3.31
is_student = True

print(type(gpa)) # to identify variables type

gpa = str(gpa)
print(type(gpa))#float

age = float(age)
print(age) #22.0

age = str(age)
age += "1"
print(age) #22.01

name = bool(name)
print(name)
                       #If you have at least 1 character it becomes True, else False
name2= bool(name2)
print(name2)
