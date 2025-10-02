#For loops = execute a block of code a fixed number of times
#            you can iterate over a range, string, sequence, etc.

for x in range(1, 11): #11 is excluded
    print(x)

print(" ")

for x in reversed(range(1, 11)): #reversed version
    print(x)

print(" ")

for x in range(1, 11, 2): #1 3 5 7 9
    print(x)

for x in range(1, 21): #21 is excluded
    if x == 13:
        continue  # to skip 13
    else:
        print(x)
