while True:
    p1, p2 = input("Rock, paper or scissors?\n"), input("Rock, paper or scissors?\n")
    if p1 == "rock" and p2 == "scissors" or p1 == "paper" and p2 == "rock" or p1 == "scissors" and p2 == "paper":
        print("Player 1 wins!")
    elif p2 == "rock" and p1 == "scissors" or p2 == "paper" and p1 == "rock" or p2 == "scissors" and p1 == "paper":
        print("Player 2 wins!")
    else:
        print("It's a draw!")
    restart = bool(input("Restart? (True or False)\n"))