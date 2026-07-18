import random

options = ("rock", "paper", "scissors")
player = None
pc = 0
cc = 0
playing = True

while playing:
    computer = random.choice(options)

    player = input('''Enter your choice: (Rock, Paper, Scissors)
                               Or 
                      type end to stop: ''').casefold()

    if player == "end":
        print("Game Over. Thanks for playing!")
        break

    if player not in options:
        print("Invalid option entered. Please try again")
        continue

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
        pc = pc + 1
        cc = cc + 1

    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):

        print("You win!")

        if player == "rock":
            print("Rock smashes Scissors")
        elif player == "paper":
            print("Paper covers Rock")
        else:
            print("Scissors cuts Paper")

        pc = pc + 1

    else:
        print("You lose! Better luck next time ")

        if computer == "rock":
            print("Rock smashes Scissors")
        elif computer == "paper":
            print("Paper covers Rock")
        else:
            print("Scissors cuts Paper")

        cc = cc + 1

    print("Player Score:", pc)
    print("Computer Score:", cc)