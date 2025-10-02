# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#          * unpacking operator
# 1. positional      2. default    3.keyword    4.ARBITRARY

def add(*nums):    #type of nums is tuple
    total = 0
    for num in nums:
        total += num
    return total

print(add(1,2,3,4)) # we use multiple argument with *args
print()

def print_address(**kwargs): #type of kwargs is dictionary
    for key,value in kwargs.items():
        print(f"{key} {value}")

print_address(street= "123 Fake St." ,
              city= "Detroit" ,
              state= "MI",
              zip = "54321" )

