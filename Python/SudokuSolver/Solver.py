import sys
import time
sys.argv.append("Puzzle.txt")

lines=[]
options=[1,2,3,4,5,6,7,8,9]
board = [["_" for i in range(9)] for j in range(9)]

with open(sys.argv[1],"r") as f:
    lines=f.read().split("\n")

for x in range(len(lines)):
    for y in range(len(lines[x])):
        if(lines[x][y]!="_"):
            board[x][y]=int(lines[x][y])


def getOptions(i,j,board):
    new_options=list(options)
    #modify new_options based on quadrant, column, and row
    r=getQuadrant(i,j,board)
    r+=getColumn(i,j,board)
    r+=getRow(i,j,board)
    for x in r:
        if(x in new_options):
            new_options.remove(x)
    return new_options
    
def getColumn(i,j,board):
    column=[]
    for x in range(len(board)):
        if(board[x][j]!="_"):
            column+=[board[x][j]]
    return column

def getRow(i,j,board):
    row=[]
    for x in range(len(board[i])):
        if(board[i][x]!="_"):
            row+=[board[i][x]]
    return row

def getQuadrant(i,j,board):
    quadrant=[]
    qx=(i//3)*3
    qy=(j//3)*3
    for x in range(qx,qx+3):
        for y in range(qy,qy+3):
            if(board[x][y]!="_"):
                quadrant+=[board[x][y]]
    return quadrant



def solve(i,j,board):
    if(i>=len(board) or j>=len(board)):
        return board
    if(board[i][j]!="_"):
        ni=(i+1)%9
        nj=j
        if(ni<i):
            nj+=1
        eboard=solve(ni,nj,board)
        return eboard
    nboard=[[x for x in row] for row in board]
    noptions=getOptions(i,j,nboard)
    if(len(noptions)==0):
        return None
    #nboard[0][0]="example"
    for x in noptions:
        nboard[i][j]=x
        #print("\n",i,j)
        #printBoard(nboard)
        ni=(i+1)%9
        nj=j
        if(ni<i):
            nj+=1
        eboard=solve(ni,nj,nboard)
        if(eboard==None):
            continue
        else:
            return eboard

def printBoard(board):
    if(board == None):
        print(board)
        return
    for x in board:
        for y in x:
            print(str(y)+" ",end="")
        print("")

print("Start:")
t=time.time()
printBoard(board)
print("End:")
printBoard(solve(0,0,board))
print(str(time.time()-t)[:6],"seconds")