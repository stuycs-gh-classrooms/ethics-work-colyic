board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def printBoard():
    ret = "\n"

    for i in range(4):
        if i < 3:
            ret += str(i) + " "
            for j in range(3):
                if j==0 or j==1:
                    ret += f'{board[i][j]} | '
                else:
                    ret+=board[i][j]
        else:
            ret += "  "

            for j in range(3):
                ret += str(j) + "   "
        ret += "\n"
    print(ret)

def addChar(x, y, char):
    if  x < 0 or x > 2 or y < 0 or y > 2 or  board[x][y] != " ":
        print("\n\nInvalid Coordinate. Try Again!\n\n")
        return False
    else:
        board[x][y] = char
        return True

#addChar(0, 1, "O")
#addChar(0, 2, "X")
#printBoard()

def win():
    ret = ""

    for i in range(3):
        # check for horizontal win
        if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                ret = "Player 1"
            else:
                ret = "Player 2"
        # check for vertical win
        elif board[0][i] != " " and board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                ret = "Player 1"
            else:
                ret = "Player 2"

    # check for diagonal win
    if ret == "":
        if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == "X":
                ret = "Player 1"
            else:
                ret = "Player 2"
        elif board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == "X":
                ret = "Player 1"
            else:
                ret = "Player 2"
    return ret

def runGame():
    winner = ""
    player = 0
    goodTurn = True

    print("Players take turns entering the X and Y coordinates of the box they would like to mark. Player 1 is Xs, Player 2 is Os")

    while winner == "":
        if goodTurn:
            printBoard()
            print(f'Player {player+1} is up!')
        else:
            print(f'Try Again, Player {player+1}')

        xCor = input("Enter desired X Coordinate: ")
        yCor = input("Enter desired Y Coordinate: ")

        if not (xCor.isdigit() or yCor.isdigit()):
            goodTurn = False

        else:    
            xCor = int(xCor)
            yCor = int(yCor)

            if player==0:
                goodTurn = addChar(yCor, xCor, "X")
            elif player==1:
                goodTurn = addChar(yCor, xCor, "O")

        winner = win()

        if goodTurn:
            player += 1
            player%=2
    printBoard()
    print(f'\nCongratulations to {winner}!')

runGame()