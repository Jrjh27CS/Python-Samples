newGame = True
prompt = "rock, paper, or scissors? >"
while (newGame):
    player1 = input(prompt)
    player2 = input(prompt)
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins!")
        elif player2 == "paper":
            print("Player 2 wins!")
        elif player2 == "rock":
            print("Stalemate!")
        else:
            print("Player 2, Please enter a valid input next time")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!")
        elif player2 == "rock":
            print("Player 2 wins!")
        elif player2 == "scissors":
            print("Stalemate!")
        else:
            print("Player 2, Please enter a valid input next time")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")
        elif player2 == "paper":
            print("Stalemate!")
        else:
            print("Player 2, Please enter a valid input next time")
    else:
        print("Player 1, Please enter a valid input next time")
    newGame = input("Would you like to play again? y or n:")
    if newGame == "y":
        newGame = True
    else:
        newGame = False
