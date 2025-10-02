import random

low = 1
high = 100
options = ("Rock", "Paper", "Scissor")
# number = random.randint(low, high) #Last number is included

#number = random.random() #random floating number

number = random.choice(options) # Rock Scissor or Paper. just one of them

print(number)