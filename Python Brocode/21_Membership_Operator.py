# Membership operator = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

word = "APPLE"

letter = input("Guess the letter in the secret word: ")

if letter in word:
    print(f"{letter} is in the word.")
else:
    print(f"{letter} is not in the word.")
                                                 #They have the same output
if letter not in word:
    print(f"{letter} is not in the word.")
else:
    print(f"{letter} is in the word.")
