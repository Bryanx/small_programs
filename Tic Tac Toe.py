print("Let's play Tic-Tac-Toe!")

board = [[0]*3 for i in range(3)]

def printboard(board):
    for x in board:
        print(x)

printboard(board)

p1row = int(input("Player 1 enter your chosen row\n"))
p1col = int(input("Player 1 enter your chose column\n"))

if board[p1row] == "O" or board[p1col] == "O":
    print("That place is already taken by Player 2")


board[p1row][p1col] = "X"
printboard(board)





