#keyword arguments = an argument preceded by an identifier
#                    helps with readability
#                    order of argument doesn't matter
#                    1.positional 2.default 3.KEYWORD 4.arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting}, {title}{first} {last}")

hello("Hello", "Mr.","Deniz Umut","Bayrak")   #positional
hello("Hello", title = "Mr.", last ="Bayrak", first ="Deniz Umut") #keyword
#They have the same output

for x in range(1,11):
    print(x, end =" ") #this is also a keyword argument
print()
print ("1", "2", "3", "4", "5", "6",sep = "-")