from __future__ import print_function
global N
N = 8

def printSolution(board): 
    print ("final configuration of queens:")
    for i in range(N): 
        for j in range(N): 
            if board[i][j]:
              board[i][j]="Q|"
            else:
              board[i][j]="_|"
            print(board[i][j], end = " ")
        print() 

#Checks three conditions.
#1. Whether there is any queen in that row. Checks only the left columns from given one
#2,3. Go through diagonals, top and bottom
#zip function maps values from those two lists.
#zip((1,2),(3,4)) ==> (1,3) and (2,4)
def isSafe(board, row, col): 
    for i in range(col):
        if board[row][i] == 1: 
            return False
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
        if board[i][j] == 1: 
            return False
    for i,j in zip(range(row,N,1), range(col,-1,-1)): 
        #print(i,j)
        if board[i][j] == 1: 
            return False
    return True

def solveNQUtil(board, col): 
    if col >= N: 
        return True
    for i in range(N): 
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col+1) == True: 
                return True
            board[i][col] = 0
    return False

def solveNQ(): 
    board = [ [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    if solveNQUtil(board,0) == False: 
        print ("Solution does not exist")
        return False
    printSolution(board) 
    return True
solveNQ()