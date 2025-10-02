#format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f  round  to that many decimal places (fixed point)
# :(number) allocate that many spaces
# :03  allocate and zero pad that many spaces
# :< left justify
# :> right justify
# :^ center align
# :+ use a plus sign to indicate positive value
# :  insert a space before positive numbers
# :, comma seperator

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 1000.5678

print(f"Price1: ${price1:.2f}")  #3.14
print(f"Price2: ${price2:10}") #have total 10 spaces ___-987.65
print(f"Price3: ${price3:010}")#have total 10 spaces with 0  0000012.34
print(" ")
print(f"Price1: ${price1:<10}") #3.14______
print(f"Price2: ${price2:>10}") #___-987.65
print(f"Price3: ${price3:^10}") #__12.34___
print(" ")
print(f"Price1: ${price1:+}") #+3.14159
print(f"Price2: ${price2:+}") #-987.65
print(f"Price3: ${price3: }") #_12.34  makes space before positive numbers
print(" ")
print(f"Price4: ${price4:,}") #1,000.5678
print(f"Price2: ${price4:,.2f}") #1,000.57  we can mix the flags

