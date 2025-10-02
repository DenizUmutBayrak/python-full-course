#Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("What food do you want to buy? (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("What price of " + food + " is now?: "))
        foods.append(food)
        prices.append(price)

for x in range(len(foods)):
    total += prices[x]

print("-----Your Cart-----")
for x in range(len(foods)):
    print(foods[x], prices[x],end=" / ")
print()
print(f"Total is: {total}")
