#default arguments = a default value for certain parameters
#                    default is used when the argument is omitted
#                    make your functions more flexible, reduces # of arguments
#                    1. positional, 2. DEFAULT, 3. keyword, 4.arbitrary

import time

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1+ tax)

print(net_price(500)) #If you don't write any discount or tax value it uses the values which is in the function
print(net_price(500, 0.2)) #If you write a value it uses that value

def count(end, start=0 ):       #we cannot use start=0, end
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

count(10)