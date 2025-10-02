import time

my_time = int(input("Enter time in seconds: "))

for x in range(my_time, 0, -1): # you can also use reversed() to make backward
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24 # we do not use day so %24 is unnecessary
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")