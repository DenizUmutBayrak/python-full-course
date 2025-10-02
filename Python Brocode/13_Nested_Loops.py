#Nested Loop = A loop within another loop (outer, inner)
# outer loop:
#     inner loop:

rows = int(input("How many rows do you want? "))
columns = int(input("How many columns do you want? "))
symbol = input("What is your symbol? ")

for x in range (rows):
    for y in range (1,columns+1):
        print(symbol, end="")  # to write side by side
    print()
