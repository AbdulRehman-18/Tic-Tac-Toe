theBoard = {'0': ' ', '1': ' ', '2': ' ',
 '3': ' ', '4': ' ', '5': ' ',
 '6': ' ', '7': ' ', '8': ' '}
def printBoard(board):
 print(board['0'] + '  | ' + board['1'] + ' | ' + board['2'])
 print('---|---|---')
 print(board['3'] + '  | ' + board['4'] + ' | ' + board['5'])
 print('---|---|---')
 print(board['6'] + '  | ' + board['7'] + ' | ' + board['8'])
turn = 'X'
for i in range(9):
  printBoard(theBoard)
  print('Turn for ' + turn + '. Move on which space?')
  move = input()
  theBoard[move] = turn
  if turn == 'X':
   turn = 'O'
  else:
    turn = 'X'

printBoard(theBoard)

