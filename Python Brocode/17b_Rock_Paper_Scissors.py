import random

options = ("rock", "paper", "scissor")
player = None
player_score = 0
computer_score = 0
game_state = True




while game_state:

    player = input("Enter a choice Rock, Paper, Scissor: ").lower()
    computer = random.choice(options)

    if not (player == "rock" or player == "paper" or player == "scissor"):
        print("Invalid choice!")
        continue

    else:
        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissor":
                print("Player wins!")
                player_score += 1

            elif computer == "paper":
                print("Computer wins!")
                computer_score += 1

        elif player == "scissor":
            if computer == "paper":
                print("Player wins!")
                player_score += 1

            elif computer == "rock":
                print("Computer wins!")
                computer_score += 1

        elif player == "paper":
            if computer == "scissor":
                print("Computer wins!")
                computer_score += 1

            elif computer == "rock":
                print("Player wins!")
                player_score += 1

    print(f"Computer chose {computer}.")
    print(f"Player chose {player}.")
    print(f"P: {player_score}, C: {computer_score}")

    if player_score == 3 or computer_score == 3:
        print("The game is over!")
        game_state = False

print(f"P: {player_score}, C: {computer_score}")

if player_score == 3:
    print(f"Player wins!")
else:
    print(f"Computer wins!")




