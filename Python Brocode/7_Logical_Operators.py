# Logical Operators = (or, and, not)
#or = at least one condition must be True
#and = both conditions must be True
#not = inverts the conditions

temp = 25
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print(f"The event is cancelled")
else:
    print(f"The event is still scheduled")

if temp > 28 and is_sunny:
    print(f"It is hot outside")
if temp < 25 and not is_sunny:
    print(f"It is cold outside")