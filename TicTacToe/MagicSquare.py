magicSquare = [4,9,2,3,5,7,8,1,6]
board=[' ',' ',' ','X',' ',' ','O',' ',' ']

def display_board(board):
    print('   |     |')
    print(' ' + board[6] + ' | ' +board[7] +'   | ' +board[8])
    print('   |     |')
    print('-------------')
    print('   |     |')
    print(' ' + board[3] + ' | ' +board[4] +'   | ' +board[5])
    print('   |     |')
    print('-------------')
    print('   |     |')
    print(' ' + board[0] + ' | ' +board[1] +'   | ' +board[2])
    print('   |     |')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def hasWon(theBoard,player):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if(i !=j and i!=k and j!=k):
                    if(theBoard[i] == player and theBoard[j] == player and theBoard[k] == player):
                        if(magicSquare[i] + magicSquare[j] + magicSquare[k] == 15):
                            return True
    return False

def place_marker(board,marker,position):
    board[position] = marker

def space_check(board, position):  
    return board[position] == ' '

def player_choice(board):
    position = 9
    while position not in [0,1,2,3,4,5,6,7,8] or not space_check(board, position):
        position = int(input('Choose your next position: (0-8) '))
        
    return position

def getpos(board,AImarker,player1marker):
  sum = 0
  for i in range(9):
    if board[i] == AImarker:
         sum = sum + magicSquare[i]
  rem_sum = 15 - sum
  if (rem_sum <= 9):
      pos = magicSquare.index(rem_sum)
      if space_check(board,pos):
          return pos
      else:
          if board[4] == ' ':
             return 4
          elif board[6] == ' ':
             return 6
          elif board[8] == ' ':
             return 8    
          elif board[2] == ' ':
             return 2
          elif board[0] == ' ':
             return 0 
          elif board[1] == ' ':
             return 1 
          elif board[3] == ' ':
             return 3     
  else:
    playersum = 0
    for i in range(9):
        if board[i] == player1marker:
           playersum = playersum + magicSquare[i]
    rem_sum = 15 - playersum
    if (rem_sum <= 9):
      pos = magicSquare.index(rem_sum)
      if space_check(board,pos):
          return pos
      else:
          if board[4] == ' ':
             return 4
          elif board[6] == ' ':
             return 6
          elif board[8] == ' ':
             return 8
    else:
      if board[4] == ' ':
        return 4
      elif board[6] == ' ':
        return 6
      elif board[8] == ' ':
        return 8
      
  
 

def full_board_check(board):
    for i in range(0,9):
        if space_check(board, i):
            return False
    return True

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print("Welcom to Tic Tac Toe")

while True:
    theBoard = [' '] * 9
    player1_marker, AI_marker = player_input()
    turn = "Player 1"

    game_on = True

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if hasWon(theBoard,player1_marker):
                display_board(theBoard)
                print("COngruatel you won!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Draw")
                    game_on = False
                else:
                    turn = 'AI'
        else:
            display_board(theBoard)
            position = getpos(theBoard,AI_marker,player1_marker)
            place_marker(theBoard,AI_marker, position)
            
            if hasWon(theBoard,player1_marker):
                display_board(theBoard)
                print("COngruatel you won!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Draw")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break



