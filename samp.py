# Code Edited By Abdul_Rehman 
theBoard = {'0': ' ', '1': ' ', '2': ' ',
            '3': ' ', '4': ' ', '5': ' ',
            '6': ' ', '7': ' ', '8': ' '}

def printBoard(board):
     print(board['0'] + '  | ' + board['1'] + ' | ' + board['2'])
     print('---|---|---')
     print(board['3'] + '  | ' + board['4'] + ' | ' + board['5'])
     print('---|---|---')
     print(board['6'] + '  | ' + board['7'] + ' | ' + board['8'])
# added winner check
def checkwin(board, player):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if board[str(win[0])] == board[str(win[1])] == board[str(win[2])] == player:
            return True
    return False


turn = 'X'
game_over = False
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    
    #To check invalid input
    if move not in theBoard.keys() or theBoard[move] != ' ':
        print("Invalid move! Try again.")
        continue
    
    theBoard[move] = turn

    if checkwin(theBoard, turn):
        game_over = True
        printBoard(theBoard)
        print('Congratulations '+ turn + ' wins!')
        break
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
# if tie 
if not game_over:
    printBoard(theBoard)
    print("It's a tie!")

