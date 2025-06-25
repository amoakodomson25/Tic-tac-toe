board = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ]


def printBoard():
    print()
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def checkWinner(player):
    combos = [
                (0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)
             ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in combos)

turn = 'X'
for _ in range(9):
    printBoard()
    while True:
        try:
            move = int(input("pick a spot(1-9): ")) - 1
            if move > 8 or move < 0:
                print("Enter a number from 1-9 ")
            elif board[move] in ['X','O']:
                print("Spot has already been taken")
            else:
                break
        except ValueError:
            print("type a number")

    board[move] = turn
    if checkWinner(turn):
        printBoard()
        print(f"player {turn} won")
        break
    turn = 'O' if turn == 'X' else 'X'
else:
    printBoard()
    print("its a tie")
