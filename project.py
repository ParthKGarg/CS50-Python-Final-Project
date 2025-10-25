import time

def printBoard(board):
    print()
    for k in range(3):
        for i in range(0,3):
            for j in range(0+3*k,3+3*k):
                print(f"{board[j][i][0]}|{board[j][i][1]}|{board[j][i][2]}",end='' )
                if (j+1)%3!=0:
                    print("  |  ",end='')
            print()
            if (i+1)%3==0 and i!=8 and k!=2:
                print(" "*7 + "|" + " "*9 + "|" + " "*7)
                print("-"*26)
                print(" "*7 + "|" + " "*9 + "|" + " "*7)
            elif (i+1)%3 !=0:
                print("-"*5 + "  |  " + "-----" + "  |  " + "-----")
    print()

def checkValidMove(board, movePos):
    movePos -= 1
    i = movePos//3
    j = movePos%3

    if board[i][j] == ' ':
        return True
    return False

def updateBoard(board, movePos, turn):
    movePos -= 1
    i = movePos//3
    j = movePos%3
    board[i][j] = 'X' if turn else 'O'

def playerInput(board, boardNo):
    if boardNo == 0 :
        print("You can play in any mini board.")
        # take input of board
        while True:
            try:
                boardNo = int(input("Enter the mini board you want to play in(1-9): "))
            except ValueError:
                print("Invalid Input")
                continue
            try:
                movePos = int(input("Enter the position you want to play in(1-9): "))
            except ValueError:
                print("Invalid Input")
                continue
            if 0<boardNo<=9 and 0<movePos<=9 and checkValidMove(board[boardNo-1], movePos):
                break
            else:
                print("Not a valid move.Please enter another move.")
                continue
    else:
        print(f"You have to play in mini board {boardNo}.")
        while True:
            try:
                movePos = int(input("Enter the position you want to play in(1-9): "))
            except ValueError:
                print("Invalid Input")
                continue
            if 0<movePos<=9 and checkValidMove(board[boardNo-1], movePos):
                break
            else:
                print("Not a valid move.Please enter another move.")
                continue
    return boardNo, movePos

def checkWin(board):
    arr = [
        [[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
        [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
        [[0,2],[1,1],[2,0]],[[0,0],[1,1],[2,2]]
        ]

    for i in range(8):
        a=arr[i][0][0]
        b=arr[i][0][1]
        c=arr[i][1][0]
        d=arr[i][1][1]
        e=arr[i][2][0]
        f=arr[i][2][1]

        if (board[a][b]==board[c][d] and board[c][d]==board[e][f] and board[c][d]!=' '):
            return True

    return False

def updateBoardAfterWin(board, turn):
    sym = 'X' if turn else 'O'
    for i in range(3):
        for j in range(3):
            board[i][j] = sym

def checkDraw(board):
    for mb in board:
        for row in mb:
            for ele in row:
                if ele == ' ':
                    return False
    return True

def checkWinWin(arr):
    com = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    if len(arr)<3:
        return False
    for set in com:
        result = True
        for ele in set:
            if ele not in arr:
                result = False
                break
        if result:
            return result
    return result

def main():
    # essential variables
    board = [
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
        [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    ]
    turn = 1
    boardNo = 0
    movePos = 0
    wins = {True:[], False:[]}
    count = 0

    # print empty board
    printBoard(board)

    # main game loop
    while True:
        if turn:
            print(f"Player X's turn.")
        else:
            print(f"Player O's turn.")

        # take player input
        boardNo, movePos = playerInput(board, boardNo)
        count+=1
        print()
        updateBoard(board[boardNo-1], movePos, turn)
        printBoard(board)

        # check if anyone won a mini board
        if count>=5:
            if checkWin(board[boardNo-1]):
                print(f"Player {'X' if turn else 'O'} won one mini board. Updating board.", end='', flush = True)
                for i in range(4):
                    time.sleep(0.5)
                    print('.', end='', flush = True)

                updateBoardAfterWin(board[boardNo-1], turn)
                print()
                printBoard(board)
                wins[turn].append(boardNo)

        # check if anyone won the game
        if checkWinWin(wins[turn]):
            print("Game Over.")
            print(f"Result - Player {'X' if turn else 'O'} Won.")
            break


        # check for draw
        if checkDraw(board):
            print("Game Over.")
            print("Result - DRAW.")
            break

        if (movePos in wins[True]) or (movePos in wins[False]):
            boardNo = 0
        else:
            boardNo = movePos

        turn = not(turn)

if __name__ == "__main__":
    main()