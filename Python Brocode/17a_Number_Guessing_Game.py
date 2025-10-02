import random

lowest_num = 1
highest_num = 100
guess_num = 0

answer = random.randint(lowest_num, highest_num)

while True:
    guess = input(f"Guess a number between {lowest_num} and {highest_num}: ")


    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)

    if guess < lowest_num or guess > highest_num:
        print("Not in the scale")
        continue

    guess_num += 1

    if guess > answer:
        print("Lower Number")
    elif guess < answer:
        print("Higher Number")
    else:
        print(f"Correct!! You found {answer} in {guess_num} guesses ")
        break
