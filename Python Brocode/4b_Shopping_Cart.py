#Exercise 2 Shopping Cart Program
item = input("What do you want to buy? ")
price = float(input("What is the price? "))
quantity = float(input("How many do you want to buy? "))
total = price * quantity

print(f"${total}")