# List comprehension = a concise way to create lists in python
#                      compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

#Normal Way
doubles = []

for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

#List comprehension
doubles2 =[x*2 for x in range(1,11) if x % 2 == 0]
triples =[x*3 for x in range(1,11)]
print(doubles2)
print(triples)

fruits = ["apple","banana","orange"]
fruits = [ fruit.upper() for fruit in fruits ]
print(fruits)
