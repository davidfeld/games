import copy
import random

dash = '--------------'
tab = '\t\t\t\t\t'
board  = [['1','2','3'],['4','5','6'],['7','8','9']]
valid = [str(i+1) for i in range(9)]

players = raw_input('How many human players (0,1,2)?  ')
while players not in ['0','1','2']:
    print 'Not a valid option.'
    players = raw_input('How many human players (0,1,2)?  ')
if players == '1':
    first = raw_input('Who moves first (h for human, c for computer)? ')
    while first not in ['h','c','H','C']:
        print 'Not a valid option.'
        first = raw_input('Who moves first (h for human, c for computer)? ')

def printboard(board):
    board2 = copy.deepcopy(board)
    for i in range(3):
        for j in range(3):
            if board2[i][j] in valid: board2[i][j] = ' '
    print '\n\n'
    for i in range(3):
        print tab+('  |  '.join(board2[i]))
        if i < 2:    print tab+dash

    print '\n\n'


def checkwin(board):
    win = False
    #check rows
    for i in range(3):
        if len(set(board[i])) == 1: win = True
    #check columns
    for i in range(3):
        temp = [board[0][i],board[1][i],board[2][i]]
        if len(set(temp)) == 1: win= True

    #check diagonals
    temp =  [board[0][0],board[1][1],board[2][2]]
    if len(set(temp)) == 1: win= True
    temp =  [board[0][2],board[1][1],board[2][0]]
    if len(set(temp)) == 1: win= True

    return win

printboard(board)
count = 0
nowinner = True
while nowinner:
    if count % 2 == 0:
        if players == '2': X = raw_input("X's move: ")
        elif players == '1' and first in ['h','H']: X = raw_input("X's move: ")
        else: X = random.choice(valid)
        
        if X not in valid: 
            print X+' is not a valid option'
            continue
        else:
            valid.remove(X)
            sq = int(X)
            board[(sq-1) /3][(sq-1) % 3] = 'X'

    else:
        if players == '2': O = raw_input("O's move: ")
        elif players =='1' and first in ['c','C']: O = raw_input("O's move: ")
        else: O = random.choice(valid)

        if O not in valid:
            print O+' is not a valid option'
            continue
        else:
            valid.remove(O)
            sq = int(O)
            board[(sq-1) /3][(sq-1) % 3] = 'O'

    printboard(board)

    count += 1
    if checkwin(board): 
        if count % 2 == 0: print 'O Wins!!!'
        else: print 'X Wins!!!'
        nowinner = False
    elif count == 9:
        print "Cat's Game Yo!!"
        nowinner = False
    
