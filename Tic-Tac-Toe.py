from random import randrange
def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print('+-------+-------+-------+','|       |       |       |', sep = '\n')
    print('|  ',board[0],'  |  ',board[1],'  |  ',board[2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+','|       |       |       |', sep = '\n')
    print('|  ',board[3],'  |  ',board[4],'  |  ',board[5],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+','|       |       |       |', sep = '\n')
    print('|  ',board[6],'  |  ',board[7],'  |  ',board[8],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    num = int(input('Enter your move: '))
    if ((num not in board) or num > 9 or num < 1):
        print('Enter a valid move')
        EnterMove(board)
    else:
        board[num-1] = 'O'
        return board

def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    if((board[0] == board[1] == board[2] == sign) or (board[3] == board[4] == board[5] == sign) or (board[6] == board[7] == board[8] == sign)\
    or (board[0] == board[3] == board[6] == sign) or (board[1] == board[4] == board[7] == sign) or (board[2] == board[5] == board[8] == sign)\
    or (board[0] == board[4] == board[8] == sign) or (board[2] == board[4] == board[6] == sign)):
        if(sign == 'X'):
            print('Computer Won!')
            return False
        else:
            print('You Won!')
            return False
    else:
        return True

def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    Signal = True
    while Signal:
        choice = randrange(9)
        if (choice not in board or choice == 0):
            Signal = True
        else:
            Signal = False
    else:
        board[choice-1] = 'X'
        return board

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board[4] = 'X'
DisplayBoard(board)
Msg = True
count = 0
while Msg:
    board = EnterMove(board)
    DisplayBoard(board)
    Msg = VictoryFor(board, 'O')
    if(Msg == False):
        break
    board = DrawMove(board)
    DisplayBoard(board)
    Msg = VictoryFor(board, 'X')
    if(Msg == False):
        break
    count += 1
    if (count == 4):
        print ('Match Draw')
        Msg = False
print('Game End')
input('Press enter to exit')
