import random

turn = 0
rnumber = random.randint(1, 9)

while True:
    print("Turn", turn)
    turn += 1
    guess = input("Guess a number between 1 and 9:  ")
    if guess == "exit":
        break
    guess = int(guess)
    if guess == rnumber:
        print("Congrats! You guessed the right number")
        break
    elif guess > rnumber:
        print("You guessed to high")
    elif guess < rnumber:
        print("You guessed to low")