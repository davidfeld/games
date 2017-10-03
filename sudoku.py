import numpy as np
from numpy import array

nrows = 9
nsqrs = nrows**2
rows = array(range(nsqrs)).reshape(nrows,nrows)
columns = array([list(rows[:,i]) for i in range(nrows)])
squares = [[j+9*i+3*k+27*p for i in range(3) for j in range(3)] for k in range(3) for p in range(3)]

rcs = []
for i in range(nsqrs):
    temp = []
    for j in range(nrows): 
        if i in rows[j]: temp.append(j)
    for j in range(nrows): 
        if i in columns[j]: temp.append(j)
    for j in range(nrows): 
        if i in squares[j]: temp.append(j)
    rcs.append(temp)

#board = [0,0,9,4,6,1,0,7,0, 3,0,0,0,0,0,2,0,0,6,0,0,3,0,0,0,9,0,0,9,0,2,7,0,0,5,4,5,7,2,0,0,0,6,3,9,4,3,0,0,5,9,0,8,0,0,8,0,0,0,2,0,0,7,0,0,4,0,0,0,0,0,5,0,2,0,7,4,6,3,0,0]
board = []
load = raw_input('Load board? ')
if load != 'y' and load != 'Y':
    for i in range(nsqrs):
        board.append(raw_input('box '+str(i+1)+': '))
else: board = list(np.load("board.npy"))

for i in range(nsqrs):
    try:
        board[i] = int(board[i])
    except: continue
np.save("board.npy", array(board))

board = [[i] for i in board]

for i in range(nsqrs): 
    if board[i] == [0] or board[i] == ['']: 
        board[i] = [1,2,3,4,5,6,7,8,9]

#gives a list of the known values in a row/col/sq
def getknown(list):
    temp = []
    for i in list:
        if len(i) == 1: temp.append(i[0])
    return temp






#####################################
def check(board):
    for i in range(nsqrs):
        if len(board[i]) == 1: continue
        row, col, sq = rcs[i][0], rcs[i][1], rcs[i][2]
        temp = []
        for j in board[i]:
            if j in getknown( [board[k] for k in rows[row]] ): continue
            elif j in getknown( [board[k] for k in columns[col]] ): continue
            elif j in getknown( [board[k] for k in squares[sq]] ): continue
            else: temp.append(j)

        board[i] = temp    
    return board
#########################################

def execute(board):
    keepgoing = True
    count = 0
    while keepgoing:
        oldboard = board[:]
        newboard = check(board)
        if newboard == oldboard: keepgoing = False
        else: board = newboard
        count += 1

execute(board)

def checksolved(board):
    solved = True
    for i in board:
        if len(i) != 1:
            solved = False
            break
    return solved

def checkerror(board):
    error = False
    for i in board:
        if i == ['']:
            error = True
            break
    return error

def checkrcs(sqr):
    oldb = board[:]
    row, col, sq = rcs[sqr][0], rcs[sqr][1], rcs[sqr][2]
    R = [oldb[k] for k in rows[row]]
    C = [oldb[k] for k in columns[col]]
    S = [oldb[k] for k in squares[sq]]
    print R,C,S

checkrcs(5)
    


def printboard(board):
    solved = checksolved(board)
    if solved:
        board = array([i[0] for i in board]).reshape(nrows,nrows)
        for i in board: print i

    else:
        board = array([i for i in board]).reshape(nrows,nrows)
        for i in board: print i        
        #print("{:.2e}".format(combos))

printboard(board)
