#   Collection = single "variable" used to store multiple values
#   Lists      = [] ordered and changeable. Duplicates OK
#   Set        = {} unordered and immutable, but Add/Remove OK. No Duplicates
#   Tuple      = () ordered and unchangeable. Duplicates OK. Faster

fruits = ["apple", "orange", "banana", "coconat"]

print(fruits[1]) #orange
print(fruits[0:3]) #apple orange banana
print(fruits[-1]) #coconat
print(fruits[::-1]) #coconot banana orange apple
print(fruits[::2]) #apple banana

# fruits[0] = "pineapple"  change apple with pineapple
fruits.append("pineapple") #adds pineapple to end of the list
fruits.remove("coconat") #to remove coconat
fruits.insert(0,"pineapple") # add pineapple at the beginning and do not delete the values
fruits.sort() #make alphabetical order
fruits.reverse() #to make reverse
# fruits.clear()  clear all the list
print(fruits.index("orange")) #to return index
print(fruits.count("pineapple")) #to return number of things

for fruit in fruits: #one below the other/ use singular version of List name
    print(fruit)

# print(dir(fruits)) == print(help(fruits))  tells us which function we can use

print(len(fruits))
print("apple" in fruits) #True