#Dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("USA")) #Washington D.C.

capitals.update({"Germany": "Berlin"}) #add this at the beginning of dictionary
#with this we also update the existing values "USA": "New Delhi" change the USA's value not add new one
print(capitals)

print()

capitals.pop("Germany")
capitals.popitem() #pop the last item
#capitals.clear() clear the dictionary
print(capitals)

print()

keys = capitals.keys() #give us the all off the keys
print(keys)

print()

for key in capitals.keys():
    print(key)

print()

values = capitals.values()
print(values)

print()

items = capitals.items() #give us 2D List version of dictionary
print(items)

print()

for key, value in capitals.items():
    print(f"{key}: {value}")
