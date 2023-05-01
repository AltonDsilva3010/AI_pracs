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

def getposnew(board, AImarker, player1marker):
    def minimax(board, depth, is_maximizing_player):
        # Check for terminal state
        if hasWon(board, AImarker):
            return 1
        elif hasWon(board, player1marker):
            return -1
        elif full_board_check(board):
            return 0

        # Recursive case
        if is_maximizing_player:
            best_score = -float('inf')
            for i in range(9):
                if space_check(board, i):
                    board[i] = AImarker
                    score = minimax(board, depth+1, False)
                    board[i] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if space_check(board, i):
                    board[i] = player1marker
                    score = minimax(board, depth+1, True)
                    board[i] = ' '
                    best_score = min(best_score, score)
            return best_score

    # Main function logic
    best_score = -float('inf')
    best_pos = None
    for i in range(9):
        if space_check(board, i):
            board[i] = AImarker
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_pos = i
    return best_pos

      
  
 

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
            position = getposnew(theBoard,AI_marker,player1_marker)
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



