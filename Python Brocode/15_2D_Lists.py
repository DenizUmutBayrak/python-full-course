#2D Lists

fruits = ["apple", "banana", "orange", "coconut"]
vegetables = ["celery", "carrot", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[1]) #vegetables lists
print(groceries[1][1]) #carrot

print()

for collection in groceries: #all elements in all lists
    for food in collection:
        print(food, end= " ")
    print()
