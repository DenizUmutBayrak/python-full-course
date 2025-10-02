#indexing = accessing elements of a sequence using [] (Indexing operator)
# [start : end : step]

credit_number = "1234-5678-9012-3456"
print(credit_number[0]) #first character 1
print(credit_number[-1]) #last character 6
print(credit_number[0:5]) #from index 0 to index 5 = 1234- //Also you can write [:5] automatically index 0 is beginning.
print(credit_number[5:9]) #do not take the last index 5678
print(credit_number[5:]) #5678-9012-3456
print(credit_number[::2]) #13-6891-46
print(credit_number[-4:]) #3456
print(credit_number[::-1]) #Reverse the number 6543-2109-8765-4321
