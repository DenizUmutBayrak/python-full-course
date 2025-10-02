

fruits = {"apple", "orange", "banana", "coconut", "coconut"}
#We write to coconut but sets only see 1 coconut

print(fruits) #unordered

#print(dir(fruits)) == print(help(fruits))

print(len(fruits)) #4
print("pineapple" in fruits) #False

#print(fruits[0]) we cannot use this function because sets are unordered

fruits.add("pineapple")
fruits.remove("apple")
fruits.pop() # remove the first element but in sets it is random
#fruits.clear() to clear sets

print(fruits) #unordered

